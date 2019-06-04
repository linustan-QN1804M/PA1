class CalUtils:

    def __init__(self, listOfStudentHeight):
        self.targetfilename = listOfStudentHeight

    def calAvgHeight(self):
        names = []
        heights = []
        self.totalStudentHeight = 0.0
        self.totalStudentCount = 0

        with open(self.targetfilename, 'r') as file:
            for line in file:
                splitline = line.split("\t")
                names.append(splitline[0])
                heights.append(float(splitline[1]))
                self.totalStudentHeight += float(splitline[1])
                self.totalStudentCount += 1

            print('Student average height is ' + str(round(self.totalStudentHeight/self.totalStudentCount, 2)) +
                  'm for ' + str(self.totalStudentCount) + ' students.')

