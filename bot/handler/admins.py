

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from bot.dispatcher import dp
from bot.States import Admin_State
from dp.model import Film,save
channel_link = "https://t.me/+1Sn77WSRC5wzNWMy"

@dp.message(F.text=='Admin')
async def admin_handler(message:Message,state:FSMContext):
    await state.set_state(Admin_State.videos)
    await message.answer(text='🎬 Throw away the movie:')


@dp.message(Admin_State.videos,F.video)
async def hand_video(message:Message,state:FSMContext):
    file_id=message.video.file_id
    await state.update_data(file_id=file_id)
    await state.set_state(Admin_State.name)
    await message.answer(text='Film  name:')
@dp.message(Admin_State.name)
async def hand_name(message:Message,state:FSMContext):
    name=message.text
    await state.update_data(name=name)
    await state.set_state(Admin_State.release_year)
    await message.answer(text='Film release_year:')
@dp.message(Admin_State.release_year)
async def hand_release(message:Message,state:FSMContext):
    release_year=message.text
    await state.update_data(released_year=release_year)
    await state.set_state(Admin_State.rating)
    await message.answer(text='Film rating:')
@dp.message(Admin_State.rating)
async def hand_rating(message:Message,state:FSMContext):
    rating=message.text
    await state.update_data(rating=rating)
    await state.set_state(Admin_State.category_id)
    await message.answer(text='Film category_id:')
@dp.message(Admin_State.category_id)
async def hand_category(message:Message,state:FSMContext):
    category_id=message.text
    await state.update_data(category_id=category_id)
    await state.set_state(Admin_State.picture)
    await message.answer(text='Film picture selka :')
@dp.message(Admin_State.picture)
async def hand_category(message:Message,state:FSMContext):
    photo_id=message.text
    await state.update_data(photo_id=f"{photo_id}")
    data=await state.get_data()
    users={
        'file_id':data.get('file_id'),
        'name':data.get('name'),
        'released_year':data.get('released_year'),
        'rating':data.get('rating'),
        'category_id':data.get('category_id'),
        'photo_id':data.get('photo_id'),
    }
    save(Film,users)
    await message.answer(text='Data received:')

