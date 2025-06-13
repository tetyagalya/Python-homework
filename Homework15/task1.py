#Ask for the user to input number of years and print out how many days, weeks, and hours are present in the number of years provided.

year=int(input("Enter number of years: "))

print(year*365, "days")
print(year*52, "weeks")
print(year*365*24, "hours")