def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
numbers_list = [23, 45, 17, 11, 8, 29, 6, 31, 2, 4, 5]
prime_numbers = filter_prime(numbers_list)
print("Prime numbers in the list:", prime_numbers)