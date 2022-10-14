# Import the Expense module
from . import Expense
import collections
import matplotlib.pyplot as plt

# Read in the Spending Data
expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

# Create a list of the Spending Categories
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

# Count Categories with a Counter Collection
spending_counter = collections.Counter(spending_categories)
# print(spending_counter)

# Get the Top 5 Categories
top5 = spending_counter.most_common(5)

# Convert the Dictionary to 2 lists
"""
If you’ve used the zip() function before it combines 2 iterables. (For example, zip(list1, list2) would combine two lists into a list of tuples). We can also use zip(*dictionary_variable) to separate the keys and values of a dictionary into separate lists. Since we want to have 2 separate lists for the categories and their counts for the bar graph, let’s call zip(*top5) and set the result equal to two variables - categories, count.
"""

categories, count = zip(*top5)

# Plot the Top 5 Most Common Categories
fig, ax = plt.subplots()

# Create the bar chart
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

# Display the graph
plt.show()