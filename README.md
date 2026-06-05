
---

```markdown id="w9qk3p"
** Weather AI — Intelligent Weather Analysis Platform***

![Status](https://img.shields.io/badge/status-production--ready-success)
![Architecture](https://img.shields.io/badge/architecture-hybrid%20AI%20%2B%20rules-blueviolet)
![Backend](https://img.shields.io/badge/backend-FastAPI-009688)
![Frontend](https://img.shields.io/badge/frontend-React-61DAFB)
![Deployment](https://img.shields.io/badge/deployment-Vercel%20%7C%20Render-blue)

---

## 1. Project Overview

Weather AI is a full-stack weather intelligence system designed to demonstrate **API integration, system design, and data transformation capabilities** using the Weather AI Developer Platform.

The application converts raw meteorological inputs into **structured forecasts, deterministic risk evaluation, and AI-generated interpretations**.

The system is designed with a **hybrid architecture combining rule-based logic and LLM-driven reasoning**.

---

## 2. Live Deployment

- Frontend: https://your-vercel-app.vercel.app  
- Backend API: https://weather-ai-5h6m.onrender.com  
- API Reference: https://weather-ai.co/docs  

---

## 3. System Objectives

This project was built to demonstrate:

- Robust external API consumption
- Structured backend service design
- Separation of deterministic and probabilistic logic
- Scalable frontend architecture
- Production-ready deployment configuration

---

## 4. System Architecture

### High-Level Design

```

Frontend (React - Vercel)
│
│ HTTPS (Axios Client)
▼
Backend API (FastAPI - Render)
│
├── Rule-Based Engine (Deterministic Logic)
│
├── AI Engine (Claude / Anthropic)
│
▼
Unified Response Layer
│
▼
Structured Weather Intelligence Payload

```

### Design Principles

- Separation of concerns (UI / API / AI / Rules)
- Stateless backend architecture
- Environment-driven configuration
- Modular service-based backend design
- Single responsibility components

---

## 5. Core Features

### Weather Intelligence Engine
- Multi-parameter weather analysis (lat/lon/days)
- Structured forecast aggregation
- Normalized weather response schema

### AI Interpretation Layer
- Natural language weather summaries
- Context-aware environmental reasoning
- Risk explanation and forecasting insights

### Rule-Based Decision Engine
- Deterministic weather classification
- Risk scoring system
- Consistent evaluation logic independent of AI

### Interactive Mapping Interface
- Click-based geolocation selection
- Real-time coordinate binding
- Seamless API integration

### Visualization Layer
- Forecast trend rendering
- Weather condition cards
- Responsive dashboard layout

---

## 6. Tech Stack

### Frontend
- React (Vite)
- Axios (API abstraction layer)
- Tailwind CSS
- React Leaflet
- Recharts

### Backend
- FastAPI (Python)
- Uvicorn ASGI server
- Anthropic Claude API integration
- Modular service architecture

### Deployment
- Vercel (Frontend)
- Render (Backend)

---

## 7. Backend API Design

### Endpoint

```

POST /weather/analysis

````

### Request Schema

```json
{
  "lat": 3.848,
  "lon": 11.502,
  "days": 1,
  "units": "metric",
  "mode": "hybrid",
  "ai_style": "detailed"
}
````

### Response Structure

* `weather` → raw forecast data
* `rules` → deterministic evaluation output
* `ai` → LLM-generated interpretation
* `mode` → execution mode (rules / ai / hybrid)

---

## 8. Frontend Architecture

### Structure

* `/api` → centralized Axios client
* `/pages` → application screens
* `/components` → reusable UI modules
* `/hooks` → state and logic abstraction (if extended)

### Data Flow

User Input → API Request → Backend Processing → Unified Response → UI Rendering

---

## 9. Environment Configuration

### Backend (.env)

```env
ANTHROPIC_API_KEY=your_api_key
```

### Frontend (.env)

```env
VITE_API_URL=https://weather-ai-5h6m.onrender.com
```

---

## 10. Engineering Considerations

* Strict separation between AI and deterministic logic
* Centralized API communication layer
* Environment-based deployment safety
* Stateless backend design for horizontal scalability
* Component-driven frontend architecture

---

## 11. Known Limitations

* No persistent storage layer (stateless design only)
* No authentication layer implemented
* No caching layer for repeated requests
* Leaflet marker asset optimization required

---

## 12. Future Improvements

* Introduce Redis caching for API optimization
* Add authentication + rate limiting
* Implement CI/CD pipeline (GitHub Actions)
* Add historical weather analytics module
* Improve AI prompt tuning for consistency

---

## 13. Author

**Ndelle Herbert**

---

## 14. Submission Context

This project was completed within a 48-hour technical assessment window.

The implementation prioritizes:

* System design clarity
* API integration correctness
* Modular architecture
* Production deployment readiness
* Maintainable full-stack structure


