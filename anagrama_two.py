import random

print("<<<<< Отгадай имя >>>>>")
WORDS = ("Виктор", "Владислав", "Владимир", "Вячеслав")
your_input = input("Отгадайте мужское имя которое начинается на букву В: ")
choice = random.choice(WORDS)
mistakes_count = 1

while your_input != choice:
    mistakes_count += 1
    print("Не Верно! Вот вам подсказка: ", end=" ")
    print(choice[:mistakes_count], "*"*(len(choice)-mistakes_count))

    your_input = input("Попробуйте еще раз: ")

print("Верно! Слово было: ", choice)


