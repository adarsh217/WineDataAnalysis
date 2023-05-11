import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('winereviews.csv')
# Perform EDA here...
print(data.shape)  # will print the number of rows and columns
print(data.info())  # will print the column names and its datatypes, along with non-null counts
print(data.describe())  # will print the statistical summary for numerical columns
print(data.head())  # will print the first 5 rows of the dataset
print(data.isnull().sum())  # will print the count of null values in each column

sns.histplot(data['points'])
plt.show()

sns.histplot(data['price'])
plt.show()

print(data['country'].value_counts())
print(data['province'].value_counts())
print(data['variety'].value_counts())

# Add a new column for review length
data['review_length'] = data['review_description'].apply(len)