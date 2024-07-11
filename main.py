from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Слишком короткая фамилия")
            if len(phone_number) < 11:
                raise NameError("Номер телефона должен быть не менее 11 символов")
        except NameError as err:
            print(err)
        else: 
            flag = True
    last_name = "Иванов"
    phone_number = "+7805675345"
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)
    
def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standart_write(file_name, res)

def row_search(file_name):
    last_name = input("Введите Фамилию: ")
    res = read_file(file_name)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена"

def delete_row(file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    res.pop(row_number - 1)
    standart_write(file_name, res)

def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def change_row(file_name):
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    data = get_data()
    res[row_number - 1] ["Имя"] = data[0]
    res[row_number - 1] ["Фамилия"] = data[1]
    res[row_number - 1] ["Телефон"] = data[2]
    standart_write(file_name, res)

def move_to_new_file (file_name, new_file_name): # дополнение для ДЗ
    row_number = int(input("Введите номер строки: "))
    res = read_file(file_name)
    obj = read_file(new_file_name)
    obj.append(res[row_number - 1])
    standart_write(new_file_name, obj)


file_name = 'phone.csv'
new_file_name = 'target.csv' # дополнение для ДЗ

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_data())
        elif command == "r":
            if not exists(file_name):
                print("Файл не существует, создайте его")
                continue
            print(read_file(file_name))
        elif command == "f":
            if not exists(file_name):
                print("Файл не существует, создайте его")
                continue
            print(row_search(file_name))
        elif command == "d":
            if not exists(file_name):
                print("Файл не существует, создайте его")
                continue
            delete_row(file_name)
        elif command == "c":
            if not exists(file_name):
                print("Файл не существует, создайте его")
                continue
            change_row(file_name)
        elif command == "m": # дополнение для ДЗ
            if not exists(new_file_name):
                create_file(new_file_name)
                continue
            move_to_new_file(file_name, new_file_name)

main()