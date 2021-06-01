while True:
 num = int(input())
 if num >= 0 and num < 10:
    print("{0} is one digit".format(num))
 elif num>=10 and num <=99:
    print("{0} is two digit".format(num))
 elif num >= 100 and num <= 999:
    print("{0} is three digit".format(num))
 else:
     print("{0} is four digit".format(num))
