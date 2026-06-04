export default function WeatherCard({ weather }) {
  if (!weather) return null;

  return (
    <div className="bg-gray-900 p-4 rounded-xl">
      <h2 className="text-xl font-bold mb-3">🌍 Weather</h2>

      <p>📍 {weather.location || weather.city}</p>
      <p>🌡 {weather.temperature}°C</p>
      <p>💧 {weather.humidity}%</p>
      <p>🌬 {weather.wind_speed} m/s</p>
      <p>☁️ {weather.description}</p>
    </div>
  );
}