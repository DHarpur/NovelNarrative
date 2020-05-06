from lightfm import LightFM
from lightfm.data import Dataset
import joblib
from database import database


def connectToDatabase():
    connection = database.DatabaseManager()
    return connection


def initialiseBookModel():
    print("Loading in data from database...")
    connection = connectToDatabase()
    bookRatingsDF = connection.get_book_ratings()
    booksDF = connection.get_all_books()
    bookFeaturesDF = connection.get_book_features(booksDF)
    print("All data loaded from database!")

    print("Prep datasets...")
    bookDataSet = Dataset()
    print("Datasets prepped...")

    print("Fit user and item interactions to datasets...")
    bookDataSet.fit(users=bookRatingsDF['user_id'].unique(), items=bookRatingsDF['book_id'].unique(),
                    item_features=bookFeaturesDF['tag_name'].values.flatten())
    print("Datasets user and item interactions fitted...")

    print("Build user and item interactions in datasets...")
    (bookInteractions, bookWeights) = bookDataSet.build_interactions(
        ((x['user_id'], x['book_id']) for _, x in bookRatingsDF.iterrows()))
    print("Datasets user and item interactions built...")

    print("Build item features to datasets...")
    bookFeatures = bookDataSet.build_item_features(
        (x, [y]) for x, y in zip(bookFeaturesDF['book_id'], bookFeaturesDF['tag_name']))
    print("Datasets item features built...")

    print("Fit book model...")
    bookModel = LightFM(loss='warp')
    bookModel.fit(bookInteractions, item_features=bookFeatures)
    print("Book model fitting complete!")

    print("Begin dumping model to file")
    joblib.dump(bookModel, "./RecommenderDump/BookModel")
    joblib.dump(bookFeatures, "./RecommenderDump/BookFeatures")
    print("Model saved to file!")


def initialiseMovieModel():
    print("Loading in data from database...")
    connection = connectToDatabase()
    movieRatingsDF = connection.get_movie_ratings()
    # movieFeaturesDF = connection.get_movie_tags()
    print("All data loaded from database!")

    print("Prep datasets...")
    movieDataSet = Dataset()
    print("Datasets prepped...")

    print("Fit user and item interactions to dataset...")
    movieDataSet.fit(users=movieRatingsDF['userid'].unique(), items=movieRatingsDF['movieid'].unique())
    print("Dataset user and item interactions fitted...")

    print("Build user and item interactions in dataset...")
    (movieInteractions, movieWeights) = movieDataSet.build_interactions(
        ((x['userid'], x['movieid']) for _, x in movieRatingsDF.iterrows()))
    print("Dataset user and item interactions built...")

    '''
    print("Build item features to dataset...")
    movieFeatures = movieDataSet.build_item_features(
        (x, [y]) for x, y in zip(movieFeaturesDF['movieid'], movieFeaturesDF['tag']))
    print("Dataset item features built...")
    '''
    print("Fit movie model...")
    movieModel = LightFM(loss='warp')
    movieModel.fit(movieInteractions)
    print("Movie model fitting complete!")

    print("Begin dumping model to file")
    joblib.dump(movieModel, "./RecommenderDump/MovieModel")
    # joblib.dump(movieFeatures, "./RecommenderDump/MovieFeatures")
    print("Models saved to file!")


def main():
    initialiseBookModel()
#     initialiseMovieModel()


# main()
