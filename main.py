from readwrite import get_todos, write_todos
from time import strftime

print(strftime("It is %b %d, %Y %I:%M:%S"))

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)
    
    elif user_action.startswith("show"):
        todos = get_todos()
        
        new_todos = [item.strip("\n") for item in todos]

        [print(f"{index + 1}- {todo}") for index, todo in enumerate(new_todos)]

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos()

            todos[number] = input("Enter the new todo: ") +"\n"

            write_todos(todos)
        except (ValueError, IndexError):
            print("Invalid entry. Enter a valid integer.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1

            todos = get_todos()

            todo_to_remove = todos[number].strip("\n\n")
            todos.pop(number)

            write_todos(todos)
            
            print(f"{todo_to_remove} was removed successfully")
        except (ValueError, IndexError):
            print("Invalid entry. Enter a valid integer.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Unknown command!")

print("Bye!")
