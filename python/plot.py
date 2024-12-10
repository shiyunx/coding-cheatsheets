# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# Draw plot and present chart in cell
%matplotlib inline

# Create an empty plot of the given figsize
plt.figure(figsize=(10,10))

# Set linewidth, color and linestyle
# linewidth: adjust the width
# linestyle: "solid", "dotted", "dashed" or "dashdot"
plt.plot([xplot], [yplot], linewidth = 5, color="red", linestyle="dotted")

# set x-axis(x1,x2) and y-axis(y1,y2)
plt.axis([0,5,0,10])

# Set title
plt.title("Plot")  
# Display plot
plt.show()

# Seaborn scatter plot
# Hue: determines which column in the data frame should be used for colour encoding
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm',
                hue='Species', data=data, )

