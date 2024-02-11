from aiogram import Bot, Dispatcher, executor, types
from TOKEN import TOKEN_API


bot = Bot(TOKEN_API) # создаем бота с нашим токеном
dp = Dispatcher(bot) # анализ и инициализая всех входящих апдейтов, функциональность нашего бота


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # ответить на сообщение


if __name__ == '__main__':
    executor.start_polling(dp) # запускаем бота в режиме пулинга