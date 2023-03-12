from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Бот для руслана")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Он пидорас")


@dp.message_handler()
async def description_command(message: types.Message):

    #присваивание значение к переменной
    reply1 = message.text 

    # создание подключения к таблице
    conn = sqlite3.connect('db1.db')
    cur = conn.cursor()
    
    # получение данных из таблицы ориентируясь на ячейку question_user и забирая значение ячейки answer_user(таблица question)
    [que] = cur.execute('select answer_user from question where question_user = ?', (reply1, ))
    
    # закрытие таблицы
    conn.commit()
    #отправка значений с нашим значением
    await bot.send_message(chat_id=message.from_user.id,
                           text=que[0],
                           parse_mode="HTML")


# проверка загрузки
if __name__ == '__main__':
    executor.start_polling(dp)
