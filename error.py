try:
    n = int (input ("Enter a number: "))
    a = [4, 6]
    print (a[n])

except ValueError:
    print ("Invalid Input")

except IndexError:
    print ("Invalid Index")