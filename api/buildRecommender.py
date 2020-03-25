from surprise import SVD, Dataset, Reader, dump
from mySVDAlgo import mySVDAlgo
import surprise

reader1 = Reader(line_format='user item rating', sep=',', skip_lines=1)
bookRatingsData = Dataset.load_from_file('./data/book/ratings.csv', reader1)

reader2 = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
movieRatingsData = Dataset.load_from_file('./data/movie/ratings.csv', reader2)

bookTrain, bookTest = surprise.model_selection.train_test_split(bookRatingsData, test_size=0.25)
movieTrain, movieTest = surprise.model_selection.train_test_split(movieRatingsData, test_size=0.25)

sim_options = {'name': 'pearson_baseline', 'user_based': False}
algorithm1 = mySVDAlgo()
algorithm2 = mySVDAlgo()

kSplit = surprise.model_selection.split.KFold(n_splits=10, shuffle=True)

print("Book Algorithm Training beginning...")
algorithm1.fit(bookTrain)
print("Book Algorithm Training complete!")
print("Book Algorithm Testing beginning...")
predictionsBook = algorithm1.test(bookTest)
print("Book Algorithm Testing complete!")
dump.dump("./RecommenderDump/algorithm1_dump", predictions=predictionsBook, algo=algorithm1)
print("Book Algorithm and results sent to dump file")

print("Movie Algorithm Training beginning...")
algorithm2.fit(movieTrain)
print("Movie Algorithm Training complete!")
print("Movie Algorithm Testing beginning...")
predictionsMovie = algorithm2.test(movieTest)
print("Movie Algorithm Testing complete!")
dump.dump("./RecommenderDump/algorithm2_dump", predictions=predictionsMovie, algo=algorithm2)
print("Movie Algorithm and results sent to dump file")
