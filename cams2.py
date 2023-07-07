import streamlit as st
import graphviz as gv

def create_process_flow_diagram():
    dot = gv.Digraph(comment='Expense Management App Process Flow')

    # Add nodes
    dot.node('A', 'User Registration/Login')
    dot.node('B', 'Create a New Group')
    dot.node('C', 'Add Group Members')
    dot.node('D', 'Enter Expenses')
    dot.node('E', 'Upload Receipts')
    dot.node('F', 'Tag/Untag Group Members')
    dot.node('G', 'Split Expenses Equally or Select Individual Payments')
    dot.node('H', 'Mark Trip Closure')

    # Add edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')

    # Render the flowchart
    st.graphviz_chart(dot.source)

# Main function to run the Streamlit app
def main():
    st.title('Expense Management App')
    create_process_flow_diagram()

if __name__ == '__main__':
    main()
