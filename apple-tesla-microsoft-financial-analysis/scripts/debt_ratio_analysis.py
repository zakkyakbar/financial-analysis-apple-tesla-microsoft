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
# CALCULATE DEBT RATIO
# =================================

df["Debt Ratio"] = df["Total Liabilities in USD"] / df["Total Assets in USD"]

print("===== DEBT RATIO DATA =====")

debt_ratio_data = df[["Company", "Year", "Debt Ratio"]]

print(debt_ratio_data)
print()

# =================================
# SAVE CSV OUTPUT
# =================================

debt_ratio_data.to_csv("../outputs/debt_ratio_data.csv", index=False)

print("Debt ratio data saved to outputs/debt_ratio_data.csv\n")

# =================================
# AVERAGE DEBT RATIO PER COMPANY
# =================================

print("===== AVERAGE DEBT RATIO PER COMPANY =====")

avg_debt_ratio = df.groupby("Company")["Debt Ratio"].mean().reset_index()

print(avg_debt_ratio)
print()

# simpan hasil
avg_debt_ratio.to_csv("../outputs/average_debt_ratio_per_company.csv", index=False)

print("Average debt ratio saved to outputs/average_debt_ratio_per_company.csv\n")

# =================================
# DEBT RATIO CHART
# =================================

for company in df["Company"].unique():

    company_data = df[df["Company"] == company]

    plt.plot(
        company_data["Year"],
        company_data["Debt Ratio"],
        marker="o",
        label=company
    )

plt.title("Debt Ratio Comparison (2022-2024)")
plt.xlabel("Year")
plt.ylabel("Debt Ratio")
plt.legend()
plt.grid(True)

# simpan chart
plt.savefig("../charts/debt_ratio_trend.png")

print("Debt ratio chart saved to charts/debt_ratio_trend.png\n")
print("Debt ratio analysis completed successfully.")
