from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from src.api.api_functions import get_weather
import requests
from src.keyboards.bot_keyboard import get_location_keyboard

router = Router()


@router.message(Command("start"))
async def cmd(message: Message):
    location_keyboard = get_location_keyboard()
    await message.answer("Привет! Нажми на кнопку ниже, чтобы отправить свою геолокацию:",
                         reply_markup=location_keyboard)


@router.message(F.location)
async def handle_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(
        f"широта: {latitude}\n"
        f"долгота: {longitude}\n"
    )

    weather_data = get_weather(latitude, longitude)

    if weather_data:
        text = f"Город: {weather_data['city']}\nТемпература: {weather_data['temperature']}C\nВлажность: {weather_data['humidity']}%\nВетер: {weather_data['wind_speed']} м/с\n{weather_data['description']}"
        await message.answer(text)
    else:
        await message.answer("Не удалось получить погоду")