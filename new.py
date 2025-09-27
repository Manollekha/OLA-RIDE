import pandas as pd

try:
    # Load the partially cleaned dataset you created in the last step
    df = pd.read_csv('ola_data_cleaned.csv')
    print("Loaded 'ola_data_cleaned.csv' successfully.")
except FileNotFoundError:
    print("Error: 'ola_data_cleaned.csv' not found. Make sure it's in the same folder.")
    exit()

# --- Step 1: Drop Irrelevant Columns ---
# 'Unnamed: 20' is completely empty and 'Vehicle Images' is not needed for this analysis.
df.drop(columns=['Unnamed: 20', 'Vehicle Images'], inplace=True)
print("Dropped 'Unnamed: 20' and 'Vehicle Images' columns.")

# --- Step 2: Combine Date and Time into a Single Datetime Column ---
# This is crucial for any time-based analysis.
df['booking_timestamp'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce')
df.drop(columns=['Date', 'Time'], inplace=True) # Drop the original columns
print("Combined 'Date' and 'Time' into a single 'booking_timestamp' column.")

# --- Step 3: Logically Handle Categorical Missing Data ---
# For these columns, a blank value often means the event didn't happen.
# We will fill them with a clear description like 'Not Applicable'.
categorical_na_cols = [
    'Canceled_Rides_by_Customer',
    'Canceled_Rides_by_Driver',
    'Incomplete_Rides',
    'Incomplete_Rides_Reason'
]
for col in categorical_na_cols:
    if col in df.columns:
        df[col].fillna('Not Applicable', inplace=True)
print("Filled missing categorical data with 'Not Applicable'.")

# --- Step 4: Address Missing Payment Method ---
# We can assume that rides with missing payment methods were canceled before completion.
if 'Payment_Method' in df.columns:
    df['Payment_Method'].fillna('Not Available', inplace=True)
    print("Filled missing 'Payment_Method' with 'Not Available'.")

# --- Final Step: Save the Fully Cleaned Data ---
df.to_csv('ola_data_final.csv', index=False)

print("\n--- Refined Cleaning Complete! ---")
print("Final Data Info:")
df.info()
print("\nFully cleaned data saved to 'ola_data_final.csv'.")
print("This is the file you will use for the rest of the project.")