import pandas as pd
import matplotlib.pyplot as plt

# =================================
# LOAD DATASET
# =================================

print("Loading dataset...")

df = pd.read_csv("../dataset/financial_data.csv")

print("Dataset loaded successfully\n")

# =================================
# CALCULATE PROFIT MARGIN
# =================================

df["Profit Margin"] = df["Net Income in USD"] / df["Total Revenue in USD"]

print("===== PROFIT MARGIN DATA =====")

profit_margin = df[["Company", "Year", "Profit Margin"]]

print(profit_margin)
print()

# =================================
# SAVE PROFIT MARGIN DATA
# =================================

profit_margin.to_csv("../outputs/profit_margin_data.csv", index=False)

print("Profit margin data saved to outputs/profit_margin_data.csv\n")

# =================================
# AVERAGE PROFIT MARGIN PER COMPANY
# =================================

print("===== AVERAGE PROFIT MARGIN PER COMPANY =====")

profit_margin_company = df.groupby("Company")["Profit Margin"].mean().reset_index()

print(profit_margin_company)
print()

# =================================
# SAVE RESULT
# =================================

profit_margin_company.to_csv("../outputs/profit_margin_per_company.csv", index=False)

print("Average profit margin saved to outputs/profit_margin_per_company.csv\n")

# =================================
# PROFIT MARGIN CHART
# =================================

for company in df["Company"].unique():

    company_data = df[df["Company"] == company]

    plt.plot(
        company_data["Year"],
        company_data["Profit Margin"],
        marker="o",
        label=company
    )

plt.title("Profit Margin Comparison (2022-2024)")
plt.xlabel("Year")
plt.ylabel("Profit Margin")
plt.legend()
plt.grid(True)

# SAVE CHART
plt.savefig("../charts/profit_margin_trend.png")

print("Profit margin chart saved to charts/profit_margin_trend.png\n")
print("Profit margin analysis completed successfully.")
