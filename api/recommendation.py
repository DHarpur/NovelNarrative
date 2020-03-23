import surprise
from collections import defaultdict
import pandas as pd


def get_top_n(predictions, n=10):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def get_book_title(book_id):
    return bookData.loc[bookData['book_id'] == book_id].title


bookData = pd.read_csv("./data/book/books.csv", header=0)

bookPredictions, bookAlgorithm = surprise.dump.load("./RecommenderDump/algorithm1_dump")


topRecommendations = get_top_n(bookPredictions, n=10)

print(topRecommendations['22771'])

topRecommendationsBooks = topRecommendations['22771'][0][0]
print(get_book_title(int(topRecommendationsBooks)))
