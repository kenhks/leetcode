SELECT DISTINCT v.author_id as id
FROM views v
WHERE v.author_id = v.viewer_id
ORDER BY v.author_id