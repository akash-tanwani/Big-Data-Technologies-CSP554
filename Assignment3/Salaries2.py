from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (name,jobTitle,agencyID,agency,hireDate,annualSalary,grossPay) = line.split('\t')
        if 0.0<= float(annualSalary) <= 49999.99:
        	yield "Low", 1
        elif 50000 <= float(annualSalary) <= 99999.99:
        	yield "Medium", 1
        elif float(annualSalary)>=100000.00:
        	yield "High", 1

    def combiner(self, jobTitle, counts):
        yield jobTitle, sum(counts)

    def reducer(self, jobTitle, counts):
        yield jobTitle, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()


