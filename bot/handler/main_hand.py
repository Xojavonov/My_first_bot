from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineQueryResultArticle, InputTextMessageContent, InlineQuery
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import   InlineKeyboardBuilder
from dp.model import films
from bot.dispatcher import dp
from bot.States import Buttons
from bot.button.reply import reply_button_builder
from bot.button.inline import inline_button_builder
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __


@dp.message(CommandStart())
@dp.message(F.text==__('⬅️Back'))
async def request_user(message:Message , state : FSMContext):
    chat_id = message.chat.id
    check_id= 5320724806
    await state.update_data(chat_id=chat_id)
    data=await state.get_data()
    text=[_('🎥Films'),_('📞 Call center'),_('🇷🇺 🇺🇿 🇬🇧 Language')]
    if check_id == data['chat_id']:
        text.append(_('Admin'))
    markup=reply_button_builder(text,(3,))
    ikb=InlineKeyboardBuilder()
    ikb.add(InlineKeyboardButton( text=" 🔎 Search",switch_inline_query_current_chat=' '))
    ikb=ikb.as_markup(resize_keyboard=True)
    await message.answer(text=_('Search films'),reply_markup=ikb)
    await message.answer(text=_('✅ Main menu:'),reply_markup=markup)


@dp.message(F.text == __('🇷🇺 🇺🇿 🇬🇧 Language'))
async def language_user(message: Message, state: FSMContext):
    text = ['🇺🇿 Uzbek', '🇷🇺 Russian', '🇬🇧 English', _('⬅️Back')]
    markup = reply_button_builder(text, (3, 1))
    await state.set_state(Buttons.language)
    await message.answer(text=_('Chose language:'), reply_markup=markup)


@dp.message(Buttons.language)
async def language_handler(message: Message, state: FSMContext, i18n):
    map_lang = {
        '🇺🇿 Uzbek': 'uz',
        '🇷🇺 Russian': 'rus',
        '🇬🇧 English': 'en'
    }
    code = map_lang.get(message.text)
    i18n.current_locale = code
    await state.update_data(locale=code)
    if not code:
        await message.answer(_('❌ Iltimos, menyudan tilni tanlang!'))
        return
    lang = await state.get_value('locale')
    await state.clear()
    await state.update_data({'locale': lang})
    text = [_('🎥Films'), _('📞 Call center'), _('🇷🇺 🇺🇿 🇬🇧 Language')]
    markup = reply_button_builder(text, (3,))
    await message.answer(text=_('✅ Main menu:'), reply_markup=markup)


@dp.message(F.text==__('⬅️ Back'))
@dp.message(F.text==__('🎥Films'))
async def first_command(message:Message,state:FSMContext):
    text=[_('🎭Drama'),_('😂Comedy'),_('🎬Action'),_('⬅️Back')]
    markup=reply_button_builder(text,(3,1))
    await state.set_state(Buttons.films_group)
    await message.answer(text=_('✅ In the movies section:'),reply_markup=markup)


@dp.message(F.text==__('📞 Call center'))
async def call_center(message:Message):
    text = [_('⬅️Back')]
    markup = reply_button_builder(text, (1,))
    await message.answer(text='+998(99)277-12-81',reply_markup=markup)




#===============================================================================================


@dp.callback_query(F.data == "search")
async def search_handler(callback: CallbackQuery):
    text=[("Search","search")]
    markup=inline_button_builder(text,(1,))
    await callback.message.edit_reply_markup( reply_markup=markup)


@dp.inline_query()
async def inline_query(inline: InlineQuery):
    query = inline.query
    result = []
    for film in films:
        if query in film.get('name') or query in str(film.get('rating')):
            i=InlineQueryResultArticle(
                id=str(film.get('id')),
                title=film.get('name'),
                description=f"⭐️ {film.get('rating')} | 📅 {film.get('release_year')}",
                thumbnail_url=film.get('photo_id'),
                input_message_content=InputTextMessageContent(message_text=str(film.get('id')))
            )
            result.append(i)
    await inline.answer(result, cache_time=5, is_personal=True)


@dp.message(F.via_bot)
async def any_text(message: Message):
    film_id = message.text
    film = next((i for i in films if str(i.get('id')) == film_id), None)
    if film:
        caption = f'''
        🎬 Nomi: {film.get('name')}
        📅 Yili: {film.get('release_year')}
        ⭐️ Ratingi: {film.get('rating')}'''

        await message.delete()
        await message.answer_video(video=film.get('video'), caption=caption)
    else:
        await message.answer("Film topilmadi.")