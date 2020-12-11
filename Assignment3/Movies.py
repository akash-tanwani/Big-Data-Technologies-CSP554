from mrjob.job import MRJob

class MRMovies(MRJob):

    def mapper(self, _, line):
        (userId,movieId,rating,timeStamp) = line.split(',')
        yield userId, 1

    def combiner(self, userId, counts):
        yield userId, sum(counts)

    def reducer(self, userId, counts):
        yield userId, sum(counts)


if __name__ == '__main__':
    MRMovies.run()
