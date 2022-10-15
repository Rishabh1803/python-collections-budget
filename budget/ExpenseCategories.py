from . import Expense
import matplotlib.pyplot as plt

# Import timeit
import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()

    # Use categorize_set_comprehension
    divided_set_comp = expenses.categorize_set_comprehension()

    # Check that the categorized sets are equal
    if divided_for_loop != divided_set_comp:
        print('Sets are NOT equal by == test')
    
    # Call timeit.timeit()
    # Print the timeit result
    print(timeit.timeit(stmt = 'expenses.categorize_for_loop()', setup = """from . import Expense\nexpenses = Expense.Expenses()\nexpenses.read_expenses('data/spending_data.csv')""", number = 100000, globals = globals()))
    
    # Duplicate the timeit.timeit() call for set comprehension
    print(timeit.timeit(stmt = 'expenses.categorize_set_comprehension()', setup = """from . import Expense\nexpenses = Expense.Expenses()\nexpenses.read_expenses('data/spending_data.csv')""", number = 100000, globals = globals()))

    '''Set comprehension may be faster than a for loop in general for a single loop. However, we had 2 set comprehensions that each required looping to check separate conditionals whereas the for loop method only used one iteration to check the conditionals.'''

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create the list of labels
    labels = ['Necessary', 'Food', 'Unnecessary']

    # Create the list of sums
    divided_expenses_sum = []

    # Sum the amounts in each set
    for category_exps in divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_exps))

    # Create the pie chart
    ax.pie(divided_expenses_sum, labels = labels, autopct = '%1.1f%%')

    # Show the figure
    plt.show()


    # Create for loop for subset test
    for a,b in zip(divided_for_loop, divided_set_comp):
        # Check that the categorized sets are equal by subset test
        if not(a.issubset(b) and b.issubset(a)):
            print('Sets are NOT equal by subset test')


if __name__ == "__main__":
    main()