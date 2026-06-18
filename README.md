# 2026SpringStat2-Cycle4
# Safety-First Behavior Pattern: Exploring the Association Between Bicycle Helmet Use and Interpersonal Violence Involvement Among Adolescents

**Presentation Video Link** - [Insert Your Individual Presentation Video Link Here / 請在此貼上您的個人影片連結]

## 1. Student Information / 個人基本資料

* **Name / 姓名:** 簡愷毅 (Eric)
* **Student ID / 學號:** 113370201
* **Course / 課程名稱:** Applied Statistics (Spring 2026) / 應用統計學 (2026春季)
* **Project Cycle / 專案階段:** Final Individual Project (Cycle 4) / 個人最終專案 (Cycle 4)

---

## 2. Selected Research Question / 選定的研究問題

* Is there a statistically significant association between bicycle helmet use and the prevalence of physical fighting among adolescents?
* 青少年騎乘自行車配戴安全帽之守法行為，與其過去一年參與身體打架之暴力衝突之間是否存在顯著統計關聯？（以此探討青少年是否存在「安全守規」與「冒險偏差」的潛在行為人格特質關聯。）

---

## 3. Group Variable and Response Variable / 群組變數與反應變數

* **Primary Explanatory Variable (X) / 主要群組變數（自變數）:**
  * `Helmet_Numeric` (1 = Always wore a helmet / 總是配戴安全帽 [n=4,693], 0 = Never wore a helmet / 從不配戴安全帽 [n=6,451])
* **Primary Response Variable (Y) / 主要反應變數（應變數）:**
  * `Fight_Numeric` (1 = Engaged in physical fighting at least once / 過去一年內曾參與打架 [n=3,950], 0 = Never engaged in physical fighting / 從未參與打架 [n=7,194])

---

## 4. Method Used / 使用的統計方法

* **Logistic Regression (Logit Model) / 邏輯斯迴歸分析** (符合課程指定之進階迴歸方法)

---

## 5. Statistical Results & Final Conclusion / 統計結果與最終結論

### 📊 交叉描述性統計表 (Contingency Table)

| 安全帽配戴習慣 (X) | 無打架行為 (Y=0) | 有打架行為 (Y=1) | 總計 (Total) | 實際打架比例 |
| :--- | :---: | :---: | :---: | :---: |
| **No (0 - 從不戴)** | 3,759 筆 | 2,692 筆 | 6,451 筆 | **41.73%** |
| **Yes (1 - 總是戴)** | 3,435 筆 | 1,258 筆 | 4,693 筆 | **26.81%** |
| **總計** | **7,194 筆** | **3,950 筆** | **11,144 筆** | **35.44%** |

### 💻 邏輯斯迴歸分析模型報表 (Logistic Regression Output)
* **Dependent Variable: Fight_Numeric**
  * Number of Observations: 11,144
  * Df Residuals: 11,142
  * LLR p-value: 2.086e-60 (Extremely Significant)
* **Model Parameter Estimates:**
  * Intercept (const): coef = -0.3339
  * z = -13.223 |
  * P>|z| = 0.000
  * 95% CI = [-0.383, -0.284]
  * Bicycle Helmet Use (Helmet_Numeric): coef = -0.6706 | z = -16.154 | P>|z| = 0.000 | 95% CI = [-0.752, -0.589]
  
### 🔑 勝算比與信賴區間分析 (Odds Ratio Results)

| 評估指標 | 統計數值 (Value) | 95% 信賴區間 (95% CI) |
| :--- | :---: | :---: |
| **迴歸係數 ($\beta_1$)** | -0.6706 | [-0.752, -0.589] |
| **勝算比 (Odds Ratio, $OR$)** | **0.5114** | **[0.4714, 0.5549]** |

---

## 📝 Final Interpretation & Conclusions / 最終決策與學術解讀

### English Version
Based on our Logistic Regression analysis on $n = 11,144$ valid adolescent samples from the YRBS 2007 dataset, we found an extremely statistically significant negative association between bicycle helmet use and involvement in physical fighting ($Z = -16.15$, $P = 2.09 \times 10^{-60} \ll 0.05$). We strongly reject the null hypothesis ($H_0: \beta_1 = 0$).

Students who consistently wore bicycle helmets exhibited a significantly lower physical fighting rate (**26.81%**) compared to those who never wore helmets (**41.73%**). Our regression model yielded an **Odds Ratio ($OR$) of 0.5114** ($95\%$ Confidence Interval: $[0.4714, 0.5549]$). This indicates that adolescents who practice safety compliance (wearing helmets) have **0.51 times the odds** of engaging in physical fighting compared to their non-compliant peers—representing an approximate **49% reduction in the odds of violence involvement**.

This robust correlation strongly supports the "Safety-First Persona" hypothesis, suggesting that preventative safety compliance and violent behavioral risk tend to cluster within individual behavioral profiles.

*As this is an observational study using cross-sectional survey data, these findings establish a strong statistical association but do not imply direct causality.*

---

### 中文版
本研究針對 2007 年 YRBS 數據中篩選出的 11,144 筆有效青少年樣本進行邏輯斯迴歸分析（Logistic Regression），得到以下最終結論：

1. **統計與實質顯著性：** 迴歸分析結果顯示，配戴安全帽習慣對打架暴力行為具有極端顯著的負向影響（檢定統計量 $Z = -16.154$，$P$ 值為 $2.086 \times 10^{-60} \ll 0.05$），我們強烈拒絕虛無假設。總是配戴安全帽之青少年的打架比例（**26.81%**）顯著低於從不配戴者（**41.73%**）。
2. **勝算比（Odds Ratio）與安全人格洞察：** 邏輯斯迴歸模型算出的 **勝算比（OR）為 0.5114**（95% 信賴區間為 $[0.4714, 0.5549]$）。這意味著有配戴安全帽習慣的青少年，其參與身體打架的勝算（Odds）僅有從不配戴者的 **0.51 倍**，相當於**降低了近 49% 的暴力參與風險**。此數據有力地支持了「安全守規人格（Safety-First Persona）」假說，說明規律的安全守法行為與低暴力傾向在青少年群體中具有高度共存性。

*防禦性宣告：由於本研究採用的是觀察性橫斷面研究資料（Observational Cross-Sectional Data），此處結果僅能證實青少年的「安全帽配戴守規行為」與「打架衝突」之間存在強烈的統計相關性（Association），絕不宣稱其具備因果關係（Causality），潛在的第三方混淆變數（如家庭教養、同儕環境等）必須一併納入考量。*

---

## 🎨 6. Key Data Visualizations / 核心數據視覺化展示

### Figure 1: Proportional Stacked Bar Chart
outputs/figures/helmet_fighting_plot.png

### Figure 2: Mosaic Plot of Sample Counts
outputs/figures/helmet_vs_fighting_analysis.png
