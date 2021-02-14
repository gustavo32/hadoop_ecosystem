SELECT DISTINCT u.occupation as Ocupation, count(*) as ratingsCount
FROM mongo.movielens.users u
JOIN hive.movielens.ratings r
ON u.userId = r.userId
GROUP BY u.occupation;