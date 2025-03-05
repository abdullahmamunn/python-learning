while True:
    num = int(input())
    if num > 0:
        print("{0} is positive".format(num))
        if num >= 10 and num <=99:
            print("{0} is two digit positive number".format(num))
    else:
        print("{0} is negative".format(num))
        if num >= -99 and num <= -10:
            print("{0} is two digit negatve number".format(num))