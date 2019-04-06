from json import loads

todo_list = open('todo_list.json').read()
todo_list = loads(todo_list)


def view_todo_list():
    print("Список задач: \n")
    for i, c in enumerate(todo_list):
        print('[', i, ']', todo_list[i]['task'], '|', todo_list[i]['status'])


while True:
    view_todo_list()
    input()
