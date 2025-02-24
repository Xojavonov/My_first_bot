import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _, I18n,FSMI18nMiddleware
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

TOKEN = "7484603263:AAFL9qlzDCar6f4aeA5qIZn9KSWFxHOqAGA"

dp = Dispatcher()

@dp.message(CommandStart())
async def choice_language(message:Message):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='🇺🇸 English'),
            KeyboardButton(text='🇺🇿 Uzbek')
    )
    rkb.adjust(2)
    rkb=rkb.as_markup(resize_keyboard=True)
    await message.answer(_('Choise language'),reply_markup=rkb)
@dp.message(F.text=='🇺🇿 Uzbek')
async def uzbek_lang_handler(message:Message,state:FSMContext,i18n):
    rkb=ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='🇺🇸 English'),
            KeyboardButton(text='🇺🇿 Uzbek')
    )
    rkb.adjust(2)
    rkb=rkb.as_markup(resize_keyboard=True)
    await state.update_data({'locale':'uz'})
    i18n.current_locale='uz'

    await message.answer(_('Choise language'),reply_markup=rkb)

@dp.message(F.text=='🇺🇸 English')
async def eng_lang_handler(message: Message, state: FSMContext, i18n):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='🇺🇸 English'),
        KeyboardButton(text='🇺🇿 Uzbek')
    )
    rkb.adjust(2)
    rkb = rkb.as_markup(resize_keyboard=True)
    await state.update_data({'locale': 'en'})
    i18n.current_locale = 'en'
    await message.answer(_('Chose language'), reply_markup=rkb)

async def main() -> None:
    i18n = I18n(path='C:/Users/User/PycharmProjects/project5/Module5/PythonProject5/locales', default_locale='en', domain='messages')
    dp.update.middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())