from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.weather import router

app = FastAPI(
    title="Weather AI System"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://weather-ai-1rby.vercel.app",
        "https://*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(router)

@app.get("/")
def home():
    return {
        "status": "Weather AI running"
    }



