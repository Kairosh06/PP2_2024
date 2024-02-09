def spy_game(nums):

    zeros = 0
    ones = 0
    sevens = 0
    
    for num in nums:
        if num == 0:
            if ones == 1:
                zeros += 1
            elif zeros < 2:
                zeros += 1
        elif num == 7:
            if zeros == 2:
                sevens += 1
    
    return zeros == 2 and sevens == 1

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False