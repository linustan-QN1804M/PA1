from CalUtils import CalUtils
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

datafile = CalUtils(filename)
datafile.calAvgHeight()

Name = input("Name: ")
Height = 0.0

flag = True
while flag:
    try:
        Height = float(input("Height: "))
        flag = False
    except ValueError:
        print("You need to type in a number")

NewTotalHeight = datafile.totalStudentHeight + Height
NewTotalStudents = datafile.totalStudentCount + 1

print('Student average height is ' + str(round(NewTotalHeight/NewTotalStudents, 2)) +
      'm for ' + str(NewTotalStudents) + ' students.')