# Insurance Risk Analytics

An end-to-end insurance risk analytics and machine learning project focused on exploratory data analysis, reproducible data pipelines, and predictive insurance insights using Python, GitHub Actions, and DVC.

---

# Project Overview

This project simulates a real-world insurance analytics workflow where data science and machine learning are used to analyze insurance risk, claims behavior, customer profitability, and policy trends.

The project follows professional ML engineering practices including:
- Git/GitHub workflow
- Branch-based development
- CI/CD automation
- Data Version Control (DVC)
- Reproducible analytics pipelines
- Exploratory Data Analysis (EDA)
- Modular Python utilities

---

# Objectives

- Analyze insurance policy and claims data
- Understand profitability and risk behavior
- Build reproducible ML/data workflows
- Track dataset versions using DVC
- Prepare the foundation for hypothesis testing and machine learning modeling

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
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── reports/
│   └── final_report.md
├── tests/
├── .dvc/
├── .gitignore
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

# Task 1 — Git, GitHub & Exploratory Data Analysis

## Completed Work

### Repository & Development Setup
- Created GitHub repository
- Configured Python virtual environment
- Added `.gitignore`
- Added `requirements.txt`
- Structured project directories professionally

### CI/CD Pipeline
Implemented GitHub Actions workflow to:
- install dependencies
- run flake8 linting
- run pytest automatically on every push

### Exploratory Data Analysis (EDA)
Performed comprehensive EDA including:

#### Data Understanding
- Dataset inspection
- Data type validation
- Descriptive statistics
- Datetime conversion

#### Data Quality Assessment
- Missing value analysis
- Dataset consistency checks

#### Univariate Analysis
- Histograms for financial variables
- Distribution analysis
- Categorical count plots

#### Bivariate & Multivariate Analysis
- Correlation analysis
- Scatter plots
- Premium vs claims relationships

#### Geographic Analysis
- Province-based comparisons
- Auto make trends across regions
- Cover type analysis

#### Outlier Detection
- Boxplot analysis
- Extreme claims detection
- Financial outlier identification

#### Business Insights
Analyzed:
- Loss Ratio
- Claims trends
- Vehicle risk patterns
- Temporal insurance behavior
- Customer profitability indicators

---

# Key Metric

## Loss Ratio

```math
Loss Ratio = TotalClaims / TotalPremium
```

This metric measures insurance profitability and risk exposure.

---

# Task 2 — Data Version Control (DVC)

## Completed Work

### DVC Setup
- Installed and initialized DVC
- Configured local DVC remote storage
- Integrated DVC with Git workflow

### Dataset Versioning
Tracked:
- Raw insurance dataset
- Cleaned insurance dataset

using DVC metadata and remote storage.

### Reproducibility
Implemented reproducible data versioning workflow allowing:
- dataset recovery
- dataset history tracking
- experiment reproducibility
- auditable ML pipelines

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Git
- GitHub
- GitHub Actions
- DVC
- Jupyter Notebook

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd insurance-risk-analytics
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Pull DVC Tracked Data

```bash
dvc pull
```

---

## 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

---

# DVC Workflow

## Add Dataset

```bash
dvc add data/insurance_data.csv
```

## Push Dataset to Remote Storage

```bash
dvc push
```

## Retrieve Dataset

```bash
dvc pull
```

---

# Branching Strategy

- `main` → stable production-ready branch
- `task-1` → EDA and project setup
- `task-2` → DVC and reproducibility pipeline

---

# Future Work

Upcoming tasks include:
- Statistical hypothesis testing
- Machine learning modeling
- Risk prediction
- Explainable AI (SHAP/LIME)
- Insurance premium optimization

---
