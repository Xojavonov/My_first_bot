import asyncio
import logging
import sys

# from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, UniqueConstraint, Index,  CheckConstraint, DateTime
# from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, DeclarativeBase

# Bazaga ulanish
# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")
# engine = create_engine("oracle+oracledb://scott:tiger@tnsalias")
# engine = create_engine("sqlite:///test.db")
# engine = create_engine("postgresql+psycopg2://postgres:4321@localhost:5432/project")
#
#
# class Base (DeclarativeBase):
#     pass

# class Customer(Base):
#     __tablename__  = 'customers'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     full_name: Mapped[str] = mapped_column(String(100))
#     email: Mapped[str] = mapped_column(String(100), unique=True)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
#
#     table_args = (
#         UniqueConstraint("email", name="uq_customer_email"),
#         Index("idx_customer_email", "email"),
#     )
#
#     def __repr__(self):
#         return f'<Customer(id={self.id}, full_name={self.full_name})>'
#
#
# class Order(Base):
#     __tablename__  = 'orders'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     order_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
#     customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
#     total_price: Mapped[float] = mapped_column(Float, CheckConstraint('total_price > 0'))
#
#     def __repr__(self):
#         return f'<Order(id={self.id}, total_price={self.total_price})>'


# class Category(Base):
#     __tablename__  = 'categories'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#
#     def __repr__(self):
#         return f'<Category(id={self.id}, name={self.name})>'
#
#
# class Product(Base):
#     __tablename__ = 'products'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
#     price: Mapped[float] = mapped_column(Float, CheckConstraint('price > 0'))
#
#     def __repr__(self):
#         return f'<Product(id={self.id}, name={self.name})>'
#
#
# class CategoryProduct(Base):
#     __tablename__ = 'categories_products'
#
#     category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), primary_key=True)
#     product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), primary_key=True)
#
#     def repr(self):
#         return f'<CategoryProduct(category_id={self.category_id}, product_id={self.product_id})>'
# p=Product()
# =======================================================HOMEWORK======================


from bot.button.reply import reply_button_builder
from bot.button.inline import inline_button_builder
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from Module_5.Homeworks.dp import States,User,save,check_user,users,ups,dlt,admin_id,get,filters
TOKEN = "7484603263:AAFL9qlzDCar6f4aeA5qIZn9KSWFxHOqAGA"

dp = Dispatcher()


@dp.message(Command('register'))
async def command_start_handler(message: Message,state:FSMContext) -> None:
    user_id=message.chat.id
    await state.update_data(user_id=user_id)
    await state.set_state(States.first_name)
    await message.answer(f"Ismingizni kiriting!")


@dp.message(States.first_name)
async def first_name_hand(message:Message,state:FSMContext):
    first_name=message.text
    await state.update_data(first_name=first_name)
    await state.set_state(States.last_name)
    await message.answer('Familyangizni kiriting')


@dp.message(States.last_name)
async def last_name_hand(message:Message,state:FSMContext):
    last_name=message.text
    await state.update_data(last_name=last_name)
    data=await state.get_data()
    check=check_user(User,data.get('user_id'))
    if not check:
        save(User,data)
    else:
        await message.answer(text='Siz allaqachon royxatdan otgansiz!')
        return
    await state.clear()
    await message.answer(text='Siz muvafiqyatli royhatdan otdingiz')


@dp.message(Command('users'))
async def admin_hand(message:Message):
    chat_id=message.chat.id
    if chat_id==admin_id  :
        if users:
            await message.answer(text=str(users))
        else:
            await message.answer(text='Hozircha hech kim yoq')
    await message.answer(text='Barcha foydalanuvchilar keltirilidi')


@dp.message(Command('update_fullname'))
async def update_handler(message:Message,state:FSMContext):
    user_id=message.chat.id
    await state.update_data(user_id=user_id)
    await state.set_state(States.admin_name)
    await message.answer(text='Yangi familiyangizni kiriting:')


@dp.message(States.admin_name)
async def update_name(message:Message,state:FSMContext):
    last_name=message.text
    await state.update_data(last_name=last_name)
    data=await state.get_data()
    check=check_user(User,data.get('user_id'))
    if  check:
        new_values = {"last_name": data.get("last_name")}
        ups(User, data.get("user_id"), **new_values)
    else:
        await message.answer('Avval royhatdan oting')
        return
    await state.clear()
    await message.answer('Familyangiz yangilandi')


