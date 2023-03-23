import matplotlib.pyplot as plt

# Data for the graph
countries = ['United States', 'China', 'Great Britain', 'Russia', 'Germany', 'Japan']
gold_medals = [57, 48, 39, 25, 20, 10]
silver_medals = [28, 30, 21, 25, 18, 16]

# Creating the figure and axis objects
fig, ax = plt.subplots()

# Setting the x-axis to the country names
x_pos = [i for i, _ in enumerate(countries)]
ax.set_xticks(x_pos)
ax.set_xticklabels(countries)

# Creating the bars
ax.bar(x_pos, gold_medals, color='gold', width=0.4, label='Gold Medals')
ax.bar([i + 0.4 for i in x_pos], silver_medals, color='silver', width=0.4, label='Silver Medals')

# Adding labels and titles
ax.set_ylabel('Number of Medals')
ax.set_title('Medals Won by Country in 2021')
ax.legend()

# Displaying the graph
plt.show()
