# make a random number list.
numbers = [2, 1, 3, 4, 6, 5]

# function for sorting, maybe with three if, elif, else statemns
def sort_list(order_type):
    if order_type == "asc":
        numbers.sort()  # Sort in ascending order
        return numbers
    elif order_type == "desc":
        numbers.sort(reverse=True)  # Sort in descending order
        return numbers
    else:   # for "none" return
        return numbers
    
# User input

sort_input = input("Enter sorting order(asc, desc, none): ").strip().lower()

# Sort and print the list

sorted_list = sort_list(sort_input)
print("Sorted List: ", sorted_list)
   
  

