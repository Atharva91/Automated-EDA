
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the dataset
data = pd.read_csv("datasets/cars.csv")

# print the columns of the dataset
print(data.columns)

# plot the heatmap for all the columns in the dataset
plt.figure(figsize=(20,10))
sns.heatmap(data.corr(),annot=True)
plt.show()


# find the column having second highest correlation with price  
print(data.corr()['price'].sort_values(ascending=False)[1])