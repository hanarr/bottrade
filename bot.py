from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import requests
import os

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=8092612300:AAH0rz8m6v9C5G2KD5Car-SffIo9M9cnoyc)
dp = Dispatcher(bot)

def get_currency_rate(symbol):
    url = f"https://api.exchangerate.host/latest?base=USD"
    data = requests.get(url).json()
    return round(data["rates"].get(symbol.upper(), 0), 2)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Введи /usd или /eur чтобы узнать курс валют.")

@dp.message_handler(commands=["usd"])
async def usd(message: types.Message):
    rate = get_currency_rate("RUB")
    await message.answer(f"Курс USD: {rate} ₽", reply_markup=buy_button())

@dp.message_handler(commands=["eur"])
async def eur(message: types.Message):
    url = "https://api.exchangerate.host/latest?base=EUR"
    data = requests.get(url).json()
    rate = round(data["rates"].get("RUB", 0), 2)
    await message.answer(f"Курс EUR: {rate} ₽", reply_markup=buy_button())

def buy_button():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("💳 Купить крипту", url="https://www.binance.com"))
    return kb

if __name__ == "__main__":
    executor.start_polling(dp)
