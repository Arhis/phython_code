import sys
import os
import time

if sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')

strength = []
health = []
wisdom = []
dexterity = []

the_pool = ["быстрый", "задумчивый", "осмотрительный", "восприимчивый", "накаченный", "бодрый", "находчевый",
            "безустанный",
            "мыслящий", "улыбающийся", "непривзойдённый", "решительный", "воспреимчевый", "милосердный",
            "красивый", "усидчевый", "шустрый", "здоровый", "бегующий", "прыгающий", "читающий", "уставший",
            "слушащий", "внимающий", "разговорчевый", "сдержанный", "неустанный", "работающий", "поющий", "рискующий"]
choice = None
print()
print("<<<<< Добро пожаловать в генератор персонажей >>>>>>\n")
print("У нас есть четыре характеристики: Сила, Здоровье, Мудрость и Ловкость")
print("Ваша задача распределить всё по спискам")

while choice != "exit":
    print(
        """
        ***********
        Меню:
        ***********
        add - Добавить элемент к категории
        delete - Удалить элемент, вернув его в общий список
        show - Вывести что где на экран
        exit - Выход

        """
    )
    choice = input("Ваш выбор: ")
    # --------------------------------------------------------------------------
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    if choice == "add":
        element = input("Введите какое свойство вы хотите присвоить: ")
        element = element.lower()
        if element in the_pool:
            print("""\n
            Выберите куда вы хотите переместить элемент:
            1) Сила
            2) Здоровье
            3) Мудрость
            4) Ловкость
            """)
            address_to_move = input("Ваш выбор(1-4): ")
            if address_to_move == "1":
                strength.append(element)
                the_pool.remove(element)
                time.sleep(1)
                print("Элемент успешно добавлен в категорию.")
            elif address_to_move == "2":
                health.append(element)
                the_pool.remove(element)
                time.sleep(1)
                print("Элемент успешно добавлен в категорию.")
            elif address_to_move == "3":
                wisdom.append(element)
                the_pool.remove(element)
                time.sleep(1)
                print("Элемент успешно добавлен в категорию.")
            elif address_to_move == "4":
                dexterity.append(element)
                the_pool.remove(element)
                time.sleep(1)
                print("Элемент успешно добавлен в категорию.")
            else:
                print("Не верный выбор категории")
        else:
            print("Элемента нету в списке")
    # --------------------------------------------------------------------------
    elif choice == "delete":
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        print("""\n
            Выберите от куда вы хотите удалить элемент:
            1) Сила
            2) Здоровье
            3) Мудрость
            4) Ловкость
            """)
        category_to_delete_with = input("Категория №: ")
        element = input("Введите свойство которое вы хотите удалить с категории: ")
        element = element.lower()
        if category_to_delete_with == "1":
            if element in strength:
                strength.remove(element)
                the_pool.append(element)
                print("Свойство успешно удалено")
            else:
                print("Ошибка! Свойства нету в списке")
        elif category_to_delete_with == "2":
            if element in health:
                health.remove(element)
                the_pool.append(element)
                print("Свойство успешно удалено")
            else:
                print("Ошибка! Свойства нету в списке")
        elif category_to_delete_with == "3":
            if element in wisdom:
                wisdom.remove(element)
                the_pool.append(element)
                print("Свойство успешно удалено")
            else:
                print("Ошибка! Свойства нету в списке")
        elif category_to_delete_with == "4":
            if element in wisdom:
                dexterity.remove(element)
                the_pool.append(element)
                print("Свойство успешно удалено")
            else:
                print("Ошибка! Свойства нету в списке")
        else:
            print("Категория задана неверно")
    # --------------------------------------------------------------------------
    elif choice == "show":
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

        print(
            """
            -------
            Сила:
            -------
            """)
        if strength:
            for i in range(len(strength)):
                print(i + 1, ")", strength[i])
        else:
            print("Список пуст")

        print(
            """
            -------
            Здоровье:
            -------
            """)
        if health:
            for i in range(len(health)):
                print(i + 1, ")", health[i])
        else:
            print("Список пуст")

        print(
            """
            -------
            Мудрость:
            -------
            """)
        if wisdom:
            for i in range(len(wisdom)):
                print(i + 1, ")", wisdom[i])
        else:
            print("Список пуст")

        print(
            """
            -------
            Ловкость:
            -------
            """)
        if dexterity:
            for i in range(len(dexterity)):
                print(i + 1, ")", dexterity[i])
        else:
            print("Список пуст")

        input("Нажмите Enter чтобы показать больше")
        print(
            """
            -------
            Список доступных свойств:
            -------
            """)
        if the_pool:
            for i in range(len(the_pool)):
                print(i + 1, ")", the_pool[i])
                if i == 10 or i == 20:
                    input("Нажмите Enter чтобы показать больше")
        else:
            print("Список пуст")
    elif choice == "exit":
        print("Спасибо что вы были с нами, до свиданья")
        time.sleep(2)

    else:
        print("Нету такого меню в списке! попробуйте еще раз")
