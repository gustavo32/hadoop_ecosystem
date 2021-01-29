from pyspark.sql import SparkSession
from utils import rename_cols

if __name__ == '__main__':
    spark = SparkSession.builder.appName('worstMovies').getOrCreate()
    ratings = spark.read.csv('hdfs:///user/maria_dev/data/ratings.data', sep='\t', inferSchema=True)
    ratings = rename_cols(ratings, ['userId', 'movieId', 'rating', 'timestamp'])

    movies = spark.read.csv('hdfs:///user/maria_dev/data/movies.item', sep='|', inferSchema=True)
    movies = rename_cols(movies, ['movieId', 'title', 'date'], ['_c0', '_c1', '_c2'])

    grouped_df = ratings.groupby('movieId')

    avgRating = grouped_df.avg('rating')
    countRating = grouped_df.count()

    df = avgRating.join(countRating, 'movieId').join(movies, 'movieId')
    ordered_df = df.orderBy('avg(rating)')

    for row in ordered_df.take(10):
        print(row)

    spark.stop()
    

