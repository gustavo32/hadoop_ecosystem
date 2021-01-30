CREATE VIEW IF NOT EXISTS groupedRatings AS
SELECT movieId, AVG(rating) as ratingAvg, COUNT(rating) as ratingCount
FROM ratings
GROUP BY movieId
ORDER BY ratingAvg DESC;


SELECT m.title, gp.ratingAvg
FROM groupedRatings as gp JOIN movies as m ON gp.movieId == m.movieId
WHERE gp.ratingCount > 10
LIMIT 10;