from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.dispatcher import dp
from bot.States import Buttons
from bot.button.reply import reply_button_builder
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
@dp.message(Buttons.action_film,F.text==__('⬅️ Back'))
@dp.message(Buttons.films_group, F.text==__('🎬Action'))
async def third_command(message:Message,state:FSMContext):
    text=['🎬 John Wick','🎬 Mad Max',_('⬅️ Back')]
    markup=reply_button_builder(text,(3,1))
    await state.set_state(Buttons.drams_group)
    await message.answer(text=_('✅Internal departments'),reply_markup=markup)

caption='📜 **John Wick**🗓 \n **2014-years** \n ⭐ **IMDB: 9.5** \n '
@dp.message(Buttons.drams_group,F.text=='🎬 John Wick')
async def five_command(message:Message,state:FSMContext):
    text=[_('⬅️ Back')]
    markup=reply_button_builder(text,(1,))
    await state.set_state(Buttons.action_film)
    await message.answer_video(video="BAACAgIAAxkBAAEdNL1ntYdBv8CzypVPd9qCiLRCidx4hAACkWgAAj0xmUlLv8QJ2FiQhDYE",caption=caption,reply_markup=markup)

caption2='📜 **Mad Max**🗓 \n **2015-years** \n ⭐ **IMDB: 7.7** \n '
@dp.message(Buttons.drams_group,F.text=='🎬 Mad Max')
async def five_command(message:Message,state:FSMContext):
    text=[_('⬅️ Back')]
    markup=reply_button_builder(text,(1,))
    await state.set_state(Buttons.action_film)
    await message.answer_video(video="BAACAgIAAxkBAAEdNL9ntYdmtdfZbOCXtU_hq3ULBuaIMQACP2gAAiTUeUm070LTLhDygzYE",caption=caption2,reply_markup=markup)