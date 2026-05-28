# Insurance Risk Analytics & Pricing System

## Project Overview

This project develops a complete analytics-driven insurance risk modeling pipeline for AlphaCare Insurance Solutions (ACIS), a South African auto-insurance company preparing for aggressive growth and modernization of its pricing strategy.

The objective is to transition from intuition-based insurance pricing toward evidence-based, risk-adjusted premium optimization using statistical analysis and machine learning.

The project covers:

* Exploratory Data Analysis (EDA)
* Statistical Hypothesis Testing
* Predictive Modeling
* Risk-Based Pricing
* Explainable AI (SHAP)
* Data Version Control (DVC)
* CI/CD Automation with GitHub Actions

---

# Business Problem

Traditional insurance pricing approaches often rely heavily on manual assumptions and generalized customer segmentation.

This project aims to identify statistically significant risk drivers and build predictive models capable of:

* estimating insurance claim severity,
* predicting claim occurrence probability,
* identifying high-risk and low-risk customer segments,
* supporting dynamic premium optimization.

Two core business metrics were central throughout the analysis:

### Loss Ratio

Loss Ratio = TotalClaims / TotalPremium

Measures how much of collected premium is consumed by claims.

### Margin

Margin = TotalPremium − TotalClaims

Measures insurer profitability after claims are paid.

---

# Dataset

The project uses an 18-month historical insurance claims dataset containing:

* Customer demographics
* Vehicle information
* Policy characteristics
* Geographic information
* Claims history
* Premium values
* Financial risk indicators

Key variables include:

* TotalPremium
* TotalClaims
* ClaimAmount
* RiskScore
* VehicleType
* Province
* AutoMake
* CoverType
* ZipCode
* Gender

---

# Project Structure

```text
insurance-risk-analytics/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── reports/
├── tests/
├── requirements.txt
├── dvc.yaml
└── README.md
```

---

# Task 1 — Exploratory Data Analysis (EDA)

## Objectives

* Understand portfolio risk patterns
* Assess data quality
* Explore profitability drivers
* Identify geographic and demographic trends

## Completed Analysis

### Data Summarization

* Reviewed data types
* Generated descriptive statistics
* Analyzed distributions of numerical variables

### Data Quality Assessment

* Checked for missing values
* Validated feature consistency
* Confirmed categorical and numerical feature structure

### Univariate Analysis

* Histograms for financial variables
* Bar charts for categorical features
* Distribution analysis for claims and premiums

### Bivariate & Multivariate Analysis

* Examined TotalPremium vs TotalClaims relationships
* Correlation analysis
* Risk comparisons by ZipCode and Province

### Geographic Trends

* Compared:

  * CoverType
  * AutoMake
  * Premium behavior
    across provinces

### Outlier Detection

* Boxplots used to detect extreme values in:

  * TotalClaims
  * CustomValueEstimate
  * Premium variables

---

# Key EDA Findings

## Loss Ratio Trends

* Loss ratios varied moderately across provinces and vehicle groups.
* Some zip codes exhibited noticeably lower margins and higher loss ratios.

## Vehicle Risk Insights

Higher claim amounts were associated with:

* Luxury vehicles
* Certain high-value vehicle brands
* Customers with higher historical risk scores

## Temporal Patterns

Claim frequency and severity showed moderate fluctuations across the 18-month period.

## Financial Distributions

Several financial variables exhibited right-skewed distributions and contained outliers typical of insurance claims datasets.

---

# Task 2 — Data Version Control (DVC)

## Objectives

Establish a reproducible and auditable data pipeline suitable for regulated insurance analytics environments.

## Completed Work

* Installed and configured DVC
* Initialized DVC repository
* Configured local remote storage
* Tracked datasets using `.dvc` files
* Created dataset versions for reproducibility

## Importance

DVC ensures:

* reproducibility,
* traceability,
* auditability,
* consistent experimentation.

This is especially critical in regulated industries such as insurance and finance.

