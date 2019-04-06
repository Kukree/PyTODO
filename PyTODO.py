from json import loads

todo_list = open('todo_list.json').read()
todo_list = loads(todo_list)

while True:
    print("Список задач: \n")
    for i, c in enumerate(todo_list):
        print('[', i, ']', todo_list[i]['task'], '|', todo_list[i]['status'])
    input()
