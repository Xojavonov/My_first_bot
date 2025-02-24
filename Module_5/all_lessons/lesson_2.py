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
TOKEN = "7484603263:AAHAHDXPrkZhOR0wy7ctYoEZI-e5doJNzQw"

dp = Dispatcher()

@dp.message(CommandStart())
@dp.message(F.text=='Ortga qaytish')
async def command_start_handler(message: Message) -> None:
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Shaxsiy kabinet"),
        KeyboardButton(text='Eventlar') ,
    )
    rkb.adjust(1,1)
    rkb = rkb.as_markup(resize_keyboard=True , one_time_keyboard=True)
    await message.answer("Asosiy menyu" , reply_markup=rkb)

@dp.message(F.text=='Eventlar')
async def hand_message(mess:Message):
    await mess.answer('Hozir birorta eventlar mavjud emas')

@dp.message(F.text=='Shaxsiy kabinet')
async def check_message(mess:Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Uyga vazifa"),
        KeyboardButton(text='Ozlashtirish'),
        KeyboardButton(text='Ortga qaytish'),
    )
    rkb.adjust(1, 1,1)
    rkb = rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
    await mess.answer("Tanlang", reply_markup=rkb)
@dp.message(Command('region'))
async def inline_button_show(message : Message):
    ikb = InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text="Toshkent" , callback_data="T"),
        InlineKeyboardButton(text='Samarqand',callback_data='S'),
        InlineKeyboardButton(text='Xiva',callback_data='X'),
        InlineKeyboardButton(text='Namangan',callback_data='N'),
        InlineKeyboardButton(text='Jizzax',callback_data='J'),
        InlineKeyboardButton(text='Navoi',callback_data='N'),
        InlineKeyboardButton(text='Xorazm ',callback_data='Xo'),
        InlineKeyboardButton(text='Surxondaryo',callback_data='Su'),
        InlineKeyboardButton(text='Qashqadaryo',callback_data='Q'),
        InlineKeyboardButton(text='Buxoro',callback_data='B'),
        InlineKeyboardButton(text='Fargʻona ',callback_data='b'),
        InlineKeyboardButton(text='Andijon  ',callback_data='A'),
    )
    ikb.adjust(2,2,2,2,2,2)
    ikb = ikb.as_markup()
    await message.answer(text="Tanlang" , reply_markup=ikb)
@dp.callback_query(F.data=='T')
async def send_Toshkent(call:CallbackQuery):
    ikb=InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text='Sergili',callback_data='ser'),
        InlineKeyboardButton(text='Shayxontohur',callback_data='shay')
    )
    ikb.adjust(2)
    ikb=ikb.as_markup()
    await call.message.answer('Tumanlar',reply_markup=ikb)
@dp.callback_query(F.data=='S')
async def send_Samarqand(call:CallbackQuery):
    ikb=InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text='Samarqant',callback_data='sam'),
        InlineKeyboardButton(text='Urgut',callback_data='ur')
    )
    ikb.adjust(2)
    ikb=ikb.as_markup()
    await call.answer('Tumanlar',reply_markup=ikb)
@dp.callback_query(F.data=='X')
async def send_Xiva(call:CallbackQuery):
    ikb=InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text='Xiva',callback_data='xiv'),
        InlineKeyboardButton(text='Bogbot',callback_data='bog')
    )
    ikb.adjust(2)
    ikb=ikb.as_markup()
    await call.answer('Tumanlar',reply_markup=ikb)
@dp.callback_query(F.data=='N')
async def send_Namangan(call:CallbackQuery):
    ikb=InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text='Chust',callback_data='chus'),
        InlineKeyboardButton(text='Pop',callback_data='po')
    )
    ikb.adjust(2)
    ikb=ikb.as_markup()
    await call.answer('Tumanlar',reply_markup=ikb)
@dp.callback_query(F.data=='J')
async def send_Jizzax(call:CallbackQuery):
    ikb=InlineKeyboardBuilder()
    ikb.add(
        InlineKeyboardButton(text='Paxtakor',callback_data='pax'),
        InlineKeyboardButton(text='Zarbdor',callback_data='zar')
    )
    ikb.adjust(2)
    ikb=ikb.as_markup()
    await call.answer('Tumanlar',reply_markup=ikb)
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())