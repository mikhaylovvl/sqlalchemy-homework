import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_all_tables, Publisher, Book, Stock, Shop, Sale
import os
from dotenv import load_dotenv


class DataBase:
    load_dotenv()

    def __init__(self):
        self.engine = sqlalchemy.create_engine(os.getenv("DSN"))

    # создаем таблицы
    def create_tables(self):
        create_all_tables(self.engine)

    # добавляем данные
    def add_data(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        pub1 = Publisher(name="Eksmo")
        pub2 = Publisher(name="Azbuka")
        pub3 = Publisher(name="Alfa-book")
        pub4 = Publisher(name="Amfora")
        pub5 = Publisher(name="Piter")
        pub6 = Publisher(name="Nauka")

        book1 = Book(title="Мальчик в полосатой пижаме", publisher_id=1)
        book2 = Book(title="Источник", publisher_id=1)
        book3 = Book(title="Все та же я", publisher_id=2)
        book4 = Book(title="Восхитительная ведьма", publisher_id=2)
        book5 = Book(title="Гордость и предубеждение", publisher_id=3)
        book6 = Book(title="Позже", publisher_id=4)
        book7 = Book(title="Царство Греха", publisher_id=5)
        book8 = Book(title="Ведьмак", publisher_id=6)

        shop1 = Shop(name="Litres")
        shop2 = Shop(name="Ozon")
        shop3 = Shop(name="Labirint")
        shop4 = Shop(name="chitai-gorod")

        stock1 = Stock(id_book=1, id_shop=1, count=100)
        stock2 = Stock(id_book=2, id_shop=2, count=55)
        stock3 = Stock(id_book=3, id_shop=3, count=2)
        stock4 = Stock(id_book=4, id_shop=3, count=21)
        stock5 = Stock(id_book=5, id_shop=4, count=7)
        stock6 = Stock(id_book=6, id_shop=4, count=33)

        session.add_all([pub1, pub2, pub3, pub4, pub5, pub6, book1, book2, book3, book4, book5, book6, book7, book8,
                         shop1, shop2, shop3, shop4, stock1, stock2, stock3, stock4, stock5, stock6])
        session.commit()
        session.close()

    # поиск издателя
    def find_publisher(self, id_name):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        if id_name_publisher.isdigit():
            print(session.query(Publisher).filter(Publisher.id == id_name).first())
        else:
            print(session.query(Publisher).filter(Publisher.name == id_name).first())

        session.close()

    # запрос выборки магазинов, где продают книги издателя
    def find_shops(self, id_name):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        if id_name.isdigit():
            a_query = session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.id == id_name).all()
            for i in a_query:
                print(i)
        else:
            a_query = session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == id_name).all()
            for i in a_query:
                print(i)

        session.close()


if __name__ == '__main__':
    data_base = DataBase()

    # создаем таблицы
    data_base.create_tables()

    # заполняем таблицы данными
    data_base.add_data()

    # поиск издателя
    id_name_publisher = input("Введите имя или идентификатор publisher: ").strip()
    data_base.find_publisher(id_name_publisher)

    # запрос выборки магазинов, где продают книги издателя
    id_name_publisher = input("Введите имя или идентификатор publisher: ").strip()
    data_base.find_shops(id_name_publisher)
