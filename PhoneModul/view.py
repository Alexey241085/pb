

# def main_menu() -> int:
#     return int(input('''Главное меню

#     1. Открыть файл
#     2. Сохранить файл
#     3. Показать контакты
#     4. Добавить контакт
#     5. Изменить контакт
#     6. Найти контакт
#     7. Удалить контакт
#     8. Выйти

# Выберите пункт меню: '''))


# def show_contacts(book: list[dict], error_message: str):
#     if not book:
#         print(error_message)
#     else:
#         for i, contact in enumerate(book, 1):
#             print(
#                 f'{i}.{contact.get("name"):<20}'
#                 f'{contact.get("phone"):<20}'
#                 f'{contact.get("comment"):<20}')
#         return True


# def add_contact() -> dict:
#     name = input('Введите имя: ')
#     phone = input('Введите номер телефона: ')
#     comment = input('Введите комментарий: ')
#     return {'name': name, 'phone': phone, 'comment': comment}


# def input_index(message: str):
#     return int(input(message))


# def input_search(message: str):
#     return input(message)


# def change_contact(book: list[dict], index: int):
#     print('Введите новые данные или оствьте пустое поле, если нет изменений')
#     contact = add_contact()
#     return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
#             'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
#             'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}


# def show_message(message: str):
#     print('- '*len(message))
#     print(message)
#     print('- '*len(message))
