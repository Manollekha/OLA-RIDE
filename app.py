import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ola Ride Insights",
    page_icon="🚕",
    layout="wide"
)

# --- DATABASE CONNECTION & DATA LOADING ---
@st.cache_data
def load_data():
    """Function to load the entire rides table from the database."""
    with sqlite3.connect('ola.db') as conn:
        return pd.read_sql_query("SELECT * FROM rides", conn)

# Load all the data once
df = load_data()

# --- ADVANCED STYLING ---
st.markdown("""
<style>
    /* Animated Gradient Background */
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(-45deg, #001f3f, #0074D9, #7FDBFF, #39CCCC);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    /* Content Block Styling */
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.9); /* White with 90% opacity */
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .st-emotion-cache-16txtl3 {
        background-color: rgba(240, 242, 246, 0.9); /* Light grey with 90% opacity */
    }

    /* Custom KPI Card Styling */
    .kpi-card {
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .kpi-card h3 { margin: 0; font-size: 1.2rem; font-weight: 300; }
    .kpi-card p { margin: 0; font-size: 2.5rem; font-weight: 700; }
    .kpi-card-1 { background: linear-gradient(45deg, #FF416C, #FF4B2B); }
    .kpi-card-2 { background: linear-gradient(45deg, #11998e, #38ef7d); }
    .kpi-card-3 { background: linear-gradient(45deg, #2980B9, #6DD5FA); }

    /* Page Header Styling */
    .page-header {
        background-color: #001f3f; color: white; padding: 1rem; border-radius: 10px; margin-bottom: 2rem; text-align: center;
    }
    .page-header h2 { margin: 0; }
    
    /* Hide Streamlit footer */
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR FOR NAVIGATION ---
with st.sidebar:
    st.title("🚕 Ola Ride Insights")
    st.markdown("---")
    page = st.radio("Choose a Page", ["Home", "Power BI Dashboard", "Detailed Analysis", "Raw Data View"])
    st.markdown("---")
    st.info(f"Project for OLA. Current Time: {pd.Timestamp.now(tz='Asia/Kolkata').strftime('%I:%M %p, %d-%b-%Y')}")

# --- PAGE 1: HOME ---
if page == "Home":
    st.markdown("<div class='page-header'><h2>🏠 Home: Project Overview</h2></div>", unsafe_allow_html=True)
    st.markdown("Welcome to the Ola Ride Insights dashboard...")
    st.subheader("Overall Key Metrics")

    successful_rides_df = df[df['Booking_Status'] == 'Success']
    total_value = successful_rides_df['Booking_Value'].sum()
    total_rides = len(successful_rides_df)
    avg_rating = successful_rides_df['Customer_Rating'].mean() if not successful_rides_df.empty else 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="kpi-card kpi-card-1"><h3>Total Revenue</h3><p>₹ {total_value:,.0f}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="kpi-card kpi-card-2"><h3>Total Successful Rides</h3><p>{total_rides:,}</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="kpi-card kpi-card-3"><h3>Average Customer Rating</h3><p>{avg_rating:.2f} ⭐</p></div>', unsafe_allow_html=True)

# --- PAGE 2: POWER BI DASHBOARD ---
elif page == "Power BI Dashboard":
    st.markdown("<div class='page-header'><h2>📊 Power BI Dashboard</h2></div>", unsafe_allow_html=True)
    power_bi_embed_code = """<iframe title="OLA" width="100%" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiYTIzM2FiMzYtMjk3Zi00ZjI5LTlmNDYtMTMwMDRiODkyOGMxIiwidCI6Ijc5ZjBjMGNkLWEyZmYtNGRkMS1hN2ZkLTQxODliOGQ1MDUwMCJ9" frameborder="0" allowFullScreen="true"></iframe>"""
    st.components.v1.html(power_bi_embed_code, height=600, scrolling=True)

# --- PAGE 3: DETAILED ANALYSIS ---
elif page == "Detailed Analysis":
    st.markdown("<div class='page-header'><h2>📈 Detailed Analysis</h2></div>", unsafe_allow_html=True)
    vehicle_options = df['Vehicle_Type'].unique().tolist()
    selected_vehicle = st.selectbox("Select a Vehicle Type to Filter", ["All"] + vehicle_options)
    filtered_df = df if selected_vehicle == "All" else df[df['Vehicle_Type'] == selected_vehicle]
    
    col1, col2 = st.columns(2)
    with col1:
        revenue_df = filtered_df.groupby('Payment_Method')['Booking_Value'].sum().reset_index().rename(columns={'Booking_Value': 'Total_Revenue'})
        fig_revenue = px.bar(revenue_df, x="Total_Revenue", y="Payment_Method", orientation='h', title=f"Revenue for {selected_vehicle}", template="plotly_white")
        st.plotly_chart(fig_revenue, use_container_width=True)
    with col2:
        status_df = filtered_df['Booking_Status'].value_counts().reset_index()
        fig_status = px.pie(status_df, names="Booking_Status", values="count", title=f"Booking Status for {selected_vehicle}", template="plotly_white")
        st.plotly_chart(fig_status, use_container_width=True)

# --- PAGE 4: RAW DATA VIEW ---
elif page == "Raw Data View":
    st.markdown("<div class='page-header'><h2>📋 Raw Data View</h2></div>", unsafe_allow_html=True)
    st.markdown("Click on any query below to see the detailed data table.")

    with st.expander("1. Retrieve all successful bookings"):
        st.dataframe(df[df['Booking_Status'] == 'Success'])
    
    with st.expander("2. Find the average ride distance for each vehicle type"):
        avg_dist_df = df[df['Booking_Status'] == 'Success'].groupby('Vehicle_Type')['Ride_Distance'].mean().reset_index()
        st.dataframe(avg_dist_df)

    with st.expander("3. Get the total number of cancelled rides by customers"):
        cancelled_by_cust = len(df[df['Canceled_Rides_by_Customer'] != 'Not Applicable'])
        st.metric("Total Rides Cancelled by Customers", f"{cancelled_by_cust:,}")

    with st.expander("4. List the top 5 customers who booked the highest number of rides"):
        top_5_customers_df = df.groupby('Customer_ID')['Booking_ID'].count().reset_index().rename(columns={'Booking_ID':'Number_of_Rides'}).nlargest(5, 'Number_of_Rides')
        st.dataframe(top_5_customers_df)

    with st.expander("5. Get the number of rides cancelled by drivers by reason"):
        cancelled_by_driver_df = df[df['Canceled_Rides_by_Driver'] != 'Not Applicable']['Canceled_Rides_by_Driver'].value_counts().reset_index()
        st.dataframe(cancelled_by_driver_df)

    with st.expander("6. Find the maximum and minimum driver ratings for Prime Sedan"):
        prime_sedan_ratings = df[(df['Vehicle_Type'] == 'Prime Sedan') & (df['Booking_Status'] == 'Success')]['Driver_Ratings'].agg(['min', 'max']).reset_index()
        st.dataframe(prime_sedan_ratings)
    
    with st.expander("7. Retrieve all rides where payment was made using UPI"):
        st.dataframe(df[df['Payment_Method'] == 'UPI'])

    with st.expander("8. Find the average customer rating per vehicle type"):
        avg_cust_rating_df = df[df['Booking_Status'] == 'Success'].groupby('Vehicle_Type')['Customer_Rating'].mean().reset_index()
        st.dataframe(avg_cust_rating_df)

    with st.expander("9. Calculate the total booking value of successful rides"):
        total_booking_value = df[df['Booking_Status'] == 'Success']['Booking_Value'].sum()
        st.metric("Total Booking Value of Successful Rides", f"₹ {total_booking_value:,.0f}")