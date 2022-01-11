from os import link
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv

def get_row():

    with open('result.csv', encoding='utf-8') as file:
        
        src = csv.reader(file, delimiter=',')
        for row in src:
                pass
                
def insertToPostgreSQL():
    try:
        with psycopg2.connect(user='user_one', password='12345', host='127.0.0.1', port='5432', database='test') as connection:
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with connection.cursor() as cursor:
                
                with open('result.csv', encoding='utf-8') as file:
                    
                    src = csv.reader(file,delimiter=',')
                  
                    for row in src:
                        title = str(row[1])
                        author = str(row[2])
                        year = str(row[3])
                        link = str(row[4])
                        insert_query = """INSERT INTO books (title,author,year,link) VALUES (%s,%s,%s,%s);"""
                        cursor.execute(insert_query,(title, author, year, link))


                select_query = """SELECT * FROM books;"""
                cursor.execute(select_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

    except (Exception, Error) as err:
        print(err)

    finally:
        pass

if __name__=="__main__":
    insertToPostgreSQL()
