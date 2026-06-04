import { useState } from "react";
import { analyzeWeather } from "../api/weather";

import WeatherCard from "../components/WeatherCard";
import AICard from "../components/AICard";
import RulesCard from "../components/RulesCard";
import WeatherChart from "../components/WeatherChart";
import WeatherMap from "../components/WeatherMap";

export default function Dashboard() {
  const [lat, setLat] = useState(3.848);
  const [lon, setLon] = useState(11.502);
  const [days, setDays] = useState(1);
  const [units, setUnits] = useState("metric");
  const [mode, setMode] = useState("hybrid");

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchWeather = async () => {
    setLoading(true);

    try {
      const res = await analyzeWeather({
        lat,
        lon,
        days,
        units,
        mode,
        ai_style: "detailed",
      });

      setData(res);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  const handleMapClick = (newLat, newLon) => {
    setLat(newLat);
    setLon(newLon);
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white">

      {/* HEADER */}
      <div className="border-b border-gray-800 bg-gray-950">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <h1 className="text-2xl font-bold">🌤 Weather AI Dashboard</h1>
          <p className="text-gray-400 text-sm">
            AI + Rules Engine Weather System
          </p>
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-6 py-6 space-y-6">

        {/* INPUTS */}
        <div className="grid md:grid-cols-5 gap-3">
          <input
            className="p-2 bg-gray-800 border border-gray-700 rounded"
            value={lat}
            onChange={(e) => setLat(e.target.value)}
            placeholder="Latitude"
          />

          <input
            className="p-2 bg-gray-800 border border-gray-700 rounded"
            value={lon}
            onChange={(e) => setLon(e.target.value)}
            placeholder="Longitude"
          />

          <input
            className="p-2 bg-gray-800 border border-gray-700 rounded"
            value={days}
            onChange={(e) => setDays(e.target.value)}
            placeholder="Days"
          />

          <select
            className="p-2 bg-gray-800 border border-gray-700 rounded"
            value={units}
            onChange={(e) => setUnits(e.target.value)}
          >
            <option value="metric">Metric</option>
            <option value="imperial">Imperial</option>
          </select>

          <select
            className="p-2 bg-gray-800 border border-gray-700 rounded"
            value={mode}
            onChange={(e) => setMode(e.target.value)}
          >
            <option value="rules">Rules</option>
            <option value="ai">AI</option>
            <option value="hybrid">Hybrid</option>
          </select>
        </div>

        {/* BUTTON */}
        <button
          onClick={fetchWeather}
          disabled={loading}
          className="bg-blue-600 px-6 py-2 rounded font-bold hover:bg-blue-500 transition disabled:opacity-50"
        >
          {loading ? "Loading..." : "Analyze Weather"}
        </button>

        {/* MAP */}
        <div className="mt-6">
          <WeatherMap onLocationSelect={handleMapClick} />
        </div>

        {/* RESULTS */}
        {data && (
          <div className="mt-6 space-y-6">

            {/* SUMMARY */}
            <div className="bg-gray-900 border border-gray-800 rounded-xl p-4">
              <h2 className="text-lg font-semibold mb-3">
                📍 Analysis Summary
              </h2>

              <div className="grid md:grid-cols-4 gap-3 text-sm">
                <div>
                  <p className="text-gray-400">Latitude</p>
                  <p className="font-bold">{lat}</p>
                </div>

                <div>
                  <p className="text-gray-400">Longitude</p>
                  <p className="font-bold">{lon}</p>
                </div>

                <div>
                  <p className="text-gray-400">Mode</p>
                  <p className="font-bold">{mode}</p>
                </div>

                <div>
                  <p className="text-gray-400">Units</p>
                  <p className="font-bold">{units}</p>
                </div>
              </div>
            </div>

            {/* CURRENT WEATHER + AI + RULES */}
            <div className="grid lg:grid-cols-3 gap-4">

              <WeatherCard weather={data.weather?.data || data.weather} />

              {data.rules && (
                <RulesCard rules={data.rules} />
              )}

              {data.ai && (
                <AICard ai={data.ai} />
              )}
            </div>

            {/* FORECAST (WeatherCard GRID) */}
            {data?.weather?.type === "forecast" && (
              <div>
                <h2 className="text-lg font-semibold mb-3">
                  📊 Forecast
                </h2>

                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {data.weather.data?.map((item, i) => (
                    <WeatherCard
                      key={i}
                      weather={{
                        date: item.date || `Day ${i + 1}`,
                        temp: item.temp,
                        condition: item.condition,
                        humidity: item.humidity,
                        wind: item.wind,
                      }}
                    />
                  ))}
                </div>
              </div>
            )}

          </div>
        )}

        {/* CHART */}
        {data?.weather?.type === "forecast" && (
          <div className="mt-6">
            <WeatherChart forecast={data.weather.data} />
          </div>
        )}

      </div>
    </div>
  );
}