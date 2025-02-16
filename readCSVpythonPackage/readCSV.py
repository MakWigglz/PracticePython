import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file
data = pd.read_csv('data.csv')

# display the summary statistics of the dataframe.
summary = data.describe()
print(summary)

# Plot histograms for 'Product Name', 'Quantity sold', and 'total revenue'
fig, axes = plt.subplots(3,1, figsize=(9,10))

data['Product Name'].value_counts().plot(kind='bar', ax=axes[0], title='Product Name Disribution')
axes[0].set_xlabel('Product Name')
axes[0].set_ylabel('Frequency')

data['Quantity Sold'].plot(kind='hist', ax=axes[1], title='Quantity Sold Distribution')
axes[1].set_xlabel('Quantity Sold')
axes[1].set_ylabel('Frequency')

data['Total Revenue (USD)'].plot(kind='hist', ax=axes[2], title='Total Revenue Distribution')
axes[2].set_xlabel('Total Revenue (USD)')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
