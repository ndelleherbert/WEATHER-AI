import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

export default function WeatherChart({ forecast }) {

  if (!forecast?.forecast) return null;

  const data = forecast.forecast.map(item => ({
    time: item.datetime.slice(5, 16),
    temp: item.temperature,
    humidity: item.humidity
  }));

  return (
    <div className="bg-gray-900 p-4 rounded-xl mt-6">
      <h2 className="text-xl font-bold mb-3">📈 Forecast Charts</h2>

      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />

            <Line dataKey="temp" stroke="#f97316" name="Temp" />
            <Line dataKey="humidity" stroke="#3b82f6" name="Humidity" />

          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}