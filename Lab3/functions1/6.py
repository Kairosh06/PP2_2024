def reverse_sentence(input_string):

    words = input_string.split()

    reversed_words = words[::-2]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

if __name__ == "__main__":
    user_input = input()
    reversed_sentence = reverse_sentence(user_input)
    print(reversed_sentence)