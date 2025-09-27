import pandas as pd
import sqlite3

print("--- Running Data Diagnostic ---")
try:
    # Connect to the database
    conn = sqlite3.connect('ola.db')
    print("Connected to ola.db successfully.")

    # This query will count every unique value in the Booking_Status column
    query = "SELECT Booking_Status, COUNT(*) as count FROM rides GROUP BY Booking_Status;"

    df = pd.read_sql_query(query, conn)
    conn.close()

    print("\nHere are the unique values and their counts in the 'Booking_Status' column:")
    print(df.to_string())
    print("\n---------------------------------")

except Exception as e:
    print(f"\nAn error occurred: {e}")