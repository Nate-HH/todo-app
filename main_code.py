#from todo_functions import get_todos, write_todos
import todo_functions
import time

while True:
    # get user action and strip spaces from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = todo_functions.get_todos()

        todos.append(todo + '\n')

        todo_functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = todo_functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = todo_functions.get_todos()

            new_todo = input("Enter a New todo: ")
            todos[number] = new_todo + '\n'

            todo_functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = todo_functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todo_functions.write_todos(todos)

            message = f"Todo {index + 1}-{todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number. ")
            continue



    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")

print('Bye!')