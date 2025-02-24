

from sqlalchemy import create_engine
from sqlalchemy.orm import  DeclarativeBase

class Base (DeclarativeBase):
    pass



class DB:
    engine = create_engine("postgresql+psycopg2://postgres:4321@localhost:5432/projects")


# ==========================================================================


# def to_dict(cursor):
#     columns=list(cursor.description)
#     result=cursor.fetchall()
#     results=[]
#     for r in result:
#         row_dict={}
#         for i, c in enumerate(columns):
#             row_dict[c.name]=r[i]
#         results.append(row_dict)
#     return results

# class CRUD(DB):
#     # DB_NAME = getenv('DB_NAME')
#     # USER = getenv('DB_USER')
#     # PORT = getenv('DB_PORT')
#     # HOST = getenv('DB_HOST')
#     # PASSWORD = getenv('DB_PASSWORD')
#     # connect = psycopg2.connect(dbname = DB_NAME,user=USER,password=PASSWORD,host=HOST,port=PORT)     # PEP8
#     # cursor = connect.cursor()
#     def get_objects(self ,*cols) -> list:
#         data: list[dict] = self.get(*cols)
#         objects = []
#         for d in data:
#             obj = self.__class__(**d)
#             objects.append(obj)
#         return objects
#     def save(self):
#         cols = [key for key , val in self.__dict__.items() if val != None]
#         args = [val for key , val in self.__dict__.items() if val != None]
#         table_name = self.__class__.__name__.lower() + "s"
#         cols_format = ",".join(cols)
#         values_format = ",".join(["%s"]*len(cols))
#         query = f"""insert into {table_name}({cols_format}) values ({values_format})"""
#         self.cur.execute(query , args)
#         self.connect.commit()
#
#     def get(self, *cols):
#         cols_format = "*"
#         if cols:
#             cols_format = ",".join(cols)
#         table_name = self.__class__.__name__.lower() + "s"
#         condition_attr = [key for key, val in self.__dict__.items() if val != None]
#         condition_val = [val for key, val in self.__dict__.items() if val != None]
#         condition_format = "where " + " = %s and ".join(condition_attr) + " = %s" if condition_attr else ""
#         query = f"""select {cols_format} from {table_name} {condition_format}"""
#         self.cur.execute(query, condition_val)
#         print(query)
#         return to_dict(self.cur)
#     def update(self , **kwargs):
#         condition_attr = [key for key , val in self.__dict__.items() if val != None]
#         condition_val = [val for key , val in self.__dict__.items() if val != None]
#
#         set_attr = " = %s , ".join(kwargs.keys()) + " = %s"
#         set_val = list(kwargs.values())
#         condition_format = "where "+"= %s and ".join(condition_attr) + " = %s" if condition_attr else ""
#
#         table_name = self.__class__.__name__.lower() + "s"
#
#         query = f"""update {table_name} set {set_attr} {condition_format}"""
#         self.cur.execute(query , set_val + condition_val)
#         self.connect.commit()
#     def delete(self , **kwargs):
#         condition_attr = [key for key, val in self.__dict__.items() if val != None]
#         condition_val = [val for key, val in self.__dict__.items() if val != None]
#         condition_format = "where "+"= %s and ".join(condition_attr) + " = %s" if condition_attr else ""
#         table_name = self.__class__.__name__.lower() + "s"
#         query = f"""delete from {table_name}  {condition_format}"""
#         self.cur.execute(query , condition_val)
#         print(query)
#         self.connect.commit()
