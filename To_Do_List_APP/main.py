""" To-Do List

This program is a simple to-do list

CHANGES:
    1-17-25
    When user types in task it is automatically capitalized.
    Program checks for task compared with lower case.
    Added due dates
    Added edit task function and choice in main menu.
    Updated delete task function to look for task and print not found if task not found.
    Updated add task function for notes and due date (if none prints N/A)

todo:
    add comments
    Error Handling: Add error handling to manage unexpected situations, such as file read/write errors.
    User Authentication: Implement user accounts so multiple users can have their own task lists.
    Export/Import: Allow users to export their task list to a file and import it back.
"""

import json
import os

class ToDo_List:
    def __init__(self, filename="tasks.json"):  #Initialize, sets default name to tasks.json
        self.filename = filename  #Assigns filename to self.filename
        self.tasks = self.load_tasks()  #Assigns loaded file from load_tasks method

    def load_tasks(self):  #Method for loading tasks
        if os.path.exists(self.filename):  #Checks if file exists
            with open(self.filename, "r") as file:  #Opens file using read("r")
                return json.load(file)  #Returns loaded tasks (.load) from file
        return []  #Returns as empty if file does not exist

    def save_tasks(self):
        with open(self.filename, "w") as file:  #Opens the file in write mode ("w")
            json.dump(self.tasks, file)  #Saves task to the file using .dump

    def add_tasks(self, task, due_date=None, notes=None):
        task = task.capitalize()
        due_date = due_date if due_date else "N/A"
        notes = notes if notes else "N/A"
        self.tasks.append({"Task": task, "Done": False, "Due Date": due_date, "Notes": notes})  #Adds task to list with done = False
        self.save_tasks()  #Updates the list



    def delete_task(self, task):
        task_delete = task.lower()  #Sets it to lowercase for comparison
        task_found = False  #Sets task found to false
        for t in self.tasks:
            if t["Task"].lower() == task_delete:  #If it finds the task it is set to True
                task_found = True
                break  #Stops looking for task

        if task_found:  #If task found is True
            self.tasks = [t for t in self.tasks if t["Task"].lower() != task_delete]  #Saves all tasks other than the task typed
            self.save_tasks()
        else:
            print("Task Not Found")


    def mark_done(self, task):
        task = task.lower()
        for t in self.tasks:
            if t["Task"].lower() == task:
                t["Done"] = True
                break
        self.save_tasks()

    def show_tasks(self):
        for i in self.tasks:
            if i["Done"] == True:
                status = "Done"
            else:
                status = "Not Done"
            due_date = i.get("Due Date", None)  #Gets due date, if none puts none as default
            notes = i.get("Notes", "No Notes")
            print(f"{status} - {i["Task"]} - (Due: {due_date}) - Notes: {notes}")
        print()

    def edit_tasks(self, new_task):
        new_task = new_task.lower()
        for task in self.tasks:
            if task["Task"].lower() == new_task:  #Looks for new_task(task name) in tasks
                new_task_name = input("Enter new task name. Leave Blank If Unchanged: ").capitalize()
                new_task_due_date = input("Enter new task date. Leave Blank If Unchanged: ")
                new_task_notes = input("Enter new notes for task. Leave Blank If Unchanged: ")
                new_task_done = input("Is this task done? yes or no").lower()

                if new_task_name:
                    task["Task"] = new_task_name
                if new_task_due_date:
                    task["Due Date"] = new_task_due_date
                if new_task_notes:
                    task["Notes"] = new_task_notes

                if new_task_done == "yes":
                    task["Done"] = True

                if new_task_done == "no":
                    task["Done"] = False

                self.save_tasks()
                break
        else:
            print("Task not found.")

def main():
    todo = ToDo_List()
    user = ""
    while user != "5":
        print("\nToDo List:")
        todo.show_tasks()
        print("1. Add Task\n"
              "2. Delete Task\n"
              "3. Mark as Done\n"
              "4. Edit a Task\n"
              "5. Exit")
        user = input("Enter your choice: ")
        if user == "1":
            task = input("Enter task: ")
            due_date = input("Enter Due Date (YYYY-MM-DD). If No Due Date Leave Blank: ")
            notes = input("Enter notes. If No Notes Leave Blank: ")
            todo.add_tasks(task, due_date, notes)
        elif user == "2":
            task = input("Enter task: ")
            todo.delete_task(task)
        elif user == "3":
            task = input("Enter task: ")
            todo.mark_done(task)
            task_found = False
            for t in todo.tasks:
                if task == t["Task"]:
                    task_found = True
                if not task_found:
                    print("No Task Found")
                    break

        elif user == "4":
            new_task = input("Enter task name: ")
            todo.edit_tasks(new_task)

        elif user == "5":
            print("Exiting")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
