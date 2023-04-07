import view
import model


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('ФАЙЛ ОТКРЫТ')
            case 2:
                model.save_file()
                view.show_message('ФАЙЛ УСПЕШНО СОХРАНЕн')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
                view.show_message('Контакт успешно добавлен')
            case 5:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
                index = view.input_index('Введите номер изменяемого котакта: ')
                contact = view.change_contact(pb, index)
                model.change_contact(contact, index)
                view.show_message('Контакт успешно изменен')
            case 6:
                search = view.input_search('Введите искомый элемент: ')
                result = model.search(search)
                view.show_contacts(result, 'Контакт не найден')
            case 7:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
                # view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
                index = int(
                    input("Введите номер контакта, который хотите удалить: "))
                pb.pop(index-1)
                view.show_message('Контакт успешно удален')
            case 8:
                break
