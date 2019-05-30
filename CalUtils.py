import csv


class CalUtils:

    def __init__(self, filename):
        self.targetfilename = filename

    def calAvgHeight(self):
        names = []
        heights = []
        self.totalStudentHeight = 0.0
        self.totalStudentCount = 0

        with open(self.targetfilename, 'r') as file:
            parsed = csv.reader(file)
            for line in parsed:
                names.append(line[0])
                heights.append(float(line[1]))
                self.totalStudentHeight += float(line[1])
                self.totalStudentCount += 1

            print('Student average height is ' + str(round(self.totalStudentHeight/self.totalStudentCount, 2)) +
                  'm for ' + str(self.totalStudentCount) + ' students.')

