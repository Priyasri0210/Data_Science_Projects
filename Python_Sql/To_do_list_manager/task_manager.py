from task_model import *

#Display the menu options

def display_menu():
    print("==============To-Do-List-Manager=================")
    print("Enter the option number only")
    print("1. Add new tasks")
    print("2. Retrive all tasks")
    print("3. Update task status")
    print("4. Delete task")
    print("5. filter by status")
    print("6. Overdue tasks")
    print("7. Exit")

# get user's choice to perform
def main():
    while True:
        display_menu()
        choice = int(input("Enter the choice : "))

        if choice == 1:
            add_task()
        elif choice == 2:
           retrieve_tasks()
        elif choice == 3:
             update_task()
        elif choice == 4:
            delete_task()
        elif choice == 5:
             filter_by_status()
        elif choice == 6:
            overdue_tasks()
        elif choice == 7:
            break
        else:
            print('Invalid input')

# calling main function
if __name__ == '__main__':
    main()