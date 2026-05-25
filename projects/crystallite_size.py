# Calculate crystallite average 
import numpy as np

# use numpy array and copy data from sch width / nm (5 peaks)
sch_widths = [38.01998242688474, 41.35548936203639, 34.085196859217334, 33.59588740626099, 32.89888138839362, ]

# Calculate the average (d_average) and standard deviation (error)
d_average = np.mean(sch_widths)
d_std = np.std(sch_widths)

# Results
print(f' Average Crystallite Size: {d_average} nm')
print(f' Standard Deviation: {d_std} nm')
print('-' * 50)
print(f' Results: {d_average:.2f} \pm {d_std:.2f} nm')