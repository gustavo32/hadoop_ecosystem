from pyspark import SparkConf, SparkContext
from utils import getMapTitlesById, parseInput

if __name__ == '__main__':
    conf = SparkConf().setAppName('WorstMovies')
    sc = SparkContext(conf=conf)

    title_by_id = getMapTitlesById()
    lines = sc.textFile('hdfs:///user/maria_dev/data/ratings.data')
    ratings = lines.map(parseInput)
    grouped_ratings = ratings.reduceByKey(lambda movie1, movie2: (movie1[0] + movie2[0], movie1[1] + movie2[1]))

    avg_ratings = grouped_ratings.mapValues(lambda movie: movie[0]/movie[1])
    sorted_ratings = avg_ratings.sortBy(lambda x: x[1])
    
    for movieId, rating in sorted_ratings.take(10):
        print('{} -> {}'.format(title_by_id[movieId], rating))