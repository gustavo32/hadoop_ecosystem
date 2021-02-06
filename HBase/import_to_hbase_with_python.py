from starbase import Connection

c = Connection('127.0.0.1', '8001')

ratings = c.table('ratings')

if ratings.exists():
    print('Ratings table already exists. Dropping table...')
    ratings.drop()

ratings.create('rating')
ratingFile = open('data/ratings.data', 'r')

batch = ratings.batch()

for line in ratingFile:
    (userId, movieId, rating, timestamp) = line.split('\t')
    batch.update(userId, {'rating': {movieId: rating}})

ratingFile.close()
batch.commit(finalize=True)

print('Fetching data of UserId = 32')
print(ratings.fetch('32'))




    
    