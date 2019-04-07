import sqlite3
from sac_app import db
from sac_app.models import Ingredients
import psycopg2


def get_sqlite3_ingredients():
    conn = sqlite3.connect("Skyrim.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredients")
    result = cursor.fetchall()
    conn.close()
    return result

def insert_postgres_ingredients(data):
    # перенос в бд
    for _ in data:
        db.session.add(Ingredients(name=_[0], id_object=_[1], attribute_1=_[2], attribute_2=_[3], attribute_3=_[4],
                                   attribute_4=_[5]))
    db.session.commit()

def del_postgres_ingredients():
    # удаление из бд
    ingredients = Ingredients.query.all()
    for _ in ingredients:
        db.session.delete(_)
    db.session.commit()



def get_sqlite3_positive():
    conn = sqlite3.connect("Skyrim.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Positive")
    result = cursor.fetchall()
    conn.close()
    return result

def insert_postgres_positive(data):
    conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='postgres', dbname='skyrim')
    cursor = conn.cursor()
    for _ in data:
        cursor.execute("INSERT INTO positive(attribute) VALUES (%s)", (str(_[0]),))
    conn.commit()
    cursor.close()
    conn.close()



def get_sqlite3_negative():
    conn = sqlite3.connect("Skyrim.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Negative")
    result = cursor.fetchall()
    conn.close()
    return result

def insert_postgres_negative(data):
    conn = None
    data_extend = data
    try:
        conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='postgres', dbname='skyrim')
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO negative(attribute) VALUES (%s)", data_extend) #not all arguments converted during string formatting
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()



def main():
    data = get_sqlite3_ingredients()
    insert_postgres_ingredients(data)


    data = get_sqlite3_positive()
    insert_postgres_positive(data)

    data = get_sqlite3_negative()
    insert_postgres_negative(data)

if __name__ == '__main__':
    main()




