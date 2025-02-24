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
# ==========================================================================1
# @dp.message(CommandStart)
# async def request_user(message:Message):
#     ikb = InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text="Yaxshi" , callback_data="yax"),
#         InlineKeyboardButton(text="Ortacha" , callback_data="ort"),
#         InlineKeyboardButton(text="Yomon" , callback_data="yom"),
#     )
#     ikb.adjust(1,1,1)
#     ikb = ikb.as_markup()
#     await message.answer(text="Salom! Qanday kayfiyatda siz?" , reply_markup=ikb)

# @dp.callback_query(F.data=='yax')
# async def first_request(call:CallbackQuery):
#     await call.message.answer(text='Ajoyib! 😊 Sizga yana ham yaxshi kun tilayman')

# @dp.callback_query(F.data=='ort')
# async def first_request(call:CallbackQuery):
#     await call.message.answer(text='Hammasi yaxshi bo‘lib ketadi! 😃')

# @dp.callback_query(F.data=='yom')
# async def first_request(call:CallbackQuery):
#     await call.message.answer(text='Xafa bo‘lmang, hammasi yaxshi bo‘ladi! 💪')
# ================================================================================2
# @dp.message(CommandStart)
# async def request_user(message:Message):
#     ikb = InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text="Ha" , callback_data="ha"),
#         InlineKeyboardButton(text="Yoq" , callback_data="yo")
#     )
#     ikb.adjust(1,1,1)
#     ikb = ikb.as_markup()
#     await message.answer(text="Siz Python dasturlash tilini bilasizmi?" , reply_markup=ikb)
# @dp.callback_query(F.data=='ha')
# async def first_request(call:CallbackQuery):
#     await call.message.answer(text='Ajoyib! ✅ Siz yaxshi dasturchisiz')
#
# @dp.callback_query(F.data=='yo')
# async def first_request(call:CallbackQuery):
#     await call.message.answer(text='Hali ham kech emas, boshlash uchun eng yaxshi vaqt hozir! 🚀')
# async def main() -> None:
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     await dp.start_polling(bot)
# ==================================================================================3

# @dp.message(CommandStart)
# async def request_user(message:Message):
#     ikb = InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text="Ha, obuna bo‘ldim" , callback_data="boldim"),
#         InlineKeyboardButton(text="Yo‘q, hali obuna bo‘lmadim" , callback_data="bolmadim")
#     )
#     ikb.adjust(1,1,1)
#     ikb = ikb.as_markup()
#     await message.answer(text="Siz bizning kanalimizga obuna bo‘lgansizmi?" , reply_markup=ikb)
# @dp.callback_query(F.data=='boldim')
# async def first_request(call:CallbackQuery):
#     await call.message.answer(text='Rahmat! ✅ Endi botdan foydalanishingiz mumkin.')

# @dp.callback_query(F.data=='bolmadim')
# async def first_request(call:CallbackQuery):
#     ikb = InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text="♻️ Qayta tekshirish" , callback_data="qay")
#     )
#     ikb.adjust(1,1,1)
#     ikb = ikb.as_markup()
#     await call.message.answer(text='Iltimos, oldin bizning kanalimizga obuna bo‘ling! 📢',reply_markup=ikb )

# @dp.callback_query(F.data=='qay')
# async def request_user(call:CallbackQuery):
#     ikb = InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text="Ha, obuna bo‘ldim" , callback_data="boldim"),
#         InlineKeyboardButton(text="Yo‘q, hali obuna bo‘lmadim" , callback_data="bolmadim")
#     )
#     ikb.adjust(1,1,1)
#     ikb = ikb.as_markup()
#     await call.message.answer(text="Siz bizning kanalimizga obuna bo‘lgansizmi?" , reply_markup=ikb)
# ====================================================================================4
# @dp.message(CommandStart)
# async def inform_menu(message:Message):
#     ikb=InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text='📖Kurslar',callback_data='kurr'),
#         InlineKeyboardButton(text='❓Biz haqimizda',callback_data='haq'),
#         InlineKeyboardButton(text='📞Boglanish',callback_data='bog'),
#     )
#     ikb.adjust(1,1,1)
#     ikb=ikb.as_markup()
#     await message.answer(text='Tanlang',reply_markup=ikb)
# @dp.callback_query(F.data=='kurr')
# async def course_menu(call:CallbackQuery):
#     ikb=InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text='Python Backend',callback_data='py'),
#         InlineKeyboardButton(text='Telegram Bot',callback_data='tg'),
#         InlineKeyboardButton(text='Fullstack Web',callback_data='full'),
#         InlineKeyboardButton(text='⬅️ Ortga',callback_data='back'),
#     )
#     ikb.adjust(1,1,1,1)
#     ikb=ikb.as_markup()
#     await call.message.answer(text='Tanlang',reply_markup=ikb)
# @dp.callback_query(F.data=='back')
# async def back_menu(call:CallbackQuery):
#     ikb=InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text='📖Kurslar',callback_data='kurr'),
#         InlineKeyboardButton(text='❓Biz haqimizda',callback_data='haq'),
#         InlineKeyboardButton(text='📞Boglanish',callback_data='bog'),
#     )
#     ikb.adjust(1,1,1)
#     ikb=ikb.as_markup()
#     await call.message.answer(text='Tanlang',reply_markup=ikb)
# @dp.callback_query(F.data=='haq')
# async def information(call:CallbackQuery):
#     await call.message.answer(text='Bizning oquv markazimiz eng yaxshisi !')
# @dp.callback_query(F.data=='bog')
# async def information(call:CallbackQuery):
#     await call.message.answer(text='+998(99)277-12-81')


# CHANNEL_USERNAME = "@Python"
# async def is_subscribed(user_id: int) -> bool:
#     member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
#     return member.status in ["member", "administrator", "creator"]
#
# async def start_command(message: Message):
#     user_id = message.from_user.id
#     if await is_subscribed(user_id):
#         await message.answer("✅ Siz kanalga obuna bo‘lgansiz! Botdan foydalanishingiz mumkin.")
#     else:
#         # Kanalga obuna bo‘lish tugmalari
#         keyboard = InlineKeyboardMarkup(inline_keyboard=[
#             [InlineKeyboardButton(text="📢 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}")],
#             [InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subscription")]
#         ])
#         text=[("✅ Obunani tekshirish", "check_subscription")]
#         await message.answer("❌ Kanalga obuna bo‘lmadingiz! Iltimos, obuna bo‘ling va tekshiring.", reply_markup=keyboard)
#
# @dp.callback_query(F.data == "check_subscription")
# async def check_subscription(callback_query:CallbackQuery):
#     user_id = callback_query.from_user.id
#     if await is_subscribed(user_id):
#         await callback_query.message.edit_text("✅ Rahmat! Siz kanalga obuna bo‘lgansiz. Endi botdan foydalanishingiz mumkin.")
#     else:
#         await callback_query.answer("❌ Hali ham kanalga obuna bo‘lmagansiz!", show_alert=True)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())