def tinh_giai_thua(n):
    if n < 0:
        return "Không tính được giai thừa cho số âm"
    elif n == 0 or n == 1:
        return 1
    else:
        giai_thua = 1
        for i in range(2, n + 1):
            giai_thua *= i
        return giai_thua

# Kiểm tra
n = int(input("Nhập số nguyên dương n: "))
print(f"Giai thừa của {n} là: {tinh_giai_thua(n)}")
def tinh_trung_binh(day_so):
    if not day_so:
        return 0
    return sum(day_so) / len(day_so)

# Ví dụ với một dãy số
numbers = [10, 20, 30, 40, 50]
trung_binh = tinh_trung_binh(numbers)
print(f"Giá trị trung bình của dãy {numbers} là: {trung_binh}")
def tinh_loi_nhuan(von_dau, lai_suat_nam):
    # Chuyển lãi suất năm (%) sang lãi suất tháng (thập phân)
    lai_suat_thang = (lai_suat_nam / 100) / 12
    thoi_gian = 12 # tháng
    
    # Tổng số tiền nhận được sau 12 tháng (gốc + lãi)
    tong_tien = von_dau * (1 + lai_suat_thang)**thoi_gian
    loi_nhuan = tong_tien - von_dau
    
    return tong_tien, loi_nhuan

# Nhập dữ liệu
von = float(input("Nhập số tiền gốc ban đầu: "))
lai = float(input("Nhập lãi suất năm (ví dụ 6.5 cho 6.5%): "))

tong, loi = tinh_loi_nhuan(von, lai)

print(f"--- Kết quả sau 12 tháng ---")
print(f"Tổng số tiền (gốc + lãi): {tong:,.2f}")
print(f"Tiền lãi thuần: {loi:,.2f}")