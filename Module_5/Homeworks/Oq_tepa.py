import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, KeyboardButton, WebAppInfo, KeyboardButtonPollType,InlineKeyboardButton,CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

def key_button_build(texts : list , size):
    rkb = KeyboardButtonPollType()
    rkb.add(*[KeyboardButton(text=text) for text in texts])
    rkb.adjust(*size)
    rkb = rkb.as_markup()
    return rkb

TOKEN = "7484603263:AAFL9qlzDCar6f4aeA5qIZn9KSWFxHOqAGA"
cap="OqTepa Lavash работает на быстрорастущем рынке Республики Узбекистан :Продукты питания и напитки.\n\nБолее подробно 👇\nhttps://oqtepalavash.uz"
dp = Dispatcher()
@dp.message(F.text=='🏠 Главное меню')
@dp.message(F.text=='Назад ↩️')
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='🏢 О компании'),
        KeyboardButton(text='💼 Вакансии') ,
        KeyboardButton(text='Меню') ,
        KeyboardButton(text='💬 Отзывы и предложения') ,
        KeyboardButton(text='📞 Контакты/Адрес') ,
        KeyboardButton(text='🇺🇿/🇷🇺 Язык')
    )
    rkb.adjust(1,1,1,1,2)
    rkb = rkb.as_markup(resize_keyboard=True , one_time_keyboard=True)
    await message.answer_photo(photo='AgACAgQAAxkBAAEdJRxnruzNywV0i_gtmVtZnmrQYWOkSgADrjEbF2HtUrrMKlTFZ8cQAQADAgADcwADNgQ' , reply_markup=rkb)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
@dp.message(F.text=='🏢 О компании')
async def hand_first_command(message:Message):
    await message.answer_photo(photo='AgACAgQAAxkBAAEdJR5nru-7MbMHWccGRdNVDEElihzzGwADrjEbvKLsUuJ6pjtpX1DeAQADAgADcwADNgQ',caption=cap)
@dp.message(F.text=='Меню')
async def hand_second_command(message:Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='🏠 Главное меню'),
        KeyboardButton(text='Назад ↩️')
    )
    rkb.adjust( 2)
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await message.answer_photo(photo='AgACAgQAAxkBAAEdJSRnrvHJ0JUCTNaFrd09GOq7Frdu0AACJK4xGxOf7FKOhlJkRWWodQEAAwIAA3MAAzYE',caption='https://oqtepalavash.uz/',reply_markup=rkb)

@dp.message(F.text=='💬 Отзывы и предложения')
async def hand_third_command(message:Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='Назад ↩️')
    )
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await message.answer(text='Напишите нам сюда, мы обязательно ответим.',reply_markup=rkb)
@dp.message(F.text=='📞 Контакты/Адрес')
async def hand_four_command(message:Message):
    await message.answer('⏰ Рабочие часы:\nПн-Пт: 09:00 – 18:00\nСб-Вс: Закрыто')
    await message.answer_location(latitude=41.33306,longitude=69.24295)

@dp.message(F.text=='🇺🇿/🇷🇺 Язык')
async def hand_five_command(message:Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='🇺🇿 Ozbekcha'),
        KeyboardButton(text='🇷🇺 Ruscha'),
        KeyboardButton(text='Назад ↩️')
    )
    rkb.adjust( 2,1)
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await message.answer(text='Смена языка',reply_markup=rkb)

@dp.message(F.text=='Orqaga↩️')
@dp.message(F.text=='💼 Вакансии')
async def hand_six_command(message:Message):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
       KeyboardButton(text='Ташкент'),
       KeyboardButton(text='Фергана'),
       KeyboardButton(text='Самарканд'),
       KeyboardButton(text='Таш.область'),
        KeyboardButton(text='🏠 Главное меню'),
        KeyboardButton(text='Назад ↩️')
    )
    rkb.adjust(2,2,2)
    rkb=rkb.as_markup(resize_keyboard=True,one_time_keyboard=True)
    await message.answer(text='Присоединяйтесь в команду Oqtepa Lavash \n Выберите город', reply_markup=rkb)

@dp.message(F.text=='Ташкент')
async def hand_seven_command(message:Message):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
       KeyboardButton(text='Uchtepa'),
       KeyboardButton(text='Olmazor'),
       KeyboardButton(text='Sergili'),
       KeyboardButton(text='Yangihayot'),
        KeyboardButton(text='Yakkasaroy'),
        KeyboardButton(text= 'Mirzo Ulugbe'),
        KeyboardButton(text= 'Yunsobod'),
        KeyboardButton(text= 'Shayxontohur'),
        KeyboardButton(text= 'Chilanzor'),
        KeyboardButton(text= 'Bektemir'),
        KeyboardButton(text= '🏠 Главное меню'),
        KeyboardButton(text= 'Orqaga↩️'),
    )
    rkb.adjust(2,2,2,2)
    rkb=rkb.as_markup(resize_keyboard=True,one_time_keyboard=True)
    await message.answer(text='Выберите район',reply_markup=rkb)

@dp.message(F.text=='Фергана')
async def hand_eight_command(message:Message):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
       KeyboardButton(text='Oshpaz'),
        KeyboardButton(text='Idish yuvuchi'),
        KeyboardButton(text='🏠 Главное меню'),
        KeyboardButton(text='Orqaga↩️'),
    )
    rkb.adjust(2,2)
    rkb=rkb.as_markup(resize_keyboard=True,one_time_keyboard=True)
    await message.answer(text='💼 Выберите интересующую Вас вакансию',reply_markup=rkb)

@dp.message(F.text=='Самарканд')
async def hand_nine_command(message:Message):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
       KeyboardButton(text='Oshpaz'),
        KeyboardButton(text='Idish yuvuchi'),
        KeyboardButton(text='Kassir'),
        KeyboardButton(text='Tozalovchi'),
        KeyboardButton(text='🏠 Главное меню'),
        KeyboardButton(text='Orqaga↩️'),
    )
    rkb.adjust(2,2)
    rkb=rkb.as_markup(resize_keyboard=True,one_time_keyboard=True)
    await message.answer(text='💼 Выберите интересующую Вас вакансию',reply_markup=rkb)

@dp.message(F.text=='Таш.область')
async def hand_teen_command(message:Message):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
       KeyboardButton(text='Toshkent viloyat'),
       KeyboardButton(text='Bostonlig'),
       KeyboardButton(text='Zangata'),
       KeyboardButton(text='Yangiyol'),
        KeyboardButton(text='Yuqorichirchiq'),
        KeyboardButton(text= 'Chinoz'),
        KeyboardButton(text= '🏠 Главное меню'),
        KeyboardButton(text= 'Orqaga↩️'),
    )
    rkb.adjust(2,2,2)
    rkb=rkb.as_markup(resize_keyboard=True,one_time_keyboard=True)
    await message.answer(text='Выберите район',reply_markup=rkb)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



#==========================================================================================
# @dp.message(Command('test'))
# async def test_func(message:Message):
#     rkb=ReplyKeyboardBuilder()
#     rkb.add(
#        KeyboardButton(text='btn1'),
#        KeyboardButton(text='btn2',request_contact=True),
#        KeyboardButton(text='btn3',request_location=True),
#        KeyboardButton(text='btn4',web_app=WebAppInfo(url='https://www.youtube.com')),
#     )
#     rkb.adjust(1,1,1,1)
#     rkb=rkb.as_markup(resize_keyboard=True,one_time_keyboard=True)
#     await message.answer('Test qiling', reply_markup=rkb)