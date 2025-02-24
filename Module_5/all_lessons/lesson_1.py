import asyncio
import logging
import random
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = '7484603263:AAHAHDXPrkZhOR0wy7ctYoEZI-e5doJNzQw'
admins= [5320724806]
dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user.id in admins:
        await message.answer("Hello admin")
    else:
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message(F.photo)
async def hand_photo(message:Message):
    await message.answer('Bu rasm')

@dp.message(F.text=='salom')
async def send_video(message:Message):
    await message.answer_video(video='BAACAgIAAxkBAAEdGLJnqvhD1ipx0bobHv2riSNNufYQIQACYnQAAu97UUmFFUn-35LFxzYE')

@dp.message(F.voice)
async def hand_voice(message:Message):
    await message.answer('Ovoz qabul qilindi')

@dp.message(F.text=='Hello')
async def send_emoji(message:Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEdHrZnrFR-KKmJLnwGMmyOSXJ_m-re-wACDAEAAiI3jgR7D1jAYFgdrjYE')

@dp.message(F.document)
async def hand_documents(message:Message):
    await message.answer('Fayl qabul qilindi')

@dp.message(F.text=='Python')
async def send_photo(mess:Message):
    await mess.answer_photo(photo='AgACAgIAAxkBAAEdGMBnqv1KKrGYC8_P_FxE_ifYpE3g7AACXekxG6sreEtRLPFlsIgJwQEAAwIAA3MAAzYE')

@dp.message(F.text=='video')
async def send_video(message:Message):
    await message.answer_video(video='BAACAgIAAxkBAAEdGLJnqvhD1ipx0bobHv2riSNNufYQIQACYnQAAu97UUmFFUn-35LFxzYE')

@dp.message(F.text=='Salom')
async def send_message_admin(mess:Message):
    if mess.from_user.id == admins:
        await mess.answer('Hush kelibsiz')
    else:
        await mess.answer("You are not admin")
@dp.message (F.text=='test')
async def check_test(mess:Message):
    await mess.answer('Siz testni muvaffaqiyatli topshirdingiz')
@dp.message (F.text=='Like')
async def check_like(mess:Message):
    await mess.answer('Siz layk bosdingiz')
@dp.message (F.text=='bugun ob-havo')
async def check_weather(mess:Message):
    await mess.answer('Hozircha ma’lumot yo‘q')
@dp.message (F.text=='Katta harf')
async def check_weather(mess:Message):
    await mess.answer('KATTA HARF')
@dp.message(F.text=='5')
async def send_number_to_five(mess:Message):
    await mess.answer('1,2,3,4,5')
@dp.message (F.text=='random')
async def random_numbers(mess:Message):
    l=random.randint(1,10)
    await mess.answer(str(l))


@dp.message()
async def square_number(message: Message):
    number = int(message.text)
    await message.answer(str(number ** 2))

@dp.message()
async def math_handler(message: Message) -> None:
    result = eval(message.text)
    await message.answer(f"Natija : {result}")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
