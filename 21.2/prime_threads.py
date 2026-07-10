from concurrent.futures import ThreadPoolExecutor


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def check_numbers(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))

    return dict(zip(numbers, results))


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

answers = check_numbers(num_list)
print(answers)
