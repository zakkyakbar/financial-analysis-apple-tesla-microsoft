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
# REVENUE DATA
# =================================

print("===== REVENUE DATA =====")

revenue_data = df[["Company", "Year", "Total Revenue in USD"]]

print(revenue_data)
print()

# =================================
# SAVE CSV OUTPUT
# =================================

revenue_data.to_csv("../outputs/revenue_data.csv", index=False)

print("Revenue data saved to outputs/revenue_data.csv\n")

# =================================
# AVERAGE REVENUE PER COMPANY
# =================================

print("===== AVERAGE REVENUE PER COMPANY =====")

avg_revenue = df.groupby("Company")["Total Revenue in USD"].mean().reset_index()

print(avg_revenue)
print()

# simpan hasil
avg_revenue.to_csv("../outputs/average_revenue_per_company.csv", index=False)

print("Average revenue saved to outputs/average_revenue_per_company.csv\n")

# =================================
# REVENUE CHART
# =================================

for company in df["Company"].unique():

    company_data = df[df["Company"] == company]

    plt.plot(
        company_data["Year"],
        company_data["Total Revenue in USD"],
        marker="o",
        label=company
    )

plt.title("Revenue Growth Comparison (2022-2024)")
plt.xlabel("Year")
plt.ylabel("Revenue (USD)")
plt.legend()
plt.grid(True)

# simpan chart
plt.savefig("../charts/revenue_growth.png")

print("Revenue chart saved to charts/revenue_growth.png\n")
print("Revenue analysis completed successfully.")
