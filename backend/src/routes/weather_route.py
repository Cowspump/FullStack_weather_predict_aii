from fastapi import APIRouter
from services.weather_service import get_weather_data
from services.gpt_service import ask_gpt

router = APIRouter()


@router.get("/weather")
async def get_weather():
    prompt = f"""
    На основе следующих погодных данных подскажи, как лучше одеться сегодня, стоит ли брать зонт, и есть ли смысл брать с собой тёплую одежду. Учитывай комфорт, практичность и возможные осадки.
    Вот данные:
    {get_weather_data()}

    Напиши ответ простым и понятным языком. Если есть вероятность дождя — обязательно упомяни это. Также скажи, нужно ли надеть тёплую куртку, кофту или подойдёт лёгкая одежда.
    """

    return ask_gpt(prompt)
