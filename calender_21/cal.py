# Example #1: Display the Calendar of a given month.
import calendar
month = 4
year = 2022
print(calendar.month(year,month))

# Example #2: Display calendar of the given year.
year = int(input('Enter a year to see the calender: '))
print(calendar.calendar(year,2,1,6))

#using firstweekday() to print starting day number
print ("The starting day number in calendar is : ",end="")
print (calendar.firstweekday())

# 3. isleap (year):- This function checks if the year mentioned in the argument is a leap or not.
if calendar.isleap(year):
    print("{0} Year is leap year".format(year))
else:
    print("Not Leap Year")

4. #using leapdays() to print leap days between years
y1, y2 = input('Enter year range to check hpw much leap year between: ').split()
# print(type(y1))
# print ("The leap days between {0} and {0} are : ".format(y1,y2))
print (calendar.leapdays(int(y1), int(y2)))

# 5. month (year, month, w, l) :- This function prints the month of a specific year mentioned in arguments.
# It takes 4 arguments, year, month, width of characters and no. of lines taken by a week.
print(calendar.month(2022,4))


