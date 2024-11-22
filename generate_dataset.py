import pandas as pd
import numpy as np

# Generating a sample dataset with missing columns added
np.random.seed(42)

# Creating the dataset
data = {
    'Campaign': np.random.choice(['A', 'B'], size=500),
    'Date': pd.date_range(start='2024-01-01', periods=500, freq='D'),
    'Customer_ID': np.arange(1, 501),
    'Customer_Spend': np.random.uniform(10, 500, size=500).round(2),
    'Converted': np.random.choice([0, 1], size=500, p=[0.7, 0.3]),
    'Clicks': np.random.randint(10, 1000, size=500),
    'Impressions': np.random.randint(500, 5000, size=500)
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Saving to CSV
df.to_csv('marketing_campaign_extended.csv', index=False)
