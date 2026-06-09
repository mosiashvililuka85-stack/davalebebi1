def sum_user_numbers(count=5):
    total = 0

    for i in range(count):
        number = int(input(f"Enter number {i + 1}: "))
        total = total + number

    return total


def split_even_odd(*numbers):
    odd_numbers = []
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return odd_numbers, even_numbers


def count_words(sentence):
    words_count = {}

    sentence = sentence.lower()
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("?", "")

    words = sentence.split()

    for word in words:
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1

    return words_count


# Examples
print(sum_user_numbers())
print(split_even_odd(1, 2, 3, 4, 5, 6, 7, 8))
print(count_words("This is a test. This test is fun."))
