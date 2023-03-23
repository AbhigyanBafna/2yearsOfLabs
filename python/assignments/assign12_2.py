import matplotlib.pyplot as plt

# Data for the pie chart
countries = ['United States', 'China', 'Great Britain', 'Russia', 'Germany', 'Japan']
gold_medals = [57, 48, 39, 25, 20, 10]

# Creating the figure and axis objects
fig, ax = plt.subplots()

# Creating the pie chart
ax.pie(gold_medals, labels=countries, autopct='%1.1f%%', startangle=90)

# Adding labels and title
ax.set_title('Gold medals obtained by countries in Olympics 2012')

# Displaying the graph
plt.show()