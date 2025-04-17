import uvicorn
from fastapi import FastAPI
from routes.weather_route import router as weather_router

app = FastAPI()
app.include_router(weather_router, tags=["Start_processes"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
