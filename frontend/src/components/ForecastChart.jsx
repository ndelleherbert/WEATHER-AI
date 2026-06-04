export default function ForecastChart({ data }) {
  const forecast = data?.weather?.data?.forecast;

  if (!forecast || forecast.length === 0) {
    return <p className="text-gray-500">No forecast data</p>;
  }

  return (
    <div>
      <h2 className="font-bold mb-3">📊 Forecast</h2>

      <div className="space-y-2">
        {forecast.slice(0, 6).map((item, i) => (
          <div
            key={i}
            className="flex justify-between border-b pb-1 text-sm"
          >
            <span>{item.datetime?.split(" ")[0]}</span>
            <span>{item.temperature}°</span>
          </div>
        ))}
      </div>
    </div>
  );
}