@dp.message(Command('delete_me'))
async def delete_user(message:Message,state:FSMContext):
    user_id = message.chat.id
    await state.update_data(user_id=user_id)
    text=['✅Ha','❎Yoq']
    markup=reply_button_builder(text,(2,))
    await message.answer(text='"Siz rostdan ham hisobingizni o‘chirmoqchimisiz?',reply_markup=markup)


@dp.message(F.text=='✅Ha')
async def user_deleted(message:Message,state:FSMContext):
    data=await state.get_data()
    check=check_user(User,data.get('user_id'))
    if check:
        dlt(User,data.get('user_id'))
    else:
        await message.answer(text='Siz royhatdan otmagansiz')
    await message.answer(text='Sizning hisobingiz muvaffaqiyatli o‘chirildi!')


@dp.message(Command('delete_user'))
async def admin_delete_user(message:Message,state:FSMContext):
    chat_id=message.chat.id
    if admin_id==chat_id:
        await state.set_state(States.user_id)
        await message.answer(text='Foydalanuvchi idsini kiriting!')


@dp.message(States.user_id)
async def delete_handler(message:Message,state:FSMContext):
    user_id=message.text
    await state.update_data(user_id=user_id)
    data = await state.get_data()
    check = check_user(User, data.get('user_id'))
    if check:
        dlt(User, data.get('user_id'))
    else:
        await message.answer(text='Foydalanuvchi yoq')
    await state.clear()
    await message.answer(text='Foydalanuvchi muvaffaqiyatli yangilandi!')


@dp.message(Command('update_user'))
async def admin_update_user(message:Message,state:FSMContext):
    chat_id=message.chat.id
    if admin_id==chat_id:
        await state.set_state(States.chat_id)
        await message.answer(text='Foydalanuvchi id sini kiriting!')


@dp.message(States.chat_id)
async def update_id(message:Message,state:FSMContext):
    user_id=message.text
    await state.update_data(user_id=user_id)
    await state.set_state(States.new_name)
    await message.answer(text='Foydalanuvchi familyasini kiriting kiriting!')


@dp.message(States.new_name)
async def delete_handler(message:Message,state:FSMContext):
    last_name = message.text
    await state.update_data(last_name=last_name)
    data = await state.get_data()
    check = check_user(User, data.get('user_id'))
    if check:
        ups(User, data.get('user_id'),last_name=data.get('last_name') )
    else:
        await message.answer(text='Foydalanuvchi yoq')
    await state.clear()
    await message.answer(text='Foydalanuvchi muvaffaqiyatli o‘chirildi!')

@dp.message(Command('my_info'))
async  def user_checked(message:Message,state:FSMContext):
    user_id=message.chat.id
    await state.update_data(user_id=user_id)
    text=[('✅Tasdiqlayman','tastiq'),('❌Ochirish','ochir')]
    markup=inline_button_builder(text,(2,))
    await message.answer(text='Tanlang',reply_markup=markup)


@dp.callback_query(F.data=='tastiq')
async def user_get(callback:CallbackQuery,state:FSMContext):
    data=await state.get_data()
    check=check_user(User,data.get('user_id'))
    if check:
        user_inf = get(User, ["first_name",'last_name','user_id'],'user_id', data.get("user_id"))
        await callback.message.answer(text=str(user_inf))
    else:
        await callback.message.answer(text='Avval royhatdan oting')
    await callback.message.answer(text="Rahmat! Ma’lumotlaringiz to‘g‘ri")


@dp.callback_query(F.data=='ochir')
async def user_get(callback:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    check = check_user(User, data.get('user_id'))
    if check:
        dlt(User, data.get('user_id'))
    else:
        await callback.message.answer(text='Avval royhatdan oting')
    await callback.message.answer(text='Hisob o‘chirildi!')


@dp.message(Command('filter'))
async def filter_user(message:Message,state:FSMContext):
    user_id=message.chat.id
    await state.update_data(user_id=user_id)
    await state.set_state(States.filter)
    await message.answer(text='Sozni kiriting:')


@dp.message(States.filter)
async def filter_handler(message:Message,state:FSMContext):
    filts=message.text
    data=await state.update_data(value=filts)
    check = check_user(User, data.get('user_id'))
    if check:
        filt=filters(User,data.get('value'))
        await message.answer(text=str(filt))
    else:
        await message.answer(text='Avval royhatdan oting')
        return
    await message.answer(text=f'{data.get('value')} foydalanuvchilar')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())