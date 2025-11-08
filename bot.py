from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# вставь токен твоего бота сюда
BOT_TOKEN = "8202829469:AAGB-dGzg8FLQQJBKZ65OspQcA790h3ukrY"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="💰 Открыть Crypto Testnet",
            url="https://t.me/CryptoTestnetBot/crypto"  # ссылка на оригинальный WebApp
        )
    )
    await message.answer(
        "Добро пожаловать в MyCrypto Wallet!\n\nНажми кнопку ниже, чтобы открыть кошелёк:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp)
