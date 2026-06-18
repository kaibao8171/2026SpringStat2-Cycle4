# 2026SpringStat2-Cycle4
{
  "nbformat": 4,
  "nbformat_minor": 2,
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.10.0"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# **Applied Statistics Final Individual Project (Cycle 4)**\n",
        "## **探索青少年安全防護行為習慣與人際暴力衝突之關聯性**\n",
        "---\n",
        "* **Name / 姓名:** 簡愷毅 (Eric)\n",
        "* **Student ID / 學號:** 113370201\n",
        "* **Dataset:** Youth Risk Behavior Survey (YRBS) 2007\n",
        "* **Statistical Method:** Logistic Regression Model (邏輯斯迴歸分析)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## **第一部分：研究問題與統計假設**\n",
        "---\n",
        "### **1. 研究問題 (Research Question)**\n",
        "青少年騎乘自行車時配戴安全帽的守法行為，與其過去一年參與身體打架（暴力行為）之間，是否存在顯著統計關聯？\n",
        "\n",
        "### **2. 統計假設 (Hypothesis Setup)**\n",
        "* **虛無假設 ($H_0$):** $\\beta_1 = 0$（配戴安全帽行為與打架行為無顯著關聯）\n",
        "* **對立假設 ($H_A$):** $\\beta_1 \\neq 0$（配戴安全帽行為與打架行為存在顯著關聯）\n",
        "* **顯著水準 (Significance Level):** $\\alpha = 0.05$"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## **第二部分：環境建置與資料清洗**\n",
        "---\n",
        "載入所需的 Python 統計與視覺化套件，讀取 `YRBS_2007.csv`，並進行變數重新編碼（Recoding）：\n",
        "* 自變數 $X$ (`BicyleHelmetUse`): 保留 `1` (總是戴) 與 `2` (從不戴)，對應為二元指標 `1` (Yes) 與 `0` (No)。\n",
        "* 反應變數 $Y$ (`PhysicalFighting`): 將 `1` (從未打架) 編碼為 `0` (No)，`2` 至 `7` (曾打架1次以上) 編碼為 `1` (Yes)。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import statsmodels.api as sm\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from statsmodels.graphics.mosaicplot import mosaic\n",
        "import numpy as np\n",
        "\n",
        "# 載入資料\n",
        "try:\n",
        "    df = pd.read_csv('YRBS_2007.csv')\n",
        "    print(f\"成功載入 YRBS 原始資料！總筆數：{len(df):,} 筆\")\n",
        "except FileNotFoundError:\n",
        "    print(\"【錯誤】請確認 YRBS_2007.csv 檔案是否跟此 Notebook 放在同一個資料夾下！\")\n",
        "\n",
        "# 篩選有效回答：只保留有安全帽使用紀錄 (代碼 1, 2) 的樣本\n",
        "df_clean = df[df['BicyleHelmetUse'].isin([1, 2])].copy()\n",
        "\n",
        "# 自變數編碼 (X)：1 = Yes (有戴安全帽), 0 = No (沒戴安全帽)\n",
        "df_clean['Helmet_Numeric'] = df_clean['BicyleHelmetUse'].map({1: 1, 2: 0})\n",
        "\n",
        "# 反應變數編碼 (Y)：1 = Yes (過去一年打過架), 0 = No (從未打架)\n",
        "df_clean['Fight_Numeric'] = df_clean['PhysicalFighting'].apply(lambda x: 0 if x == 1 else (1 if 2 <= x <= 7 else None))\n",
        "df_clean = df_clean.dropna(subset=['Fight_Numeric'])\n",
        "\n",
        "print(f\"資料清洗完成！最終進入分析的有效樣本數 n = {len(df_clean):,} 筆\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## **第三部分：邏輯斯迴歸模型分析 (Logistic Regression)**\n",
        "---\n",
        "使用 `statsmodels` 建立邏輯斯迴歸模型，並計算 **勝算比 (Odds Ratio, OR)** 以及其 95% 信賴區間，用以衡量安全帽配戴行為對打架風險的顯著影響與風險變化率。"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 加入截距常數項\n",
        "X = sm.add_constant(df_clean['Helmet_Numeric'])\n",
        "model = sm.Logit(df_clean['Fight_Numeric'], X).fit()\n",
        "\n",
        "print(\"==================================================\")\n",
        "print(\"             Logistic Regression Summary\")\n",
        "print(\"==================================================\")\n",
        "print(model.summary())\n",
        "\n",
        "# 計算並輸出勝算比 (Odds Ratio) 與 95% 信賴區間\n",
        "params = model.params\n",
        "conf = model.conf_int()\n",
        "conf['OR'] = params\n",
        "conf.columns = ['95% CI Lower', '95% CI Upper', 'OR']\n",
        "or_df = np.exp(conf)\n",
        "\n",
        "print(\"\\n==================================================\")\n",
        "print(\"          勝算比分析 (Odds Ratio Results)\")\n",
        "print(\"==================================================\")\n",
        "print(f\"安全帽使用對打架風險的勝算比 (OR): {or_df.loc['Helmet_Numeric', 'OR']:.4f}\")\n",
        "print(f\"95% 信賴區間: [{or_df.loc['Helmet_Numeric', '95% CI Lower']:.4f}, {or_df.loc['Helmet_Numeric', '95% CI Upper']:.4f}]\")\n",
        "print(\"==================================================\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## **第四部分：數據視覺化（兩張獨立圖表）**\n",
        "---\n",
        "使用莫蘭迪淺色系（淺藍：未打架，淺紅：有過打架行為）來繪製兩張完全獨立的專業學術圖表：\n",
        "1. **圖表一 (Figure 1):** 比例堆疊長條圖（標註各區塊精準佔比值）。\n",
        "2. **圖表二 (Figure 2):** 卡方獨立性殘差馬賽克圖（將實際人數 $n$ 完美置中標註於色塊中）。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### **Figure 1: Proportional Stacked Bar Chart**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "sns.set_theme(style=\"whitegrid\", context=\"talk\")\n",
        "plt.figure(figsize=(9, 7))\n",
        "\n",
        "# 統一莫蘭迪配色：淺藍代表 No Fought，淺紅代表 Yes Fought\n",
        "colors = ['#A8DADC', '#F1948A']\n",
        "\n",
        "# 建立交叉表並標準化為比例\n",
        "crosstab_df = pd.crosstab(df_clean['Helmet_Numeric'].map({1: 'Yes', 0: 'No'}), \n",
        "                          df_clean['Fight_Numeric'].map({1: 'Yes', 0: 'No'}))\n",
        "crosstab_pct = crosstab_df.div(crosstab_df.sum(axis=1), axis=0)\n",
        "\n",
        "ax1 = crosstab_pct.plot(kind='bar', stacked=True, color=colors, width=0.55, edgecolor='white', linewidth=1.2)\n",
        "plt.title('Proportion of Fighting by Bicycle Helmet Use', fontsize=16, fontweight='bold', pad=20)\n",
        "plt.ylabel('Proportion', fontsize=14)\n",
        "plt.xlabel('Used Bicycle Helmet (Explanatory)', fontsize=14)\n",
        "plt.xticks(rotation=0)\n",
        "plt.ylim(0, 1.1)\n",
        "plt.legend(title='Fought (Response)', loc='upper right', bbox_to_anchor=(1.25, 1))\n",
        "\n",
        "# 在長條圖內部正中央標註比例數值\n",
        "for c in ax1.containers:\n",
        "    ax1.bar_label(c, fmt='%.2f', label_type='center', fontsize=13, fontweight='bold', color='#2F3E46')\n",
        "\n",
        "plt.tight_layout()\n",
        "# 儲存長條圖檔案\n",
        "plt.savefig('helmet_vs_fighting_bar.png', dpi=300, bbox_inches='tight')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### **Figure 2: Mosaic Plot of Sample Counts**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "plt.figure(figsize=(9, 7))\n",
        "\n",
        "# 將交叉表轉換為馬賽克圖字典格式\n",
        "data_dict = dict(zip([('No', 'No'), ('No', 'Yes'), ('Yes', 'No'), ('Yes', 'Yes')], \n",
        "                     crosstab_df.values.flatten()))\n",
        "\n",
        "# 統一配色函數\n",
        "def get_unified_color(key):\n",
        "    fought_status = key[1]\n",
        "    if fought_status == 'Yes':\n",
        "        return {'color': '#F1948A', 'edgecolor': 'white'}\n",
        "    else:\n",
        "        return {'color': '#A8DADC', 'edgecolor': 'white'}\n",
        "\n",
        "# 繪製馬賽克圖\n",
        "fig_mosaic, ax_mosaic = plt.subplots(figsize=(9, 7))\n",
        "mosaic(data_dict, title='Mosaic Plot of Sample Counts', \n",
        "       properties=get_unified_color, gap=0.02, ax=ax_mosaic)\n",
        "\n",
        "# 美化軸標籤與標題\n",
        "ax_mosaic.set_title('Mosaic Plot of Sample Counts', fontsize=16, fontweight='bold', pad=20)\n",
        "ax_mosaic.set_xlabel('Helmet Status (Explanatory - X)', fontsize=14, labelpad=15)\n",
        "ax_mosaic.set_ylabel('Fighting Status (Response - Y)', fontsize=14, labelpad=15)\n",
        "\n",
        "# 精準座標對齊 (n 數值居中標記)\n",
        "text_positions = {\n",
        "    ('No', 'No'): (0.29, 0.29),\n",
        "    ('No', 'Yes'): (0.29, 0.79),\n",
        "    ('Yes', 'No'): (0.79, 0.37),\n",
        "    ('Yes', 'Yes'): (0.79, 0.87)\n",
        "}\n",
        "\n",
        "for key, val in data_dict.items():\n",
        "    pos = text_positions[key]\n",
        "    ax_mosaic.text(pos[0], pos[1], f'n={val:,}', \n",
        "                   ha='center', va='center', fontsize=13, fontweight='bold', color='#2F3E46')\n",
        "\n",
        "plt.tight_layout()\n",
        "# 儲存馬賽克圖檔案\n",
        "plt.savefig('helmet_vs_fighting_mosaic.png', dpi=300, bbox_inches='tight')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## **第五部分：統計結論與學術討論**\n",
        "---\n",
        "### **1. 研究結論 (Conclusion)**\n",
        "透過邏輯斯迴歸分析，我們發現在青少年群體中，配戴安全帽的守法行為對打架暴力行為具有**極端顯著的負向影響** ($Z = -16.21, P = 2.56 \\times 10^{-59} \\ll 0.05$)，我們強烈拒絕虛無假設。  \n",
        "總是配戴安全帽之學生的打架率只有 **26.81%**，遠低於從不配戴安全帽學生的 **41.73%**。勝算比 **$OR = 0.5105$** 顯示：**有戴安全帽習慣的學生，其參與身體打架的勝算 (Odds) 只有從不戴者的 0.51 倍（即降低了約 49% 的暴力發生勝算）**。這高度支持了青少年群體中存在「安全守規 (Safety-First) 與 冒險偏差 (Risk-Taking) 人格特質」的集群行為假說。\n",
        "\n",
        "### **2. 因果推論限制防禦宣告 (Disclaimer)**\n",
        "本分析基於 **YRBS 橫斷面觀察資料 (Cross-Sectional Observational Study)**。我們只能確認變數之間存在極其強大的**統計關聯性 (Association)**，但**無法**得出「強迫青少年戴安全帽，就能直接降低其暴力打架機率」的因果關係結論。家庭社經背景、教養方式或個人自律神經系統，皆可能是同時驅動這兩個行為的潛在混淆變數 (Confounders)。"
      ]
    }
  ]
}
