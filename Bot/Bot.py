from aiogram import Bot, Dispatcher, executor, types
from TOKEN import TOKEN_API
from model import get_model, TextCNN
from Vocabulary import Vocabulary
import torch
from database import engine
import pandas as pd



bot = Bot(TOKEN_API) # создаем бота с нашим токеном
dp = Dispatcher(bot) # анализ и инициализая всех входящих апдейтов, функциональность нашего бота

model = get_model().to('cpu') # инициализируем нашу модель

texts = pd.read_sql(
    """
        SELECT *
        FROM public.data_for_voc
    """,
    con=engine
)['text'] # берем из наших данных только тексты

voc = Vocabulary(texts.values, 4) # экземпляр класса словарь
pad_idx = len(voc.vocabulary) # длина словаря

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text) # ответить на сообщение

@dp.message_handler()
async def echo(message: types.Message):
    text_list = voc.encode(message.text)
    for_model = torch.tensor(text_list + [pad_idx] * (4 - len(text_list))).unsqueeze(0) # максимальное ядро свертки 4
    answer = int(torch.round(torch.sigmoid(model(for_model)[0][0])))

    if answer:
        await message.answer(text='Spam')
    else:
        await message.answer(text='Ham')


if __name__ == '__main__':
    executor.start_polling(dp) # запускаем бота в режиме пулинга