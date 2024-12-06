#----------Notes----------
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
# Draw plot and present chart in cell
%matplotlib inline

# Seaborn
# Hue: determines which column in the data frame should be used for colour encoding

# Reset axis label
plt.ticklabel_format(style="plain")

#----------Directory----------
# mkdir means make a directory
import os
if not os.path.exists('images'):
    os.mkdir('images')

#----------Save----------
# Save image
fig.write_image("images/fig.png")

# Save figures to file
fig.savefig('test.png')

#----------1d and 2d----------
# Plot simple 2d graph
data = {
    'country': ['Singapore', 'France', 'Germany', 'Netherlands', 'England'],
    'population': [5.6, 64.3, 81.3, 16.9, 64.9],
    'area': [30510, 671308, 357050, 41526, 244820],
    'capital': ['Singapore', 'Paris', 'Berlin', 'Amsterdam', 'London']
}
countries = pd.DataFrame(data)
countries
countries.plot()

#----------Multiple plots----------
# Multiple plots
import numpy as np
x = np.linspace(0, 20, 100)
fig = plt.figure()

# Create first of two panels and set current axis
# Row, columns, panel number
plt.subplot(2, 1, 1)
# Sine plot
plt.plot(x, np.sin(x))

# Create second pane1 and set current axis
plt.subplot(2, 1, 2)
# Cosine plot
plt.plot(x, np.cos(x))

#----------Line plots----------
# Plot simple line graph
import matplotlib.pyplot as plt
x = [1,3,4,5]
y = [4,6,7,9]
plt.xlabel('xaxis') 
plt.ylabel('yaxis') 
plt.title('Simple line graph') 
plt.plot(x,y)
plt.show()

# Basic line plot within pandas
plot_df = pd.DataFrame({
    'col1': [1, 3, 2, 4],
    'col2': [3, 6, 5, 1],
    'col3': [4, 7, 6, 2],
})
plot_df.plot()

# Line plot
import matplotlib.pyplot as plt
years = [2014, 2015, 2016, 2017, 2018]
total_population = [8939002, 8954511, 8960389, 8956742, 8943720]
plt.plot(years, total_population)
plt.title("Year vs Population on Mars")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()

# Line plot
plt.figure(figsize=(10,7))
sns.lineplot(x='age', y='hours_per_week', hue='gender', data=census_data)

#----------Bar plots----------
# Veritical bar plot for average age for each sex
agemean = tdf.groupby('sex')['age'].mean()
agemean
plt.bar(agemean.index, agemean)

# Horizontal bar plot for average age for each sex
plt.barh(agemean.index, agemean)

# Basic bar plot within pandas
plot_df.plot(kind='bar')

# Bar plot
plt.figure(figsize=(10,5))
sns.barplot(x='income_bracket', y='age', hue='gender', data=census_data)
plt.figure(figsize=(12,5))
sns.countplot(x='marital_status', data=census_data)

#----------Scatter plots----------
# Scatter plot
import matplotlib.pyplot as plt
temp = [30, 32, 33, 28.5, 35, 29, 29]
ice_creams = [100, 115, 115, 75, 123, 76, 82]
plt.scatter(temp, ice_creams)
plt.title("Temperature vs Ice Creams Sold")
plt.xlabel("Temperature")
plt.ylabel("Ice Creams Sold")
plt.show()

#----------Histogram plots----------
labels = ["JavaScript", "Java", "Python", "R"]
usage = [62.8, 43.3, 36.8, 32.4]
y_positions = range(len(labels))
plt.bar(y_positions, usage)
plt.title("Usage of different programming lanuguages")
plt.xticks(y_positions, labels)
plt.ylabel("Usage (%)")
plt.show()

#----------Box plots----------
# Boxplot displays summary of data (minimum, first quartile, median, third quartile and maximum)
import pandas as pd
df = pd.DataFrame([
    {'Name': 'aa', 'Salary': 1121, 'Hours': 35},
    {'Name': 'bb', 'Salary': 2121, 'Hours': 45},
    {'Name': 'cc', 'Salary': 1221, 'Hours': 40},
    {'Name': 'dd', 'Salary': 3421, 'Hours': 41},
    {'Name': 'ee', 'Salary': 9821, 'Hours': 38},
    {'Name': 'ff', 'Salary': 6121, 'Hours': 30},
])
df
# Quantile of Hours (first quantile = 25%, median = 50%, third quantile = 75%)
df['Hours'].quantile([0.25, 0.5, 0.75])

# Box plot
plt.figure(figsize=(16,9))
sns.boxplot(x='age', y='marital_status', data=census_data)
plt.figure(figsize=(16,9))
sns.boxplot(x='age', y='marital_status', hue='gender', data=census_data)

#----------Relationship plots----------
# Relationship plot
plt.figure(figsize=(10,7))
sns.relplot(x='capital_loss', y='capital_gain', 
            hue='marital_status', 
            size='age', 
            sizes=(0,300), 
            col='gender', 
            data=census_data)