---

# Task 3 — Statistical Hypothesis Testing

## Objectives

Statistically validate whether observed customer risk differences are significant.

## Tested Hypotheses

1. No risk difference across provinces
2. No risk difference between zip codes
3. No margin difference between zip codes
4. No significant risk difference between women and men

## Statistical Methods

* Chi-Square Test of Independence
* Independent Two-Sample T-Test

## Key Findings

### Province Risk Difference

No statistically significant claim frequency difference was found between Addis Ababa and Oromia.

### ZipCode Risk Difference

Claim severity differences between major zip codes were relatively small.

### Margin Differences

Certain zip codes showed stronger margin variation, suggesting potential pricing optimization opportunities.

### Gender Risk Difference

Claim frequency differences between male and female policyholders were negligible.

## Business Insight

The analysis demonstrated that some intuitive segmentation assumptions are not statistically supported, emphasizing the importance of evidence-based pricing decisions.

---

# Task 4 — Statistical Modeling & Risk-Based Pricing

## Objectives

Develop predictive models capable of:

* estimating claim severity,
* supporting dynamic premium optimization,
* identifying major drivers of insurance risk.

---

# Machine Learning Models

The following algorithms were implemented:

| Model             | RMSE    | R²     |
| ----------------- | ------- | ------ |
| Linear Regression | 5284.27 | 0.2105 |
| Random Forest     | 5436.32 | 0.1644 |
| XGBoost           | 5704.43 | 0.0800 |

## Best Performing Model

Linear Regression achieved the strongest performance on this dataset.

---

# Feature Engineering

Engineered features included:

* VehicleAge
* Margin
* ClaimFrequency

Categorical features were encoded using One-Hot Encoding.

---

# Explainable AI (SHAP)

SHAP was used to identify the most influential claim severity drivers.

## Top Influential Features

| Feature                 | Importance |
| ----------------------- | ---------- |
| RiskScore               | 1926.08    |
| VehicleType_Luxury      | 597.93     |
| VehicleType_Sedan       | 448.02     |
| PastClaims              | 358.50     |
| VehicleType_Hatchback   | 287.06     |
| NCD                     | 282.22     |
| Age                     | 264.75     |
| Province_Addis Ababa    | 231.73     |
| AutoMake_Mercedes-Benz  | 229.67     |
| CoverType_Comprehensive | 214.43     |

## Business Interpretation

The analysis suggests that:

* RiskScore is the strongest driver of claim severity.
* Luxury vehicles significantly increase predicted claim amounts.
* Previous claims history strongly influences future claim risk.
* Certain geographic regions and premium cover types contribute meaningfully to claim behavior.

---

# Claim Probability Classification

A Logistic Regression classifier was implemented to estimate claim occurrence probability.

## Classification Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.857 |
| Precision | 0.566 |
| Recall    | 0.228 |
| F1 Score  | 0.325 |

This classification framework supports future implementation of dynamic premium estimation.

---

# Risk-Based Pricing Framework

The project supports a pricing framework based on:

Premium = (P(claim) × Predicted Severity) + Expense Loading + Profit Margin

This enables:

* personalized pricing,
* analytics-driven underwriting,
* improved profitability management,
* more competitive customer segmentation.

---

# Reproducibility & Automation

## CI/CD

GitHub Actions automatically:

* runs validation checks,
* verifies pipeline integrity,
* supports reproducible development.

## DVC

DVC tracks dataset versions and supports reproducible experimentation workflows.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* SHAP
* Matplotlib
* Seaborn
* DVC
* GitHub Actions

---

# Conclusion

This project demonstrates a complete end-to-end insurance analytics workflow combining:

* exploratory analytics,
* statistical inference,
* predictive modeling,
* explainable AI,
* reproducibility engineering,
* and business-focused pricing strategy.

The system establishes a strong foundation for future deployment of dynamic, analytics-driven insurance pricing solutions.
