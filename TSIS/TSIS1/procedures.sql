-- ============================================================
-- UPSERT: добавить или обновить контакт + телефон
-- ============================================================
CREATE OR REPLACE PROCEDURE upsert_u(
    p_name  VARCHAR,
    p_phone VARCHAR,
    p_type  VARCHAR DEFAULT 'mobile'
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INT;
BEGIN
    INSERT INTO contacts(username)
    VALUES (p_name)
    ON CONFLICT (username) DO NOTHING;

    SELECT id INTO v_id FROM contacts WHERE username = p_name;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (v_id, p_phone, p_type);
END;
$$;

-- ============================================================
-- ADD_PHONE: добавить телефон к существующему контакту
-- ============================================================
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR DEFAULT 'mobile'
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INT;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE username = p_contact_name;

    IF v_id IS NULL THEN
        RAISE EXCEPTION 'Контакт "%" не найден', p_contact_name;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (v_id, p_phone, p_type);
END;
$$;

-- ============================================================
-- MOVE_TO_GROUP: переместить контакт в группу (создать если нет)
-- ============================================================
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name   VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_gid INT;
    v_cid INT;
BEGIN
    -- Создаём группу если не существует
    INSERT INTO groups(name)
    VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO v_gid FROM groups WHERE name = p_group_name;
    SELECT id INTO v_cid FROM contacts WHERE username = p_contact_name;

    IF v_cid IS NULL THEN
        RAISE EXCEPTION 'Контакт "%" не найден', p_contact_name;
    END IF;

    UPDATE contacts SET group_id = v_gid WHERE id = v_cid;
END;
$$;

-- ============================================================
-- SEARCH_CONTACTS: поиск по имени, email, телефону
-- Возвращает контакты даже без телефонов (LEFT JOIN + HAVING/WHERE fix)
-- ============================================================
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    id         INT,
    username   VARCHAR,
    email      VARCHAR,
    birthday   DATE,
    group_name VARCHAR,
    phones     TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.username,
        c.email,
        c.birthday,
        g.name AS group_name,
        STRING_AGG(p.phone || ' (' || COALESCE(p.type, '?') || ')', ', ') AS phones
    FROM contacts c
    LEFT JOIN groups g  ON g.id = c.group_id
    LEFT JOIN phones p  ON p.contact_id = c.id
    WHERE
        p_query = ''
        OR c.username ILIKE '%' || p_query || '%'
        OR c.email    ILIKE '%' || p_query || '%'
        OR p.phone    ILIKE '%' || p_query || '%'
        OR g.name     ILIKE '%' || p_query || '%'
    GROUP BY c.id, c.username, c.email, c.birthday, g.name
    ORDER BY c.username;
END;
$$;

-- ============================================================
-- PAGINATION: постраничный вывод
-- ============================================================
CREATE OR REPLACE FUNCTION pagination(lim INT, offs INT)
RETURNS TABLE(
    id         INT,
    username   VARCHAR,
    email      VARCHAR,
    birthday   DATE,
    group_name VARCHAR,
    phones     TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.username,
        c.email,
        c.birthday,
        g.name AS group_name,
        STRING_AGG(p.phone || ' (' || COALESCE(p.type, '?') || ')', ', ') AS phones
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    GROUP BY c.id, c.username, c.email, c.birthday, g.name
    ORDER BY c.username
    LIMIT lim OFFSET offs;
END;
$$;