#----------Notes----------
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
# Draw plot and present chart in cell
%matplotlib inline

# Warnings
# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Check length
len(df)

# Convert frame to 2d 
df.values

# Display rows and columns of data file
df.shape
df.shape[0]

# Display columns
df.columns

# Display data first five rows
df.head()

# Display data last five rows
df.tail()

# Display basic statistical details
df.describe()

# Print full summary
df.info()

# Check variable names data types
# Check columns and types
df.dtypes
# Most commonly dtypes: floating point values (real numbers), integers, strings (text), and date/time values. 

# Create 3X1 array
a = np.array([a, b, c])
# Create 3X2 array
a = np.array([[a, b], [c,d], [e,f]])
# Type of array
type(a)
# Dimension of array
a.ndim
# Shape (row, column) of array
a.shape
# Len of array a
len(a)
# Print values
a[0], a[1], a[2]

#----------Read and load----------
# Read data file
df = pd.read_csv("file.csv")
#load data
df = pd.read_csv("cardio.csv", sep=";")
#load data
df = pd.read_csv("cardio.csv", encoding="unicode_escape")
# display all data
df

# Load data set
url = "http://bit.ly/wksp

#----------Map data to strings----------
titanic_data["alive"] = titanic_data.survived.map({0: "no", 1: "yes"})
# View one record
titanic_data.head(2)

#----------Convert age from days to years---------
Convert age from days to years df['age'] = df['age'] / 365

#-----------Date and time-----------
# Convert date parameter to string format
df['Date'] = df['Date'].astype(str) # astype(): convert column data type to another data type

# Convert date into date time format
df['Date'] = pd.to_datetime(df['Date'])

#-----------1d and 2d-----------
# Pandas data frame is a data table
# Rows represent cases
# Columns represent variables

# Data structures
# 1d data structure - pandas Series rep 1 column
# 2d data structure - pandas Dataframes

# Read dataframe
df = pd.DataFrame({'name':['Jack', 'Jill', 'John', 'Joel'], 
                 'salary':[1500,25000,125000,8000]})   
df

	name	salary
0	Jack	1500
1	Jill	25000
2	John	125000
3	Joel	8000

s = pd.Series([0.1, 0.2, 0.3, 0.4]) #list array
s

0    0.1
1    0.2
2    0.3
3    0.4
dtype: float64

# 1d pandas series = a column in excel
s = pd.Series(df['Names'])

# 2d with columns of different types
data = {
    'Fruit': ['Mango', 'Pear', 'Apple', 'Berries'],
    'Colour': ['Yellow', 'Green', 'Red', 'Blue'],
    'Cost': [1, 0.5, 0.6, 2]
}
healthy_fruits = pd.DataFrame(data)
healthy_fruits

# 1d series using a dictionary {key:value}
pop_dict = {"Singapore":5.7,
            "Indonesia":126,
            "Italy":15.3,
            "UK":29,
            "Netherlands":17.2
           }
pop_series = pd.Series(pop_dict)
pop_series

Singapore        5.7
Indonesia      126.0
Italy           15.3
UK              29.0
Netherlands     17.2
dtype: float64

# Pass in key and get value
pop_dict["Singapore"] 

5.7

pop_series["Singapore"]

5.7

# Dataframes - 2d data structure
data = {'country': ['Singapore', 'France', 'Germany'],
        'population': [5.5, 64, 82],
        'area': [31000, 67200, 360000],
        'capital': ['Singapore', 'Paris', 'Berlin']
       }
#convert into a dataframe
countries = pd.DataFrame(data)
countries

    country	population     area      capital
0	Singapore 5.5	      31000	 Singapore
1	France	64.0	       67200	  Paris
2	Germany	82.0	      360000	  Berlin

# Set inplace do not need to reassign
countries.set_index('country', inplace=True) 
countries

        population      area	capital
country			
Singapore 5.5	       31000	Singapore
France	64.0	        67200	 Paris
Germany	82.0	      360000	 Berlin

# What is this data structure?
countries['area']

country
Singapore     31000
France        67200
Germany      360000
Name: area, dtype: int64

# Can perform operations on series and dataframes
#e.g from a country perspective, find population density of every country in dataframe
countries['population'] / countries['area']

country
Singapore    0.000177
France       0.000952
Germany      0.000228
dtype: float64

#-----------Index and slice-----------
# Indexing and slicing data
# Indexing: access different parts of data using rows and columns index
# Slicing: extract a subset of data using index of rows and columns

# Reset index column with one of the column
healthy_fruits = healthy_fruits.set_index('Colour')
healthy_fruits

# Display index column with another selected column
healthy_fruits['Cost']

# Change index and set to columnname
df = df.set_index('columnname')
df

# Slice rows
df['columnname2': 'columnname4']

#-----------Minimum and maximum----------
# Find selected column minimum 
healthy_fruits['Cost'].min()

# Find selected column minimum 
healthy_fruits['Cost'].max()

#----------Mean, median and mode----------
# Find mean(average) of a column
mean_columnname = d['columnname'].mean()

# Find median(middle) of a column
d['columnname'].median()

# Find mode(most frequent) of a column
d['columnname'].mode()

# Find mean
mean_rbp = df.RestBP.dropna().mean()

# Find population proportion of the people who have the higher RestBP than the mean RestBP
len(df[df["RestBP"] > mean_rbp])/len(df)

#---------- Sort----------
# Sort values from min to max
healthy_fruits.sort_values('Cost')

