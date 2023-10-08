import os


def main_menu():
    print('Меню')
    print('Если хотите создать заметку нажмите 1')
    print('Если хотите редактировать готовую заметку нажмите 2')
    print('Если хотите удалить заметку нажмите 3')

    return input('Выберете действие: ')


def main():
    while True:
        choice = main_menu()

        if choice == '1':
            build_note()

        elif choice == '2':
            edit_note()
        elif choice == '3':
            break
        else:
            print('Введите другое число')


def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")


def create_note():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)


def read_note(note_name):
    note_name = input("Введите название заметки: ")
    if os.path.isfile(note_name):
        with open(note_name, 'r') as file:
            contens = file.read()
        print(contens)
    else:
        print('Заметка не найдена')


def edit_note(note_name):
    note_name = input("Введите название заметки: ")
    if os.path.isfile(note_name):
        with open(note_name, 'r') as file:
            contens = file.read()
            print(contens)

        new_contens = input('Введите текст заметки: ')
        with open(note_name, 'w') as file:
            file.write(new_contens)
    else:
        print('Замтека не надйена')


def delete_note(note_name):
    note_name = input("Введите название заметки: ")
    if os.path.isfile(note_name):
        os.remove(note_name)
    else:
        print('Заметка не найдена')
