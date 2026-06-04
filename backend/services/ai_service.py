import json
import re
import anthropic
from core.config import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)


class AIService:

    @staticmethod
    async def analyze_weather(weather: dict, style: str):

        clean_weather = weather.get("data")

        prompt = f"""
You are a professional meteorologist AI.

IMPORTANT:
- Return ONLY valid JSON
- No markdown
- No backticks
- No explanations

JSON FORMAT:
{{
  "summary": "short weather summary",
  "risk_level": "LOW | NORMAL | HIGH | EXTREME",
  "recommendations": ["...", "...", "..."],
  "insight": "detailed explanation",
  "style": "{style}"
}}

Style instruction:
{style}

Weather data:
{clean_weather}
"""

        res = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=800,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}]
        )

        text = res.content[0].text

        # -------------------------
        # CLEAN OUTPUT (CRITICAL FIX)
        # -------------------------

        # remove markdown code blocks if present
        text = re.sub(r"```json", "", text)
        text = re.sub(r"```", "", text).strip()

        # extract JSON safely
        try:
            start = text.find("{")
            end = text.rfind("}") + 1

            if start != -1 and end != -1:
                json_text = text[start:end]
                return json.loads(json_text)

        except json.JSONDecodeError:
            pass

        # fallback (never crash API)
        return {
            "summary": "AI returned invalid JSON",
            "risk_level": "UNKNOWN",
            "recommendations": [],
            "insight": text,
            "style": style
        }