import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = "7484603263:AAFL9qlzDCar6f4aeA5qIZn9KSWFxHOqAGA"

dp = Dispatcher()

# class PizzaState(StatesGroup):
#     type = State()
#     size = State()
#     drink = State()
#
# @dp.message(CommandStart())
# async def hand_inform(message: Message, state: FSMContext):
#     await state.set_state(PizzaState.type)
#     await message.answer("Pitsa turini kiriting:")
#
# @dp.message(PizzaState.type)
# async def hand_type(message: Message, state: FSMContext):
#     types = message.text
#     await state.update_data(type=types)
#     await state.set_state(PizzaState.size)
#     await message.answer("Hajmni kiriting:")
#
# @dp.message(PizzaState.size)
# async def hand_size(message: Message, state: FSMContext):
#     size = message.text
#     await state.update_data(size=size)
#     await state.set_state(PizzaState.drink)
#     await message.answer("Ichimlikni kiriting:")
#
# @dp.message(PizzaState.drink)
# async def hand_drink(message: Message, state: FSMContext,bot:Bot):
#     drink = message.text
#     await state.update_data(drink=drink)
#     data = await state.get_data()
#     Pizza(**data).save()
#     await state.clear()
#     await message.reply("Ma'lumotlar saqlandi")
#================================================================================
# class Questions(StatesGroup):
#     question1=State()
#     question2=State()
#     question3=State()
#     score=State()
# correct_answer={
#     'question1' : '8',
#     'question2'  :'96',
#     'question3' : '20',
# }
# @dp.message(CommandStart())
# async def hand_inform(message: Message, state: FSMContext):
#     await state.set_state(Questions.question1)
#     await message.answer("3+5 jabobi nechi?:")
# @dp.message(Questions.question1)
# async def hand_question1(message:Message,state:FSMContext):
#     quest1=message.text
#     await state.update_data(question1=quest1)
#     await state.set_state(Questions.question2)
#     await message.answer('24*4 javobi nechi?:')
#
# @dp.message(Questions.question2)
# async def hand_question2(message:Message,state:FSMContext):
#     quest2 = message.text
#     await state.update_data(question2=quest2)
#     await state.set_state(Questions.question3)
#     await message.answer('100 ÷ 5  javobi nechi?:')
#
# @dp.message(Questions.question3)
# async def hand_question3(message:Message,state:FSMContext):
#     quest3 = message.text
#     score = 0
#     await state.update_data(question3=quest3)
#     data = await state.get_data()
#     if data['question1']==correct_answer['question1']:
#         score+=1
#     if data['question2']==correct_answer['question2']:
#         score+=1
#     if data['question3']==correct_answer['question3']:
#         score+=1
#     await state.set_state(Questions.score)
#     await state.update_data(score=score)
#     data = await state.get_data()
#     Question(**data).save()
#     await state.clear()
#     await message.answer(text=f'Javoblaringiz tekshiriladi:{score}')
#====================================================================================

# correct={'request':'inglis tililda yozilgan'}
# class Request(StatesGroup):
#     request=State()
#
# @dp.message(CommandStart())
# async def hand_inform(message: Message, state: FSMContext):
#     await state.set_state(Request.request)
#     await message.answer(text="Matn qanday tilda yozilgan:")
# @dp.message(Request.request)
# async def hand_request(message:Message,state:FSMContext,):
#     request=message.text
#     await state.update_data(request=request)
#     chat_id=''
#     data=await state.get_data()
#     if data['request']==correct['request']:
#         chat_id+=str(message.chat)
#     User(chat_id=chat_id).save()
#     await message.answer(f'Javob togri {chat_id}')

#======================================================================
# class Questions(StatesGroup):
#     question1=State()
#     question2=State()
#     question3=State()
#     score=State()
# correct_answer={
#     'question1' : 'olma',
#     'question2'  :'ot',
#     'question3' : 'banan',
# }
# @dp.message(CommandStart())
# async def hand_inform(message: Message, state: FSMContext):
#     await state.set_state(Questions.question1)
#     await message.answer("\'apple\' nima?")
# @dp.message(Questions.question1)
# async def hand_question1(message:Message,state:FSMContext):
#     quest1=message.text
#     await state.update_data(question1=quest1)
#     await state.set_state(Questions.question2)
#     await message.answer('\'horse\' nima?')
#
# @dp.message(Questions.question2)
# async def hand_question2(message:Message,state:FSMContext):
#     quest2 = message.text
#     await state.update_data(question2=quest2)
#     await state.set_state(Questions.question3)
#     await message.answer('\'banan\' nima?')
#
# @dp.message(Questions.question3)
# async def hand_question3(message:Message,state:FSMContext):
#     quest3 = message.text
#     score = 0
#     await state.update_data(question3=quest3)
#     data = await state.get_data()
#     if data['question1']==correct_answer['question1']:
#         score+=1
#     if data['question2']==correct_answer['question2']:
#         score+=1
#     if data['question3']==correct_answer['question3']:
#         score+=1
#     await state.set_state(Questions.score)
#     await state.update_data(score=score)
#     data = await state.get_data()
#     Question(**data).save()
#     await state.clear()
#     await message.answer(text=f'Javoblaringiz tekshiriladi:{score}')
#==================================================================================




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())