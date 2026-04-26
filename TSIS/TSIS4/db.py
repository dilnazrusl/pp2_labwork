import psycopg2
from config import DB_CONFIG


def connect():
    return psycopg2.connect(**DB_CONFIG)


def get_or_create_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    row = cur.fetchone()

    if row:
        pid = row[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return pid


def save_score(username, score, level):
    conn = connect()
    cur = conn.cursor()

    pid = get_or_create_player(username)

    cur.execute("""
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES(%s, %s, %s)
    """, (pid, score, level))

    conn.commit()
    cur.close()
    conn.close()


def get_top10():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def get_personal_best(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT MAX(score)
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username=%s
    """, (username,))

    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result if result else 0