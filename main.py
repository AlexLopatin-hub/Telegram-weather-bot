import asyncio
import logging
import pywttr

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7527348944:AAHPqtbr7qAFPGoSVf5w9vdYEPDYb5ZYX-8"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_weather_text() -> str:
    weather = pywttr.get_weather('Saint-Petersburg', pywttr.Language.RU)
    date = weather.weather[0].date
    temperature = weather.weather[0].avgtemp_c
    sunrise_time = weather.weather[0].astronomy[0].sunrise
    sunset_time = weather.weather[0].astronomy[0].sunset
    res = (f'Дата: {date}\n'
           f'Температура: {temperature} °С\n'
           f'Время рассвета: {sunrise_time}\n'
           f'Время заката: {sunset_time}\n')
    return res


@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="/weather")]], resize_keyboard=True)
    await message.answer("Введи команду /weather, чтобы получить погоду в Санкт-Петербурге.", reply_markup=keyboard)


@dp.message(Command("weather"))
async def type_weather(message: types.Message):
    await message.answer(get_weather_text(), reply_markup=types.ReplyKeyboardRemove())


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
