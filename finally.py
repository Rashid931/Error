def listIndex ():
    '''
        Takes index input as int, returns corresponding value from list...
    '''
    
    l = [11,22,33,44,55,66,77,88,99]
    try:
        i = int (input ("Enter an Index: "))
        return print (f"{l [i]}")
    
    except:
        return print (f"Invalid Index {i}")
    
    finally:
        print ("Allah Hafiz")

print (listIndex.__doc__)
listIndex ()
