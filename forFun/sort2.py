# more compact version

def main():
    numbers = [2, 1, 3, 4, 6, 5]
    
    print(sort_numbers(numbers, "acs"))
    print(sort_numbers(numbers, "desc"))
    print(sort_numbers(numbers, "none"))


def sort_numbers(numbers, sorted_versions):
    if sorted_versions == "acs":
        return sorted(numbers)
    elif sorted_versions == "desc":
        return sorted(numbers, reverse=True)
    elif sorted_versions == "none":
        return numbers
    

if __name__ == "__main__":
    main()
