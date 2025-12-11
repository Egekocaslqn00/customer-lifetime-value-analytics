# Predictive CLV Engine

> An end-to-end customer lifetime value prediction system using probabilistic models and machine learning

## 🎯 Key Results

- **Identified high-value customers**: 15.3% of customers generate 22.2% of total revenue
- **Segmented 10,000 customers** into 8 actionable groups for targeted marketing
- **Predicted future value** using BG/NBD and Pareto/NBD probabilistic models
- **Discovered revenue concentration**: Top 50.5% of customers drive 64.7% of revenue
- **Flagged 438 at-risk customers** worth $450K+ in potential lost revenue
- **Analyzed 100,000 transactions** across 7 years of e-commerce data

## 📊 Sample Visualizations

### RFM Distribution Analysis
![RFM Distribution](reports/figures/01_rfm_distribution.png)

### Customer Segmentation
![Customer Segments](reports/figures/02_rfm_segments.png)

### Segment Characteristics
![Segment Characteristics](reports/figures/03_segment_characteristics.png)

### RFM 3D Scatter Plot
![RFM Scatter](reports/figures/04_rfm_scatter.png)

### K-Means Clustering Results
![K-Means Clusters](reports/figures/05_kmeans_clusters.png)

### Segment Value Analysis
![Segment Value](reports/figures/07_segment_value_analysis.png)

### Transaction Timeline
![Transaction Timeline](reports/figures/08_transaction_timeline.png)

## What This Project Does

This system helps e-commerce businesses understand which customers are most valuable and predict how much they'll spend in the future. It combines:

- **RFM Analysis**: Evaluates customers based on recency, frequency, and monetary value
- **Customer Segmentation**: Groups customers into 8 segments (Champions, Loyal, At Risk, etc.)
- **CLV Prediction**: Uses statistical models to forecast future customer value
- **Actionable Insights**: Provides specific recommendations for each customer group

## Why This Matters

Knowing your customer lifetime value is critical for:
- Allocating marketing budget efficiently
- Identifying which customers to prioritize
- Preventing high-value customer churn
- Optimizing acquisition costs

This project shows how to build a complete CLV prediction system from scratch.

## 🚀 How to Run This Project

### Step 1: Install Python

Make sure you have Python 3.9 or higher installed.

**Check your Python version:**
```bash
python --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/)

### Step 2: Clone the Repository

**Option A: Using Git**
```bash
git clone https://github.com/Egekocaslqn00/predictive-clv-engine.git
cd predictive-clv-engine
```

**Option B: Download ZIP**
1. Go to https://github.com/Egekocaslqn00/predictive-clv-engine
2. Click green "Code" button
3. Click "Download ZIP"
4. Extract to your desired location
5. Open terminal/command prompt in that folder

### Step 3: Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your command line.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages (pandas, numpy, scikit-learn, lifetimes, matplotlib, seaborn).

**Wait 3-5 minutes** for installation to complete.

### Step 5: Create Data Folders

**On Windows:**
```bash
mkdir data
mkdir data\raw
mkdir data\processed
```

**On Mac/Linux:**
```bash
mkdir -p data/raw data/processed
```

### Step 6: Generate Sample Data

```bash
python generate_sample_data.py
```

**Expected output:**
```
Generating 100,000 transactions for 10,000 customers...
✓ Data generated successfully!
  Shape: (100000, 9)
  Date range: 2018-01-01 to 2025-12-11
  Total amount: $10,015,143.57
✓ Data saved to: data/raw/ecommerce_transactions.csv
```

### Step 7: Run Complete Analysis

```bash
python run_complete_analysis.py
```

**This will take 2-5 minutes.** You'll see:

```
================================================================================
E-COMMERCE CUSTOMER LIFETIME VALUE (CLV) PREDICTION AND SEGMENTATION
================================================================================

[STEP 1] Loading and Exploring Data...
Total Customers: 10,000
Total Transactions: 100,000
Total Revenue: $10,015,143.57

[STEP 2] Data Cleaning and Preparation...
[STEP 3] RFM Analysis...
Recency: 286.2 days (avg)
Frequency: 10.0 purchases (avg)
Monetary: $1,001.51 (avg)

[STEP 4] Customer Segmentation (K-Means)...
Optimal number of clusters: 3

[STEP 5] Advanced CLV Modeling...
BG/NBD Model: ✓
Pareto/NBD Model: ✓

[STEP 6] Model Evaluation and Comparison...
[STEP 7] Business Insights and Recommendations...

Champions: 1,533 customers (15.3%)
  - Average CLV: $1,447.07
  - Total Value: $2,218,000+

Loyal Customers: 3,514 customers (35.1%)
  - Average CLV: $1,212.09
  - Total Value: $4,260,000+

At Risk: 438 customers (4.4%)
  - Average CLV: $1,029.58
  - Total Value: $450,000+

[STEP 8] Saving Results...
✓ Results saved successfully!

