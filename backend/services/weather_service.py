import httpx
from core.config import settings


class WeatherService:

    @staticmethod
    async def get_weather(lat: float, lon: float, days: int = 1, units: str = "metric"):

        # 🌤 CURRENT WEATHER (1 DAY)
        if days <= 1:
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

                return {
                    "type": "current",
                    "data": WeatherService._normalize_current(data)
                }

        # 🌦 FORECAST (5 DAYS)
        url = "https://api.openweathermap.org/data/2.5/forecast"

        params = {
            "lat": lat,
            "lon": lon,
            "appid": settings.WEATHER_API_KEY,
            "units": units
        }

        async with httpx.AsyncClient() as client:
            res = await client.get(url, params=params)
            data = res.json()

            return {
                "type": "forecast",
                "data": WeatherService._normalize_forecast(data)
            }

    # -------------------------
    # CLEAN CURRENT WEATHER
    # -------------------------
    @staticmethod
    def _normalize_current(data: dict):

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
            "description": weather.get("description"),
            "condition": weather.get("main"),
            "raw": data
        }

    # -------------------------
    # CLEAN FORECAST DATA
    # -------------------------
    @staticmethod
    def _normalize_forecast(data: dict):

        daily = []

        for item in data.get("list", []):
            main = item.get("main", {})
            wind = item.get("wind", {})
            weather = item.get("weather", [{}])[0]

            daily.append({
                "datetime": item.get("dt_txt"),
                "temperature": main.get("temp"),
                "humidity": main.get("humidity"),
                "wind_speed": wind.get("speed"),
                "condition": weather.get("main"),
                "description": weather.get("description"),
            })

        return {
            "city": data.get("city", {}).get("name"),
            "country": data.get("city", {}).get("country"),
            "forecast": daily,
            "raw": data
        }