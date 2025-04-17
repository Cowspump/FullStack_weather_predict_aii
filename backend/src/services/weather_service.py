import json
import requests
from services.time_service import get_current_time
from utils.config import YANDEX_API_KEY

def get_weather_data() -> str:
    headers = {
        "X-Yandex-Weather-Key": YANDEX_API_KEY
    }
    query = """{
      weatherByPoint(request: { lat: 43.238949, lon: 76.889709 }) {
        forecast {
          days(limit: 1) {
            hours {
              time
              temperature
              precType
              precStrength
              windSpeed
              cloudiness
              icon(format: SVG, theme: LIGHT)
            }
          }
        }
      }
    }"""

    try:
        ydx_response = requests.post(
            'https://api.weather.yandex.ru/graphql/query',
            headers=headers,
            json={'query': query}
        )
        json_ydx_response = json.loads(ydx_response.text)
        now_data = json_ydx_response["data"]["weatherByPoint"]["forecast"]["days"][0]["hours"]
        current_time = get_current_time()
        data_for_prompt = [hour for hour in now_data if hour["time"] in current_time]

        return json.dumps(data_for_prompt)

    except Exception as e:
        return json.dumps({"error": str(e)})
