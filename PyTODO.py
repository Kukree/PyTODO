from json import loads

todo_list = open('todo_list.json').read()
todo_list = loads(todo_list)


def view_todo_list():
    for i, c in enumerate(todo_list):
        print('[', i + 1, ']', todo_list[i]['task'], '|', todo_list[i]['status'])


def edit_task(task):
    print(todo_list[task]['task'], '|', todo_list[task]['status'], '\n')


while True:
    print("Список задач: \n")
    view_todo_list()
    print('\nВведите номер задачи или введите "+" чтобы добавить новую')
    command = input("> ")
    if command == "+":
        pass
    else:
        try:
            command = int(command)
        except ValueError:
            print("Неверно введенное значение!")
        try:
            todo_list[command]
            edit_task(command)
        except IndexError:
            print("Данного номера не существует!")
