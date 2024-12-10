#----------Notes-----------
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
# Draw plot and present chart in cell
%matplotlib inline

#----------Kmeans----------
from sklearn import datasets
from sklearn.cluster import KMeans
# Load data
myData = datasets.load_iris()
myData_df = pd.DataFrame(myData.data, columns = myData.feature_names)
myData_df.head(10)
# Find clusters mean
# Use kmeans
# Obtain the most optimal number of clusters
wcss = []
for i in range(1,21):
    kmeans = KMeans(n_clusters = i) 
    kmeans.fit(myData_df) 
    wcss.append(kmeans.inertia_) #every thing will store here
plt.plot(range(1,21),wcss)
plt.title("The elbow plot to determine k")
plt.xlabel("Number of clusters(k)")
plt.ylabel("WCSS")
plt.xticks(range(1,21))
plt.show() #increase number of clusters, it decrease
# Elbow chart above
# Plot the elbow chart to identify the best number of clusters: k=3
# Build clusters
kmeans = KMeans(n_clusters= 3)
kmeans_fmodel = kmeans.fit(myData_df) #fit and want to know which data fit into the clusters
y_kmeans = kmeans_fmodel.predict(myData_df)
myData_df['Cluster'] = y_kmeans
myData_df.head(10)
myData_df['Cluster']
# Find centroids, 3 clusters so 3 centroids (number of centroid = number of cluster)
# Identify the cluster centers
kmeans_fmodel.cluster_centers_
# Take one point in space will have 4 values
# Multiple dimensions so have mulitple values above
x = myData_df.iloc[:,[0,1,2,3]].values
plt.figure(figsize=(15,6))
plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=80,c='red',label='Cluster 0')
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=80,c='blue',label='Cluster 1')
plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=80,c='green',label='Cluster 2')
plt.scatter(kmeans_fmodel.cluster_centers_[:,0],
            kmeans_fmodel.cluster_centers_[:,1],s=100,
            c = 'yellow', label='Centroids')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.legend()
plt.show()

#-----------Linear regression----------
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Load data
url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
s_data.head(10)
plt.scatter(x="Hours",y="Scores",data=s_data)
plt.title("Hours vs Scores")
plt.xlabel("Hours studied")
plt.ylabel("Scores")
plt.show()
# iloc[rows,columns]
x = s_data.iloc[:,0].values.reshape(-1,1)
y = s_data.iloc[:,1].values
# Split data into 4 categories
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=False)
# Define linear regression
# Create linear regression object
regressor = LinearRegression()
# Fit data and train model
regressor.fit(x_train,y_train)
# Visualise model train
line = regressor.coef_ * x + regressor.intercept_
plt.scatter(x="Hours",y="Scores",data=s_data)
plt.plot(x, line)
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("Linear Regression Model - Hours vs Scores")
plt.show()
# 2 data, splitted into test and train
# Build using training data
# x_test compare with y_test
# Call predict method on actual test data set
y_pred = regressor.predict(x_test)
# Check y prediction closer to actual values y_test
y_pred
# regressor.predict(x_test)
# Check accuracy of model by calling score method
regressor.score(x_test,y_test)
# Accuracy is 93%
# Compare
#{"given new column name: "}
compare_df = pd.DataFrame({"Actual Output": y_test, "Pred Output":y_pred})
compare_df
# Tells how close a regression line is to a set of points. It does this by taking the distances from the points to the regression line (these distances are the “errors”) and squaring them.
# Bigger difference higher square
print("Mean square error = ", metrics.mean_absolute_error(y_test,y_pred))
own_pred = regressor.predict([[10.23]])
own_pred
- input hours, output scores

#----------Logestic regression-----------
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Load data
url = "http://bit.ly/wkspdata"
df = pd.read_csv(url)
df.tail(10)
df.columns
- what features can be used in prediction
def cleanData(df):    
    df = df.drop(["name","cabin","ticket"],axis = 1)    
    df = df.dropna()    
    cat_feat = ["embarked","sex"]    
    df = pd.get_dummies(df,columns=cat_feat )    
    return df
#df = cleanData(df)
#df.tail(10)
df = cleanData(df)
df.tail(10)
# Evaluation metrics
# Confusion matrix
X = df.iloc[:,1:].values #inputs, [rows,columns]
y = df.iloc[:,0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
log_reg = LogisticRegression(max_iter= 1000) #create logistic regression object
log_reg.fit(X_train,y_train)
y_pred = log_reg.predict(X_test)
test_acc = metrics.accuracy_score(y_test,y_pred)
print("accuracy", test_acc)
conf_mat = metrics.confusion_matrix(y_test,y_pred)
import seaborn as sns
sns.heatmap(conf_mat.T,annot=True)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
test_pre = metrics.precision_score(y_test,y_pred)
print("Testing precision= ",test_pre)
test_rec = metrics.recall_score(y_test,y_pred)
print("Testing recall= ",test_rec)
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Step1: load data
from sklearn import datasets
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names) #inputs(4 input columns)
iris_target = iris.target
# Train - Test - Split
X_train, X_test, y_train, y_test = train_test_split(iris_df, iris_target, test_size=0.2)
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
test_acc = metrics.accuracy_score(y_test, y_pred)
print("Testing Accuracy = ", test_acc)
# Confusion Matrix
conf_mat = metrics.confusion_matrix(y_test, y_pred)
import seaborn as sns 
# Visualization library
sns.heatmap(conf_mat.T, annot=True) #annot=True is used to show the numbers in the confusion matrix
plt.xlabel("Actuals")
plt.ylabel("Predicted")
plt.show()
# Precision
test_pre = metrics.precision_score(y_test, y_pred, average=None)
print("Testing Precision = ", test_pre)
# Recall 
test_rec = metrics.recall_score(y_test, y_pred, average=None)
print("Testing Recall = ", test_rec)

