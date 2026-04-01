--insert or update user
CREATE OR REPLACE PROCEDURE upsert_user(
    p_username VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM phonebook
        WHERE username=p_username
    ) THEN
        UPDATE phonebook
        SET phone=p_phone
        WHERE username=p_username;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_username, p_phone);
    END IF;
END;
$$;


--bulk insert users with validation 
CREATE OR REPLACE PROCEDURE bulk_insert_users(
    names TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    invalid_data := ARRAY[]::TEXT[];

    FOR i IN 1..array_length(names, 1)
    LOOP
        IF phones[i] ~ '^[0-9]{11}$' THEN
            INSERT INTO phonebook(username, phone)
            VALUES (names[i], phones[i]);
        ELSE
            invalid_data := array_append(
                invalid_data,
                names[i] || ' -> ' || phones[i]
            );
        END IF;
    END LOOP;
END;
$$;



--delete by username or phone
CREATE OR REPLACE PROCEDURE delete_user(
    p_value TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username=p_value
       OR phone=p_value;
END;
$$;