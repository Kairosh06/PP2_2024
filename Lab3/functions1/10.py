def unique_elements(original_list):
    unique_list = []
    for element in original_list:
        if element not in unique_list:
            unique_list.append(element)
    
    return unique_list

# Test the function
original_list = [1, 2, 3, 4, 3, 2, 1, 5]
print("Original list:", original_list)
print("List with unique elements:", unique_elements(original_list))