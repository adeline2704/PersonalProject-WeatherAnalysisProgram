"""Each day is an object, this module breaks down the data from each day
Eg. month, day, year, temp, precip
- creates a full day
- converts the month into words
- displays the info neatly

"""
class Day(object):
  """organizes the data collected from a day from the selected txt file

  """
  def __init__(self,month,numDay,year,temp,precip):
    """sets variables
    inputs:
    - month
    - numDay
    - year
    - temp
    - precip
    no returns

    """
    self.month = month
    self.numDay = numDay
    self.year = year
    self.temp = temp
    self.precip = precip
  
  def getFullDate(self):
    """returns the fulldate by adding together the month, day and year
    no inputs
    return-str

    """
    return (self.month+"/"+self.numDay+"/"+self.year)
  
  def getWordMonth(self):
    """converts the month from number to word by matching up the number with the index of a wordMonth list
    no inputs
    returns-str(wordMonth[correctIndex])

    """
    wordMonth = ["JAN","FEBR","MARCH","APRIL", "MAY", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC"]
    if self.month == "01" or self.month == "02" or self.month == "03" or self.month == "04" or self.month == "05" or self.month == "06" or self.month == "07" or self.month == "08" or self.month == "09":
      monthNum = self.month[1:]
      return wordMonth[int(monthNum)-1]
    else:
      return wordMonth[int(monthNum)-1]
  
  def __str__(self):
    """returns the data of a singular date
    no input
    return - str
    
    """
    return "\nDate: {0:1}\nTemperature: {1:1} F \nPrecipitation: {2:1} in".format(self.getFullDate(), self.temp,self.precip)