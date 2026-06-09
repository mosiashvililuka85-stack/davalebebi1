def count_uppercase_and_convert(text):
    uppercase_count = 0

    for char in text:
        if char.isupper():
            uppercase_count = uppercase_count + 1

    uppercase_text = text.upper()
    return uppercase_count, uppercase_text


def camel_to_snake(name):
    snake_case = ""

    for char in name:
        if char.isupper():
            snake_case = snake_case + "_"
            snake_case = snake_case + char.lower()
        else:
            snake_case = snake_case + char

    return snake_case


if __name__ == "__main__":
    sample_text = "Hello woRld"
    result = count_uppercase_and_convert(sample_text)

    print("Number of uppercase letters:", result[0])
    print("Uppercase text:", result[1])

    print(camel_to_snake("firstName"))
    print(camel_to_snake("name"))
    print(camel_to_snake("preferredFirstName"))
    print(camel_to_snake("lastName"))
