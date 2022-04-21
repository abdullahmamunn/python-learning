# -----------Calendar Functions in Python | Set 2(monthrange(), prcal(), weekday()…)------------
import calendar
# 1. monthrange(year, month) :-
# This function returns two integers, first, the starting day number of week(0 as monday) ,
# second, the number of days in the month.
print(calendar.monthrange(2022,2))

# 2. prcal(year, w, l, c) :- This function also prints the calendar of specific year but there is no need of “print” operation to
# execute this.
calendar.prcal(2022,2,1,6)

# 3. prmonth(year, month, w, l) :- This function also prints the month of specific year but there is no need of “print” operation
# to execute this.
calendar.prmonth(2022,4,2,1)

# 4. setfirstweekday(num) :- This function sets the day start number of week.

# print(calendar.day_name.weekday(2022,4,21))
# print(calendar.day_name(calendar.weekday(2022,4,21)))
print((calendar.day_name[0]).upper())
print((calendar.day_name[1]).upper())
print((calendar.day_name[2]).upper())
print((calendar.day_name[3]).upper())
print((calendar.day_name[4]).upper())
print((calendar.day_name[5]).upper())
print((calendar.day_name[6]).upper())