#-----------Count plots----------
# Count plot
plt.figure(figsize=(24,5))
sns.countplot(x='occupation', data=census_data)

#----------Correlation analysis----------
# Explore relationship between numerical columns, 2 ways
# Correlation analysis
# Pairplot

# Find correlation
correlation = df.corr()

# Stretching image for plt.figure
plt.figure(figsize=(10,7))
corr = census_data.corr()
# Plot correlation data
# annot=True to display numbers
sns.heatmap(corr, annot=True)
plt.show()

#i.e. 0.15 weakly correlated
# Values closer to -1 or +1, implies strong correlation relation between our features
values closer to 0, indicates no correlation
based on above features have little to no correlation

# Pairplot analysis 
# Distribution and relationships
sns.pairplot(census_data)
# Scatter plot
plt.figure(figsize=(10,7))
sns.scatterplot(x='capital_loss', 
                y='capital_gain', 
                hue='marital_status',
                size='age',
                sizes=(0,300),
                data=census_data)

#----------Seaborn dashboard----------
# Create dashboard
fig = plt.figure(figsize=(24,20))
fig.suptitle("Analysis of US Census", fontsize=30)
#2 rows and 2 columns
# First chart
plt.subplot(2, 2, 1)
sns.lineplot(x='age', y='hours_per_week', hue='gender', data=census_data)
plt.title("Age vs Hours per week")
plt.xlabel('Age')
plt.ylabel('Hours per week')
# Second chart 
plt.subplot(2, 2, 2)
sns.scatterplot(x='capital_loss', 
                y='capital_gain', 
                hue='marital_status',
                size='age',
                sizes=(0,300),
                data=census_data)
plt.title("Capital loss vs Capital gain")
plt.xlabel('Capital loss')
plt.ylabel('Capital gain')
# Third chart
plt.subplot(2, 2, 3)
sns.boxplot(x='age', y='marital_status', hue='gender', data=census_data)
plt.title("Age vs Marital Status")
plt.xlabel('Age')
plt.ylabel('Marital Status')
# Fourth chart
plt.subplot(2, 2, 4)
sns.barplot(x='income_bracket', y='age', hue='gender', data=census_data)
plt.title("Age vs Income Bracket")
plt.xlabel('Age')
plt.ylabel('Income Bracket')
plt.show()

#----------Plotly libraries----------
# Plotly will work offline
py.offline.init_notebook_mode(connected=True)
# Import plotly
import plotly
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
init_notebook_mode(connected=True)
# Import javascript
import plotly.graph_objs as go
init_notebook_mode(connected=True)

#----------Plotly plots----------
# Create our capital loss vs capital gain
trace0 = go.Scattergl(x=census_data['capital_loss'], y=census_data['capital_gain'], 
            mode='markers'
            )
layout = go.Layout(title="Capital loss versus Capital gain",
                   title_x =0.5,
                  xaxis=dict(title="Capital Loss"),
                  yaxis=dict(title="Capital Gain"))

iplot({"data":trace0,"layout":layout})
# Create a bar chart to show marital status count
trace1 = go.Bar(
    x = census_data['marital_status'].unique(),
    y = census_data.groupby('marital_status')['age'].count()
)
layout1 = go.Layout(title="Marital Status count",
                   title_x =0.5,
                  xaxis=dict(title="Marital status"),
                  yaxis=dict(title="Count"))
iplot({"data":trace1,"layout":layout1})
# Create a scatter plot
trace2 = go.Scatter3d(
    x=census_data['capital_loss'], 
    y=census_data['capital_gain'],
    z=census_data['hours_per_week'],
    mode='markers',
    marker= dict(size=12,
                 color=census_data['hours_per_week'],
                 colorscale= 'Viridis')
)

layout2 = go.Layout(title="3D scatter plot",
                   title_x =0.5)
iplot({"data":trace2,"layout":layout2})

#----------Plotly dashboard----------
# Creating a dashboard with any four of the single charts above using the concept of subplots
# Subplot of 2rows 2columns
from plotly import subplots
import numpy as np
x = np.arange(1,11)
y1 = np.exp(x)
y2 = np.log(x)
# First trace - as a line chart
trace1 = go.Scatter(
   x = x,
   y = y1,
   name = 'exp'
)
# Second trace - as a line chart
trace2 = go.Scatter(
   x = x,
   y = y2,
   name = 'log'
)
# Third trace - Bar chart
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
barr = go.Bar(
   x = langs,
   y = students
)
# Fourth trace histogram
x1 = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
hist = go.Histogram(x = x1)
fig = subplots.make_subplots(rows=2, cols=2)
fig.append_trace(trace1, 1,1)
fig.append_trace(trace2, 1,2)
fig.append_trace(barr, 2,1)
fig.append_trace(hist, 2,2)
fig['layout'].update(height=600, width=800, title="New Dashboard")
iplot(fig)
