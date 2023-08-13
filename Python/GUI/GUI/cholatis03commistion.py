Month = input("Enter your month: ")
Day = input("Enter your day: ")
Year = input("Enter your year: ")
def leap_year(year):
    return ((year % 400 == 0) or ((year % 100 !=0) and (year % 4 ==0)))
def last_day(month, year):
    months_31_days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    if month == 'February':
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in months_31_days:
        return 31
    else:
        return 30
def nextDate(month, day, year):
    if day == 31 and month == "December":
        month = 'January'
        day = 1
        year = year + 1
    elif day == last_day(month, year):
        if month == "December":
            month = 'January'
            year = year + 1
        else:
            month_index = ["January","February","March","April","May","June","July","August","September","October","November","December"].index(month)
            month = ["January","February","March","April","May","June","July","August","September","October","November","December"][month_index + 1]
        day = 1     
    elif day >= 1 and day < last_day(month, year):
        day = day + 1
    return [str(month), int(day), int(year)]
def display():
    try:
        month = str(Month)
        day = int(Day)
        year = int(Year)
        if month.isdigit():
            print("Error!", "Invalid input. Ensure month as name month")
        elif month not in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
            print("Error!", "ใส่เดือนผิด")
        elif (day < 1 or day > 31):
            print("Error!", "Invalid input. Ensure day between 1-31")
        elif (year < 1812 or year > 2012):
            print("Error!", "Invalid input. Ensure year for 1812-2012")
        else:
            date = nextDate(month, day, year)
            print(date)
    except ValueError:
       print("Error!", "Please enter the month as a string, the date as an integer and the year from 1812-2012.")
display()
exit()