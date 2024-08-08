import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f'Marked task "{self.tasks[index]["task"]}" as complete.')
        else:
            print("Invalid task number.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Removed task: "{removed_task["task"]}"')
        else:
            print("Invalid task number.")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)
        print(f"Tasks saved to {self.filename}.")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
            print(f"Loaded tasks from {self.filename}.")
        except FileNotFoundError:
            print("No saved tasks found.")

    def run(self):
        while True:
            print("\nTo-Do List Options:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Remove Task")
            print("5. Save Tasks")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                task = input("Enter a new task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                try:
                    index = int(input("Enter the task number to mark as complete: ")) - 1
                    self.complete_task(index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                try:
                    index = int(input("Enter the task number to remove: ")) - 1
                    self.remove_task(index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "5":
                self.save_tasks()
            elif choice == "6":
                print("Exiting the to-do list.")
                self.save_tasks()  # Save before exiting
                break
            else:
                print("Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
