import streamlit as st
import graphviz as graph
def login_section():
    st.subheader('Login')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login')
    
    if login_button:
        # Perform login authentication logic
        # Your code here
        st.success('Login successful!')

def registration_section():
    st.subheader('New Registration')
    email = st.text_input('Email_id')
    password = st.text_input('Password(up to 8 charecter)', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    name = st.text_input('Name')
    dob = st.date_input('Date of Birth')
    phone = st.text_input('Phone')
    address = st.text_area('Address')
    
    st.subheader('User Type')
    is_viewer = st.checkbox('I am a viewer')
    is_group_member = st.checkbox('I am a group member')
    is_investor = st.checkbox('I am an investor')
    is_tour_manager = st.checkbox('I am a tour manager')
    
    register_button = st.button('Register')
    
    if register_button:
        # Perform registration logic
        # Your code here
        st.success('Registration successful!')



def create_flow_diagram():
    dot = graph.Digraph()
    
    # Add nodes
    dot.node('Start', 'Start')
    dot.node('C', 'C - Travel Booking')
    dot.node('B', 'B - Accommodation Booking')
    dot.node('A', 'A - Food Payment (A, B, C)')
    dot.node('E', 'E - Food Payment (D, E)')
    
    # Add edges
    dot.edge('Start', 'C')
    dot.edge('C', 'B')
    dot.edge('B', 'A')
    dot.edge('B', 'E')
    
    return dot
def create_flow_diagram():
    dot = graph.Digraph()
    
    # Add nodes
    dot.node('Start', 'Start')
    dot.node('C', 'C - Travel Booking')
    dot.node('B', 'B - Accommodation Booking')
    dot.node('A', 'A - Food Payment (A, B, C)')
    dot.node('E', 'E - Food Payment (D, E)')
    
    # Add edges
    dot.edge('Start', 'C')
    dot.edge('C', 'B')
    dot.edge('B', 'A')
    dot.edge('B', 'E')
    
    return dot


def main():
    st.title('Travel Plan Flow Diagram')
    st.graphviz_chart(create_flow_diagram().source)

if __name__ == '__main__':
    main()

def main():
    st.title('User Login and Registration')
    login_section()
    st.markdown('---')
    registration_section()

if __name__ == '__main__':
    main()
    
    
    
    
    
    import streamlit as st
import pandas as pd

def receipt_management():
    st.subheader("Receipt Management")

    uploaded_file = st.file_uploader("Drag and Drop or Upload Receipt", type=["png", "jpg", "pdf", "csv", "json"], accept_multiple_files=False, key="fileUploader")

    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

        # Display the uploaded file
        st.image(uploaded_file)
        # Process the uploaded file here, such as saving it, parsing data, or performing any necessary operations

def create_user_group():
    st.header("Create User Group")
    group_name = st.text_input("Group Name")
    
    members_list = ['A', 'B', 'C', 'D', 'E']

    selected_members = st.multiselect("Select Members", members_list)

    if st.button("Create Group"):
        new_group = {
            "group_name": group_name,
            "members": selected_members,
            "expenses": [],
            "payments": {}
        }

        # Store the new group in a data structure or database
        # For example, you can use a list of dictionaries or a database table
        # groups.append(new_group)

        st.success(f"User group '{group_name}' with members '{selected_members}' created successfully!")
        # Add code to create a new user group with the given name and members

def modify_user_group():
    st.header("Modify User Group")
    # Add code to select a user group and modify its members

def user_group_management():
    st.subheader("User Group Management")
    create_user_group()
    modify_user_group()
    
def expense_entry():
    st.subheader("Expense Entry")
    # Add code to enter expenses and associate them with the user group and relevant group members

def record_payment():
    st.subheader("Record Payment")
    # Add code to record payments made by group members and update the remaining balance

def payback():
    st.subheader("Payback")
    # Add code to perform payback to selected group members, either in full or partial amounts

def group_closure():
    st.subheader("Group Closure")
    # Add code to monitor expenses and payments, and close the group when necessary


def main():
    st.title("Expense Tracker")

    # Add navigation options for each functionality
    menu = ["User Group Management", "Expense Entry", "Receipt Management", "Payment/Payback", "Group Closure"]
    choice = st.sidebar.selectbox("Select Functionality", menu)

    if choice == "User Group Management":
        user_group_management()
    elif choice == "Expense Entry":
        expense_entry()
    elif choice == "Receipt Management":
        receipt_management()
    elif choice == "Payment/Payback":
        record_payment()
        payback()
    elif choice == "Group Closure":
        group_closure()

if __name__ == '__main__':
    main()

















import streamlit as st
import pandas as pd

# Create a DataFrame to store the expenses and payments
expenses_df = pd.DataFrame(columns=['Expense', 'Payer', 'Participants', 'Amount', 'Receipt'])
payments_df = pd.DataFrame(columns=['Payer', 'Recipient', 'Amount'])

# Function to add an expense to the DataFrame
def add_expense(expense, payer, participants, amount, receipt):
    new_row = {'Expense': expense, 'Payer': payer, 'Participants': participants, 'Amount': amount, 'Receipt': receipt}
    expenses_df.loc[len(expenses_df)] = new_row

# Function to add a payment to the DataFrame
def add_payment(payer, recipient, amount):
    new_row = {'Payer': payer, 'Recipient': recipient, 'Amount': amount}
    payments_df.loc[len(payments_df)] = new_row

# Function to display the expenses table
def display_expenses():
    st.subheader('Expenses')
    st.table(expenses_df)

# Function to display the payments table
def display_payments():
    st.subheader('Payments')
    st.table(payments_df)

# Function to calculate and display individual shares
def display_shares():
    total_expenses = expenses_df['Amount'].sum()
    num_participants = len(expenses_df['Participants'].sum())
    individual_share = total_expenses / num_participants

    shares_df = pd.DataFrame(columns=['Participant', 'Share'])

    for participant in expenses_df['Participants'].sum():
        participant_share = individual_share
        if participant == expenses_df['Payer']:
            participant_share -= expenses_df.groupby('Payer')['Amount'].sum()
        participant_share -= payments_df.loc[payments_df['Recipient'] == participant, 'Amount'].sum()
        shares_df.loc[len(shares_df)] = {'Participant': participant, 'Share': participant_share}

    st.table(shares_df)

# Function to perform payback
def perform_payback(payer, recipient, amount):
    add_payment(payer, recipient, amount)

# Main function to run the Streamlit app
def main():
    st.title('Expense Manager')

    menu_options = ['Add Expense', 'Add Payment', 'Show Expenses', 'Show Payments', 'Calculate Shares', 'Perform Payback']
    choice = st.sidebar.selectbox('Menu', menu_options)

    if choice == 'Add Expense':
        expense = st.text_input('Expense')
        payer = st.selectbox('Payer', ['A', 'B', 'C', 'D', 'E'])
        participants = st.multiselect('Participants', ['A', 'B', 'C', 'D', 'E'], default=['A', 'B', 'C', 'D', 'E'])
        amount = st.number_input('Amount')
        receipt = st.file_uploader('Receipt')

        if st.button('Add Expense'):
            add_expense(expense, payer, participants, amount, receipt)

    elif choice == 'Add Payment':
        payer = st.selectbox('Payer', ['A', 'B', 'C', 'D', 'E'])
        recipient = st.selectbox('Recipient', ['A', 'B', 'C', 'D', 'E'])
        amount = st.number_input('Amount')

        if st.button('Add Payment'):
            add_payment(payer, recipient, amount)

    elif choice == 'Show Expenses':
        display_expenses()

    elif choice == 'Show Payments':
        display_payments()

    elif choice == 'Calculate Shares':
        display_shares()

    elif choice == 'Perform Payback':
        st.subheader('Payback')
        payer = st.selectbox('Payer for Payback', ['A', 'B', 'C', 'D', 'E'])
        recipient = st.selectbox('Recipient for Payback', ['A', 'B', 'C', 'D', 'E'])
        amount = st.number_input('Amount for Payback')

    if st.button('Perform Payback'):
        perform_payback(payer, recipient, amount)
        st.success(f'Payback of {amount} from {payer} to {recipient} has been recorded.')

if __name__ == '__main__':
    main()