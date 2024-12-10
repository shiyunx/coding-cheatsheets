#----------Notes---------
# Import libraries
import pandas as pd
import numpy as np

#----------Display maximum columns----------
pd.set_option("display.max_columns", None)
df.head() 

#----------Dataframe with null values---------
df = pd.DataFrame([[1,np.nan,2],
                  [2,3,5],
                  [np.nan,4,6]])
df

    0	1   2
0	1.0	NaN	2
1	2.0	3.0	5
2	NaN	4.0	6

#----------1d and 2d---------
# 1d check null values
data = pd.Series([1, np.nan, 'hello', None])
data.isnull()

# 2d
df = pd.DataFrame([[1, np.nan, 2],[2, 3, 5],[np.nan, 4, 6]])
df

#---------Pandas series null values-----------
# Create pandas series with null values
data = pd.Series([1, np.nan, 'hello', None]) #np.nan and None represent null in data
data

0        1
1      NaN
2    hello
3     None

#----------Boolean series null values---------
# Create boolean series True for NaN values
data.isnull()

0    False
1     True
2    False
3     True

# Create boolean series False for NaN values
data.notnull()

0     True
1    False
2     True
3    False

# ---------Check number of rows where particular columns of null values--------
# Explain: rows of column contains NaNs
data.isnull().sum()

# Check null values
data[data.isnull()]

# Check non null values
data[data.notnull()]

#----------Filter----------
# Filter data
data[data.isnull()] #isnull is a function that detects null

1     NaN
3    None

#----------Extract----------
# Extract those which are not null
data[data.notnull()]

0        1
2    hello

# Find the sum 
df["column names"].value_counts()

1 100
0 10
# Extract 0 or 1 
df[df["column names"] ==0]

#----------Drop----------
# Drop NaN values and set fix the data
data.dropna(inplace=True)
data

0        1
2    hello

# Drop only drop full rows or columns of null values
# Drop and do not save if enter data(df) will appear nans again or can assign another df name
data.dropna()

# Drop and save 
data.dropna(inplace=True)

# If want to drop rows with all nans only
data.dropna(how='all')

# If want to drop only one column[0] nans values 
data.dropna(subset=[0])

# Drop selected columns
data.drop(columns=['column1', 'column2'])

# Drop columns null values
df.dropna(axis='columns')

# Example: if have at least one non NaN value then keep it
new_df = df.dropna(thresh=1)
new_df

# Drop unnecassary columns
df1 = df.drop(['columnname1','columnname2'], axis='columns')
df1.head()

# Drop columns and save
drpcols = ['LAW_CODE', 'ARREST_BORO']
df.drop(columns=drpcols, inplace=True)
df

#----------Replace---------
# 3 methods to replace null values
ndata = pd.Series([np.nan, np.nan, 3, None, 2])
ndata

0    NaN
1    NaN
2    3.0
3    NaN
4    2.0

# Method 1 : fill using specific number
# Consider using 0 or something more meaningful (i.e mean/average)
nmean = ndata.mean()
# Fill in with mean
ndata.fillna(nmean)

0    2.5
1    2.5
2    3.0
3    2.5
4    2.0

# Fill in with 0
ndata.fillna(0)

0    0.0
1    0.0
2    3.0
3    0.0
4    2.0

# Method 2: forward
ndata.fillna(method='ffill')

0    NaN
1    NaN
2    3.0
3    3.0
4    2.0

# Method 3: backfill
ndata.fillna(method='bfill')

0    3.0
1    3.0
2    3.0
3    2.0
4    2.0

# Drop rows with NaN using dropna
df.dropna()

    0	1   2
1	2.0	3.0	5

# Drop columns using dropna
df.dropna(axis=1)

	2
0	2
1	5
2	6

# Method 1: fill with something mean, 0
df.fillna(0)

    0	1   2
0	1.0	0.0	2
1	2.0	3.0	5
2	0.0	4.0	6

# Method 2: forward with rows
df.fillna(method='ffill')

    0	1	2
0	1.0	NaN	2
1	2.0	3.0	5
2	2.0	4.0	6

# Method 2: forward with columns
df.fillna(method='ffill', axis=1)

    0	1	2
0	1.0	1.0	2.0
1	2.0	3.0	5.0
2	NaN	4.0	6.0

