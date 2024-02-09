def histogram(numbers):
    numbers_list = [int(num) for num in numbers.split()]
    for num in numbers_list:
        print('*' * num)

if __name__ == "__main__":
    input_numbers = input("Enter a list of integers separated by spaces: ")
    histogram(input_numbers)