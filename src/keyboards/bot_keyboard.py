from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_location_keyboard():
    location_button = KeyboardButton(text="Запросить геолокацию",request_location=True)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[location_button]],
        resize_keyboard=True,
        one_time_keyboard=False
    )

    return keyboard