================================================================================
Analysis completed successfully!
================================================================================
```

### Step 8: Create Visualizations

```bash
python create_visualizations_and_report.py
```

**This creates 7 charts** in `reports/figures/`:
1. RFM distribution plots
2. Customer segment pie chart
3. Segment characteristics heatmap
4. RFM scatter plot
5. K-Means clusters
6. Segment value analysis
7. Transaction timeline

### Step 9: View Results

**Check the generated files:**

**On Windows:**
```bash
dir data\processed
dir reports\figures
```

**On Mac/Linux:**
```bash
ls data/processed
ls reports/figures
```

**You should see:**
- `data/processed/rfm_analysis.parquet` - RFM metrics for each customer
- `data/processed/rfm_with_clv.parquet` - CLV predictions
- `data/processed/segmented_customers.parquet` - Customer segments
- `reports/figures/*.png` - 7 visualization charts

### Step 10: Open Visualizations

Navigate to `reports/figures/` folder and open the PNG files to see:
- Customer distribution charts
- Segment analysis
- CLV predictions
- Business insights

## 📊 Understanding the Results

### Customer Segments

After running the analysis, you'll see 8 customer segments:

| Segment | % of Customers | % of Revenue | What to Do |
|---------|----------------|--------------|------------|
| **Champions** | 15.3% | 22.2% | VIP treatment, exclusive offers, early access |
| **Loyal Customers** | 35.1% | 42.5% | Loyalty programs, personalized recommendations |
| **At Risk** | 4.4% | 4.5% | Win-back campaigns, special discounts |
| **New Customers** | 5.4% | 3.3% | Onboarding programs, welcome offers |
| **Lost** | 11.2% | 6.7% | Survey why they left, very special offers |
| **Need Attention** | 13.0% | 10.6% | Re-engagement campaigns |
| **Potential Loyalists** | 4.0% | 3.0% | Encourage repeat purchases |
| **Others** | 11.5% | 7.1% | Minimal marketing spend |

### Key Insights

1. **15.3% of customers (Champions) generate 22.2% of revenue** - Focus your best efforts here
2. **Top 50.5% of customers drive 64.7% of revenue** - The 80/20 rule in action
3. **438 at-risk customers worth $450K+** - Immediate action needed to prevent churn
4. **Average customer value: $1,001** - Benchmark for acquisition costs

## 🛠️ Troubleshooting

### "Python not found"
Install Python from [python.org](https://www.python.org/downloads/)

### "pip not found"
```bash
python -m ensurepip --upgrade
```

### "Module not found: pandas"
Make sure virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Then reinstall:
```bash
pip install -r requirements.txt
```

### "Permission denied"
**On Windows:** Run command prompt as Administrator

**On Mac/Linux:** Add `sudo` before commands

### Visualizations not showing
Make sure you ran:
```bash
python create_visualizations_and_report.py
```

Check if files exist:
```bash
ls reports/figures/  # Mac/Linux
dir reports\figures  # Windows
```

## Project Structure

```
├── src/                        # Core analysis modules
│   ├── data_processing.py      # Data cleaning and prep
│   ├── rfm_analysis.py         # RFM calculations
│   ├── segmentation.py         # Customer segmentation
│   ├── clv_modeling.py         # CLV prediction models
│   └── visualization.py        # Charts and plots
├── data/
│   ├── raw/                    # Original transactions
│   └── processed/              # Analysis results
├── reports/
│   └── figures/                # Generated visualizations
├── notebooks/                  # Jupyter notebooks
└── config/                     # Configuration files
```

## How It Works

### 1. RFM Analysis

Every customer gets scored 1-5 on three metrics:
- **Recency**: How recently did they buy? (avg: 286 days)
- **Frequency**: How often do they buy? (avg: 10 purchases)
- **Monetary**: How much do they spend? (avg: $1,001)

### 2. Customer Segmentation

RFM scores determine which of 8 segments each customer belongs to.

### 3. CLV Prediction

Two probabilistic models predict future value:

**BG/NBD (Beta-Geometric/Negative Binomial)**
- Predicts how many times a customer will buy
- Accounts for customers becoming inactive
- Industry standard for CLV prediction

**Pareto/NBD**
- Alternative model with different assumptions
- Provides second opinion on predictions

### 4. K-Means Clustering

Machine learning finds 3 natural customer groups based on behavior patterns.

## Technologies

- **pandas** & **numpy**: Data manipulation
- **scikit-learn**: Machine learning (K-Means)
- **lifetimes**: BG/NBD and Pareto/NBD models
- **matplotlib** & **seaborn**: Visualizations
- **jupyter**: Interactive analysis

## What I Learned

- Implementing advanced statistical models (BG/NBD, Pareto/NBD)
- Customer segmentation strategies
- Translating data into business recommendations
- Building production-quality data science code
- Creating effective visualizations

## Future Improvements

- Deep learning models for better accuracy
- Real-time prediction API
- Business dashboard
- A/B testing framework
- Marketing platform integration

## Contact

GitHub: [@Egekocaslqn00](https://github.com/Egekocaslqn00)

---

*Built to demonstrate data science and machine learning skills for e-commerce analytics*
