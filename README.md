# 🚕 Ola Ride Insights Dashboard

### A comprehensive data analytics project analyzing ride-sharing data to derive actionable business insights.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ola-ride123.streamlit.app/)  This project is a complete, end-to-end data analytics solution built in a single day. It processes raw ride data, performs SQL-based analysis, and presents the findings in a live, interactive, multi-page web application.

## 📊 Dashboard Preview

![Dashboard Preview](![Uploading Screenshot 2025-09-27 231336.png…]()
)

## ✨ Key Features

* **Multi-Page Interface:** A clean, professional UI with sidebar navigation for different analysis sections.
* **Live KPIs:** Key Performance Indicators on the Home page provide an immediate overview of business health (Total Revenue, Total Rides, Average Ratings).
* **Embedded Power BI Report:** A fully interactive and live Power BI dashboard is embedded for deep-dive analysis.
* **Detailed Interactive Charts:** A dedicated page with Plotly charts that can be filtered by vehicle type.
* **Raw Data View:** An expandable view of all the key SQL query results, allowing for transparent data validation.
* **Professional UI/UX:** Features a custom, responsive design with a modern aesthetic, including an animated background and styled content cards.

## 🛠️ Tech Stack

* **Language:** Python
* **Data Manipulation:** Pandas
* **Database:** SQLite
* **Dashboarding & Visualization:** Streamlit, Power BI, Plotly
* **Version Control & Deployment:** Git, GitHub, Streamlit Community Cloud

## 🚀 How to Run Locally

To run this project on your own machine, please follow these steps:

**Prerequisites:**
* Python 3.8+
* Git


**1. Clone the repository:**
```bash
git clone [https://github.com/Manollekha/OLA-RIDE.git](https://github.com/Manollekha/OLA-RIDE.git)
cd OLA-RIDE

2. Create a virtual environment (recommended):

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install the required dependencies:

pip install -r requirements.txt

4. Run the Streamlit application:

streamlit run app.py

The application will open in your web browser at http://localhost:8501.

📂 Project Structure
├── OLA/
│   ├── app.py                  # Main Streamlit application script
│   ├── ola.db                  # SQLite database with cleaned data
│   ├── requirements.txt        # Python dependencies for deployment
│   ├── OLA.pbix                # Power BI dashboard source file
│   ├── ola_data_final.csv      # The final cleaned dataset
│   ├── (utility_scripts)/      # Helper scripts for data cleaning, etc.
│   └── ...

---

### **Final Step: Update Your GitHub Repository**

After you create the `README.md` file and add your `screenshot.png`, go to your terminal in the `OLA` folder and run these final commands to update your GitHub repository:

```bash
git add README.md screenshot.png
git commit -m "Add final project README with documentation and screenshot"
git push origin main
