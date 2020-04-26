import sqlite3
import csv
from collections import namedtuple

Table = namedtuple('Table', ['csvfile', 'table_name', 'table_cols'])

###########################################
# ADD all the new tables here
##########################################
ALL_TABLES = [
    Table('./quickstart_books.csv', 'quickstart_books', ['book_id','book_title','author_name','published_year','folder_name','genre','number_of_chapters','thumbnail_url']),
    #Table('./quickstart_books.csv', 'quickstart_books', ['book_id','book_title','author_name','published_year','folder_name','genre','number_of_chapters','thumbnail_url']),
]


def delete_data_in_db(data):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    deleteSQLStatememnt1 = f"DELETE from {data.table_name};"

    cur.execute(deleteSQLStatememnt1)

    con.commit()
    con.close()


def add_table_data_to_db(data):
    cols = data.table_cols
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    with open(data.csvfile) as fin:
        dr = csv.DictReader(fin)
        to_db = [tuple([i[c] for c in cols]) for i in dr]

    len_cols = len(cols)
    cols = ",".join(cols)
    print(cols)
    values_param = ['?'] * len_cols
    values_param = ','.join(values_param)
    cur.executemany(f"INSERT INTO {data.table_name} ({cols}) VALUES ({values_param});", to_db)
    con.commit()
    con.close()
    print('data added to', data.table_name, 'from', data.csvfile)


def main():
    for data in ALL_TABLES:
        delete_data_in_db(data)
        add_table_data_to_db(data)


if __name__ == "__main__":
    main()
