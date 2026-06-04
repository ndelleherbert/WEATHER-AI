from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal, Optional

from services.weather_service import WeatherService
from services.rule_engine import WeatherRulesEngine
from services.ai_service import AIService

router = APIRouter(prefix="/weather")


class WeatherRequest(BaseModel):
    lat: float
    lon: float
    days: int = 1
    units: Literal["metric", "imperial", "standard"] = "metric"
    mode: Literal["rules", "ai", "hybrid"] = "rules"
    ai_style: Optional[str] = "detailed"


@router.post("/analysis")
async def analyze(req: WeatherRequest):

    weather = await WeatherService.get_weather(
        req.lat,
        req.lon,
        req.days,
        req.units
    )

    rules_result = WeatherRulesEngine.analyze(weather)

    if req.mode == "rules":
        return {
            "mode": "rules",
            "weather": weather,
            "result": rules_result
        }

    ai_result = await AIService.analyze_weather(weather, req.ai_style)

    if req.mode == "ai":
        return {
            "mode": "ai",
            "weather": weather,
            "result": ai_result
        }

    return {
        "mode": "hybrid",
        "weather": weather,
        "rules": rules_result,
        "ai": ai_result
    }

@router.get("/test")
def test():
    return {"status": "Weather endpoint is working"}


@router.get("/rules-test")
def rules_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 35,
            "humidity": 80,
            "wind_speed": 20,
            "weather_main": "Thunderstorm",
            "visibility": 2000
        }
    }
    result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "Rules engine test",
        "input": sample_weather,
        "result": result
    }

@router.get("/ai-test")
async def ai_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 35,
            "humidity": 80,
            "wind_speed": 20,
            "weather_main": "Thunderstorm",
            "visibility": 2000
        }
    }
    result = await AIService.analyze_weather(sample_weather, "detailed")
    return {
        "status": "AI service test",
        "input": sample_weather,
        "result": result
    }

@router.get("/hybrid-test")
async def hybrid_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 35,
            "humidity": 80,
            "wind_speed": 20,
            "weather_main": "Thunderstorm",
            "visibility": 2000
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    ai_result = await AIService.analyze_weather(sample_weather, "detailed")
    return {
        "status": "Hybrid test",
        "input": sample_weather,
        "rules_result": rules_result,
        "ai_result": ai_result
    }

@router.get("/error-test")
async def error_test():
    # Simulate an error by calling with invalid coordinates
    weather = await WeatherService.get_weather(999, 999)
    return {
        "status": "Error handling test",
        "input": {"lat": 999, "lon": 999},
        "result": weather
    }

@router.get("/style-test")
def style_test():
    styles = ["detailed", "concise", "bullet_points", "casual", "formal"]
    return {
        "status": "AI style test",
        "available_styles": styles
    }

@router.get("/risk-levels-test")
def risk_levels_test():
    levels = ["LOW", "NORMAL", "HIGH", "EXTREME"]
    return {
        "status": "Risk levels test",
        "available_levels": levels
    }

@router.put("/update-style")
def update_style(new_style: str):
    # This is a placeholder for updating the style in a real application
    return {
        "status": "Style update test",
        "new_style": new_style,
        "message": f"AI response style updated to '{new_style}' (simulated)"
    }

@router.get("/extreme-weather-test")
def extreme_weather_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 45,
            "humidity": 90,
            "wind_speed": 30,
            "weather_main": "Heatwave",
            "visibility": 1000
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "Extreme weather test",
        "input": sample_weather,
        "rules_result": rules_result
    }

@router.get("/cold-weather-test")
def cold_weather_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": -5,
            "humidity": 60,
            "wind_speed": 15,
            "weather_main": "Snow",
            "visibility": 500
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "Cold weather test",
        "input": sample_weather,
        "rules_result": rules_result
    }

@router.get("/high-humidity-test")
def high_humidity_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 25,
            "humidity": 85,
            "wind_speed": 5,
            "weather_main": "Rain",
            "visibility": 3000
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "High humidity test",
        "input": sample_weather,
        "rules_result": rules_result
    }


@router.get("/strong-wind-test")
def strong_wind_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 20,
            "humidity": 50,
            "wind_speed": 25,
            "weather_main": "Windy",
            "visibility": 4000
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "Strong wind test",
        "input": sample_weather,
        "rules_result": rules_result
    }

@router.get("/combined-risk-test")
def combined_risk_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 40,
            "humidity": 90,
            "wind_speed": 20,
            "weather_main": "Heatwave with strong winds",
            "visibility": 2000
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "Combined risk test",
        "input": sample_weather,
        "rules_result": rules_result
    }

@router.get("/no-risk-test")
def no_risk_test():
    sample_weather = {
        "type": "current",
        "data": {
            "temperature": 22,
            "humidity": 50,
            "wind_speed": 5,
            "weather_main": "Clear",
            "visibility": 10000
        }
    }
    rules_result = WeatherRulesEngine.analyze(sample_weather)
    return {
        "status": "No risk test",
        "input": sample_weather,
        "rules_result": rules_result
    }

@router.get("/all")
def all_tests():
    return {
        "status": "All tests",
        "tests": [
            style_test(),
            risk_levels_test(),
            extreme_weather_test(),
            cold_weather_test(),
            high_humidity_test(),
            strong_wind_test(),
            combined_risk_test(),
            no_risk_test()
        ]
    }

@router.get("/all-ai-styles")
async def all_ai_styles():
    styles = ["detailed", "concise", "bullet_points", "casual", "formal"]
    results = {}
    for style in styles:
        sample_weather = {
            "type": "current",
            "data": {
                "temperature": 30,
                "humidity": 70,
                "wind_speed": 10,
                "weather_main": "Sunny",
                "visibility": 8000
            }
        }
        ai_result = await AIService.analyze_weather(sample_weather, style)
        results[style] = ai_result
    return {
        "status": "All AI styles test",
        "results": results
    }

@router.get("/all-rules-combinations")
def all_rules_combinations():
    combinations = [
        {"temperature": 35, "humidity": 80, "wind_speed": 20},
        {"temperature": -5, "humidity": 60, "wind_speed": 15},
        {"temperature": 25, "humidity": 85, "wind_speed": 5},
        {"temperature": 20, "humidity": 50, "wind_speed": 25},
        {"temperature": 40, "humidity": 90, "wind_speed": 20},
        {"temperature": 22, "humidity": 50, "wind_speed": 5}
    ]
    results = {}
    for i, combo in enumerate(combinations):
        weather = {
            "type": "current",
            "data": combo
        }
        rules_result = WeatherRulesEngine.analyze(weather)
        results[f"combination_{i+1}"] = rules_result
    return {
        "status": "All rules combinations test",
        "results": results
    }
