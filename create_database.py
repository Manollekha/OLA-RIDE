import pandas as pd
import sqlite3

# Load the cleaned data
df = pd.read_csv('ola_data_final.csv')

# Create a connection to a new SQLite database file
conn = sqlite3.connect('ola.db')

# Write the DataFrame to a SQL table named 'rides'
# if_exists='replace' means it will overwrite the table if the script is run again
df.to_sql('rides', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Database 'ola.db' created successfully with a 'rides' table.")