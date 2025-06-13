country_capitals={"USA" : "Washington, D.C.","France": "Paris","Germany": "Berlin","Japan": "Tokyo","UK": "London"}
country=input("Enter the name of the country: ")

if country in country_capitals:
    print(f"The capital of {country} is {country_capitals[country]}")
else:
    print("The country cannot be found in the dictionary.")