#-----------Multiple regression----------
from sklearn.linear_model import LinearRegression
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Load data
url = "http://bit.ly/316tYZT"
df = pd.read_csv(url)
df.head()
df.columns
# Define function
# X,y input,split data, model, fit, predict
# X all input data with final label
# Use X, y as input and test_size as ratio of spliting > will get 4 parameters back
def split_and_train(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X,y,
                                test_size=0.2, shuffle=False)
    lr_model = LinearRegression() #create linear regression object
    lr_model.fit(X_train,y_train) #fit to train model
    
    y_pred = lr_model.predict(X_test) #predict data
    print("Mean square error",metrics.mean_absolute_error #find Mse of (predicted output,actual output)
          (y_pred,y_test))
    
    return lr_model #return train model
# Remove column
X = df.drop('SalePrice',axis=1)
y = df['SalePrice']
X
y
# Call function of def split_and_train(X,y):
lr_baseline_model = split_and_train(X,y) #passing X,y
# Define new dataframe
df_new = df[['Lot Area','Year Built','Gr Liv Area', 'SalePrice']]
df_new
# Remove column
X = df_new.drop('SalePrice',axis=1)
y = df_new['SalePrice']
X
y
# Smaller the means squared error, the closer you are to finding the line of best fit. 
split_and_train(X,y) #passing X,y
df_new = df[['Lot Area','Year Built','Gr Liv Area', 'SalePrice']]
df_new.head(2)
#remove column
L = df_new.drop('SalePrice', axis=1)
M = df_new['SalePrice']
# Call function
split_and_train(L,M)
# Create a new column
df_combine = df.copy()
df_combine['overall_Score'] = df['Overall Qual']*df['Overall Cond']
df_combine
# Remove column
x_a = df_combine.drop('SalePrice',axis=1)
y_b = df_combine['SalePrice']
x_a
y_b
# Call function
split_and_train(x_a,y_b)
# Define function
def change_categorical(x):
    if x>5:
        return 1
    else:
        return 0
df_combine = df.copy()
df_combine['overall_Score'] = df['Overall Qual']*df['Overall Cond']
df_combine['high_score'] = df['Overall Qual'].apply(lambda x:change_categorical(x)) #Applying lambda function to find change_categorical(x) using df['Overall Qual']
df_combine

#----------SVM----------
from sklearn.model_selection import train_test_split
from sklearn import metrics
#Q1
# Load data
from sklearn import datasets
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names) #inputs(4 input columns)
iris_target = iris.target
# Train - Test - Split
X_train, X_test, y_train, y_test = train_test_split(iris_df, iris_target, test_size=0.2)
from sklearn import svm
svm_classifier = svm.SVC() #model svc
svm_classifier.fit(X_train, y_train) #fit it
y_pred = svm_classifier.predict(X_test)
test_acc = metrics.accuracy7_score(y_test, y_pred)
print("Testing Accuracy = ", test_acc)
# Confusion Matrix
conf_mat = metrics.confusion_matrix(y_test, y_pred)
import seaborn as sns 
# Visualization library
sns.heatmap(conf_mat.T, annot=True) #annot=True is used to show the numbers in the confusion matrix
plt.xlabel("Actuals")
plt.ylabel("Predicted")
plt.show()
# Precision
test_pre = metrics.precision_score(y_test, y_pred, average=None)
print("Testing Precision = ", test_pre)
# Recall 
test_rec = metrics.recall_score(y_test, y_pred, average=None)
print("Testing Recall = ", test_rec)
test_pre = metrics.precision_score(y_test, y_pred, average=None)
print("Testing Precision = ", test_pre)
test_rec = metrics.recall_score(y_test, y_pred, average=None)
print("Testing Precision = ", test_rec)
#Q2
# Predict digits 
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm
from sklearn import datasets
# Load the digits dataset
digits = datasets.load_digits()
# Pixel values
digits
# Plot the data
for i in range(0,25):
    plt.subplot(5,5,i+1)
    plt.axis('off')
    im = np.reshape(digits.data[i],(8,8)) 
    plt.imshow(im) 
plt.show()
# Split data images
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.2)
# Create a support vector classifier
svm_dig_classifier = svm.SVC(gamma=0.0001) # Fit to the training data
svm_dig_classifier.fit(X_train,y_train)
y_pred = svm_dig_classifier.predict(X_test)
test_acc = metrics.accuracy_score(y_test, y_pred)
print("Testing Accuracy = ", test_acc)
# Confusion Matrix
conf_mat = metrics.confusion_matrix(y_test, y_pred)
import seaborn as sns 
# Visualization library
sns.heatmap(conf_mat.T, annot=True) #annot=True is used to show the numbers in the confusion matrix
plt.xlabel("Actuals")
plt.ylabel("Predicted")
plt.show()