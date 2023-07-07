# Trip_Expenses_Manager_App
# Overview
Expense Manager App is a simple application designed to help groups of friends manage their expenses during a trip or outing. The app allows users to create groups, record expenses, upload receipts, split costs among group members, and reconcile payments. This README provides an overview of the app's features, the process flow diagram, wireframes, and information on how the data is stored and tracked using a simplified Excel grid.
## Problem Statement
### A group of 5 friends (A, B, C, D, E) go on a 2-day trip.'C' handles the travel booking for the group.Accommodation is booked by B.Food is shared in groups where 'A' paid for A, B, C. E paid for D and herself.

# Features
#### User Onboarding: Users can create accounts and log in to the app.
#### Group Management: Users can create and modify groups for specific purposes, such as a trip or meal.
#### Expense Entry: Users can enter expenses with details such as amount, description, and payment date.
#### Receipt Upload: Users can upload copies of receipts to keep track of expenses.
#### Tagging Group Members: Users can tag relevant group members for each expense.
#### Splitting Expenses: The app calculates and displays the amount owed by each group member for every expense.
#### Partial or Full Payback: Users can record payments made by group members to settle their debts partially or fully.
#### Group Closure: The app allows the closure of a group once all expenses have been split equally and reconciled.

![Screenshot 2023-07-02 132818](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/2cbf5341-5f6d-4278-b6db-4c992213a0e7)
![Screenshot 2023-07-03 045029](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/13e50f54-ce1f-459c-8928-11dc9ee1b32c)
![Screenshot 2023-07-02 120841](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/a5313aba-6fbd-4fc7-ae00-c577b4da06e6)
![Screenshot 2023-07-02 131405](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/bf2775a3-6277-4f89-bdc8-ed32945ee688)
![Screenshot 2023-07-02 131436](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/1be0c19f-2f51-46a5-9a9e-79ecc459da0e)
![Screenshot 2023-07-03 045138](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/166826ed-e4e2-4d4e-b443-67d414683d76)
![Screenshot 2023-07-03 045411](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/8672c839-97be-44a8-8f39-7d4d082a3014)
![Screenshot 2023-07-03 045421](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/886f33a3-f378-4843-8a06-39e50b83e86c)
![Screenshot 2023-07-03 045623](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/132fc26a-58b2-4813-972a-ff00b59c4266)
![Screenshot 2023-07-03 063619](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/8e4a161d-2419-437f-b821-8351bc0bff18)
![Screenshot 2023-07-03 063636](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/4e92b4cf-0b0f-46cc-a752-cf4626da6252)
![Screenshot 2023-07-03 064349](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/cc286eb9-a84b-4623-a001-ff0dbae6335b)
![Screenshot 2023-07-03 070341](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/7b92c578-ae21-4374-b265-0185655260b3)
![Screenshot 2023-07-03 083311](https://github.com/omkarm0542/Trip_Expenses_Manager/assets/123791884/5ae7ae58-b03a-41a3-ad19-fef9bcb4c2be)


# ata Storage and Tracking
To store and track the data for expense management, a simplified Excel grid can be used. The following columns can be included:

**Expense ID:** A unique identifier for each expense.
**Description:** Description of the expense.
**Amount:** The total amount of the expense.
**Date: **The date of the expense.
**Payer**: The user who paid for the expense.
**Members:** The group members involved in the expense.
**Receipt:** File path or link to the uploaded receipt.
**Status: **Indicates if the expense has been reconciled or not.
**Payment:** The amount paid by each group member.
**Closure Status:** Indicates if the group has been closed or not.
This data can be stored in a MySQL database, with each row representing an expense entry. The app can use a Python backend to handle data processing and interactions with the database.

# Getting Started
To run the Expense Manager App locally, follow these steps:

* Clone the repository from GitHub: [insert repository URL]
* Install the necessary dependencies listed in the requirements.txt file.
* Set up a MySQL database and configure the connection details in the app.
* Run the Python file to start the app.
* Access the app through your preferred web browser.
# Dependencies
Python 

MySQL 

Streamlit 
