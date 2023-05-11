# Wine Data Analysis using Machine Learning

## Insights from the data analysis
### Insight 1: Correlation between price and points

To analyze the correlation between price and points, you can use the following code snippet:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('your_file.csv')

sns.scatterplot(data=data, x='price', y='points')
plt.xlabel('Price')
plt.ylabel('Points')
plt.title('Price vs Points')
plt.show()
```

### Insight 2: Top wine-producing countries

To visualize the top wine-producing countries, use the following code snippet:

```python
country_counts = data['country'].value_counts().head(10)
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.xlabel('Country')
plt.ylabel('Number of Wines')
plt.title('Top Wine-Producing Countries')
plt.xticks(rotation=45)
plt.show()
```

### Insight 3: Top-rated varieties

To find the top-rated wine varieties, use the following code snippet:

```python
grouped_variety = data.groupby('variety')['points'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=grouped_variety.index, y=grouped_variety.values)
plt.xlabel('Variety')
plt.ylabel('Average Points')
plt.title('Top-rated Wine Varieties')
plt.xticks(rotation=45)
plt.show()
```

### Insight 4: Relationship between region and points

To explore the relationship between region and points, use the following code snippet:

```python
grouped_region = data.groupby('region_1')['points'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=grouped_region.index, y=grouped_region.values)
plt.xlabel('Region')
plt.ylabel('Average Points')
plt.title('Top-rated Wine Regions')
plt.xticks(rotation=45)
plt.show()
```

### Insight 5: Impact of winery on wine quality

To analyze the impact of winery on wine quality, use the following code snippet:

```python
grouped_winery = data.groupby('winery')['points'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=grouped_winery.index, y=grouped_winery.values)
plt.xlabel('Winery')
plt.ylabel('Average Points')
plt.title('Top-rated Wineries')
plt.xticks(rotation=45)
plt.show()
```
