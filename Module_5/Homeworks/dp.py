#
# from dataclasses import dataclass
#
# import psycopg2
#
#
# @dataclass
# class Pizza:
#     type:str=None,
#     size:str=None,
#     drink:str=None,
#
#     def save(self):
#         connect = psycopg2.connect(
#             dbname = 'lesson_3',
#             user = 'postgres',
#             password = '4321',
#             host = 'localhost',
#             port = 5432
#         )
#         cur = connect.cursor()
#         query = """
#         insert into pizza(type,size,drink) values (%s,%s,%s)
#         """
#         cur.execute(query , (self.type , self.size , self.drink))
#         connect.commit()
#
# @dataclass
# class Question:
#     question1:str=None
#     question2:str=None
#     question3:str=None
#     score:int=0
#
#     def save(self):
#         connect = psycopg2.connect(
#             dbname = 'projects',
#             user = 'postgres',
#             password = '4321',
#             host = 'localhost',
#             port = 5432
#         )
#         cur = connect.cursor()
#         query = """
#         insert into questions(question1,question2,question3,score) values (%s,%s,%s,%s)
#         """
#         cur.execute(query , (self.question1,self.question2,self.question3,self.score))
#         connect.commit()
# @dataclass
# class User:
#     chat_id:str=None
#
#     def save(self):
#         connect = psycopg2.connect(
#             dbname = 'projects',
#             user = 'postgres',
#             password = '4321',
#             host = 'localhost',
#             port = 5432
#         )
#         cur = connect.cursor()
#         query = """
#         insert into users(user_id) values (%s)
#         """
#         cur.execute(query , (self.chat_id,))
#         connect.commit()


from aiogram.fsm.state import StatesGroup, State
from sqlalchemy import create_engine, String,BIGINT
from sqlalchemy.orm import  sessionmaker, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import insert,delete,update,select
class Base (DeclarativeBase):
    pass
class DB:
    engine = create_engine("postgresql+psycopg2://postgres:4321@localhost:5432/project2")
engine=DB.engine

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(BIGINT)
    first_name:Mapped[str]=mapped_column(String(50))
    last_name:Mapped[str]=mapped_column(String(50))


session = sessionmaker(bind=engine)()
class States(StatesGroup):
    user_id = State()
    first_name = State()
    last_name = State()
    new_name = State()
    chat_id=State()
    admin_name=State()
    filter=State()


def save(table_name,value):
    query = insert(table_name).values(**value)
    session.execute(query)
    session.commit()


def check_user(table_name:User,message):
    query = select(table_name).filter(table_name.user_id == message)
    user = session.execute(query).scalar()
    return user


def get(table, columns, filter_column, filter_value):
    if isinstance(columns, str):
        columns = [columns]
    query = select(*[getattr(table, col) for col in columns]).where(getattr(table, filter_column) == filter_value)
    users = session.execute(query).first()
    result=''
    for i in users:
        result+=str(i)+' '
    return result


def filters(table, value):
    query = select(table.first_name, table.last_name).where(table.first_name.like(f'{value}%'))
    users = session.execute(query).first()
    result = ''
    for i in users:
        result += str(i) + ' '
    return result


def ups(table_name, user_id: int, **new_values):
    stmt = update(table_name).where(getattr(table_name,'user_id') == user_id).values(**new_values)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def dlt(table_name:User,value):
    stmt = delete(table_name).where(table_name.user_id == value)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


stmt = select(User.first_name,User.last_name)
users=''
with engine.connect() as conn:
    result = conn.execute(stmt)
    for user_name, last_name in result:
        users=f'{user_name},{last_name} \n'
Base.metadata.create_all(engine)

admin_id = 5320724806

'''
echo "# My_first_bot" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Xojavonov/My_first_bot.git
git push -u origin main
'''