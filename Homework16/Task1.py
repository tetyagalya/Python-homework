#Task1) Write a Python function called merge_lists that takes two lists as input and returns a new list that contains all the elements from both input lists in the same order.

a=["cleanser", "toner", "creme", "sunscreen"]
b=["foundation", "blush","lip gloss","mascara"]

def merge_lists(a, b):
    return a+b
print (merge_lists(a,b))