import pandas as pd
import matplotlib.pyplot as plt

# =================================
# LOAD DATASET
# =================================

print("Loading dataset...")

df = pd.read_csv("../dataset/financial_data.csv")

print("Dataset loaded successfully\n")

# =================================
# NET INCOME DATA
# =================================

print("===== NET INCOME DATA =====")

net_income = df[["Company", "Year", "Net Income in USD"]]

print(net_income)
print()

# =================================
# SAVE NET INCOME DATA
# =================================

net_income.to_csv("../outputs/net_income_data.csv", index=False)

print("Net income data saved to outputs/net_income_data.csv\n")

# =================================
# TOTAL NET INCOME PER COMPANY
# =================================

print("===== TOTAL NET INCOME PER COMPANY =====")

net_income_company = df.groupby("Company")["Net Income in USD"].sum().reset_index()

print(net_income_company)
print()

# =================================
# SAVE NET INCOME RESULT
# =================================

net_income_company.to_csv("../outputs/net_income_per_company.csv", index=False)

print("Net income per company saved to outputs/net_income_per_company.csv\n")

# =================================
# NET INCOME CHART
# =================================

for company in df["Company"].unique():

    company_data = df[df["Company"] == company]

    plt.plot(
        company_data["Year"],
        company_data["Net Income in USD"],
        marker="o",
        label=company
    )

plt.title("Net Income Trend Comparison (2022-2024)")
plt.xlabel("Year")
plt.ylabel("Net Income (USD)")
plt.legend()
plt.grid(True)

# SAVE CHART
plt.savefig("../charts/net_income_trend.png")

print("Net income chart saved to charts/net_income_trend.png\n")
print("Net income analysis completed successfully.")
