from Day import *
"""A month consists of multiple day objects,
the month class reads from a file and creates multiple Day objects, appending them to a list. That daysList is used to create tables and collect averages. 
There is a seperate function from the class: useApplication(usersName); which helps the user utilize all the features of the application as a whole

"""
class Month(object):
  """organizes the data collected from the selected txt file, creates a daysList full of Day objects, then munipulates it to creates a table of data, an analysis of averages and GeneralStatement, allows for sorting the data and printing a specific date through the Day class

  """
  def __init__(self,cityFile):
    """sets variables
    input - cityFile
    no returns

    """
    self.sortType = 0
    self.daysList = [] #list of day objects
    
    self.getMonth(cityFile)
  
  def getMonth(self,weatherFile):
    """reads the given file but skips the first line, creates Day objects and appends them to a day list
    input - weatherFile
    no returns
    
    """
    file = open(weatherFile,"r")
    fileList = file.readlines()
    fileList=fileList[1:]
    for line in fileList:
      line=line[:-1]
      myList=line.split(",")
    
      day = Day(myList[0],myList[1],myList[2],myList[3],myList[4])
   
      self.daysList.append(day)

  def setSort(self,sortVar):
    """sorts the daysList by temp or precip depending on the users choice 
    input - sortVar
    no returns 

    """
    self.sortType = sortVar
    counter = len(self.daysList)
    swap = True
    while swap:
        swap = False 
        for j in range(counter-1):
          if self.sortType == 4:
            a = self.daysList[j].temp
            b = self.daysList[j+1].temp
          elif self.sortType == 5:
            a = self.daysList[j].precip
            b = self.daysList[j+1].precip
          if a > b:
            self.daysList[j],self.daysList[j+1] = self.daysList[j+1],self.daysList[j]
            swap = True
        counter -= 1
    
  def printMonthChart(self):
    """prints a chart using data from the daysList including: year, month, day, temp and prcp 

    """
    print("{0:<5} {1:<6} {2:<4} {3:<5} {4:<4}".format("YEAR", "MONTH", "DAY","TEMP","PRCP"))
    print ("-" * 30)
    
    for day in self.daysList:
      print ("{0:<5} {1:<6} {2:<4} {3:<5} {4:<4}".format(day.year,day.getWordMonth(), day.numDay, day.temp, day.precip))

  def printSpecificDay(self,fullDate):
    """prints a specific date 
    inputs- fullDate
    no returns, but prints and str

    """
    for day in self.daysList:
      if fullDate == day.getFullDate():
        print (day)
  
  def getAverageTemp(self):
    """adds and divides the temperatures in the daysList to come up with an average
    no inputs
    returns tempAverage

    """
    sumvar = 0
    for day in self.daysList:
      sumvar += float(day.temp)
    tempAverage = sumvar/len(self.daysList)
    return tempAverage
  
  def getAveragePrecip(self):
    """adds and divides the precipitation data in the daysList to come up with an average
    no inputs
    returns precipAverage
    
    """
    mysum = 0
    for day in self.daysList:
      mysum += float(day.precip)
    precipAverage = mysum/len(self.daysList)
    return precipAverage
  
  def getGeneralStatement(self):
    """based on the average temp, returns a statement describing the weather
    no inputs
    returns an str

    """
    if self.getAverageTemp() <= 32:
      return "The weather was cold this month."
    elif self.getAverageTemp() > 32 and self.getAverageTemp() <= 64:
      return "The weather was cool this month."
    elif self.getAverageTemp() > 64 and self.getAverageTemp() < 77:
      return "The weather was warm this month."
    elif self.getAverageTemp() >= 77:
      return "The weather was hot this month."
    
  def printAnalysis(self):
    """prints a table including the averages and the getGeneralStatement
    no inputs
    no returns, but prints getAverageTemp and getAveragePrecip and getGeneralStatement

    """
    print ("\nANALYSIS:")
    print ("-"*32)
    print("Average Temperature: {0:0.2f} F".format(self.getAverageTemp()))
    print("Average Precipitation: {0:0.2f} in".format(self.getAveragePrecip()))
    print (self.getGeneralStatement())


def useApplication(userName):
  """welcomes the user and prints the monthChart and the analysis for both cities,
  asks the user if they want to print a specific date
  asks the user if they want to sort the data by temp or prcp
  inputs - userName
  no returns, just prints str

  """
  print ("Welcome to the Weather Analysis Application " + userName + "!")
  print ("\nCITY 1:")
  city1 = Month("newOrleans.txt")
  city1.printMonthChart()
  city1.printAnalysis()
  
  print ("\nCITY 2:")
  city2 = Month("winnipeg.txt")
  city2.printMonthChart()
  city2.printAnalysis()

  yes = True
  while yes:
    yesOrNo = input("\nWould you like to print a specific date?: ").lower()
    if yesOrNo == "no":
      yes = False
    else:
      cityChoice = input("Which city would you like to choose your date from? (City1 or City2): ").lower()
      specificDay = input("Enter your specific date in the form; mm/dd/yyyy: ")
      if cityChoice == "city 1" or cityChoice == "city1":
        city1.printSpecificDay(specificDay)
      else:
        city2.printSpecificDay(specificDay)
  
  userChoice = True
  while userChoice:
    sortChoice = input("\nWould you like to sort the data?: ").lower()
    if sortChoice == "no":
      print ("Thank you for using the Weather Analysis Application! Goodbye "+ userName +"!")
      userChoice = False
    else:
      tempOrPrcp = input("Would you like to sort by temperature or precipitation?: ").lower()
      if tempOrPrcp == "precip" or tempOrPrcp == "prcp" or tempOrPrcp == "precipitation":
        city1.setSort(5)
        print ("\nCITY 1:")
        city1.printMonthChart()
        city2.setSort(5)
        print ("\nCITY 2:")
        city2.printMonthChart()
      else:
        city1.setSort(4)
        print ("\nCITY 1:")
        city1.printMonthChart()
        city2.setSort(4)
        print ("\nCITY 2:")
        city2.printMonthChart()