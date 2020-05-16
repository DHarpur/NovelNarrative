# from surprise import SVD, Dataset, Reader, dump
import pandas as pd
from lightfm import LightFM
from lightfm.data import Dataset
import joblib

print("Loading dump file")
# _, movieAlgo = dump.load('./RecommenderDump/algorithm2_dump')
l = joblib.load('./RecommenderDump/BookModel')

# user = {'user_id': '55555', 'movie_id': ['70', '264', '18'], 'rating': ['4', '3', '5']}
# print("Send user data to movie ratings file")
# userDF = pd.DataFrame(data=user)
# userDF.to_csv('./data/movie/ratings.csv', mode='a', header=False)

print("Load in movie ratings file")
# reader2 = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
# ratingsDS = Dataset.load_from_file('./data/movie/ratings.csv', reader2)
# ratingsDF = pd.read_csv('./data/movie/ratings.csv')
# ratingsDF = ratingsDF.rename(columns={'userId': 'user_id', 'movieId': 'movie_id', 'rating': 'rating'})

newUser = pd.DataFrame(data=[[60000, 264, 5, 'heroic'], [60000, 18, 3, 'historic'], [60000, 70, 4, 'sci-fi']],
                       columns=['user_id', 'book_id', 'rating', 'tag_name'])
userDS = Dataset()
userDS.fit((x['user_id'] for _, x in newUser.iterrows()), (x['book_id'] for _, x in newUser.iterrows()),
           item_features=(x['tag_name'] for _, x in newUser.iterrows()))

print("Building training set")
# ratingsTrain = ratingsDS.build_full_trainset()
num_users, num_items = userDS.interactions_shape()
(interactions, weights) = userDS.build_interactions(((x['user_id'], x['book_id']) for _, x in newUser.iterrows()))

print(newUser.head())
print("Starting fit")
# movieAlgo.fit(ratingsTrain)
lightFMAlgo.fit_partial(interactions, sample_weight=weights)
print("Finished fit")
print("Sending to dump file")
# joblib.dump(lightFMAlgo, "./RecommenderDump/algorithm2_dump")
print("Sent to dump file")
