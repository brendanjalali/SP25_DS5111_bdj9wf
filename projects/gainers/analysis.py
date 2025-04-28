import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='bdj9wf@virginia.edu',
    password='DS5111bdj9wf',
    account='rja95216',
    warehouse='COMPUTE_WH',
    database='DATA_SCIENCE',
    schema='bdj9wf',
    role='DS5111_DBT'
)

# Query the symbol_gb_analysis table
query = "SELECT * FROM symbol_gb_analysis"

# Load the results into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Standardize column names to lowercase
df.columns = df.columns.str.lower()

# Now you can use df for plotting
print(df.head())

# Example simple plot: Top 10 symbols by average percent change
top10 = df.sort_values(by="avg_percent_change", ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x="avg_percent_change", y="symbol", data=top10, palette="viridis")
plt.title("Top 10 Symbols by Average % Change")
plt.xlabel("Average % Change")
plt.ylabel("Symbol")
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig("top10_symbols.png")

print("Plot saved to top10_symbols.png")
