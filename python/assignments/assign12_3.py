import random
import matplotlib.pyplot as plt

# Generate 1000 random datapoints between 0 and 100
datapoints = [random.randint(0, 100) for _ in range(1000)]

# Define the bin ranges for the histogram
ranges = [0, 5, 10, 15, 20, 95, 140]

# Create the histogram
plt.hist(datapoints, bins=ranges, edgecolor='black')

# Set the x and y axis labels and title
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Random Datapoints')

# Show the histogram
plt.show()