from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)

    for perm in perms:
        print(''.join(perm))

if __name__ == "__main__":
    user_input = input(str())
    print()
    print_permutations(user_input)