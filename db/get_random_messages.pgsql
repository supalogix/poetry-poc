-- name: get_random_messages
-- Get random messages
SELECT row_to_json(t)
FROM 
(
    SELECT message 
    FROM health_check.random_message
    LIMIT 1
) t