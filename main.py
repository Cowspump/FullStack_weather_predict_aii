import uvicorn, os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

from datetime import datetime,timedelta
from openai import OpenAI
import requests



def get_current_time()->list[str]:
    hours: list[str] = []

    # Get current time with timezone info
    now = datetime.now().astimezone()

    now = now.replace(minute=0, second=0, microsecond=0)

    for hour_later in range(0, 6):
        cur_time = now + timedelta(hours=hour_later)
        cur_time_iso = cur_time.isoformat()
        hours.append(cur_time_iso)

    # return List with (current hour - five hours later) time in iso format
    # we can use them as a key in yandex weather api

    # ["data"]["weatherByPoint"]["forecast"]["days"][0]["hours"]
    # from yandex weather api it will return list with dicts with time as key.

    return hours



def get_weather_data()->str:
    # code about parsing data with yandex api
    access_key = os.environ.get("YANDEX_API_KEY")
    headers = {
        "X-Yandex-Weather-Key": access_key
    }
    query = """{
      weatherByPoint(request: { lat: 43.238949, lon: 76.889709 }) {
        forecast {
            days(limit:1){
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


        ydx_response = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query})
        json_ydx_response = json.loads(ydx_response.text)

        now_data = json_ydx_response["data"]["weatherByPoint"]["forecast"]["days"][0]["hours"]

        current_time = get_current_time()
        data_for_prompt = []

        for cur_hour in now_data:
            if cur_hour["time"] in current_time:
                data_for_prompt.append(cur_hour)

        json_data = json.dumps(data_for_prompt)

        return json_data


    except Exception as e:
        return json.dumps({"error": str(e)})





def ask_gpt(prompt: str) -> str:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key= os.environ.get("OPEN_AI_API_KEY")
    )

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "",
                },
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )

        return response.choices[0].message.content
    except Exception as e:
        return json.dumps({"error": str(e)})




#backend Fastapi
app = FastAPI()

@app.get("/weather", tags=["Start_processes"])
async def get_weather():

    prompt = f"""
    На основе следующих погодных данных подскажи, как лучше одеться сегодня, стоит ли брать зонт, и есть ли смысл брать с собой тёплую одежду. Учитывай комфорт, практичность и возможные осадки.
    Вот данные:
    {get_weather_data()}

    Напиши ответ простым и понятным языком. Если есть вероятность дождя — обязательно упомяни это. Также скажи, нужно ли надеть тёплую куртку, кофту или подойдёт лёгкая одежда.
    """

    return ask_gpt(prompt)


#pooling
if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
