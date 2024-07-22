s = int (input ("Enter your salary: "))

if not (2000 < s < 5000):
    raise ValueError ("Salary should be between 2000 & 5000")

else:
    print (f"Salary is {s}")
    