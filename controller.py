import view
import model


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
                index = view.input_index('Введите номер изменяемого котакта: ')
                contact = view.change_contact(pb, index)
                model.change_contact(contact, index)
            case 6:
                model.search()
            case 7:
                print(pb)
                index = int(
                    input("Введите номер контакта, который хотите удалить: "))
            case 8:
                break
