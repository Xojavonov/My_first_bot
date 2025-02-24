




import asyncio
import logging
import sys
import time
from os import getenv
from aiogram.filters import Command
from aiogram.types import LabeledPrice, PreCheckoutQuery

from bot.handler.main_hand import *
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import gettext as _, I18n,FSMI18nMiddleware

TOKEN = "7484603263:AAFL9qlzDCar6f4aeA5qIZn9KSWFxHOqAGA"

dp = Dispatcher()
# PAYMENT_CLICK_TOKEN = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'
# @dp.message(Command('invoice'))
# async def invoice(message: Message):
#     products=[
#         {
#             'id':1,
#             'name':'Iphone 15 pro',
#             'price': 1000
#         }
#     ]
#     prices = [
#         LabeledPrice(label='Iphone 15 pro', amount=1000*1 * 100),
#         LabeledPrice(label='Iphone 14 pro', amount=2000*1 * 100),
#     ]
#     await message.answer_invoice('Products', "Jami 3 product order qilindi", '1',"UZS",prices, PAYMENT_CLICK_TOKEN)
# @dp.pre_checkout_query()
# async def success_handler(pre_checkout_query: PreCheckoutQuery) -> None:
#     await pre_checkout_query.answer(True)
#
# @dp.message(lambda message: bool(message.successful_payment))
# async def confirm_handler(message: Message, state: FSMContext):
#     if message.successful_payment:
#         total_amount = message.successful_payment.total_amount//100
#         order_id = int(message.successful_payment.invoice_payload)
#         # await Order.update(id_=order_id, status=Order.OrderStatusEnum.APPROVED , total_amount = total_amount)
#         await message.answer(text=f"To'lo'vingiz uchun raxmat 😊 \n{total_amount}\n{order_id}")
#
#==============================================================================
# @dp.message(Command('ad'))
# async def ad_command_handler(message: Message):
#     start = time.time()
#     # for i in range(100):
#     #     await message.bot.send_message(user, text=f"Reklama {i}")
#     # end = time.time()
#     # print(end - start)
#     #
#     # start = time.time()
#     tasks = []
#     user_id=5320724806
#     for i in range(100):
#         tasks.append(message.bot.send_message(user_id, text=f"Reklama {i}"))
#         if len(tasks) >= 25:
#             await asyncio.gather(*tasks)
#             tasks = []
#             await asyncio.sleep(1)
#     end = time.time()
#     print(end - start)
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())