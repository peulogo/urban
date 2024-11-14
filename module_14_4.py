from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

products = get_all_products()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text=f"Продукт {i}", callback_data="product_buying") for i in range(1, 5)]
])

kb.row(button, button2)
kb.add(button3)
urls = [
    'https://avatars.mds.yandex.net/get-mpic/5238069/img_id1895807587137189478.jpeg/900x1200',
    'https://avatars.mds.yandex.net/get-mpic/1374520/img_id4349174740567551666.jpeg/900x1200',
    'https://avatars.mds.yandex.net/get-mpic/6458782/img_id2581220411343816868.png/900x1200',
    'https://avatars.mds.yandex.net/get-mpic/5194288/2a000001902fc1644edb4708fbb1455f36e1/900x1200'
]

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):

    for i, product, desc, price in products:
        await message.answer_photo(urls[i-1])
        await message.answer(f'Название: {product} | Описание: {desc}| Цена: {price}')
        await asyncio.sleep(0.5)
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()



@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию", reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 х рост (см) - 5 х возраст (г) - 161')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer(f'Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Ваша норма калорий {result}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
