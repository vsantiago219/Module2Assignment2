#Is it a Leap Year?
year = int(input("What is the year? \n"))

if year %4 == 0:
    print(f"The year {year} is a Leap Year.") 
elif year %400 == 0:
    print(f"The year {year} is a Leap Year.")
else:
    print(f"The year {year} is not a Leap Year.")