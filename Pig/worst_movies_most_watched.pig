ratings = LOAD 'data/ratings.data' AS (userId:int, movieId:int, rating:int, timestamp:int);
movies = LOAD 'data/movies.item' USING PigStorage('|') AS (movieId:int, title:chararray, releasedDate:chararray);

groupedRatings = GROUP ratings BY movieId;
countedRatings = FOREACH groupedRatings GENERATE group AS movieId, AVG(ratings.rating) AS rating, COUNT(ratings.rating) AS ratingNumber;
filteredRatings = FILTER countedRatings BY rating < 2;

ratedMovies = JOIN filteredRatings BY movieId LEFT, movies BY movieId;

moviesOrderedByCount = ORDER ratedMovies BY filteredRatings::ratingNumber DESC;
finalResults = FOREACH moviesOrderedByCount GENERATE movies::title as title, filteredRatings::ratingNumber as ratingNumber, filteredRatings::rating as rating;
DUMP finalResults;
