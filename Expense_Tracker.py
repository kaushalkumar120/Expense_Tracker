import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV or use fallback data
try:
    df = pd.read_csv("expenses.csv")
    print("✅ CSV file loaded")
except FileNotFoundError:
    print("⚠ CSV not found, using sample data")
    
    data = {
        'Date': ['2024-01-15','2024-01-16','2024-01-17','2024-02-01'],
        'Category': ['Groceries','Transport','Dining','Groceries'],
        'Description': ['Shopping','Fuel','Lunch','Monthly shopping'],
        'Amount': [125.50,45.20,32.75,189.75]
    }
    df = pd.DataFrame(data)

# 2. Data Cleaning
df.dropna(subset=['Amount','Category'], inplace=True)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# 3. Total Expense
total_expense = df['Amount'].sum()

# 4. Category-wise Analysis
category_group = df.groupby('Category')['Amount'].agg(['sum','mean'])
category_group = category_group.rename(columns={
    'sum':'Total Amount',
    'mean':'Average Amount'
})

# 5. Sort
category_group = category_group.sort_values(by='Total Amount', ascending=False)

# 6. Top 5
top_5 = category_group.head(5)

# 7. Print Report
print("\n" + "="*40)
print("EXPENSE TRACKER REPORT")
print("="*40)

print(f"\nTotal Expense: ₹{total_expense:.2f}")

print("\nTop Categories:")
print(top_5)

print("="*40)

# 8. Visualization (Pie Chart)
plt.figure(figsize=(6,6))

plt.pie(
    category_group['Total Amount'],
    labels=category_group.index,
    autopct='%1.1f%%'
)

plt.title("Category-wise Expense Distribution")
plt.show()