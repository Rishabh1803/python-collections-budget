# To test this module, run the command: pytest -k module2
# To run this module, run the command: python -m budget.BudgetList

# Import the Expense module
from . import Expense

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

# Tell Python to run the main function
if __name__ == "__main__":
    main()