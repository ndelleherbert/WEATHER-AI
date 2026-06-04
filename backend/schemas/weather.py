import httpx
from core.config import settings


class WeatherService:

    @staticmethod
    async def get_weather(lat: float, lon: float, units: str = "metric"):
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "lat": lat,
            "lon": lon,
            "appid": settings.WEATHER_API_KEY,
            "units": units
        }

        async with httpx.AsyncClient() as client:
            res = await client.get(url, params=params)

            data = res.json()

            # ❌ Handle API errors cleanly
            if res.status_code != 200:
                return {
                    "error": True,
                    "status": res.status_code,
                    "message": data
                }

            # ✅ Normalize output (this is your "set weather")
            return WeatherService._set_weather(data)

    @staticmethod
    def _set_weather(data: dict):
        main = data.get("main", {})
        wind = data.get("wind", {})
        weather = data.get("weather", [{}])[0]

        return {
            "location": data.get("name"),
            "temperature": main.get("temp"),
            "feels_like": main.get("feels_like"),
            "humidity": main.get("humidity"),
            "pressure": main.get("pressure"),
            "wind_speed": wind.get("speed"),
            "weather_main": weather.get("main"),
            "weather_description": weather.get("description"),
            "visibility": data.get("visibility"),
            "country": data.get("sys", {}).get("country"),
            "raw": data  # keep full data for AI use
        }