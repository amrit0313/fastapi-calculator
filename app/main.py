from fastapi import FastAPI
from app.routes import calculator, converter
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)


app.include_router(calculator.router, prefix="/calc")
app.include_router(converter.router, prefix="/convert")
