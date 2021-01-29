from mrjob.job import MRJob
from mrjob.step import MRStep


class OrderMostWatchedTVShows(MRJob):

    def steps(self):
        return [
                MRStep(
                    mapper=self.mapper_get_ratings,
                    reducer=self.reducer_count_ratings
                ),
                MRStep(
                    reducer=self.reducer_order_by_ratings
                )
            ]
    
    def mapper_get_ratings(self, _, line):
        (userId, movieId, rating, timestamp) = line.split('\t')
        yield movieId, 1
    
    def reducer_count_ratings(self, key, values):
        yield str(sum(values)).zfill(6), key 

    def reducer_order_by_ratings(self, count, movies):
        for movie in movies:
            yield movie, count

if __name__ == "__main__":
    OrderMostWatchedTVShows.run()