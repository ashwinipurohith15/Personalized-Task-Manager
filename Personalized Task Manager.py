#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os  # Import the os module for file and directory operations

class TaskManager:
    def __init__(self, directory):
        self.directory = directory  # Initialize the directory for storing tasks
        self.tasks = {}  # Initialize an empty dictionary to store tasks

    def add_task(self, task_name, task_description):
        if task_name not in self.tasks:  # Check if the task already exists
            self.tasks[task_name] = task_description  # Add the task to the tasks dictionary
            print(f"Task '{task_name}' added successfully.")
        else:
            print(f"Task '{task_name}' already exists.")  # Print message if task already exists

    def edit_task(self, task_name, new_task_description):
        if task_name in self.tasks:  # Check if the task exists
            self.tasks[task_name] = new_task_description  # Update the task description
            print(f"Task '{task_name}' edited successfully.")
        else:
            print(f"Task '{task_name}' does not exist.")  # Print message if task does not exist

    def omit_task(self, task_name):
        if task_name in self.tasks:  # Check if the task exists
            del self.tasks[task_name]  # Delete the task from the tasks dictionary
            print(f"Task '{task_name}' omitted successfully.")
        else:
            print(f"Task '{task_name}' does not exist.")  # Print message if task does not exist

    def save_tasks(self):
        with open(os.path.join(self.directory, 'tasks.txt'), 'w') as file:  # Open file for writing
            for task_name, task_description in self.tasks.items():  # Iterate over tasks dictionary
                file.write(f"{task_name}: {task_description}\n")  # Write task name and description to file
        print("Tasks saved successfully.")  # Print confirmation message

    def load_tasks(self):
        file_path = os.path.join(self.directory, 'tasks.txt')  # Construct file path for tasks file
        if os.path.exists(file_path):  # Check if tasks file exists
            with open(file_path, 'r') as file:  # Open file for reading
                for line in file:  # Iterate over each line in the file
                    task_name, task_description = line.strip().split(': ')  # Split line into task name and description
                    self.tasks[task_name] = task_description  # Add task to tasks dictionary
            print("Tasks loaded successfully.")  # Print confirmation message
        else:
            print("No previous tasks found.")  # Print message if no tasks file exists


# In[2]:


# Create directory for storing tasks if it doesn't exist
if not os.path.exists('task_manager_data'):  # Check if directory exists
    os.makedirs('task_manager_data')  # Create directory if it does not exist


# In[ ]:


##### #Example usage
if __name__ == "__main__":
    task_manager = TaskManager('task_manager_data')  # Create instance of TaskManager
    task_manager.load_tasks()  # Load tasks from file

    while True:
        print("\n1. Add Task")
        print("2. Edit Task")
        print("3. Omit Task")
        print("4. Save Tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")  # Prompt user for choice

        if choice == '1':
            task_name = input("Enter task name: ")  # Prompt user for task name
            task_description = input("Enter task description: ")  # Prompt user for task description
            task_manager.add_task(task_name, task_description)  # Call add_task method
        elif choice == '2':
            task_name = input("Enter task name to edit: ")  # Prompt user for task name to edit
            new_task_description = input("Enter new task description: ")  # Prompt user for new task description
            task_manager.edit_task(task_name, new_task_description)  # Call edit_task method
        elif choice == '3':
            task_name = input("Enter task name to omit: ")  # Prompt user for task name to omit
            task_manager.omit_task(task_name)  # Call omit_task method
        elif choice == '4':
            task_manager.save_tasks()  # Call save_tasks method
        elif choice == '5':
            print("Exiting...")  # Print message indicating program exit
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")  # Print message for invalid choice


# In[ ]:




