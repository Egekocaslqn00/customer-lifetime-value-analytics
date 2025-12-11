"""
E-Commerce CLV Analysis - Visualization and Detailed Report Generator
Creates comprehensive visualizations and detailed analysis report
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Create output directories
output_dir = Path("reports/figures")
output_dir.mkdir(parents=True, exist_ok=True)

print("="*80)
print("E-COMMERCE CLV ANALYSIS - DETAILED VISUALIZATION & REPORT")
print("="*80)
print()

# Load data
print("[1/10] Loading analysis results...")
rfm_df = pd.read_parquet("data/processed/rfm_analysis.parquet")
rfm_clv_df = pd.read_parquet("data/processed/rfm_with_clv.parquet")
segmented_df = pd.read_parquet("data/processed/segmented_customers.parquet")
raw_data = pd.read_csv("data/raw/ecommerce_transactions.csv")

print(f"✓ Loaded {len(rfm_df):,} customers")
print(f"✓ Loaded {len(raw_data):,} transactions")
print()

# ============================================================================
# VISUALIZATION 1: RFM Distribution
# ============================================================================
print("[2/10] Creating RFM distribution plots...")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('RFM Metrics Distribution', fontsize=16, fontweight='bold')

# Recency
axes[0].hist(rfm_df['Recency'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
axes[0].axvline(rfm_df['Recency'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {rfm_df["Recency"].mean():.1f}')
axes[0].set_xlabel('Recency (days)', fontsize=12)
axes[0].set_ylabel('Number of Customers', fontsize=12)
axes[0].set_title('Recency Distribution', fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Frequency
axes[1].hist(rfm_df['Frequency'], bins=50, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1].axvline(rfm_df['Frequency'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {rfm_df["Frequency"].mean():.1f}')
axes[1].set_xlabel('Frequency (purchases)', fontsize=12)
axes[1].set_ylabel('Number of Customers', fontsize=12)
axes[1].set_title('Frequency Distribution', fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Monetary
axes[2].hist(rfm_df['Monetary'], bins=50, color='salmon', edgecolor='black', alpha=0.7)
axes[2].axvline(rfm_df['Monetary'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${rfm_df["Monetary"].mean():.2f}')
axes[2].set_xlabel('Monetary ($)', fontsize=12)
axes[2].set_ylabel('Number of Customers', fontsize=12)
axes[2].set_title('Monetary Distribution', fontsize=14, fontweight='bold')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(output_dir / "01_rfm_distribution.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_dir / '01_rfm_distribution.png'}")
plt.close()

# ============================================================================
# VISUALIZATION 2: RFM Segments
# ============================================================================
print("[3/10] Creating RFM segments visualization...")

segment_counts = segmented_df['Segment'].value_counts()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Customer Segmentation Analysis', fontsize=16, fontweight='bold')

# Bar chart
colors = plt.cm.Set3(np.linspace(0, 1, len(segment_counts)))
segment_counts.plot(kind='bar', ax=ax1, color=colors, edgecolor='black', alpha=0.8)
ax1.set_xlabel('Customer Segment', fontsize=12)
ax1.set_ylabel('Number of Customers', fontsize=12)
ax1.set_title('Customer Count by Segment', fontsize=14, fontweight='bold')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for i, v in enumerate(segment_counts):
    ax1.text(i, v + 50, str(v), ha='center', va='bottom', fontweight='bold')

# Pie chart
ax2.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'fontsize': 10, 'fontweight': 'bold'})
ax2.set_title('Customer Distribution by Segment', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(output_dir / "02_rfm_segments.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_dir / '02_rfm_segments.png'}")
plt.close()

# ============================================================================
# VISUALIZATION 3: Segment Characteristics
# ============================================================================
print("[4/10] Creating segment characteristics heatmap...")

segment_stats = segmented_df.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(segment_stats.T, annot=True, fmt='.1f', cmap='YlOrRd', 
            linewidths=0.5, cbar_kws={'label': 'Value'}, ax=ax)
ax.set_title('Average RFM Metrics by Segment', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Customer Segment', fontsize=12, fontweight='bold')
ax.set_ylabel('RFM Metric', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(output_dir / "03_segment_characteristics.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_dir / '03_segment_characteristics.png'}")
plt.close()

# ============================================================================
# VISUALIZATION 4: RFM 3D Scatter (Top view)
# ============================================================================
print("[5/10] Creating RFM scatter plot...")

fig, ax = plt.subplots(figsize=(12, 10))

# Sample data for better visualization
sample_size = min(1000, len(segmented_df))
sample_df = segmented_df.sample(n=sample_size, random_state=42)

segments = sample_df['Segment'].unique()
colors_map = dict(zip(segments, plt.cm.Set3(np.linspace(0, 1, len(segments)))))

for segment in segments:
    segment_data = sample_df[sample_df['Segment'] == segment]
    ax.scatter(segment_data['Recency'], segment_data['Frequency'], 
              s=segment_data['Monetary']/5, alpha=0.6, 
              c=[colors_map[segment]], label=segment, edgecolors='black', linewidth=0.5)

ax.set_xlabel('Recency (days)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency (purchases)', fontsize=12, fontweight='bold')
ax.set_title('RFM Scatter Plot (bubble size = Monetary value)', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(output_dir / "04_rfm_scatter.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_dir / '04_rfm_scatter.png'}")
plt.close()

# ============================================================================
# VISUALIZATION 5: K-Means Clusters
# ============================================================================
print("[6/10] Creating K-Means cluster visualization...")

if 'Cluster' in segmented_df.columns:
    fig, ax = plt.subplots(figsize=(12, 8))
    
    cluster_counts = segmented_df['Cluster'].value_counts().sort_index()
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    bars = ax.bar(cluster_counts.index, cluster_counts.values, color=colors, 
                  edgecolor='black', alpha=0.8, width=0.6)
    
    ax.set_xlabel('Cluster ID', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Customers', fontsize=12, fontweight='bold')
    ax.set_title('K-Means Clustering Results (3 Clusters)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(output_dir / "05_kmeans_clusters.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_dir / '05_kmeans_clusters.png'}")
    plt.close()

# ============================================================================
# VISUALIZATION 6: Top 20 Customers by CLV
# ============================================================================
print("[7/10] Creating top customers visualization...")

if 'predicted_clv' in rfm_clv_df.columns:
    top_20 = rfm_clv_df.nlargest(20, 'predicted_clv')
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    bars = ax.barh(range(len(top_20)), top_20['predicted_clv'], 
                   color=plt.cm.viridis(np.linspace(0, 1, len(top_20))),
                   edgecolor='black', alpha=0.8)
    
    ax.set_yticks(range(len(top_20)))
    ax.set_yticklabels([f'Customer {i+1}' for i in range(len(top_20))])
    ax.set_xlabel('Predicted CLV ($)', fontsize=12, fontweight='bold')
    ax.set_title('Top 20 Customers by Predicted CLV', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, top_20['predicted_clv'])):
        ax.text(val, i, f' ${val:.2f}', va='center', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_dir / "06_top_customers_clv.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_dir / '06_top_customers_clv.png'}")
    plt.close()

# ============================================================================
# VISUALIZATION 7: Segment Value Analysis
# ============================================================================
print("[8/10] Creating segment value analysis...")

segment_value = segmented_df.groupby('Segment').agg({
    'Monetary': ['sum', 'mean', 'count']
}).round(2)

segment_value.columns = ['Total_Value', 'Avg_Value', 'Customer_Count']
segment_value = segment_value.sort_values('Total_Value', ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Segment Value Analysis', fontsize=16, fontweight='bold')

# Total value by segment
colors = plt.cm.Spectral(np.linspace(0, 1, len(segment_value)))
bars1 = ax1.bar(range(len(segment_value)), segment_value['Total_Value'], 
               color=colors, edgecolor='black', alpha=0.8)
ax1.set_xticks(range(len(segment_value)))
ax1.set_xticklabels(segment_value.index, rotation=45, ha='right')
ax1.set_ylabel('Total Value ($)', fontsize=12, fontweight='bold')
ax1.set_title('Total Revenue by Segment', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, val in zip(bars1, segment_value['Total_Value']):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'${val:,.0f}',
            ha='center', va='bottom', fontweight='bold', fontsize=9)

# Average value by segment
bars2 = ax2.bar(range(len(segment_value)), segment_value['Avg_Value'], 
               color=colors, edgecolor='black', alpha=0.8)
ax2.set_xticks(range(len(segment_value)))
ax2.set_xticklabels(segment_value.index, rotation=45, ha='right')
ax2.set_ylabel('Average Value ($)', fontsize=12, fontweight='bold')
ax2.set_title('Average Customer Value by Segment', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, val in zip(bars2, segment_value['Avg_Value']):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'${val:.2f}',
            ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig(output_dir / "07_segment_value_analysis.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_dir / '07_segment_value_analysis.png'}")
plt.close()

# ============================================================================
# VISUALIZATION 8: Transaction Timeline
# ============================================================================
print("[9/10] Creating transaction timeline...")

raw_data['TransactionDate'] = pd.to_datetime(raw_data['TransactionDate'])
daily_transactions = raw_data.groupby(raw_data['TransactionDate'].dt.date).agg({
    'Amount': ['sum', 'count']
}).reset_index()
daily_transactions.columns = ['Date', 'Revenue', 'Transaction_Count']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))
fig.suptitle('Transaction Timeline Analysis', fontsize=16, fontweight='bold')

# Revenue over time
ax1.plot(daily_transactions['Date'], daily_transactions['Revenue'], 
        color='#2E86AB', linewidth=2, alpha=0.8)
ax1.fill_between(daily_transactions['Date'], daily_transactions['Revenue'], 
                 alpha=0.3, color='#2E86AB')
ax1.set_ylabel('Daily Revenue ($)', fontsize=12, fontweight='bold')
ax1.set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Transaction count over time
ax2.plot(daily_transactions['Date'], daily_transactions['Transaction_Count'], 
        color='#A23B72', linewidth=2, alpha=0.8)
ax2.fill_between(daily_transactions['Date'], daily_transactions['Transaction_Count'], 
                 alpha=0.3, color='#A23B72')
ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
ax2.set_ylabel('Transaction Count', fontsize=12, fontweight='bold')
ax2.set_title('Daily Transaction Count Trend', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(output_dir / "08_transaction_timeline.png", dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_dir / '08_transaction_timeline.png'}")
plt.close()

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================
print("[10/10] Generating summary statistics...")
print()
print("="*80)
print("DETAILED ANALYSIS SUMMARY")
print("="*80)
print()

print("📊 DATASET OVERVIEW")
print("-" * 80)
print(f"Total Customers: {len(rfm_df):,}")
print(f"Total Transactions: {len(raw_data):,}")
print(f"Total Revenue: ${raw_data['Amount'].sum():,.2f}")
print(f"Date Range: {raw_data['TransactionDate'].min().date()} to {raw_data['TransactionDate'].max().date()}")
print()

print("📈 RFM STATISTICS")
print("-" * 80)
print(f"Recency (days):")
print(f"  - Mean: {rfm_df['Recency'].mean():.1f}")
print(f"  - Median: {rfm_df['Recency'].median():.1f}")
print(f"  - Min: {rfm_df['Recency'].min():.1f}, Max: {rfm_df['Recency'].max():.1f}")
print()
print(f"Frequency (purchases):")
print(f"  - Mean: {rfm_df['Frequency'].mean():.1f}")
print(f"  - Median: {rfm_df['Frequency'].median():.1f}")
print(f"  - Min: {rfm_df['Frequency'].min():.1f}, Max: {rfm_df['Frequency'].max():.1f}")
print()
print(f"Monetary ($):")
print(f"  - Mean: ${rfm_df['Monetary'].mean():.2f}")
print(f"  - Median: ${rfm_df['Monetary'].median():.2f}")
print(f"  - Min: ${rfm_df['Monetary'].min():.2f}, Max: ${rfm_df['Monetary'].max():.2f}")
print()

print("🎯 SEGMENTATION RESULTS")
print("-" * 80)
for segment, count in segment_counts.items():
    pct = (count / len(segmented_df)) * 100
    avg_value = segmented_df[segmented_df['Segment'] == segment]['Monetary'].mean()
    total_value = segmented_df[segmented_df['Segment'] == segment]['Monetary'].sum()
    print(f"{segment}:")
    print(f"  - Customers: {count:,} ({pct:.1f}%)")
    print(f"  - Avg Value: ${avg_value:.2f}")
    print(f"  - Total Value: ${total_value:,.2f}")
    print()

print("="*80)
print("✓ All visualizations created successfully!")
print(f"✓ Saved to: {output_dir.absolute()}")
print("="*80)
