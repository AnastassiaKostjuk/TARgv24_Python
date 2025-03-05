from Riigid import *

# Загрузка данных из файла
riik_pealinn, pealinn_riik, riigid, pealinnad = failist_to_dict('EuroopaRiigid/riigid_pealinnad.txt')
riigid = list(riik_pealinn.keys())


while True:
    print("\n1. Показать страну по столице")
    print("2. Показать столицу по стране")
    print("3. Добавить новую страну и столицу")
    print("4. Удалить страну и столицу")
    print("5. Отсортировать страны и столицы")
    print("6. Экспортировать данные в файл")
    print("7. Начать тест")
    print("8. Выход")
    choice = input("Выберите действие: ")
        
    if choice == '1':
        kuvada_pealinna_riik() # Вызов функции из модуля Riigid
    elif choice == '2':
        kuvada_riigi_pealinn()  # Вызов функции из модуля Riigid
    elif choice == '3':
        lisamine("EuroopaRiigid/riigid_pealinnad.txt")  # Вызов функции из модуля Riigid
    elif choice == '4':
        kustuta_riik("EuroopaRiigid/riigid_pealinnad.txt")  # Вызов функции из модуля Riigid
    elif choice == '5':
        sorteeri_riigid()  # Вызов функции из модуля Riigid
    elif choice == '6':
        ekspordi_faili("EuroopaRiigid/riigid_pealinnad_eksport.txt")  # Вызов функции из модуля Riigid
    elif choice == '7':
        kontrolltest()  # Вызов функции из модуля Riigid
    elif choice == '8':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
