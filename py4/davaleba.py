print("1) სიტყვის ჩანაცვლება წინადადებაში")
sentence = input("შეიყვანე წინადადება: ")
first_word = input("შეიყვანე პირველი სიტყვა: ")
second_word = input("შეიყვანე მეორე სიტყვა: ")

new_sentence = sentence.replace(first_word, second_word)
print("შედეგი:", new_sentence)


print("\n2) ყველაზე გრძელი სიტყვის პოვნა")
sentence2 = input("შეიყვანე წინადადება: ")
words = sentence2.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("ყველაზე გრძელი სიტყვაა:", longest_word)


print("\n3) ანაგრამის შემოწმება")
word1 = input("შეიყვანე პირველი სიტყვა: ")
word2 = input("შეიყვანე მეორე სიტყვა: ")

word1 = word1.lower()
word2 = word2.lower()

if len(word1) != len(word2):
    print("ეს სიტყვები არ არის ანაგრამა")
else:
    letters1 = []
    letters2 = []

    for letter in word1:
        letters1.append(letter)

    for letter in word2:
        letters2.append(letter)

    i = 0
    while i < len(letters1):
        j = i + 1
        while j < len(letters1):
            if letters1[i] > letters1[j]:
                temp = letters1[i]
                letters1[i] = letters1[j]
                letters1[j] = temp
            j = j + 1
        i = i + 1

    i = 0
    while i < len(letters2):
        j = i + 1
        while j < len(letters2):
            if letters2[i] > letters2[j]:
                temp = letters2[i]
                letters2[i] = letters2[j]
                letters2[j] = temp
            j = j + 1
        i = i + 1

    sorted_word1 = ""
    sorted_word2 = ""

    for letter in letters1:
        sorted_word1 = sorted_word1 + letter

    for letter in letters2:
        sorted_word2 = sorted_word2 + letter

    if sorted_word1 == sorted_word2:
        print("ეს სიტყვები ანაგრამაა")
    else:
        print("ეს სიტყვები არ არის ანაგრამა")
