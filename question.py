class questionItem:
    def __init__(self, value, axes):
        self.value = value
        self.axes = axes

    def print(self):
        print("value", self.value)
        print("axes", self.axes)
        return 

def main():
  listOfQuestions = [questionItem(3, "Y"), questionItem(1, "Y"),questionItem(.25, "X"), questionItem(.5, "X"), questionItem(.75, "X"), questionItem(1, "X"), questionItem(1, "X"), questionItem(.75, "Y")] 
  for i in range(0, len(listOfQuestions)):
    #listOfQuestions[i].print()
    print("\n")
  output = processResults(listOfQuestions)
  print("output: ", output)
  string = assignGrade()
  print("Segmentation Letter Grade:", string)
  return

lettergrade = ""
outputList = [0,0]
def processResults(listOfQuestions):
    sumX = 0
    sumY = 0
    countX = 0
    countY = 0
    for i in range(0, len(listOfQuestions)):
        if(listOfQuestions[i].axes =="X"):
            sumX = sumX + listOfQuestions[i].value
            countX = countX + 1
        elif(listOfQuestions[i].axes =="Y"):
            sumY = sumY + listOfQuestions[i].value
            countY = countY + 1
    outputList[0] = sumX / countX
    outputList[1] = sumY / countY
    return outputList

def assignGrade():
    xypoint = [0,0]
    if outputList[0] >= .75:
        xypoint[0] = 1
    elif outputList [0] < .75 and outputList[0] >= .5:
        xypoint[0] = 2
    elif outputList[0] <.5:
        xypoint[0] = 3
    if outputList[1] == 1/6:
        xypoint[1] = -1
    elif outputList[1] > 1/6 and outputList[1] <= 1/3:
        xypoint[1] = -2
    elif outputList[1] > 1/3 and outputList[1] <= .5:
        xypoint[1] = -3
    elif outputList[1] > .5 and outputList[1] <= 2/3:
        xypoint[1] = -4
    elif outputList[1] > 1.25 and outputList[1] <= 4/3:
        xypoint[1] = -5
    elif outputList[1] > 4/3 and outputList[1] <= 1.5:
        xypoint[1] = -6
    else:
        xypoint[1] = -7
    # assigning xy to letters
    print('coordinates: ' , xypoint)
    if xypoint[0] == 1 and xypoint [1] ==-1 or xypoint[0] == 1 and xypoint[1] == -2 or xypoint[0]==2 and xypoint[1] == -1 or xypoint[0] == 2 and xypoint[1] == -2:
        lettergrade = "A"
    elif xypoint[0] == 3 and xypoint[1] == -1:
        lettergrade = "B"
    elif xypoint[0] == 3 and xypoint[1] == -2:
        lettergrade = "C"
    elif xypoint[0] == 1 and xypoint[1] == -3 or xypoint[0] == 1 and xypoint[1] == -4:
        lettergrade = "D"
    elif xypoint[0] == 2 and xypoint[1] == -3:
        lettergrade = "D"
    elif xypoint[0] == 3 and xypoint[1] == -3 or xypoint[0] == 3 and xypoint[1] == -4:
        lettergrade = "E"
    elif xypoint[0] == 2 and xypoint[1] == -4:
        lettergrade = "E"
    elif xypoint[0] ==1 and xypoint[1] == -5 or xypoint[0] == 1 and xypoint[1]== -6:
        lettergrade = "F"
    elif xypoint[0] == 1 and xypoint[1] == -7:
        lettergrade = "G"
    else:
        lettergrade = "H"
    return lettergrade

main()