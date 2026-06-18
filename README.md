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
