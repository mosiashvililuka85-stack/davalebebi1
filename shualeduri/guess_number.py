import random


def print_welcome_message():
    # თამაშის საწყისი ინფორმაცია.
    print("გამოიცანით რიცხვი")
    print("პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან.")
    print("არასწორი პასუხის შემთხვევაში მიიღებთ მინიშნებას: უფრო მაღალი ან უფრო დაბალი.")
    print()


def read_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("გთხოვთ შეიყვანოთ მხოლოდ მთელი რიცხვი.")


def read_number_range():
    while True:
        minimum_number = read_integer("შეიყვანეთ მინიმალური რიცხვი: ")
        maximum_number = read_integer("შეიყვანეთ მაქსიმალური რიცხვი: ")

        if minimum_number < maximum_number:
            return minimum_number, maximum_number

        print("მინიმალური რიცხვი უნდა იყოს მაქსიმალურზე ნაკლები.")


def build_result_message(secret_number, attempts_count):
    return (
        f"გილოცავთ! თქვენ გამოიცანით რიცხვი {secret_number}. "
        f"მცდელობების რაოდენობა: {attempts_count}"
    )


def print_all_guesses(user_guesses):
    print()
    print("თქვენი მცდელობები:")

    for index in range(len(user_guesses)):
        print(f"{index + 1}. {user_guesses[index]}")


def play_game():
    print_welcome_message()

    minimum_number, maximum_number = read_number_range()
    secret_number = random.randint(minimum_number, maximum_number)
    attempts_count = 0
    is_guessed = False

    user_guesses = []

    hints = ["უფრო მაღალი!", "უფრო დაბალი!"]

    while not is_guessed:
        user_guess = read_integer("შეიყვანეთ თქვენი ვარაუდი: ")
        attempts_count += 1
        user_guesses.append(user_guess)

        if user_guess < minimum_number or user_guess > maximum_number:
            print("თქვენი რიცხვი მითითებული დიაპაზონის გარეთაა.")
        elif user_guess < secret_number:
            print(hints[0])
        elif user_guess > secret_number:
            print(hints[1])
        else:
            is_guessed = True
            result_message = build_result_message(secret_number, attempts_count)
            print(result_message)

    print_all_guesses(user_guesses)


play_game()
