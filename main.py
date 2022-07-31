import sqlalchemy
from sqlalchemy.orm import sessionmaker

# импорт моделей
from models import create_tables, Publisher, Book, Stock, Shop, Sale


def main(id_name_publisher):
    # параметры подключения
    type_db = "postgresql"
    login = "postgres"
    password = ""
    name_server = "localhost"
    port_server = "5432"
    name_bd = "sqlalchemy_db"

    # абстракция для подключения к БД
    DSN = f'{type_db}://{login}:{password}@{name_server}:{port_server}/{name_bd}'
    engine = sqlalchemy.create_engine(DSN)

    # создаем таблицы
    create_tables(engine)

    # создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()

    pub1 = Publisher(name="Eksmo")
    pub2 = Publisher(name="Azbuka")
    pub3 = Publisher(name="Alfa-book")
    pub4 = Publisher(name="Amfora")
    pub5 = Publisher(name="Piter")
    pub6 = Publisher(name="Nauka")

    session.add_all([pub1, pub2, pub3, pub4, pub5, pub6])
    session.commit()

    if id_name_publisher.isdigit():
        print(session.query(Publisher).filter(Publisher.id == id_name_publisher).first())
    else:
        print(session.query(Publisher).filter(Publisher.name == id_name_publisher).first())

    session.close()


if __name__ == '__main__':
    id_name_publisher = input("Введите имя или идентификатор publisher: ").strip()
    main(id_name_publisher)
