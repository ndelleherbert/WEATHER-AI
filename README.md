Here is a **fully functional, production-ready `README.md`** for your Weather AI System (clean, structured, and suitable for GitHub + portfolio + job submission).

---

# 🌦 Weather AI System

A **Hybrid Intelligence Weather API** built with FastAPI that combines:

* 🌤 Real-time weather data (OpenWeatherMap)
* 🧠 Rule-based decision engine
* 🤖 AI-powered weather interpretation (Anthropic Claude)
* 🔀 Hybrid reasoning system (Rules + AI)

---

## 📌 Live Concept

This system simulates real-world **intelligent weather decision-making**, where:

* Rules provide instant deterministic analysis
* AI provides contextual understanding
* Hybrid mode merges both for best accuracy

---

# 🏗 System Architecture

```
Frontend (React + Vite)
        ↓
FastAPI Backend
        ↓
Weather Service Layer
        ↓
OpenWeatherMap API
        ↓
Rule Engine (Fast logic)
        ↓
AI Engine (Claude)
        ↓
Hybrid Response System
```

---

# 🚀 Features

## 🌍 Weather Data

* Current weather data
* 5-day forecast support
* Clean normalized API responses

## 🧠 Rule-Based Intelligence

* Heat risk detection
* Cold risk detection
* Wind hazard analysis
* Humidity-based warnings

## 🤖 AI Intelligence

* Natural language weather insights
* Risk classification (LOW → EXTREME)
* Human-readable recommendations
* Multi-style responses

## 🔀 Hybrid Mode

Combines:

* ⚡ Fast rule-based system
* 🧠 Deep AI reasoning

---

# 📡 API Base URL

```
http://127.0.0.1:8000
```

---

# 🔥 Main Endpoint

## 📍 POST `/weather/analysis`

Analyze weather using rules, AI, or hybrid mode.

---

## 📥 Request Body

```json
{
  "lat": 3.848,
  "lon": 11.502,
  "days": 1,
  "units": "metric",
  "mode": "hybrid",
  "ai_style": "detailed"
}
```

---

## 📊 Request Fields

| Field    | Type   | Description                  |
| -------- | ------ | ---------------------------- |
| lat      | float  | Latitude                     |
| lon      | float  | Longitude                    |
| days     | int    | Forecast days (1–5)          |
| units    | string | metric / imperial / standard |
| mode     | string | rules / ai / hybrid          |
| ai_style | string | AI response style            |

---

# ⚙️ Response Modes

## 🟢 Rules Mode

```json
{
  "mode": "rules",
  "result": {
    "risk": "HIGH HEAT",
    "advice": "Avoid outdoor activity"
  }
}
```

---

## 🤖 AI Mode

```json
{
  "mode": "ai",
  "result": {
    "summary": "Hot and humid conditions",
    "risk_level": "HIGH",
    "recommendations": ["Stay hydrated"],
    "insight": "Detailed explanation"
  }
}
```

---

## 🔀 Hybrid Mode

```json
{
  "mode": "hybrid",
  "rules": { "...": "..." },
  "ai": { "...": "..." }
}
```

---

# 🌤 Weather Service

Powered by:

OpenWeatherMap

### Features:

* Real-time weather
* Forecast support
* Data normalization layer
* Clean structured output

---

# 🧠 AI Engine

Powered by:

Anthropic

### Responsibilities:

* Weather interpretation
* Risk classification
* Natural language insights
* Structured JSON output enforcement

---

# 🧠 Rule Engine Logic

## 🔥 Heat Risk

```
temperature ≥ 35°C → HIGH HEAT
```

## ❄ Cold Risk

```
temperature ≤ 10°C → COLD
```

## 💧 Humidity Risk

```
humidity > 80% → discomfort warning
```

## 🌪 Wind Risk

```
wind_speed > 10 m/s → strong wind alert
```

---

# 🔬 Test Endpoints

## 🧪 System Tests

| Endpoint               | Description      |
| ---------------------- | ---------------- |
| `/weather/test`        | Health check     |
| `/weather/rules-test`  | Rule engine test |
| `/weather/ai-test`     | AI test          |
| `/weather/hybrid-test` | Combined test    |
| `/weather/error-test`  | Error simulation |

---

## 🌡 Weather Scenarios

* `/weather/extreme-weather-test`
* `/weather/cold-weather-test`
* `/weather/high-humidity-test`
* `/weather/strong-wind-test`
* `/weather/combined-risk-test`
* `/weather/no-risk-test`

---

## 🤖 AI Style Tests

```
/weather/all-ai-styles
```

Supports:

* detailed
* concise
* bullet_points
* casual
* formal

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/weather-ai.git
cd weather-ai
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

## 3. Install Dependencies

```bash
pip install fastapi uvicorn httpx python-dotenv anthropic
```

---

## 🔐 Environment Variables

Create `.env` file:

```env
WEATHER_API_KEY=your_openweather_key
ANTHROPIC_API_KEY=your_claude_key
```

---

# ▶️ Run Server

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# 🌐 Frontend Integration (Optional)

Recommended stack:

* React (Vite)
* Tailwind CSS
* Recharts

API endpoint:

```
/weather/analysis
```

---

# 🧩 Tech Stack

* FastAPI
* httpx (async requests)
* Pydantic
* Anthropic Claude API
* OpenWeatherMap API
* Python-dotenv

---

# 🧠 Key Engineering Concepts

## ✔ Hybrid AI Architecture

Combines:

* deterministic logic (rules)
* probabilistic reasoning (AI)

## ✔ Clean Architecture

* API Layer
* Service Layer
* Logic Layer
* AI Layer

## ✔ Fault Tolerance

* AI fallback system
* API error handling
* Safe JSON parsing

## ✔ Data Abstraction

Frontend never touches raw API responses

---

# 📈 Future Improvements

* 🔴 Redis caching layer
* 🗄 Database logging (PostgreSQL)
* 🔔 Real-time alerts (WebSockets)
* 🔐 JWT authentication
* 📱 Mobile app integration
* 🐳 Docker deployment

---

# 👨‍💻 Author

**Ndelle Herbert**

---

# 📜 License

MIT License

---

# 🔥 Summary

This project demonstrates a **real-world hybrid AI system** combining:

* Weather APIs
* Rule-based intelligence
* Large Language Models
* Clean backend architecture

It is suitable for:

* AI portfolio projects
* backend engineering interviews
* production system prototypes

---

