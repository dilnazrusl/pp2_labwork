import json
import csv
import psycopg2.extras
from connect import get_conn



# Утилита вывода

def print_contact(row):
    print(f"  [{row['id']}] {row['username']}"
          f"  | email: {row['email'] or '—'}"
          f"  | birthday: {row['birthday'] or '—'}"
          f"  | group: {row['group_name'] or '—'}"
          f"  | phones: {row['phones'] or '—'}")



# 1. Добавить / обновить контакт

def upsert():
    name = input("Имя: ").strip()
    phone = input("Телефон: ").strip()
    ptype = input("Тип (home/work/mobile): ").strip()
    email = input("Email: ").strip()
    birthday = input("Birthday (YYYY-MM-DD): ").strip()
    group = input("Group: ").strip()

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL upsert_u(%s, %s, %s, %s, %s, %s)",
                (name, phone, ptype, email, birthday, group)
            )
        conn.commit()

    print("Готово")



# 2. Добавить телефон к существующему контакту

def add_phone():
    name  = input("Имя контакта: ").strip()
    phone = input("Новый телефон: ").strip()
    ptype = input("Тип (home/work/mobile) [mobile]: ").strip() or "mobile"

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
            conn.commit()
        print(" Телефон добавлен.")
    except Exception as e:
        print(f" Ошибка: {e}")



# 3. Переместить контакт в группу

def move_group():
    name  = input("Имя контакта: ").strip()
    group = input("Группа (Family/Work/Friend/Other или новая): ").strip()

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL move_to_group(%s, %s)", (name, group))
            conn.commit()
        print(" Группа обновлена.")
    except Exception as e:
        print(f"Ошибка: {e}")



# 4. Поиск (по имени / email / телефону / группе)

def search():
    q = input("Поисковый запрос: ").strip()

    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (q,))
            rows = cur.fetchall()

    if rows:
        for row in rows:
            print_contact(row)
    else:
        print("Ничего не найдено.")



# 5. Фильтр по группе

