import pandas as pd
import sqlite3

# --- Configuration ---
DATABASE_FILE = 'ola.db'

# --- A list to hold all our queries with their titles ---
queries = [
    (
        "1. Retrieve all successful bookings (first 5 rows):",
        """
        SELECT *
        FROM rides
        WHERE Booking_Status = 'Completed'
        LIMIT 5;
        """
    ),
    (
        "2. Find the average ride distance for each vehicle type:",
        """
        SELECT
          Vehicle_Type,
          AVG(Ride_Distance) AS Average_Distance
        FROM rides
        WHERE Booking_Status = 'Completed'
        GROUP BY Vehicle_Type
        ORDER BY Average_Distance DESC;
        """
    ),
    (
        "3. Get the total number of cancelled rides by customers:",
        """
        SELECT COUNT(*) AS Total_Customer_Cancellations
        FROM rides
        WHERE Booking_Status = 'Cancelled' AND Canceled_Rides_by_Customer != 'Not Applicable';
        """
    ),
    (
        "4. List the top 5 customers who booked the highest number of rides:",
        """
        SELECT
          Customer_ID,
          COUNT(Booking_ID) AS Number_of_Rides
        FROM rides
        GROUP BY Customer_ID
        ORDER BY Number_of_Rides DESC
        LIMIT 5;
        """
    ),
    (
        "5. Get the number of rides cancelled by drivers due to various issues:",
        """
        SELECT
          Canceled_Rides_by_Driver AS Cancellation_Reason,
          COUNT(*) AS Number_of_Cancellations
        FROM rides
        WHERE Canceled_Rides_by_Driver != 'Not Applicable'
        GROUP BY Canceled_Rides_by_Driver;
        """
    ),
    (
        "6. Find the maximum and minimum driver ratings for Prime Sedan bookings:",
        """
        SELECT
          MAX(Driver_Ratings) AS Max_Driver_Rating,
          MIN(Driver_Ratings) AS Min_Driver_Rating
        FROM rides
        WHERE Vehicle_Type = 'Prime Sedan' AND Booking_Status = 'Completed';
        """
    ),
    (
        "7. Retrieve all rides where payment was made using UPI (first 5 rows):",
        """
        SELECT *
        FROM rides
        WHERE Payment_Method = 'UPI'
        LIMIT 5;
        """
    ),
    (
        "8. Find the average customer rating per vehicle type:",
        """
        SELECT
          Vehicle_Type,
          AVG(Customer_Rating) AS Average_Customer_Rating
        FROM rides
        WHERE Booking_Status = 'Completed'
        GROUP BY Vehicle_Type
        ORDER BY Average_Customer_Rating DESC;
        """
    ),
    (
        "9. Calculate the total booking value of rides completed successfully:",
        """
        SELECT SUM(Booking_Value) AS Total_Booking_Value
        FROM rides
        WHERE Booking_Status = 'Completed';
        """
    ),
    (
        "10. List all incomplete rides along with the reason (first 5 rows):",
        """
        SELECT
          Booking_ID,
          Incomplete_Rides_Reason
        FROM rides
        WHERE Incomplete_Rides = 'Yes'
        LIMIT 5;
        """
    )
]

# --- Main script execution ---
conn = None  # Initialize connection to None
try:
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE_FILE)
    print(f"Successfully connected to the database '{DATABASE_FILE}'\n")

    # Loop through the list of queries and execute each one
    for title, query in queries:
        print(f"--- {title} ---")
        
        # Use pandas to execute the query and fetch results
        df_result = pd.read_sql_query(query, conn)
        
        # Print the result DataFrame
        if df_result.empty:
            print("No results found.")
        else:
            print(df_result.to_string()) # .to_string() ensures the full table is printed
            
        print("\n" + "="*50 + "\n") # Separator for clarity

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the database connection is closed
    if conn:
        conn.close()
        print("Database connection closed.")