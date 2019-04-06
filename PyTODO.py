from json import loads

todo_list = open('todo_list.json').read()
todo_list = loads(todo_list)


def view_todo_list():
    for i, c in enumerate(todo_list):
        print('[', i, ']', todo_list[i]['task'], '|', todo_list[i]['status'])


while True:
    print("Список задач: \n")
    view_todo_list()
    print('\nВведите номер задачи или введите "+" чтобы добавить новую')
    command = input("> ")
    if command == "+":
        pass
    else:
        pass
