from json import loads

todo_list = open('todo_list.json').read()
todo_list = loads(todo_list)


def view_todo_list():
    for i, c in enumerate(todo_list):
        print('[', i + 1, ']', todo_list[i]['task'], '|', todo_list[i]['status'])


def edit_task(task):
    print(todo_list[task]['task'], '|', todo_list[task]['status'], '\n')
    print("Введите номер части задачи для редактирования (1 - Задача, 2 - Статус)")
    try:
        task_part = int(input("\n> "))
    except ValueError:
        print("Неизвестная команда!")
    if task_part != 1 and task_part != 2:
        print("Неизвестная команда!")
    elif task_part == 1:
        new_task = input(todo_list[task]['task'] + ': ')
        todo_list[task]['task'] = new_task
    elif task_part == 2:
        new_task = input(todo_list[task]['status'], ': ')
        todo_list[task]['status'] = new_task


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
            command -= 1
            todo_list[command]
            edit_task(command)
        except ValueError:
            print("Неверно введенное значение!")
        except IndexError:
            print("Данного номера не существует!")
