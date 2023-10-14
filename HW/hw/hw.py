def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
            else:
                phone_book = read_file('phone.csv')
                print(*phone_book)
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'e':
            last_name = input('Введите фамилию для изменения: ')
            new_phone_number = input('Введите новый номер: ')
            if edit_record(res, last_name, new_phone_number):
                print('Данные успешно изменены.')
                with open('phone.csv', 'w', encoding='utf-8') as f_n:
                    f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
                    f_n_writer.writeheader()
                    f_n_writer.writerows(res)
            else:
                print('Контакт не найден.')

        elif command == 'd':
            last_name = input('Введите фамилию для удаления: ')
            if delete_record(res, last_name):
                print('Контакт успешно удален.')
                with open('phone.csv', 'w', encoding='utf-8') as f_n:
                    f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
                    f_n_writer.writeheader()
                    f_n_writer.writerows(res)
            else:
                print('Контакт не найден.')