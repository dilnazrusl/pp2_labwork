-- search by pattern
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(
    ID INT,
    username VARCHAR,
    phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    WHERE p.username ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$;


--pagination function
CREATE OR REPLACE FUNCTION get_phonebook_paginated(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(
    id INT,
    username VARCHAR,
    phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$;