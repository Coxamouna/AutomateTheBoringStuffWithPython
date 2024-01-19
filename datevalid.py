import leapyear

def isValidDate(day, month, year):
    # if it's February on a leap year(eg.: 2004) and the day is within
    # the valid range(1st up-to the 29th), then it's a valid date, otherwise if it's a
    # non leap year(eg.: 2001), then if the days are within their
    # valid range(1st up-to the 28th), then this is also a valid date:
    if (month == 2):
        if (day >= 1 and day <= 29):
            if (leapyear.isLeapYear(year) == True):
                return True
            else:
                return False
        if (day >= 1 and day <= 28):
            if (leapyear.isLeapYear(year) == False):
                return True
            else:
                return False
    # if the month is either April, June, September or November, 
    # then check if the days are within the valid range, 
    # (1st up-to the 30th):
    elif (month in [4, 6, 9, 11]):
        if (day >= 1 and day <= 30):
            return True
        else:
            return False
    # if the month is either January, March, May, July, August,
    # October or December, then check if the days are within the
    # valid range, (1st up-to the 31th): 
    elif (month in [1, 3, 5, 7, 8, 10, 12]):
        if (day >= 1 and day <= 31):
            return True
        else:
            return False
    else:
        return False

assert isValidDate(31, 12, 1999) == True
assert isValidDate(29, 2, 2000) == True
assert isValidDate(29, 2, 2001) == False
# assert isValidDate(2029, 13, 1) == False
# assert isValidDate(1000000, 1, 1) == True
# assert isValidDate(2015, 4, 31) == False
# assert isValidDate(1970, 5, 99) == False
# assert isValidDate(1981, 0, 3) == False
# assert isValidDate(1666, 4, 0) == False

# d = datetime.date(1, 1, 1970)
# oneDay = datetime.timedelta(days=1)
