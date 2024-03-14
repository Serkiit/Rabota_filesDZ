from logger import input_data,  print_data, delete_data, edit_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от geekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - Удалить даных \n 4 - Редактировать даных")
    command = int(input('Введите число: '))

    while command != 1 and command != 2 and command != 3 and command != 4 :
        print("Неправельный ввод")
        command = int(input('Введите число: '))

    if command == 1:
      input_data()   
    elif command == 2:
      print_data()    
    elif command == 3: 
      delete_data()
    elif command == 4: 
      edit_data()