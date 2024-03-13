import matplotlib.pyplot as plt
import numpy as np

# Actual data from a blood test
platelet_count = 300000  # Replace with actual platelet count in cells/μL 
mpv = 10  # femtoliters (fL) - replace with actual MPV
pdw = 15  # Percentage - replace with actual PDW

# Creating data for the line graph
platelet_sizes = np.arange(int(mpv - 3 * pdw), int(mpv + 3 * pdw) + 1)
platelet_counts = [platelet_count * (1 / (pdw * (2 * 3.14) ** 0.5)) * 
                    2.718 ** (-(x - mpv) ** 2 / (2 * pdw ** 2)) for x in platelet_sizes]

# Plotting the line graph
plt.plot(platelet_sizes, platelet_counts, marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('Platelet Size (fL)')
plt.ylabel('Number of Platelets (thousands/μL)')
plt.title('Platelet Histogram (Line Graph)')

# Display the plot
plt.show()

