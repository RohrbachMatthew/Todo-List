""" To-Do List

This program is a simple to_do list

todo: add comments

todo: update script
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

def main():
    todo = ToDo_List()
    user = ""
    while user != "4":
        print("ToDo List:\n")
        todo.show_tasks()
        user = input("Enter your choice: ")
        if user == "1":
            print("1")
        elif user == "2":
            print("2")
        elif user == "3":
            print("3")
        elif user == "4":
            print("4")
            break

main()
