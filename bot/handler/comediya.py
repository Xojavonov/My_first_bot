from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message #CallbackQuery
from bot.dispatcher import dp
from bot.States import Buttons
from bot.button.reply import reply_button_builder
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

@dp.message(Buttons.comedy_film,F.text==__('⬅️ Back'))
@dp.message(Buttons.films_group, F.text==__('😂Comedy'))
async def four_command(message:Message,state:FSMContext):
    text = ['🎬 The Mask', '🎬 Home Alone', _('⬅️ Back')]
    markup=reply_button_builder(text,(3,1))
    await state.set_state(Buttons.drams_group)
    await message.answer(text=_('✅ Internal departments '),reply_markup=markup)

caption='📜 **The Mask **🗓 \n **1994-years** \n ⭐ **IMDB: 9.8** \n '
@dp.message(Buttons.drams_group,F.text=='🎬 The Mask')
async def five_command(message:Message,state:FSMContext):
    text=[_('⬅️ Back')]
    markup=reply_button_builder(text,(1,))
    await state.set_state(Buttons.comedy_film)
    await message.answer_video(video="BAACAgIAAxkBAAEdNLlntYW4bzgvw3EgnN_RiRgnvbhdDwACT3AAAtYVqElubt6AOn6ZUjYE",caption=caption,reply_markup=markup)

caption2='📜 **Home Alone **🗓 \n **1990-years** \n ⭐ **IMDB: 8.9** \n '
@dp.message(Buttons.drams_group,F.text=='🎬 Home Alone')
async def five_command(message:Message,state:FSMContext):
    text=[_('⬅️ Back')]
    markup=reply_button_builder(text,(1,))

    await state.set_state(Buttons.comedy_film)
    await message.answer_video(video="BAACAgIAAxkBAAEdNLtntYZqj2xd2ztdx3u3LHehxHSAsgACuWQAAu8TmUnDIOLYfVPqnDYE",caption=caption2,reply_markup=markup)



