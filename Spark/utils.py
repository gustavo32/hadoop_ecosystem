from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

def parseInput(line):
    (userId, movieId, rating, timestamp) = line.split('\t')
    return (int(movieId), (float(rating), 1.0))

def getMapTitlesById():
    title_by_id = {}
    with open('data/movies.item', 'rb') as f:    
        for line in f:
            fields = line.split('|')
            title_by_id[int(fields[0])] = fields[1]

    return title_by_id

def rename_cols(df, new_columns, old_columns=None):
    if old_columns is None:
        old_columns = df.schema.names

    return df.selectExpr(*['{} as {}'.format(old, new) for old, new in zip(old_columns, new_columns)])