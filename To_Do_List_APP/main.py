""" To-Do List

This program is a simple to_do list

todo: add comments

todo: update script

todo: Fix "No Task Found" printing for each task. (should only print once)
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

    def add_tasks(self, task):
        self.tasks.append({"Task": task, "Done": False})  #Adds task to list with done = False
        self.save_tasks()  #Updates the list



    def delete_task(self, task):
        self.tasks = [t for t in self.tasks if t["Task"] != task]  #Saves all tasks other than the task typed
        self.save_tasks()

    def mark_done(self, task):
        for t in self.tasks:
            if t["Task"] == task:
                t["Done"] = True
                self.save_tasks()
        self.save_tasks()

    def show_tasks(self):
        for i in self.tasks:
            if i["Done"] == True:
                status = "Done"
            else:
                status = "Not Done"
            print(f"{status} - {i["Task"]}")
        print()

def main():
    todo = ToDo_List()
    user = ""
    while user != "4":
        print("\nToDo List:")
        todo.show_tasks()
        print("1. Add Task\n"
              "2. Delete Task\n"
              "3. Mark as Done\n"
              "4. Exit")
        user = input("Enter your choice: ")
        if user == "1":
            task = input("Enter task: ")
            todo.add_tasks(task)
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
                    break
                if not task_found:
                    print("No Task Found")

        elif user == "4":
            print("Exiting")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
