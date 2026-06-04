class WeatherRulesEngine:

    @staticmethod
    def analyze(weather: dict):

        main = weather.get("main", {})
        wind = weather.get("wind", {})

        temp = main.get("temp", 0)
        humidity = main.get("humidity", 0)
        wind_speed = wind.get("speed", 0)

        risk = "NORMAL"
        advice = "Safe conditions"

        if temp >= 35:
            risk = "HIGH HEAT"
            advice = "Avoid outdoor activity"

        if temp <= 10:
            risk = "COLD"
            advice = "Wear warm clothes"

        if humidity > 80:
            advice += " | High humidity"

        if wind_speed > 10:
            advice += " | Strong winds"

        return {
            "risk": risk,
            "advice": advice,
            "summary": f"{temp}°C, {humidity}%, {wind_speed} m/s"
        }