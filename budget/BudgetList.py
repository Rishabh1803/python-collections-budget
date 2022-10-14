# To test this module, run the command: pytest -k module2
# To run this module, run the command: python -m budget.BudgetList

# Import the Expense module
from . import Expense

# Import Matplotlib
import matplotlib.pyplot as plt

# Create the BudgetList class
class BudgetList():

    # Create the Constructor
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    # Define the append method
    def append(self, item):
        
        # Add items to expenses that are under budget
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item

        # Add items to overages that are over budget
        else:
            self.overages.append(item)
            self.sum_overages += item
    

    # Define the _len_() method
    def __len__(self):
        return len(self.expenses) + len(self.overages)

    # Create the __iter__() method
    def __iter__(self):
        # Finish __iter__()
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    # Create next()
    def __next__(self):
        # Finsh __next__()
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()


# Define the main function
def main():
    myBudgetList = BudgetList(1200)

    # Read in the spending data file
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

    # Add the expenses to the BudgetList
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses: ', str(len(myBudgetList)))
    
    # Test the iterable
    for entry in myBudgetList:
        print(entry)
    
    # Create the figures and axes
    fig, ax = plt.subplots()

    # Create the list of labels
    labels = ['Expenses', 'Overages', 'Budget']

    # Create the list of values
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]

    # Create the bar graph
    ax.bar(labels, values, color = ['green', 'red', 'blue'])

    # Set the title
    ax.set_title('Your total expenses vs. total budget')

    # Show the figure
    plt.show()


# Tell Python to run the main function
if __name__ == "__main__":
    main()