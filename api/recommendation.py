import surprise
from collections import defaultdict
import pandas as pd

pd.options.display.width = 0


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


def three_lists():
    return [[], [], []]


def get_user_recommendations(user_id, predictions, n=10):
    top_n = defaultdict(list)
    i = 1
    for uid, iid, true_r, est, _ in predictions:
        if uid == user_id:
            top_n[i].append((uid, iid, est))
            i += 1

    top_n_df = pd.DataFrame.from_dict(top_n, orient='index')
    top_n_df = pd.DataFrame(top_n_df[0].to_list(), index=top_n_df.index, columns=['user_id', 'item_id', 'estimate'])

    top_n_df = top_n_df.sort_values(by='estimate', ascending=False)

    return top_n_df.head(n)


def get_book_title(book_id):
    return


bookData = pd.read_csv("./data/book/books.csv", header=0)

bookPredictions, bookAlgorithm = surprise.dump.load("./RecommenderDump/algorithm1_dump")

userRecommendations = get_user_recommendations('88', bookPredictions)

topRecommendations = get_top_n(bookPredictions, n=10)

print(bookData.loc[bookData['book_id'] == 70, ['title']])
# print(userRecommendations)
# print(topRecommendations['22771'])

# topRecommendationsBooks = topRecommendations['22771'][0][0]
for item_id in userRecommendations['item_id']:
    bookTitle = bookData[bookData['book_id'] == int(item_id)]['title'].values[0]
    print(bookTitle)

# print(bookData.head())