# Method 3: backward with rows
df.fillna(method='bfill')

    0	1   2
0	1.0	3.0	2
1	2.0	3.0	5
2	NaN	4.0	6

# Method 3: backward with columns
df.fillna(method='bfill', axis=1)

    0	1	2
0	1.0	2.0	2.0
1	2.0	3.0	5.0
2	4.0	4.0	6.0

# Fill null values and replace with 0
data.fillna(0)

# Fill different values for different columns
new_df = df.fillna({
    'columnname1':0,
    'columnname2':0,
    'columnname3': 'no data given'
})
new_df

# Forward fill null values
data.fillna(method='ffill')
# Axis=0 example
import pandas as pd
df = pd.DataFrame([[1, np.nan, 2],[2, 3, 5],[np.nan, 4, 6]])
df.fillna(method='ffill', axis=0)
# Axis=1 example
import pandas as pd
df = pd.DataFrame([[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]])
df.fillna(method='ffill', axis=1)

# Backward fill null values
data.fillna(method='bfill')

#---------Check for unique names---------
# Example: 4 Bedroom same as 4 BHK
dfnew['columnname'].unique()

#---------Groupby---------
# Count and print each area type
df.groupby('area_type')['area_type'].agg('count')

#----------Index---------
# Set column as index
df.set_index('area_type',inplace=True)
df

#-----------Add new column----------
# Create a new column and call it "JAIL_TIME"
# Creating columns has another name called Feature Engineering
df["JAIL_TIME"] = np.where(df['LAW_CAT_CD']=='F',36,
                           np.where(df['LAW_CAT_CD']=='M', 12, 1))

#----------Data cleaning----------
# isnull(): Generate a boolean mask indicating missing values
# notnull(): Opposite of isnull()
# dropna(): Return a filtered version of the data
# fillna(): Return a copy of the data with missing values filled or imputed

df.columns = ['a','b','c'] # Renames columns
pd.isnull() # Checks for null Values, Returns Boolean Array
pd.notnull() # Opposite of s.isnull()
df.dropna() # Drops all rows that contain null values
df.dropna(axis=1) # Drops all columns that contain null values
df.dropna(axis=1,thresh=n) # Drops all rows have have less than n non null values
df.fillna(x) # Replaces all null values with x
s.fillna(s.mean()) # Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section)
s.astype(float) # Converts the datatype of the series to float
s.replace(1,'one') # Replaces all values equal to 1 with 'one'
s.replace([1,3],['one','three']) # Replaces all 1 with 'one' and 3 with 'three'
df.rename(columns=lambda x: x + 1) # Mass renaming of columns
df.rename(columns={'old_name': 'new_ name'}) # Selective renaming
df.set_index('column_one') # Changes the index
df.rename(index=lambda x: x + 1) # Mass renaming of index

# Check duplicates
df.duplicated()

# Check sample rows 
df.sample(a)

# Check percentage of missing values
for col in df.columns:
    percentage_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(percentage_missing*100)))

# Check number of missing data per column
sum_percolumn_missingnan = df.isnull().sum()

# Print number of missing data in the total columns
sum_percolumn_missingnan[0:total columns]

# Number of total missing values
total_cells = np.product(df.shape)
total_missing = sum_percolumn_missingnan.sum()

# Percentage of missing data
(total_missing/total_cells) * 100

# Replace all null values (NaN) with 0
df.fillna(0)

# Replace all null values (NaN) with ""
df['column name']= df['column name'].fillna("")

# Replace 0 or other values with (NaN)
new_df = df.replace([0], np.NaN)
df

# Replace 0 or other values with (NaN) using dictionary method
new_df = df.replace([{
    'name of column1': value1 to replace from,
    'name of column2': value2 to replace from,
    'name of column3': value3 to replace from
},np.NaN)
new_df

# Replace 0 or other values with (NaN) using dictionary method
new_df = df.replace([{
    value to replace: np.NaN,
    'column variable name to replace': 'new column variable name'
})
new_df

# Display unique values
df.unique
# display data individual column
df['gender'].unique()

# Drop irrelevant columns
df = df.drop(['column name1', 'column name2'], axis=1)

# Fill NaN with median
df.column.median()
df.column = df.column.fillna(df.column.median())
df