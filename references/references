# Data Dictionary (Codebook) for YRBS 2007 Analysis

**Project:** Safety-First Behavior Pattern: Exploring the Association Between Bicycle Helmet Use and Interpersonal Violence Involvement Among Adolescents  
**Author:** Jian Kai-Yi (Eric) / 簡愷毅 (Student ID: 113370201)  

This document outlines the definitions, original survey questions, and data recoding logic for all variables used in our Logistic Regression inference and Exploratory Data Analysis (EDA) for Cycle 4. Invalid responses and missing values (NaN) were entirely excluded during the data cleaning process.

---

## Part 1: Core Variables for Logistic Regression Inference

### 1. Bicycle Helmet Use (Primary Explanatory Variable / 自變數 X)

* **Recoded Variable Name:** `Helmet_Numeric`
* **Original YRBS Variable:** `BicyleHelmetUse`
* **Original YRBS Question:** "When you rode a bicycle during the past 12 months, how often did you wear a helmet?"
* **Data Filtering Rule:** Only responses `1` (Never wore a helmet) and `5` (Always wore a helmet) were retained to examine the distinct behavioral extremes ("Always" vs. "Never"). All intermediate responses (Rarely, Sometimes, Most of the time) and "Did not ride a bicycle" were excluded.
* **Coding Logic:**
  * `1` (Always): Always wore a bicycle helmet (Original response code 5).
  * `0` (Never): Never wore a bicycle helmet (Original response code 1).

---

### 2. Physical Fighting Involvement (Primary Response Variable / 應變數 Y)

* **Recoded Variable Name:** `Fight_Numeric`
* **Original YRBS Variable:** `PhysicalFighting`
* **Original YRBS Question:** "During the past 12 months, how many times were you in a physical fight?"
* **Coding Logic:**
  * `1` (Yes): Engaged in physical fighting at least once in the past year (Original response codes 2 through 8, representing 1 time to 12 or more times).
  * `0` (No): Never engaged in physical fighting in the past year (Original response code 1).

---

## Part 2: Sample Breakdown Summary (Valid N = 11,144)

* **`Helmet_Numeric` = 0 (Never Wore Helmet):** $n = 6,451$ students
  * `Fight_Numeric` = 0 (No Fight): $n = 3,759$ ($58.27\%$)
  * `Fight_Numeric` = 1 (Fought): $n = 2,692$ ($41.73\%$)
* **`Helmet_Numeric` = 1 (Always Wore Helmet):** $n = 4,693$ students
  * `Fight_Numeric` = 0 (No Fight): $n = 3,435$ ($73.19\%$)
  * `Fight_Numeric` = 1 (Fought): $n = 1,258$ ($26.81\%$)

---

## Data Source Disclaimer
The raw data is derived from the 2007 National Youth Risk Behavior Survey (YRBS) conducted by the Centers for Disease Control and Prevention (CDC), USA. All records with missing or blank data in either variable were omitted to ensure standard sample consistency.
