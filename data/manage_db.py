import sqlite3
import csv


def delete_data_in_db():
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    deleteSQLStatememnt1 = "DELETE from quickstart_books;"
    deleteSQLStatememnt2 = "delete from quickstart_chapters;"

    cur.execute(deleteSQLStatememnt1)
    cur.execute(deleteSQLStatememnt2)
    
    con.commit()
    con.close()


def add_table_data_to_db(csvfile, table_name, table_cols):
    cols = table_cols
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    
    with open(csvfile) as fin:
        dr = csv.DictReader(fin)
        to_db = [tuple([i[c] for c in cols]) for i in dr]
    
    len_cols = len(cols)
    cols = ",".join(cols)
    print(cols)
    values_param = ['?'] * len_cols
    values_param = ','.join(values_param)
    cur.executemany(f"INSERT INTO {table_name} ({cols}) VALUES ({values_param});", to_db)
    con.commit()
    con.close()
    print('data added to', table_name, 'from', csvfile)


def add_different_tables():
    csvfile = './quickstart_books.csv'
    table_name = 'quickstart_books'
    table_cols = ['book_id','book_title','author_name','published_year','folder_name','genre','number_of_chapters','thumbnail_url']
    add_table_data_to_db(csvfile, table_name, table_cols)


def main():
    delete_data_in_db()
    add_different_tables()


if __name__ == "__main__":
    main()
