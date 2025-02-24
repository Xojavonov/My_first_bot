from dataclasses import dataclass

from dp.config import  Base,DB
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, UniqueConstraint, Index,  CheckConstraint, DateTime,Text
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import insert,delete,update,select
@dataclass
class Category(Base):
    __tablename__ = 'categories'

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(255))
    parent_id:Mapped[int]=mapped_column(ForeignKey('categories.id'))
@dataclass
class Film(Base):
    __tablename__ = 'films'
    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    released_year:Mapped[str]=mapped_column(String(50))
    file_id:Mapped[str]=mapped_column(Text)
    rating:Mapped[float]=mapped_column(Float)
    category_id:Mapped[int]=mapped_column(ForeignKey('categories.id'))
    photo_id: Mapped[str]=mapped_column(Text)

engine=DB.engine

# file_id=["BAACAgIAAxkBAAEdNL1ntYdBv8CzypVPd9qCiLRCidx4hAACkWgAAj0xmUlLv8QJ2FiQhDYE",
#         "BAACAgIAAxkBAAEdNL9ntYdmtdfZbOCXtU_hq3ULBuaIMQACP2gAAiTUeUm070LTLhDygzYE",
#         "BAACAgIAAxkBAAEdNLlntYW4bzgvw3EgnN_RiRgnvbhdDwACT3AAAtYVqElubt6AOn6ZUjYE",
#         "BAACAgIAAxkBAAEdNLtntYZqj2xd2ztdx3u3LHehxHSAsgACuWQAAu8TmUnDIOLYfVPqnDYE",
#          'BAACAgIAAxkBAAEdMypntK_SILfd30JeTgABwTYCcNIUOHMAArJoAAJEt5FJqwSPRDa_B2g2BA',
#         'BAACAgIAAxkBAAEdNLNntYPeDQTemq6nV**1990-years** 3yEXC0lO4l5LAACE4MAAvEDmUktuAmSTJLymTYE'
#          ]
# photo_id=[
#     'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1385313197i/186190.jpg',
#     'https://static1.cbrimages.com/wordpress/wp-content/uploads/2024/07/the-mask.jpg?q=70&fit=crop&w=1140&h=&dpr=1',
#     'https://s3.amazonaws.com/nightjarprod/content/uploads/sites/249/2023/07/25142008/madmaxxfury.png',
#     'https://m.media-amazon.com/images/M/MV5BZGM0YThmNGItZGU3ZS00NTFiLWIyNzEtNzk3MDk4NGE4YTFlXkEyXkFqcGc@._V1_QL75_UX492_.jpg',
#     'https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg',
#     'https://play-lh.googleusercontent.com/560-H8NVZRHk00g3RltRun4IGB-Ndl0I0iKy33D7EQ0cRRwH78-c46s90lZ1ho_F1so=w480-h960-rw'
# ]

# stmt = insert(Film)
# values_list = [
#     {"name": "📜 Forrest Gump🗓", "released_year": "1994-years", "file_id": file_id[0], "rating": 8.8, "category_id": 1, "photo_id": photo_id[0]},
#     {"name": "Mad Max🗓", "released_year": "2015-years", "file_id": file_id[1], "rating": 7.9, "category_id": 3, "photo_id": photo_id[2]},
#     {"name": "The Mask 🗓", "released_year": "2015-years", "file_id": file_id[2], "rating": 9.0, "category_id": 2, "photo_id": photo_id[1]},
#     {"name": "Home Alone 🗓", "released_year": "2015-years", "file_id": file_id[3], "rating": 8.2, "category_id": 2, "photo_id": photo_id[4]},
#     {"name": "Titanic🗓", "released_year": "1997-years", "file_id": file_id[4], "rating": 7.5, "category_id": 1, "photo_id": photo_id[5]},
#     {"name": "John Wick🗓", "released_year": "2014-years", "file_id": file_id[5], "rating": 9.1, "category_id": 3, "photo_id": photo_id[3]},
# ]
# with engine.connect() as conn:
#     conn.execute(stmt,values_list)
#     conn.commit()
def opens(stmts,res:list):
    with engine.connect() as conn:
        result = conn.execute(stmts).scalars()
        for row in result:
            res.append(row)
    return res

def save(table_name,value):
    query = insert(table_name).values(**value)
    session.execute(query)
    session.commit()

session = sessionmaker(bind=engine)()

def load_films():
    films = []
    query = select(Film.id, Film.name, Film.photo_id, Film.rating, Film.released_year, Film.file_id)
    result = session.execute(query).fetchall()
    for film in result:
        films.append({
            'id': film.id,
            'name': film.name,
            'photo_id': film.photo_id,
            'rating': film.rating,
            'release_year': film.released_year,
            'video': film.file_id
        })
    return films
films = load_films()

Base.metadata.create_all(engine)