from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from utils import rename_cols

if __name__ == '__main__':
    spark = SparkSession.builder.appName('movieRecommender').getOrCreate()
    ratings = spark.read.csv('hdfs:///user/maria_dev/data/ratings.data', sep='\t', inferSchema=True)
    ratings = rename_cols(ratings, ['userId', 'movieId', 'rating', 'timestamp'])

    movies = spark.read.csv('hdfs:///user/maria_dev/data/movies.item', sep='|', inferSchema=True)
    movies = rename_cols(movies, ['movieId', 'title', 'date'], ['_c0', '_c1', '_c2'])

    df = ratings.join(movies, 'movieId', 'left').cache()

    train, test = df.randomSplit([0.8, 0.2], seed=42)

    als = ALS(
            userCol="userId", 
            itemCol="movieId",
            ratingCol="rating", 
            nonnegative = True, 
            implicitPrefs = False,
            coldStartStrategy="drop"
    )

    param_grid = ParamGridBuilder() \
                .addGrid(als.rank, [5, 10, 50]) \
                .addGrid(als.regParam, [.01, .05, .1]) \
                .build()

    evaluator = RegressionEvaluator(
            metricName="rmse", 
            labelCol="rating", 
            predictionCol="prediction")

    print ("Num models to be tested: ", len(param_grid))

    cv = CrossValidator(estimator=als, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=5)

    model = cv.fit(train)
    best_model = model.bestModel
    test_predictions = best_model.transform(test)
    RMSE = evaluator.evaluate(test_predictions)
    print(RMSE)

    recommendations = best_model.recommendForAllUsers(5)
    recommendations.show()

    spark.stop()

    # nrecommendations = nrecommendations\
    #     .withColumn("rec_exp", explode("recommendations"))\
    #     .select('userId', col("rec_exp.movieId"), col("rec_exp.rating"))
    # nrecommendations.limit(10).show()
