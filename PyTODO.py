from json import loads, dumps

todo_list = open('todo_list.json').read()
todo_list = loads(todo_list)


def view_todo_list():
    for i, c in enumerate(todo_list):
        print('[', i + 1, ']', todo_list[i]['task'], '|', todo_list[i]['status'])


def edit_task(task):
    print(todo_list[task]['task'], '|', todo_list[task]['status'], '\n')
    print("Введите номер части задачи для редактирования (1 - Задача, 2 - Статус) или введите 3 чтобы удалить задачу")
    try:
        task_part = int(input("\n> "))
        if task_part != 1 and task_part != 2 and task_part != 3:
            print("Неизвестная команда!")
        elif task_part == 1:
            new_task = input(todo_list[task]['task'] + ' -> ')
            todo_list[task]['task'] = new_task
        elif task_part == 2:
            new_task = input(todo_list[task]['status'] + ' -> ')
            todo_list[task]['status'] = new_task
        elif task_part == 3:
            print("Вы уверены что хотите удалить эту задачу?")
            answer = input("\n(Y/n)> ")
            if answer.lower() == 'y':
                del todo_list[task]
    except ValueError:
        print("Неизвестная команда!")


def add_task():
    task_name = input("Имя новой задачи: ")
    task_status = input("Статус новой задачи: ")
    new_task = {'task': task_name, 'status': task_status}
    todo_list.append(new_task)


def save_file():
    open('todo_list.json', 'w').write(dumps(todo_list))


while True:
    print("Список задач: \n")
    view_todo_list()
    print('\nВведите номер задачи или введите "+" чтобы добавить новую')
    command = input("> ")
    if command == "+":
        add_task()
        save_file()
    else:
        try:
            command = int(command)
            command -= 1
            todo_list[command]
            edit_task(command)
            save_file()
        except ValueError:
            print("Неверно введенное значение!")
        except IndexError:
            print("Данного номера не существует!")
