import psycopg2
import csv
from config import load_config

# 1. Вставка через консоль
def insert_from_console():
    fname = input("Введите имя: ")
    lname = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    
    sql = "INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s)"
    execute_query(sql, (fname, lname, phone), "Контакт добавлен!")

# 2. Загрузка из CSV
def upload_csv(file_path):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader) # пропускаем заголовок
                    for row in reader:
                        cur.execute("INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s)", row)
                conn.commit()
                print("Данные из CSV загружены!")
    except Exception as e:
        print(f"Ошибка CSV: {e}")

# 3. Обновление (Имя или Телефон)
def update_contact():
    target_id = input("Введите ID контакта для изменения: ")
    new_phone = input("Введите новый телефон (или пустую строку, чтобы оставить как есть): ")
    
    if new_phone:
        sql = "UPDATE phonebook SET phone_number = %s WHERE contact_id = %s"
        execute_query(sql, (new_phone, target_id), "Телефон обновлен!")

# 4. Поиск (Запрос с фильтром по имени)
def search_contact():
    name = input("Введите имя для поиска (или пустую строку для всех): ")
    sql = "SELECT * FROM phonebook WHERE first_name ILIKE %s"
    
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (f"%{name}%",))
            for row in cur.fetchall():
                print(row)

# 5. Удаление по имени или телефону
def delete_contact():
    print("1 - Удалить по имени, 2 - по телефону")
    choice = input("Выбор: ")
    val = input("Введите значение для удаления: ")
    
    col = "first_name" if choice == "1" else "phone_number"
    sql = f"DELETE FROM phonebook WHERE {col} = %s"
    execute_query(sql, (val,), "Контакт(ы) удален(ы)!")

# Вспомогательная функция, чтобы не дублировать код подключения
def execute_query(sql, params, success_msg):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()
                print(success_msg)
    except Exception as e:
        print(f"Ошибка базы данных: {e}")

if __name__ == "__main__":
    # Здесь можно вызывать функции для проверки:
    # upload_csv('contacts.csv')
    # insert_from_console()
    # search_contact()
    print("Программа готова. Раскомментируй нужную функцию в блоке 'if __name__ == \"__main__\"' для теста!")