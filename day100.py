# Terminal-Based To-Do List with File Persistence

# Features:
# 1. Add a task
# 2. View all tasks
# 3. Mark a task as completed
# 4. Delete a task
# 5. Save tasks automatically to a file
# 6. Load tasks when the program starts

# File Used:
# tasks.txt

# Data Format:
# 0|Learn Python
# 1|Complete Project

# Where:
# 0 = Pending
# 1 = Completed

import os


class TodoList:

    def __init__(self, filename="tasks.txt"):
        # File used to store tasks permanently
        self.filename = filename

        # List to store tasks in memory
        self.tasks = []

        # Load existing tasks from file
        self.load_tasks()

    # --------------------------------------------------
    # Load tasks from file
    # --------------------------------------------------
    def load_tasks(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                status, task = line.split("|", 1)

                self.tasks.append(
                    {
                        "task": task,
                        "completed": bool(int(status))
                    }
                )

    # --------------------------------------------------
    # Save tasks to file
    # --------------------------------------------------
    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:

            for task in self.tasks:

                status = 1 if task["completed"] else 0

                file.write(
                    f"{status}|{task['task']}\n"
                )

    # --------------------------------------------------
    # Add a new task
    # --------------------------------------------------
    def add_task(self, task_name):

        self.tasks.append(
            {
                "task": task_name,
                "completed": False
            }
        )

        self.save_tasks()

        print("Task added successfully.")

    # --------------------------------------------------
    # View all tasks
    # --------------------------------------------------
    def view_tasks(self):

        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n===== TO-DO LIST =====")

        for index, task in enumerate(self.tasks, start=1):

            status = "✓" if task["completed"] else "✗"

            print(
                f"{index}. [{status}] {task['task']}"
            )

    # --------------------------------------------------
    # Mark task as completed
    # --------------------------------------------------
    def complete_task(self, task_number):

        if 1 <= task_number <= len(self.tasks):

            self.tasks[task_number - 1]["completed"] = True

            self.save_tasks()

            print("Task marked as completed.")

        else:
            print("Invalid task number.")

    # --------------------------------------------------
    # Delete a task
    # --------------------------------------------------
    def delete_task(self, task_number):

        if 1 <= task_number <= len(self.tasks):

            removed_task = self.tasks.pop(task_number - 1)

            self.save_tasks()

            print(
                f"Deleted: {removed_task['task']}"
            )

        else:
            print("Invalid task number.")


# ------------------------------------------------------
# Main Menu Function
# ------------------------------------------------------
def main():

    todo = TodoList()

    while True:

        print("\n==========================")
        print("      TO-DO LIST APP")
        print("==========================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter choice: ").strip()

        # ------------------------------------------
        # Add Task
        # ------------------------------------------
        if choice == "1":

            task_name = input(
                "Enter task: "
            ).strip()

            if task_name:
                todo.add_task(task_name)
            else:
                print("Task cannot be empty.")

        # ------------------------------------------
        # View Tasks
        # ------------------------------------------
        elif choice == "2":

            todo.view_tasks()

        # ------------------------------------------
        # Complete Task
        # ------------------------------------------
        elif choice == "3":

            todo.view_tasks()

            try:
                task_number = int(
                    input(
                        "\nEnter task number to complete: "
                    )
                )

                todo.complete_task(task_number)

            except ValueError:
                print("Please enter a valid number.")

        # ------------------------------------------
        # Delete Task
        # ------------------------------------------
        elif choice == "4":

            todo.view_tasks()

            try:
                task_number = int(
                    input(
                        "\nEnter task number to delete: "
                    )
                )

                todo.delete_task(task_number)

            except ValueError:
                print("Please enter a valid number.")

        # ------------------------------------------
        # Exit Program
        # ------------------------------------------
        elif choice == "5":

            print("\nTasks saved successfully.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# ------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------
if __name__ == "__main__":
    main()
