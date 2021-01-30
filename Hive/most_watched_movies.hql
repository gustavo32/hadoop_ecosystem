CREATE VIEW IF NOT EXISTS topMoviesId AS
SELECT movieId, COUNT(rating) as ratingCount
FROM ratings
GROUP BY movieId
ORDER BY ratingCount DESC;

SELECT m.title, ratingCount
FROM topMoviesId as t JOIN movies as m ON t.movieId = m.movieId
LIMIT 10;