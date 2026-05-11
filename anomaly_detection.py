import zipfile
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.ensemble import IsolationForest
import os

# Path to the zip file
zip_path = r"c:\Users\ADMIN\Downloads\financial_anomaly_data.csv.zip"
extract_path = r"c:\Users\ADMIN\Documents\KHDL&AI TH5"

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Assuming the CSV file is named 'financial_anomaly_data.csv'
csv_path = os.path.join(extract_path, 'financial_anomaly_data.csv')

# Load the data
df = pd.read_csv(csv_path)

# Print column names to verify
print("Columns in the dataset:")
print(df.columns.tolist())

# Assume columns: 'Amount' for amount, 'AccountID' for account
amount_col = 'Amount'
account_col = 'AccountID'

# Preprocessing for amount: Log scaling + Min-Max normalization
df['amount_log'] = np.log1p(df[amount_col])  # log1p to handle zero values
scaler = MinMaxScaler()
df['amount_scaled'] = scaler.fit_transform(df[['amount_log']])

# Preprocessing for account: One-Hot Encoding
encoder = OneHotEncoder(sparse_output=False)
encoded_accounts = encoder.fit_transform(df[[account_col]])
encoded_df = pd.DataFrame(encoded_accounts, columns=encoder.get_feature_names_out([account_col]))

# Combine features
features = pd.concat([df[['amount_scaled']], encoded_df], axis=1)

# Isolation Forest with contamination=0.01
iso_forest = IsolationForest(contamination=0.01, random_state=42)
df['anomaly_score'] = iso_forest.fit_predict(features)
df['anomaly'] = df['anomaly_score'] == -1  # -1 indicates anomaly

# Filter anomalies
anomalies = df[df['anomaly']]

# Save results
output_path = os.path.join(extract_path, 'anomalies_detected.csv')
anomalies.to_csv(output_path, index=False)

print(f"Anomalies detected and saved to {output_path}")
print(f"Number of anomalies: {len(anomalies)}")