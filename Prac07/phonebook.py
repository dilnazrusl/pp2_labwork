import psycopg2
import csv
from config import load_config
config=load_config()
def create_table():
    conn=psycopg2.connect(**config)
    cur=conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    username=input("Enter name: ")
    phone=input("Enter phone: ")

    conn=psycopg2.connect(**config)
    cur=conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (username, phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv():
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    count=0

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader=csv.reader(file)
        for row in reader:
            print(f"Adding {row}")
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
            count+=1
    conn.commit()
    cur.close()
    conn.close()
    print(f"{count} contacts imported from csv")

def query_all():
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def update_contact(old_name, new_name, new_phone):
    conn=psycopg2.connect(**config)
    cur=conn.cursor()

    cur.execute("""
        UPDATE phonebook
        SET username=%s, phone=%s
        WHERE username=%s
    """, (new_name, new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()

def delete_by_name(name):
    conn=psycopg2.connect(**config)
    cur= conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE username=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()



create_table()
while True:
    print("\n Phonebook Menu")
    print("1.Add contact from console")
    print("2.Add contacts from csv")
    print("3.Show all contacts")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Exit")

    ch=input("Enter your choice: ")
    if ch=="1":
        insert_from_console()
        query_all()
    elif ch=="2":
        insert_from_csv()
        query_all()
    elif ch=="3":
        query_all()
    elif ch=="4":
        old_name=input("old name: ")
        new_name=input("new name: ")
        new_phone=input("new phone: ")
        update_contact(old_name, new_name, new_phone)
        query_all()
    elif ch=="5":
        del_name=input("name to delete: ")
        delete_by_name(del_name)
        query_all()
    elif ch=="6":
        print("Exiting.")
        break
    else:
        print("Invalid choice")
