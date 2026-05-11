import pandas as pd
import os

# Load the anomalies data
anomalies_path = r"c:\Users\ADMIN\Documents\KHDL&AI TH5\anomalies_detected.csv"
df_anomalies = pd.read_csv(anomalies_path)

# Load the original data for comparison
original_path = r"c:\Users\ADMIN\Documents\KHDL&AI TH5\financial_anomaly_data.csv"
df_original = pd.read_csv(original_path)

# Basic statistics for anomalies
print("=== THỐNG KÊ GIAO DỊCH BẤT THƯỜNG ===")
print(f"Tổng số giao dịch bất thường: {len(df_anomalies)}")
print(f"Tỷ lệ bất thường: {len(df_anomalies) / len(df_original) * 100:.2f}%")

print("\n=== THỐNG KÊ SỐ TIỀN (Amount) CHO BẤT THƯỜNG ===")
amount_stats = df_anomalies['Amount'].describe()
print(amount_stats)

print("\n=== SO SÁNH VỚI TOÀN BỘ DATASET ===")
print("Toàn bộ dataset:")
print(df_original['Amount'].describe())
print("\nBất thường:")
print(amount_stats)

print("\n=== PHÂN TÍCH THEO LOẠI GIAO DỊCH (TransactionType) ===")
transaction_stats = df_anomalies.groupby('TransactionType')['Amount'].agg(['count', 'mean', 'min', 'max', 'std'])
print(transaction_stats)

print("\n=== PHÂN TÍCH THEO ĐỊA ĐIỂM (Location) ===")
location_stats = df_anomalies.groupby('Location')['Amount'].agg(['count', 'mean', 'min', 'max', 'std'])
print(location_stats)

print("\n=== PHÂN TÍCH THEO MERCHANT ===")
merchant_stats = df_anomalies.groupby('Merchant')['Amount'].agg(['count', 'mean', 'min', 'max', 'std'])
print(merchant_stats)

# Save detailed stats to CSV
stats_output = os.path.join(os.path.dirname(anomalies_path), 'anomaly_statistics.txt')
with open(stats_output, 'w', encoding='utf-8') as f:
    f.write("=== THỐNG KÊ GIAO DỊCH BẤT THƯỜNG ===\n")
    f.write(f"Tổng số giao dịch bất thường: {len(df_anomalies)}\n")
    f.write(f"Tỷ lệ bất thường: {len(df_anomalies) / len(df_original) * 100:.2f}%\n\n")
    f.write("=== THỐNG KÊ SỐ TIỀN (Amount) CHO BẤT THƯỜNG ===\n")
    f.write(amount_stats.to_string() + "\n\n")
    f.write("=== SO SÁNH VỚI TOÀN BỘ DATASET ===\n")
    f.write("Toàn bộ dataset:\n")
    f.write(df_original['Amount'].describe().to_string() + "\n\n")
    f.write("Bất thường:\n")
    f.write(amount_stats.to_string() + "\n\n")
    f.write("=== PHÂN TÍCH THEO LOẠI GIAO DỊCH (TransactionType) ===\n")
    f.write(transaction_stats.to_string() + "\n\n")
    f.write("=== PHÂN TÍCH THEO ĐỊA ĐIỂM (Location) ===\n")
    f.write(location_stats.to_string() + "\n\n")
    f.write("=== PHÂN TÍCH THEO MERCHANT ===\n")
    f.write(merchant_stats.to_string() + "\n")

print(f"\nThống kê chi tiết đã lưu vào: {stats_output}")