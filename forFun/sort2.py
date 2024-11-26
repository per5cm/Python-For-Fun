# make a random number list.
numbers = [2, 1, 3, 4, 6, 5]
#sort_label = ["acs: ", "desc: ", "none: "]

def sort_numbers(sorted_versions):
    if sorted_versions == "acs":
        return sorted(numbers)
    elif sorted_versions == "desc":
        return sorted(numbers, reverse=True)
    elif sorted_versions == "none":
        return numbers
    else:
        return "Invalid Input. Use: 'acs', 'desc', 'none'"
    
print(sort_numbers("acs"))
print(sort_numbers("desc"))
print(sort_numbers("none"))

