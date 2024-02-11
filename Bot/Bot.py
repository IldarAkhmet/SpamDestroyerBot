from aiogram import Bot, Dispatcher, executor, types
from TOKEN import TOKEN_API
from model import get_model
import Vocabulary
import torch


bot = Bot(TOKEN_API) # создаем бота с нашим токеном
dp = Dispatcher(bot) # анализ и инициализая всех входящих апдейтов, функциональность нашего бота

model = get_model() # инициализируем нашу модель

voc = Vocabulary() # экземпляр класса словарь
pad_idx = len(voc.vocabulary) # длина словаря

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text) # ответить на сообщение

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    text_list = voc.encode(message.text)
    for_model = torch.tensor(text_list + [pad_idx] * (1043 - len(text_list)))
    await message.answer(text='Иди нахуй, Рамис')


if __name__ == '__main__':
    executor.start_polling(dp) # запускаем бота в режиме пулинга