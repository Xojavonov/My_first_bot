from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.dispatcher import dp
from bot.States import Buttons
from bot.button.reply import reply_button_builder
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

@dp.message(Buttons.drama_film,F.text==__('⬅️ Back'))
@dp.message(Buttons.films_group, F.text==__('🎭Drama'))
async def second_command(message:Message,state:FSMContext):
    text = ['🎬 Forrest Gump', '🎬 Titanic', _('⬅️ Back')]
    markup=reply_button_builder(text,(3,1))
    await state.set_state(Buttons.drams_group)
    await message.answer(text=_('✅Internal departments'),reply_markup=markup)

caption='📜 **Forrest Gump**🗓 \n **1994-years** \n ⭐ **IMDB: 8.8** \n '
@dp.message(Buttons.drams_group,F.text=='🎬 Forrest Gump')
async def five_command(message:Message,state:FSMContext):
    text=[_('⬅️ Back')]
    markup=reply_button_builder(text,(1,))
    await state.set_state(Buttons.drama_film)
    await message.answer_video(video='BAACAgIAAxkBAAEdMypntK_SILfd30JeTgABwTYCcNIUOHMAArJoAAJEt5FJqwSPRDa_B2g2BA',caption=caption,reply_markup=markup)

caption2='📜 **Titanic**🗓 \n ** 1997-years** \n ⭐ **IMDB: 7.8** \n '
@dp.message(Buttons.drams_group,F.text=='🎬 Titanic')
async def five_command(message:Message,state:FSMContext):
    text=[_('⬅️ Back')]
    markup=reply_button_builder(text,(1,))
    await state.set_state(Buttons.drama_film)
    await message.answer_video(video='BAACAgIAAxkBAAEdNLNntYPeDQTemq6nV3yEXC0lO4l5LAACE4MAAvEDmUktuAmSTJLymTYE',caption=caption2,reply_markup=markup)