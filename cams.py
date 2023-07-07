import streamlit as st
import pandas as pd

# Load data from Excel file
@st.cache
def load_data():
    return pd.read_excel('expense_data.xlsx')

# Save data to Excel file
def save_data(df):
    df.to_excel('expense_data.xlsx', index=False)

# User Registration/Login
def register_login():
    st.title("Expenses App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    create_account_button = st.button("Create Account")

    if login_button:
        # Perform login logic
        st.success("Logged in successfully!")

    if create_account_button:
        # Perform account creation logic
        st.success("Account created successfully!")

# Create a New Group
def create_group():
    st.title("Create New Group")
    group_name = st.text_input("Group Name")
    group_purpose = st.text_input("Group Purpose")
    create_button = st.button("Create Group")

    if create_button:
        # Perform group creation logic
        st.success("Group created successfully!")

# Add Group Members
def add_members():
    st.title("Add Group Members")
    group_id = st.text_input("Group ID")
    member_names = st.text_input("Member Names (comma-separated)")

    add_button = st.button("Add Members")

    if add_button:
        # Perform member addition logic
        st.success("Members added successfully!")

# Enter Expenses
def enter_expenses():
    st.title("Enter Expenses")
    group_id = st.text_input("Group ID")
    amount = st.number_input("Amount")
    description = st.text_input("Description")
    add_button = st.button("Add Expense")

    if add_button:
        # Perform expense entry logic
        st.success("Expense added successfully!")

# Main function
def main():
    register_login()

    if st.button("Create New Group"):
        create_group()

    if st.button("Add Group Members"):
        add_members()

    if st.button("Enter Expenses"):
        enter_expenses()

# Run the app
if __name__ == '__main__':
    main()
