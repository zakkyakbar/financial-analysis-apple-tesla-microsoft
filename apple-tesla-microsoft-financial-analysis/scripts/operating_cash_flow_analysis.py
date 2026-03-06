import pandas as pd
import matplotlib.pyplot as plt

# =================================
# LOAD DATASET
# =================================

print("Loading dataset...")

df = pd.read_csv("../dataset/financial_data.csv")

# bersihkan spasi pada nama kolom
df.columns = df.columns.str.strip()

# perbaiki typo kolom
df = df.rename(columns={
    "Total Liablilities in USD": "Total Liabilities in USD"
})

print("Dataset loaded successfully\n")

# =================================
# CASH FLOW DATA
# =================================

print("===== OPERATING CASH FLOW DATA =====")

cashflow_data = df[["Company", "Year", "Cash Flow from operating activities in USD"]]

print(cashflow_data)
print()

# =================================
# SAVE CSV OUTPUT
# =================================

cashflow_data.to_csv("../outputs/cashflow_data.csv", index=False)

print("Cash flow data saved to outputs/cashflow_data.csv\n")

# =================================
# AVERAGE CASH FLOW PER COMPANY
# =================================

print("===== AVERAGE CASH FLOW PER COMPANY =====")

avg_cashflow = df.groupby("Company")["Cash Flow from operating activities in USD"].mean().reset_index()

print(avg_cashflow)
print()

avg_cashflow.to_csv("../outputs/average_cashflow_per_company.csv", index=False)

print("Average cash flow saved to outputs/average_cashflow_per_company.csv\n")

# =================================
# CASH FLOW CHART
# =================================

for company in df["Company"].unique():

    company_data = df[df["Company"] == company]

    plt.plot(
        company_data["Year"],
        company_data["Cash Flow from operating activities in USD"],
        marker="o",
        label=company
    )

plt.title("Operating Cash Flow Comparison (2022-2024)")
plt.xlabel("Year")
plt.ylabel("Operating Cash Flow (USD)")
plt.legend()
plt.grid(True)

# simpan chart
plt.savefig("../charts/cashflow_trend.png")

print("Cash flow chart saved to charts/cashflow_trend.png\n")
print("Cash flow analysis completed successfully.")
