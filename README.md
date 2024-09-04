# **School Management System**

## **Overview**

This project is a simple **School Management System** built using Python. The purpose of this project is to demonstrate the basics of Object-Oriented Programming (OOP) while managing student data. It includes a graphical user interface (GUI) developed using `tkinter`, enabling users to easily register and manage student information such as names, student IDs, subjects, and teachers.

## **Features**

- **Object-Oriented Design:** Implements key OOP principles with classes for student management.
- **GUI Interface:** Provides a user-friendly interface for inputting and viewing student data.
- **Data Persistence:** Uses CSV and Excel files to save and retrieve data.
- **Error Handling:** Includes basic validation and error handling for user input.
- **Scalable Structure:** Organized in a way that allows easy addition of new features in the future.

## **Project Structure**

- **`app/`**: Contains the main application files, including:
  - `student.py`: Defines the `Student` class and its attributes.
  - `data_manager.py`: Handles data operations like saving to or loading from Excel files.
  - `gui.py`: Manages the graphical user interface using `tkinter`.
- **`data/`**: Stores CSV and Excel files with student data.
- **`tests/`**: Contains unit tests to ensure that different parts of the application work correctly.
- **`docs/`**: Includes project documentation and user manuals.
- **`assets/`**: Contains any additional resources like images for the GUI.

## **Getting Started**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/SchoolManagement.git
Install the necessary dependencies:

Ensure you have Python installed and necessary libraries like tkinter and pandas:
pip install pandas openpyxl
Run the application:

Execute gui.py to start the graphical interface for managing students:
python app/gui.py
Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Contributions, bug reports, and feature requests are welcome!

