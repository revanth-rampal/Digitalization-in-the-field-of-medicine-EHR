import matplotlib.pyplot as plt

# Actual data from a CBC test
rbc_count = 5e6  # 5 million cells/μL (replace with actual RBC count)
mcv = 90  # femtoliters (fL) (replace with actual MCV)
rdw = 12  # Percentage (replace with actual RDW)

# Creating data for the line graph
cell_sizes = range(int(mcv - 3 * rdw), int(mcv + 3 * rdw) + 1)  # Adjust the range based on your actual data
cell_counts = [rbc_count * (1 / (rdw * (2 * 3.14) ** 0.5)) * 2.718 ** (-(x - mcv) ** 2 / (2 * rdw ** 2)) for x in cell_sizes]

# Plotting the line graph
plt.plot(cell_sizes, cell_counts, marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('Red Blood Cell Size (fL)')
plt.ylabel('Number of Red Blood Cells (millions/μL)')
plt.title('Red Blood Cell Histogram (Line Graph)')

# Display the plot
plt.show()
