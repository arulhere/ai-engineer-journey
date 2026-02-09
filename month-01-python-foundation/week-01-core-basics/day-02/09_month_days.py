month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid month")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
