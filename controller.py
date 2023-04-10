import phone_book

pb = phone_book.PhoneBook('file.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберете пункт меню :'))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите номоер телефона : ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(
                input('введите индекс контакта который будем изменять: '))
            name = input('Введите имя (или enter - оставить без изменения): ')
            phone = input(
                'Введите номоер телефона(или enter - оставить без изменения): ')
            comment = input(
                'Введите комментарий(или enter - оставить без изменения): ')
            pb.change(index - 1, name, phone, comment)
        case 5:
            print(pb)
            index = int(
                input('введите индекс контакта который будем удалять: '))
            pb.delete(index - 1)
        case 6:
            pb.save()
        case 7:
            break
