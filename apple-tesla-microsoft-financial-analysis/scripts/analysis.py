import pandas as pd
import matplotlib.pyplot as plt

# =================================
# LOAD DATASET
# =================================

print("Loading dataset...")

df = pd.read_csv("../dataset/financial_data.csv")

# bersihkan spasi nama kolom
df.columns = df.columns.str.strip()

# perbaiki typo kolom
df = df.rename(columns={
    "Total Liablilities in USD": "Total Liabilities in USD"
})

print("Dataset loaded successfully\n")

# =================================
# REVENUE ANALYSIS
# =================================

print("===== REVENUE ANALYSIS =====")

revenue = df[["Company","Year","Total Revenue in USD"]]

print(revenue)

revenue.to_csv("../outputs/revenue_data.csv", index=False)

# =================================
# NET INCOME ANALYSIS
# =================================

print("\n===== NET INCOME ANALYSIS =====")

net_income = df[["Company","Year","Net Income in USD"]]

print(net_income)

net_income.to_csv("../outputs/net_income_data.csv", index=False)

# =================================
# PROFIT MARGIN ANALYSIS
# =================================

print("\n===== PROFIT MARGIN ANALYSIS =====")

df["Profit Margin"] = df["Net Income in USD"] / df["Total Revenue in USD"]

profit_margin = df[["Company","Year","Profit Margin"]]

print(profit_margin)

profit_margin.to_csv("../outputs/profit_margin_data.csv", index=False)

# =================================
# DEBT RATIO ANALYSIS
# =================================

print("\n===== DEBT RATIO ANALYSIS =====")

df["Debt Ratio"] = df["Total Liabilities in USD"] / df["Total Assets in USD"]

debt_ratio = df[["Company","Year","Debt Ratio"]]

print(debt_ratio)

debt_ratio.to_csv("../outputs/debt_ratio_data.csv", index=False)

# =================================
# OPERATING CASH FLOW ANALYSIS
# =================================

print("\n===== CASH FLOW ANALYSIS =====")

cashflow = df[["Company","Year","Cash Flow from operating activities in USD"]]

print(cashflow)

cashflow.to_csv("../outputs/cashflow_data.csv", index=False)

# =================================
# SUMMARY INSIGHT
# =================================

print("\n===== SUMMARY INSIGHT =====")

avg_revenue = df.groupby("Company")["Total Revenue in USD"].mean()
avg_profit = df.groupby("Company")["Profit Margin"].mean()

print("\nAverage Revenue by Company:")
print(avg_revenue)

print("\nAverage Profit Margin by Company:")
print(avg_profit)

# =================================
# CHART REVENUE
# =================================

for company in df["Company"].unique():

    data = df[df["Company"] == company]

    plt.plot(
        data["Year"],
        data["Total Revenue in USD"],
        marker="o",
        label=company
    )

plt.title("Revenue Growth Comparison")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)

plt.savefig("../charts/revenue_growth.png")
print("\nAnalysis completed successfully.")
