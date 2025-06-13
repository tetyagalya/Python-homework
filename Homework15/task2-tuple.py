#Task 2) Create a tuple called "foods" and "calories", and populate them respectfully in order
foods=("Apple", "Banana", "Orange", "Mango", "Strawberry","Grape", "Mandarin", "Strawberry")
calories=("52kcal", "96 kcal", "62 kcal","605 kcal","33 kcal","68 kcal", "50 kcal","33 kcal")

#Convert the previously defined tuples to lists, Print out the 5th element (strawberry), out of the list, with its caloric value. Print out the second last food, and its caloric value
foods=["Apple", "Banana", "Orange", "Mango", "Strawberry","Grape", "Mandarin", "Strawberry"]
calories=["52kcal", "96 kcal", "62 kcal","605 kcal","33 kcal","68 kcal", "50 kcal","33 kcal"]
print(f"{foods[4]} has {calories[4]}")
print(f"{foods[-2]} has {calories[-2]}")

#Print out all the unique foods in the list (set)
foods={"Apple", "Banana", "Orange", "Mango", "Strawberry","Grape", "Mandarin", "Strawberry"}
print(foods)

#Create a dictionary with their unique key, values from the table listed. 
foods={"Apple" : "52 kcal", "Banana" : "96 kcal", "Orange" : "62 kcal", "Mango" : "605 kcal", "Strawberry" : "33 kcal","Grape" : "68 kcal", "Mandarin" : "50 kcal", "Strawberry" : "33 kcal"}
print(foods)
print(foods["Apple"])