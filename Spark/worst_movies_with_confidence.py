from pyspark.sql import SparkSession
from utils import rename_cols

spark = SparkSession.builder.appName('worstMoviesWithConfidence').getOrCreate()

ratings = spark.read.csv('hdfs:///user/maria_dev/data/ratings.data', sep='\t', inferSchema=True)
ratings = rename_cols(ratings, ['userId', 'movieId', 'rating', 'timestamp'])

movies = spark.read.csv('hdfs:///user/maria_dev/data/movies.item', sep='|', inferSchema=True)
movies = rename_cols(movies, ['movieId', 'title', 'date'], ['_c0', '_c1', '_c2'])

grouped_ratings = ratings.groupby('movieId')

avg_ratings = grouped_ratings.avg('rating')
count_ratings = grouped_ratings.count()

df = avg_ratings.join(count_ratings, 'movieId').join(movies, 'movieId', 'left')
df_with_confidence = df.filter('count > 10').orderBy('avg(rating)')

for row in df_with_confidence.take(10):
    print(row)

spark.stop()
