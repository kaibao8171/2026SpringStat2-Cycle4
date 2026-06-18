import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic
import numpy as np

# ==========================================
# 1. 載入資料與進行資料清洗 (Data Cleaning)
# ==========================================
df = pd.read_csv('YRBS_2007.csv')

# 篩選有效回答：只保留有安全帽使用紀錄 (1, 2) 的樣本
df_clean = df[df['BicyleHelmetUse'].isin([1, 2])].copy()

# 自變數編碼 (X)：1 = Yes (有戴安全帽), 0 = No (沒戴安全帽)
df_clean['Helmet_Numeric'] = df_clean['BicyleHelmetUse'].map({1: 1, 2: 0})

# 反應變數編碼 (Y)：1 = Yes (過去一年內打過架, 也就是代碼 2-7), 0 = No (從未打架, 也就是代碼 1)
df_clean['Fight_Numeric'] = df_clean['PhysicalFighting'].apply(lambda x: 0 if x == 1 else (1 if 2 <= x <= 7 else None))
df_clean = df_clean.dropna(subset=['Fight_Numeric'])

# ==========================================
# 2. 邏輯斯迴歸分析 (Logistic Regression)
# ==========================================
X = sm.add_constant(df_clean['Helmet_Numeric'])
model = sm.Logit(df_clean['Fight_Numeric'], X).fit()

print("==================================================")
print("             Logistic Regression Summary")
print("==================================================")
print(model.summary())

# 計算並輸出勝算比 (Odds Ratio)
or_val = np.exp(model.params['Helmet_Numeric'])
print(f"\nOdds Ratio of Helmet Use (OR): {or_val:.4f}")
print("==================================================")

# ==========================================
# 3. 繪製圖表一：比例堆疊長條圖 (Proportional Bar Chart)
# ==========================================
sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(9, 7))

# 統一色系：淺藍代表未打架 (No)，淺紅代表有打架 (Yes)
colors = ['#A8DADC', '#F1948A']

# 建立交叉表並標準化為比例
crosstab_df = pd.crosstab(df_clean['Helmet_Numeric'].map({1: 'Yes', 0: 'No'}), 
                          df_clean['Fight_Numeric'].map({1: 'Yes', 0: 'No'}))
crosstab_pct = crosstab_df.div(crosstab_df.sum(axis=1), axis=0)

ax1 = crosstab_pct.plot(kind='bar', stacked=True, color=colors, width=0.6, edgecolor='white', linewidth=1)
plt.title('Proportion of Fighting by Bicycle Helmet Use', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Proportion', fontsize=14)
plt.xlabel('Used Bicycle Helmet (Explanatory)', fontsize=14)
plt.xticks(rotation=0)
plt.ylim(0, 1.1)
plt.legend(title='Fought (Response)', loc='upper right', bbox_to_anchor=(1.2, 1))

# 在長條圖內部正中央標註比例數值
for c in ax1.containers:
    ax1.bar_label(c, fmt='%.2f', label_type='center', fontsize=13, fontweight='bold', color='#2F3E46')

plt.tight_layout()
# 儲存獨立的長條圖
plt.savefig('helmet_vs_fighting_bar.png', dpi=300, bbox_inches='tight')
plt.show()

# ==========================================
# 4. 繪製圖表二：馬賽克圖 (Mosaic Plot)
# ==========================================
plt.figure(figsize=(9, 7))

# 將交叉表轉換為馬賽克圖字典格式
data_dict = dict(zip([('No', 'No'), ('No', 'Yes'), ('Yes', 'No'), ('Yes', 'Yes')], 
                     crosstab_df.values.flatten()))

# 統一配色函數：Y 軸為 Yes (打架) 塗淺紅，No (不打架) 塗淺藍
def get_unified_color(key):
    fought_status = key[1]
    if fought_status == 'Yes':
        return {'color': '#F1948A', 'edgecolor': 'white'}
    else:
        return {'color': '#A8DADC', 'edgecolor': 'white'}

# 繪製馬賽克圖
fig_mosaic, ax_mosaic = plt.subplots(figsize=(9, 7))
mosaic(data_dict, title='Mosaic Plot of Sample Counts', 
       properties=get_unified_color, gap=0.02, ax=ax_mosaic)

# 設客製化標籤與美化
ax_mosaic.set_title('Mosaic Plot of Sample Counts', fontsize=16, fontweight='bold', pad=20)
ax_mosaic.set_xlabel('Helmet Status (Explanatory - X)', fontsize=14, labelpad=15)
ax_mosaic.set_ylabel('Fighting Status (Response - Y)', fontsize=14, labelpad=15)

# 依據數學比例精準定位 n 值的標籤座標 (完美置中於各色塊)
# 計算公式：X 軸分界點在 0.58；Y 軸左側分界點在 0.58，右側分界點在 0.73
text_positions = {
    ('No', 'No'): (0.29, 0.29),    # 沒戴安全帽，沒打架 (n=3,759)
    ('No', 'Yes'): (0.29, 0.79),   # 沒戴安全帽，有打架 (n=2,692)
    ('Yes', 'No'): (0.79, 0.37),   # 有戴安全帽，沒打架 (n=3,435)
    ('Yes', 'Yes'): (0.79, 0.87)   # 有戴安全帽，有打架 (n=1,258)
}

for key, val in data_dict.items():
    pos = text_positions[key]
    ax_mosaic.text(pos[0], pos[1], f'n={val:,}', 
                   ha='center', va='center', fontsize=13, fontweight='bold', color='#2F3E46')

plt.tight_layout()
# 儲存獨立的馬賽克圖
plt.savefig('helmet_vs_fighting_mosaic.png', dpi=300, bbox_inches='tight')
plt.show()