def filter_group():
    g = input("Группа (Family/Work/Friend/Other): ").strip()

    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                SELECT c.id, c.username, c.email, c.birthday,
                       gr.name AS group_name,
                       STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ') AS phones
                FROM contacts c
                LEFT JOIN groups gr ON gr.id = c.group_id
                LEFT JOIN phones p  ON p.contact_id = c.id
                WHERE gr.name ILIKE %s
                GROUP BY c.id, gr.name
                ORDER BY c.username
            """, (g,))
            rows = cur.fetchall()

    if rows:
        for row in rows:
            print_contact(row)
    else:
        print("Контакты в этой группе не найдены.")



# 6. Сортировка

def sort_contacts():
    print("Сортировать по: 1) имени  2) дню рождения  3) дате добавления")
    choice = input("Выбор: ").strip()

    order_map = {"1": "c.username", "2": "c.birthday", "3": "c.created_at"}
    order_col = order_map.get(choice, "c.username")

    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(f"""
                SELECT c.id, c.username, c.email, c.birthday,
                       gr.name AS group_name,
                       STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ') AS phones
                FROM contacts c
                LEFT JOIN groups gr ON gr.id = c.group_id
                LEFT JOIN phones p  ON p.contact_id = c.id
                GROUP BY c.id, gr.name
                ORDER BY {order_col} NULLS LAST
            """)
            rows = cur.fetchall()

    for row in rows:
        print_contact(row)



# 7. Постраничная навигация

def pagination():
    page = 0
    size = 3

    while True:
        print(f"\n── Страница {page + 1} ──")
        with get_conn() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM pagination(%s, %s)", (size, page * size))
                rows = cur.fetchall()

        if not rows:
            print("Больше контактов нет.")
            if page > 0:
                page -= 1
            else:
                break
        else:
            for row in rows:
                print_contact(row)

        cmd = input("n — вперёд | p — назад | q — выйти: ").strip()
        if cmd == 'n':
            page += 1
        elif cmd == 'p':
            page = max(0, page - 1)
        else:
            break



# 8. Экспорт в JSON

def export_json():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM full_contacts")
            rows = cur.fetchall()

    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "username": r[1],
            "email": r[2],
            "birthday": str(r[3]) if r[3] else None,
            "group": r[4],
            "phones": r[5]
        })

    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("JSON экспорт исправлен")

# 9. Импорт из JSON

def import_json():
    try:
        with open("contacts.json", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(" Файл contacts.json не найден.")
        return

    with get_conn() as conn:
        with conn.cursor() as cur:
            for entry in data:
                name     = entry.get("username", "").strip()
                email    = entry.get("email")
                birthday = entry.get("birthday")

                if not name:
                    continue

                cur.execute("SELECT id FROM contacts WHERE username = %s", (name,))
                exists = cur.fetchone()

                if exists:
                    choice = input(f"  '{name}' уже есть. Перезаписать? (y/n): ").strip()
                    if choice.lower() != 'y':
                        print(f"  Пропущено: {name}")
                        continue
                    cur.execute(
                        "UPDATE contacts SET email=%s, birthday=%s WHERE username=%s",
                        (email, birthday, name)
                    )
                else:
                    cur.execute(
                        "INSERT INTO contacts(username, email, birthday) VALUES (%s, %s, %s)",
                        (name, email, birthday)
                    )

        conn.commit()
    print(" Импорт из JSON завершён.")



# 10. Импорт из CSV 

def import_csv():
    try:
        with open("contacts.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            with get_conn() as conn:
                with conn.cursor() as cur:
                    for row in reader:
                        name     = row.get("username", "").strip()
                        phone    = row.get("phone", "").strip()
                        ptype    = row.get("phone_type", "mobile").strip() or "mobile"
                        email    = row.get("email", "").strip() or None
                        birthday = row.get("birthday", "").strip() or None
                        group    = row.get("group", "").strip() or None

                        if not name:
                            continue

                        # Вставляем/обновляем контакт
                        cur.execute("""
                            INSERT INTO contacts(username, email, birthday)
                            VALUES (%s, %s, %s)
                            ON CONFLICT (username) DO UPDATE
                                SET email    = EXCLUDED.email,
                                    birthday = EXCLUDED.birthday
                        """, (name, email, birthday))

                        # Привязываем группу
                        if group:
                            cur.execute("""
                                INSERT INTO groups(name) VALUES (%s)
                                ON CONFLICT (name) DO NOTHING
                            """, (group,))
                            cur.execute("""
                                UPDATE contacts
                                SET group_id = (SELECT id FROM groups WHERE name = %s)
                                WHERE username = %s
                            """, (group, name))

                        # Добавляем телефон если задан
                        if phone:
                            cur.execute(
                                "SELECT id FROM contacts WHERE username = %s", (name,)
                            )
                            cid = cur.fetchone()[0]
                            cur.execute("""
                                INSERT INTO phones(contact_id, phone, type)
                                VALUES (%s, %s, %s)
                            """, (cid, phone, ptype))

                conn.commit()
        print(" CSV импорт завершён.")
    except FileNotFoundError:
        print(" Файл contacts.csv не найден.")



# МЕНЮ
#
def main():
    menu = """
╔══════════════════════════════════════╗
║           PhoneBook TSIS1            ║
╠══════════════════════════════════════╣
║  1 — Добавить/обновить контакт       ║
║  2 — Добавить телефон                ║
║  3 — Сменить группу                  ║
║  4 — Поиск                           ║
║  5 — Фильтр по группе                ║
║  6 — Сортировка                      ║
║  7 — Постраничный просмотр           ║
║  8 — Экспорт в JSON                  ║
║  9 — Импорт из JSON                  ║
║  0 — Импорт из CSV                   ║
║  q — Выход                           ║
╚══════════════════════════════════════╝"""

    actions = {
        '1': upsert,
        '2': add_phone,
        '3': move_group,
        '4': search,
        '5': filter_group,
        '6': sort_contacts,
        '7': pagination,
        '8': export_json,
        '9': import_json,
        '0': import_csv,
    }

    while True:
        print(menu)
        c = input("Выбор: ").strip()
        if c == 'q':
            print("До свидания!")
            break
        action = actions.get(c)
        if action:
            action()
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()