Getting Started
Prerequisites
Before using this calculator, ensure you have the following:

Python installed on your computer.
Django, a Python web framework, installed.
A web browser to access the calculator.
Installation
Clone the Project:

Open your command prompt or terminal.

Navigate to the directory where you want to create the project.

Run the following command to clone the project:

git clone <project_repository_url>
Run the Development Server:

Navigate to the project directory.

Start the Django development server with this command:

python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to access the calculator.

How to Use
Performing Calculations
Input Numbers:

Enter two numbers in the "Number 1" and "Number 2" fields.
Select Operation:

Choose the operation you want to perform (Add, Subtract, Multiply, or Divide) from the dropdown menu.
Submit the Form:

Click the "Calculate" button to perform the selected operation.
Using POST Method
When you submit the form, the calculator uses the POST method to process your request and display the result below the form.
Using GET Method
You can also use the GET method to perform calculations.
Scroll down to the "GET Method Calculator" section.
Enter the numbers and select the operation.
Click the "Calculate" button, and the result will be displayed below the GET method form.
Viewing Results
The result of your calculation will be displayed as "Result."