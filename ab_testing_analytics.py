import pandas as pd

# Load the dataset
df = pd.read_csv('marketing_campaign_extended.csv')

# Take a look at the first few rows of the dataset
print(df.head())

# Check basic info, such as data types and missing values
print(df.info())

# Check summary statistics
print(df.describe())

# Calculate the conversion rate for each campaign
conversion_rate = df.groupby('Campaign')['Converted'].mean() * 100

print("Conversion Rates (%):")
print(conversion_rate)

import matplotlib.pyplot as plt

# Plotting the conversion rate for each campaign
plt.figure(figsize=(8, 5))
conversion_rate.plot(kind='bar', color=['blue', 'green'])
plt.title('Conversion Rate by Campaign')
plt.xlabel('Campaign')
plt.ylabel('Conversion Rate (%)')
plt.xticks(rotation=0)
plt.show()

from scipy.stats import ttest_ind

# Split the dataset into Campaign A and B
campaign_a = df[df['Campaign'] == 'A']['Converted']
campaign_b = df[df['Campaign'] == 'B']['Converted']

# Perform an independent t-test
t_stat, p_value = ttest_ind(campaign_a, campaign_b)

print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("The difference between Campaign A and B is statistically significant.")
else:
    print("No statistically significant difference found between Campaign A and B.")

# Calculate the click-through rate for each campaign
click_rate = df.groupby('Campaign')['Clicks'].mean() / df.groupby('Campaign')['Impressions'].mean() * 100

print("Click-Through Rate (%):")
print(click_rate)

# Visualize CTR
plt.figure(figsize=(8, 5))
click_rate.plot(kind='bar', color=['orange', 'purple'])
plt.title('Click-Through Rate by Campaign')
plt.xlabel('Campaign')
plt.ylabel('Click-Through Rate (%)')
plt.xticks(rotation=0)
#plt.show()

# Average customer spending per campaign
average_spending = df.groupby('Campaign')['Customer_Spend'].mean()

print("Average Customer Spending per Campaign:")
print(average_spending)

# Visualize average customer spending
plt.figure(figsize=(8, 5))
average_spending.plot(kind='bar', color=['red', 'yellow'])
plt.title('Average Customer Spending by Campaign')
plt.xlabel('Campaign')
plt.ylabel('Average Spending (USD)')
plt.xticks(rotation=0)
plt.show()
