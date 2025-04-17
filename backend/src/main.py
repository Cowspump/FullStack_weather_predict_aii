import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.weather_route import router as weather_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342", "http://127.0.0.1:63342"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(weather_router, tags=["Start_processes"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
