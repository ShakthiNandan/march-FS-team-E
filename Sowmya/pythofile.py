import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Chart')
plt.legend()

# Save instead of showing
plt.savefig("plot.png")
