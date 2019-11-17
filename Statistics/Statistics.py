from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import  mode
from CSVReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        pass

    def mean(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = mean(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

    def median(self, val1, val2, val3, val4, val5, val6, val7, val8, val9):
        self.result = median(val1, val2, val3, val4, val5, val6, val7, val8, val9)
        return self.result

    def mode(self, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10):
        self.result = mode(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
        return self.result

