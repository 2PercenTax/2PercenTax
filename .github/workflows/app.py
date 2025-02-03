import streamlit as st

def calculate_savings(current_tax, transaction_tax):
    return current_tax - transaction_tax

st.title("2% Transaction Tax Savings Calculator")

# User input for annual earnings
annual_income = st.number_input("Enter your annual earnings ($):", min_value=0, value=50000, step=1000)

# Calculate current tax burden (estimate: 20% of earnings)
current_tax = annual_income * 0.2

# Calculate transaction tax (2% on deposits + estimated spending breakdown)
deposit_tax = annual_income * 0.02

# Assume 90% of income is spent on taxable transactions
spent_amount = annual_income * 0.9
spending_tax = spent_amount * 0.02

# Total tax under 2% system
total_transaction_tax = deposit_tax + spending_tax

# Calculate savings
savings = calculate_savings(current_tax, total_transaction_tax)

st.write(f"### Current Tax System: You pay approximately **${current_tax:,.2f}** in taxes annually.")
st.write(f"### 2% Transaction Tax System: You would pay **${total_transaction_tax:,.2f}** in total taxes.")
st.write(f"### Your Estimated Savings: **${savings:,.2f}** per year!")
