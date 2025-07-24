## Personalized-Task-Manager Using Python

# Agenda

- Develop a personalized task manager in Python

- Create a user-friendly interface for task management
  
- Implement functionalities for adding, editing, and removing tasks

- Include features for saving and loading tasks from a file

- Ensure data integrity and reliability in task management operations

- Incorporate additional features such as task prioritization and due dates

- Focus on code readability, modularity, and scalability

- Accommodate diverse user requirements for effective task management

# Set up the project directory:

- Create a new directory for the project, e.g., "task_manager", to organize files.
  
# Initialize a Python script:
   
- Create a new Python file, e.g., "task_manager.py", for writing code.

# Import necessary modules:

- Import required modules like "os" for file handling.
  The os module in Python provides functions for interacting with the operating system, including file and directory manipulation, process management, and environment variables access.

# Define the TaskManager class:

- Create a class to manage tasks, with attributes like directory and tasks.

# Define methods for task management:

- Inside the TaskManager class, define methods to add, edit, omit, save, and load tasks.

# Implement the methods:
   
- Fill in the method bodies with the appropriate code to perform each task management operation. For example, adding a task would involve updating the tasks dictionary with the new task information.

1. add_task: Update tasks dictionary with task name as key and description as value, if task doesn't exist.

2. edit_task: Modify task description for given task name if it exists in tasks dictionary.

3. omit_task: Delete task entry for given task name if it exists in tasks dictionary.

4. save_tasks: Write tasks dictionary contents to a file in specified directory.

5. exit: To terminate the program's execution and return control to the operating system or calling process.

6. Create a directory named "task_manager_data" if it doesn't exist to store tasks and ensure organizational structure.

7. Main Program Entry: Check if the script is being run as the main program.
   
8. Task Manager Initialization: Create an instance of the TaskManager class with the directory specified as "task_manager_data".

9. Load Tasks: Call the load_tasks() method to load previously saved tasks from the file.

10. User Interaction Loop: Enter a loop to interactively manage tasks until the user chooses to exit.

11. Display Menu Options: Print a menu displaying options for adding, editing, omitting, saving tasks, or exiting.

12. Prompt User Input: Ask the user to input their choice from the displayed menu (1-5).

13. Process User Choice: Based on the user's input, execute the corresponding action.

- If the choice is '1', prompt for task name and description, then add the task.

- If the choice is '2', prompt for task name and new description, then edit the task.

- If the choice is '3', prompt for task name, then omit (delete) the task.

- If the choice is '4', save the current tasks to the file.

- If the choice is '5', print "Exiting..." and break out of the loop to end the program.

