from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from utils import rename_cols

if __name__ == '__main__':
    spark = SparkSession.builder.appName('mongoDBIntegration').getOrCreate()
    users = spark.read.csv('hdfs:///user/maria_dev/data/users.user', sep='|', inferSchema=True)
    users = rename_cols(users, ['userId', 'age', 'gender', 'occupation', 'zip'])

    users.write\
        .format('com.mongodb.spark.sql.DefaultSource')\
        .option('uri', 'mongodb://127.0.0.1/movielens.users')\
        .mode('append')\
        .save()

    read_users = spark.read\
        .format('com.mongodb.spark.sql.DefaultSource')\
        .option('uri', 'mongodb://127.0.0.1/movielens.users')\
        .load()

    print(read_users)

    read_users.createOrReplaceTempView('users')

    student_ids = spark.sql('SELECT userId FROM users WHERE occupation = "student"')
    student_ids.show()

    spark.stop()
s