# Can perform sorting in countries dataframe based on a certain column
countries.sort_values('area', ascending=False)

      population area	capital
country			
Germany	82.0	360000	Berlin
France	64.0	67200	Paris
Singapore	5.5	31000	Singapore

# Sort rows descendingly by index
df.sort_index(axis=0, ascending=False)
#sort rows ascendingly by index
df.sort_index(axis=0, ascending=True)

#-----------Filter-----------
# Filtering with query method
df.query('Country == "US"') # only display US

#----------Count----------
# Count the value of each category
df = df.categorycolumn.value_counts()
df

# Find population proportion
# Count the value of each category divide each of them with the total population
df / df.sum()
# If contains missing 
df["categorycolumn"] = df.categorycolumn.fillna("Missing")
df = df.categorycolumn.value_counts()
df / df.sum()

#----------loc and iloc----------
# Select a single row and column
df.loc['index_row', 'column_name']

# Select multiple rows and columns
df.loc['index_row1':'index_row2', ['column_name1','column_name2']]

# Access areas and populations of Singapore and France
# loc => (rows locations, column locations)
# Rows first then columns [start:stop]
countries.loc['Singapore':'France', 'population':'area']

        population       area
country		
Singapore	5.5	31000
France	      64.0	67200

# Access capital and populations of Singapore and Germany
countries.loc[['Singapore', 'Germany'],['population','capital']]

        population	capital
country		
Singapore	5.5	Singapore
Germany	     82.0	  Berlin

# Describe is a function
countries.loc[:,['population','capital']].describe()

       population
count	3.000000
mean	50.500000
std	39.996875
min	5.500000
25%	34.750000
50%	64.000000
75%	73.000000
max	82.000000

countriesrows = ['Singapore', 'Germany']
cols = ['population','capital']

countries.loc[countriesrows, cols]

      population  capital
country		
Singapore 5.5	Singapore
Germany	82.0	         Berlin

# Update a single element in dataframe using loc
countries.loc['Singapore', 'population']= 5.9
countries

      population area	capital
country			
Singapore	5.9	31000	Singapore
France	64.0	67200	Paris
Germany	82.0	360000	Berlin

# Update a single element in dataframe using iloc
countryi.iloc[0,1] = 6
countryi

country	population	area	capital
0	Singapore	6.0	31000	Singapore
1	France	64.0	67200	Paris
2	Germany	82.0	360000	Berlin

#----------Box plots----------
# Plot the Cholesterol data against the age group
# observe the difference in cholesterol levels in different age groups of people
# Make a new column in the dataset that will return the number of people in the different age groups
df["agegrp"]=pd.cut(df.Age, [29,40,50,60,70,80])
plt.figure(figsize=(12,5))
sns.boxplot(x = "agegrp", y = "Chol", data=df)
data"
titanic_data = pd.read_csv(url)
titanic_data.info()

#----------Based on conditions----------
# Select rows based on conditions
countries['columnname'] > 100000

# Subset data only area above 100000 will appear
countries[countries['area'] > 100000]

     population	area	capital
country			
Germany	82.0	360000	Berlin

#-----------Density----------
# Create a new column for population density = population / area
# Data preparation generating new column
countries['popDensity'] = countries['population'] / countries['area']
countries

population	area	capital	popDensity
country				
Singapore	5.9	31000	Singapore	0.000190
France	64.0	67200	Paris	0.000952
Germany	82.0	360000	Berlin	0.000228

#----------Add columns----------
# Select a single column
df.col1
df.['columnname']

# Select multiple columns
df[['columnname1', 'columnname2']]

# Add extra columns
countries['popD'] = 0
countries

        population area	  capital      popDensity     popD
country					
Singapore 5.9	   3100   Singapore	0.000190	0
France	64.0	   67200   Paris	0.000952	0
Germany	82.0	   360000  Berlin	0.000228	0

#----------Drop columns----------
countries.drop('popD', axis=1, inplace=True)
countries

      population area	capital	    popDensity
country				
Singapore 5.9	31000	Singapore   0.000190
France	64.0	67200	Paris	    0.000952
Germany	82.0	360000	Berlin	    0.000228

#----------Rename columns----------
# Rename column, look for population and change to pop
countries = countries.rename(columns={'population':'pop'})
countries

	    pop	  area	  capital	popDensity
country				
Singapore  5.9	31000	Singapore	0.000190
France	   64.0	67200	Paris	        0.000952
Germany	   82.0	360000	Berlin	        0.000228

#----------Grouping----------
# Grouping of data
data = {
    'key': ['A','B','C','A','B','C','A','B','C'],
    'value': [0,5,10,5,10,15,10,15,20]
}
df = pd.DataFrame(data)
df

	key	value
0	A	0
1	B	5
2	C	10
3	A	5
4	B	10
5	C	15
6	A	10
7	B	15
8	C	20

# Groupby sum
df.groupby('columnname').sum()
# Groupby - values of data based on a unique "key"
grp = df.groupby("key").sum()
grp

	value
key	
A	15
B	30
C	45

# Find average age for each sex
df.groupby('sex')['age'].mean()

sex
female    27.915709
male      30.726645
Name: age, dtype: float64

#-----------Type----------
# Find type 
type(agemean)

pandas.core.series.Series

#----------Average---------
# Find average survival passengers
df['survived'].sum() / len(df['survived'])

#-----------Convert words to numbers---------
from word2number import w2n
#convert words to numbers
df1.experience = df1.experience.apply(w2n.word_to_num)
df1