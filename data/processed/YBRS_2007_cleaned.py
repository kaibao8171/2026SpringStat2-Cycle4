import pandas as pd
df = pd.read_csv('YRBS_2007.csv')

# 1. 檢查變數名稱是否存在 (這是為了避開欄位名稱可能的空格或差異)
cols_to_check = ['BicyleHelmetUse', 'PhysicalFighting']
existing_cols = [c for c in cols_to_check if c in df.columns]
print(f"確認欄位存在: {existing_cols}")

# 2. 檢視數據分佈，確認是否為我們預期的代碼 (1, 2)
if len(existing_cols) == 2:
    print("\n--- BicycelHelmetUse 分佈 ---")
    print(df['BicyleHelmetUse'].value_counts(dropna=False))
    print("\n--- PhysicalFighting 分佈 ---")
    print(df['PhysicalFighting'].value_counts(dropna=False))