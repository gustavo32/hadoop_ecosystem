ratings = LOAD 'data/ratings.data' AS (userId:int, movieId:int, rating:int, timestamp:int);
movies = LOAD 'data/movies.item' USING PigStorage('|') AS (movieId:int, title:chararray, date:chararray);

formattedMovies = FOREACH movies GENERATE movieId, title, ToDate(date, 'dd-MMM-yyyy') AS releasedDate;

groupedRatings = GROUP ratings BY movieId;
avgRatings = FOREACH groupedRatings GENERATE group AS movieId, AVG(ratings.rating) AS rating;
filteredRatings = FILTER avgRatings BY rating > 4;

ratingsByMovie = JOIN filteredRatings BY movieId LEFT, formattedMovies BY movieId;

orderMovieByAge = ORDER ratingsByMovie BY formattedMovies::releasedDate ASC;
finalResults = FOREACH orderMovieByAge GENERATE formattedMovies::title as title, filteredRatings::rating as rating, formattedMovies::releasedDate as releaseDate;

DUMP finalResults;