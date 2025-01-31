
s_breeds = ['Chihuahua', 'Pomeranian', 'Pug', 'Yorkshire Terrier', 'Jack Russell Terrier']
m_breeds = ['Beagle', 'Border Collie', 'Shetland Sheepdog', 'English Bulldog', 'Australian Shepherd']
l_breeds = ['Labrador Retriever', 'German Shepherd', 'Dalmatian', 'Husky', 'Boxer']
el_breeds = ['Saint Bernard', 'Newfoundland', 'Irish Wolfhound', 'Central Asian Shepherd (Alabai)', 'Mastiff']

while True:
    # выбор группы пород
    while True:
        a = input("Choose a breed group - \n S for small breeds \n M for medium breeds \n L for large breeds \n EL for extra large breeds \n Your choice: ").strip().upper()
        if a == "S":
            print("Small breeds:", s_breeds)
            selected_breeds = s_breeds
            break
        elif a == "M":
            print("Medium breeds:", m_breeds)
            selected_breeds = m_breeds
            break
        elif a == "L":
            print("Large breeds:", l_breeds)
            selected_breeds = l_breeds
            break
        elif a == "EL":
            print("Extra large breeds:", el_breeds)
            selected_breeds = el_breeds
            break
        else:
            print("Invalid choice. Please select S, M, L, or EL.")

    # выполнение упражнений
    while True:
        print("\nChoose an exercise from 1 to 10:")
        choice = int(input("Number: "))

        breeds_str = ', '.join(selected_breeds)

        if choice == 1:
            print("\n1. Все породы в одной строке:")
            print(breeds_str)
        elif choice == 2:
            print(f"\n2. Общее количество пород в выбранной группе ({a}): {len(selected_breeds)}")
        elif choice == 3:
            first_breed = selected_breeds[0]
            print(f"\n3. Начинается ли список с породы '{first_breed}'?")
            if breeds_str.startswith(first_breed):
                print("Да, начинается.")
            else:
                print(f"Нет, начинается с '{breeds_str.split(', ')[0]}'.")
        elif choice == 4:
            print("\n4. Есть ли порода 'Bulldog' в строке?")
            if 'Bulldog' in selected_breeds:
                print("Bulldog найден.")
            else:
                print("Bulldog не найден.")
        elif choice == 5:
            updated_breeds_str = breeds_str.replace("Pug", "French Bulldog")
            print("\n5. Замена 'Pug' на 'French Bulldog':")
            print(updated_breeds_str)
        elif choice == 6:
            breeds_list = breeds_str.split(', ')
            print("\n6. Список пород после разбиения строки:")
            print(breeds_list)
        elif choice == 7:
            upper_breeds = [breed.upper() for breed in selected_breeds]
            print("\n7. Все породы в верхнем регистре:")
            print(upper_breeds)
        elif choice == 8:
            terr_count = breeds_str.count('Terrier')
            print("\n8. Количество пород с подстрокой 'Terrier':")
            print(terr_count)
        elif choice == 9:
            centered_breed = selected_breeds[0].center(20, '-')
            print("\n9. Отцентрованное название породы:")
            print(centered_breed)
        elif choice == 10:
            alpha_check = all(breed.replace(' ', '').isalpha() for breed in selected_breeds)
            print("\n10. Все ли названия пород содержат только буквы?")
            print(alpha_check)
        else:
            print("Некорректный выбор упражнения.")

        # Предложение продолжить работу
        cont = input("\nХотите продолжить работу с программой? (y/n): ").strip().lower()
        if cont == 'n':
            again = input("Вернуться к выбору группы? (y/n): ").strip().lower()
            if again == 'y':
                break  # возвращаемся к выбору группы
            else:
                exit()  # завершаем работу программы

      





