import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the anomalies data
data_path = r"c:\Users\ADMIN\Documents\KHDL&AI TH5\anomalies_detected.csv"
df = pd.read_csv(data_path)

# Set up the plotting style
sns.set(style="whitegrid")

# 1. Histogram of Amount for anomalies
plt.figure(figsize=(10, 6))
sns.histplot(df['Amount'], bins=50, kde=True, color='red')
plt.title('Distribution of Transaction Amounts for Detected Anomalies')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.savefig(os.path.join(os.path.dirname(data_path), 'amount_histogram.png'))
plt.close()

# 2. Bar chart of anomalies by TransactionType
plt.figure(figsize=(10, 6))
transaction_counts = df['TransactionType'].value_counts()
sns.barplot(x=transaction_counts.index, y=transaction_counts.values, palette='viridis')
plt.title('Number of Anomalies by Transaction Type')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig(os.path.join(os.path.dirname(data_path), 'transaction_type_bar.png'))
plt.close()

# 3. Scatter plot of amount_scaled vs anomaly_score
plt.figure(figsize=(10, 6))
sns.scatterplot(x='amount_scaled', y='anomaly_score', data=df, hue='anomaly', palette='coolwarm')
plt.title('Anomaly Score vs Scaled Amount')
plt.xlabel('Scaled Amount')
plt.ylabel('Anomaly Score')
plt.savefig(os.path.join(os.path.dirname(data_path), 'anomaly_scatter.png'))
plt.close()

print("Plots saved successfully!")