import streamlit as st
from datetime import datetime # To get current month and year

# --- CSS Definitions ---

# CSS for the "Slashy" Light Theme (adapted from previous version)
CSS_LIGHT_SLASHY = """
<style>
/* Base App Styling - Light Theme */
.stApp {
    background-color: #f8f9fa; /* Light, clean background */
    color: #212529; /* Dark text for readability */
}

/* Headers Styling */
h1 {
    color: #007bff; /* Primary Blue - strong and professional */
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin-bottom: 1rem;
}
h2 {
    color: #007bff; /* Primary Blue */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    border-bottom: 2px solid #007bff;
    padding-bottom: 8px;
    margin-top: 30px;
    margin-bottom: 20px;
}
h3 {
    color: #495057; /* Darker grey for sub-headers */
    font-family: 'Arial', sans-serif;
    margin-top: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Metric Styling - for the results dashboard */
div[data-testid="stMetric"] {
    background-color: #ffffff; /* White background for metric cards */
    border: 1px solid #dee2e6; /* Light grey border */
    border-left: 5px solid #007bff; /* Accent border on the left for a "slashy" touch */
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); /* Subtle shadow */
}
div[data-testid="stMetric"] > label[data-testid="stMetricLabel"] > div {
    font-weight: bold;
    color: #007bff; /* Accent color for metric labels */
    text-transform: uppercase;
}
div[data-testid="stMetric"] p { /* Metric value */
    color: #212529; /* Dark text for metric value */
    font-size: 2em;
}
div[data-testid="stMetric"] div[data-testid="stMetricDelta"] { /* Metric delta */
    color: #495057 !important; /* Ensure good contrast for delta text */
}

/* Input Widget Styling */
.stTextInput label, .stNumberInput label, .stRadio label, .stSelectbox label {
    color: #007bff !important; /* Accent color for labels */
    font-weight: 600;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
div[data-testid="stNumberInput"] input, div[data-testid="stTextInput"] input {
    background-color: #ffffff; /* White input background */
    color: #212529; /* Dark text in input */
    border: 1px solid #ced4da; /* Standard input border */
    border-radius: 5px;
}
div[data-testid="stNumberInput"] input:focus, div[data-testid="stTextInput"] input:focus {
    border-color: #007bff; /* Accent color on focus */
    box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25); /* Focus glow */
}
div[data-testid="stRadio"] label div {
     color: #212529 !important; /* Text next to radio button */
}

/* Button Styling - Keeping it consistent with the primary accent */
.stButton>button.theme-button { /* Specific class for theme button if needed, or general for all */
    background-color: #6c757d; /* Secondary grey for theme button */
    color: white;
}
.stButton>button.theme-button:hover {
    background-color: #5a6268;
}
.stButton>button { /* Default button style - will be overridden by specific classes if any */
    background-color: #007bff; /* Primary Blue */
    color: white;
    border-radius: 5px;
    padding: 10px 24px; /* Adjusted padding */
    font-weight: bold;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    border: none;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    margin-top: 5px; /* Add some margin for standalone buttons */
}
.stButton>button:hover:not(.theme-button) {
    background-color: #0056b3; /* Darker blue on hover */
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    transform: translateY(-1px);
}


/* Cost Breakdown Section Styling */
.cost-breakdown {
    background-color: #ffffff; /* White background */
    color: #212529;
    padding: 25px;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    border-left: 5px solid #007bff; /* Accent border consistent with metrics */
    margin-top: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}
.cost-breakdown ul {
    list-style-type: none;
    padding-left: 0;
}
.cost-breakdown li {
    padding: 10px 0;
    border-bottom: 1px solid #e9ecef; /* Lighter separator */
    font-family: 'Consolas', 'Monaco', monospace;
}
.cost-breakdown li:last-child {
    border-bottom: none;
}
.cost-breakdown strong {
    color: #28a745; /* Green for positive cost values - good contrast */
    font-weight: bold;
}

/* Custom Horizontal Rule */
.slashy-hr {
    border: none;
    height: 1px; /* Thinner for light theme */
    background: linear-gradient(to right, transparent, #007bff, transparent);
    margin-top: 30px; /* Adjusted margin */
    margin-bottom: 30px; /* Adjusted margin */
}

/* Footer Styling */
.footer {
    text-align: center;
    color: #6c757d; /* Standard footer grey */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 0.9em;
    padding-top: 20px; /* Adjusted padding */
    margin-top: 30px; /* Ensure space before footer */
    border-top: 1px solid #e9ecef; /* Light top border for footer */
}
</style>
"""

# CSS for the "Slashy" Dark Theme (adapted from previous version)
CSS_DARK_SLASHY = """
<style>
/* Base App Styling - Dark Theme */
.stApp {
    background-color: #1a1a2e; /* Dark desaturated blue */
    color: #e0e0e0; /* Light grey text for readability */
}

/* Headers Styling */
h1 {
    color: #00A9FF; /* Bright Electric Blue */
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
    text-shadow: 0 0 8px rgba(0, 169, 255, 0.7); /* Adjusted Neon-like glow */
    margin-bottom: 1rem; /* Add space below title */
}
h2 {
    color: #00A9FF; /* Bright Electric Blue */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    border-bottom: 2px solid #00A9FF;
    padding-bottom: 8px;
    margin-top: 30px;
    margin-bottom: 20px; /* Space after header */
}
h3 {
    color: #c0c0c0; /* Lighter grey for sub-headers */
    font-family: 'Arial', sans-serif;
    margin-top: 20px;
    text-transform: uppercase; 
    letter-spacing: 1px; 
}

/* Metric Styling */
div[data-testid="stMetric"] {
    background-color: #232946; /* Slightly lighter dark shade for metric cards */
    border: 1px solid #00A9FF; /* Electric blue border */
    border-radius: 10px; 
    padding: 20px;
    box-shadow: 0 0 12px rgba(0, 169, 255, 0.25); /* Adjusted Glow effect */
}
div[data-testid="stMetric"] > label[data-testid="stMetricLabel"] > div { 
    font-weight: bold;
    color: #00A9FF; 
    text-transform: uppercase;
}
div[data-testid="stMetric"] p { /* Metric value */
    color: #FFFFFF; 
    font-size: 2em; 
}
div[data-testid="stMetric"] div[data-testid="stMetricDelta"] { /* Metric delta */
    color: #e0e0e0 !important; /* Light grey delta text */
}

/* Input Widget Styling */
.stTextInput label, .stNumberInput label, .stRadio label, .stSelectbox label {
    color: #00A9FF !important; /* Electric blue labels */
    font-weight: 600;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
div[data-testid="stNumberInput"] input, div[data-testid="stTextInput"] input {
    background-color: #232946; /* Dark input background */
    color: #e0e0e0; /* Light text in input */
    border: 1px solid #00A9FF;
    border-radius: 5px;
}
div[data-testid="stRadio"] label div {
     color: #e0e0e0 !important; /* Text next to radio button */
}

/* Button Styling */
.stButton>button.theme-button {
    background: #3b3b58; /* Darker grey for theme button in dark mode */
    color: #00A9FF; /* Accent text color */
    border: 1px solid #00A9FF;
}
.stButton>button.theme-button:hover {
    background: #00A9FF;
    color: #1a1a2e;
}
.stButton>button { /* Default button style */
    background: linear-gradient(45deg, #00A9FF, #0078FF); 
    color: white;
    border-radius: 5px;
    padding: 10px 24px; /* Adjusted padding */
    font-weight: bold;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    border: none;
    box-shadow: 0 0 8px rgba(0, 169, 255, 0.4); /* Adjusted shadow */
    transition: all 0.3s ease; 
    margin-top: 5px;
}
.stButton>button:hover:not(.theme-button) {
    background: linear-gradient(45deg, #0078FF, #00A9FF);
    box-shadow: 0 0 12px rgba(0, 169, 255, 0.6); /* Adjusted shadow */
    transform: translateY(-1px); 
}

/* Cost Breakdown Section Styling */
.cost-breakdown {
    background-color: #232946; 
    color: #e0e0e0; 
    padding: 25px;
    border-radius: 10px;
    border: 1px solid #00A9FF; 
    margin-top: 15px;
    box-shadow: 0 0 12px rgba(0, 169, 255, 0.25); /* Adjusted shadow */
}
.cost-breakdown ul {
    list-style-type: none;
    padding-left: 0;
}
.cost-breakdown li {
    padding: 10px 0;
    border-bottom: 1px dashed #3b3b58; 
    font-family: 'Consolas', 'Monaco', monospace; 
}
.cost-breakdown li:last-child {
    border-bottom: none;
}
.cost-breakdown strong {
    color: #00F5D4; /* Teal for cost values */
    font-weight: bold;
}

/* Custom Horizontal Rule */
.slashy-hr {
    border: none;
    height: 2px;
    background: linear-gradient(to right, transparent, #00A9FF, transparent); 
    margin-top: 30px; /* Adjusted margin */
    margin-bottom: 30px; /* Adjusted margin */
}

/* Footer Styling */
.footer {
    text-align: center;
    color: #00A9FF; /* Accent color for footer in dark mode */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 0.9em;
    padding-top: 20px; /* Adjusted padding */
    margin-top: 30px; /* Ensure space before footer */
    border-top: 1px solid #3b3b58; 
}
</style>
"""

def run_streamlit_calculator_themed():
    # --- Initialize Session State for Theme ---
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'  # Default to light theme

    # --- Page Configuration (Page title is now consistent) ---
    st.set_page_config(page_title="3D Print Profit Calculator (INR)", layout="wide", initial_sidebar_state="collapsed")

    # --- Apply Chosen Theme ---
    if st.session_state.theme == 'light':
        st.markdown(CSS_LIGHT_SLASHY, unsafe_allow_html=True)
    else:
        st.markdown(CSS_DARK_SLASHY, unsafe_allow_html=True)

    # --- Theme Switcher Button ---
    # Placed after the main title, before the first HR
    cols_title_button = st.columns([0.85, 0.15]) # Create columns for title and button
    with cols_title_button[0]:
         st.markdown("<h1>⚡ Bambu Lab P1S - PLA Profit Calculator 🇮🇳</h1>", unsafe_allow_html=True)
    with cols_title_button[1]:
        button_label = "🌙 Dark Mode" if st.session_state.theme == 'light' else "☀️ Light Mode"
        button_help = "Switch to Dark Theme" if st.session_state.theme == 'light' else "Switch to Light Theme"
        if st.button(button_label, key="theme_switcher_button", help=button_help, use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun() # Crucial to re-render the app with the new theme CSS

    st.markdown("<div class='slashy-hr'></div>", unsafe_allow_html=True)

    # --- Layout for Inputs ---
    st.markdown("<h2>INPUT PARAMETERS</h2>", unsafe_allow_html=True)
    
    input_col1, input_col2 = st.columns(2)

    with input_col1:
        st.markdown("<h3>Revenue & Print Specs</h3>", unsafe_allow_html=True)
        selling_price_inr = st.number_input(
            "Selling Price for this Print (₹)",
            min_value=0.0, value=500.0, step=50.0, format="%.2f"
        )
        material_used_grams = st.number_input(
            "PLA Material Used (grams)",
            min_value=0.0, value=50.0, step=1.0, format="%.2f",
            help="Get this from your slicer software."
        )
        print_duration_hours = st.number_input(
            "Print Duration (hours)",
            min_value=0.0, value=3.0, step=0.25, format="%.2f",
            help="Total time your printer is running."
        )

    with input_col2:
        st.markdown("<h3>Material & Energy Costs</h3>", unsafe_allow_html=True)
        pla_spool_cost_inr = st.number_input(
            "Cost of 1kg PLA Filament Spool (₹)",
            min_value=0.0, value=1200.0, step=100.0,
            help="Typical 1kg PLA spools in India: ₹1000-₹2000."
        )
        printer_wattage_p1s = st.number_input(
            "Printer Avg. Power Consumption (Watts)",
            min_value=0, value=180, step=10,
            help="Bambu Lab P1S average (e.g., 150-200W)."
        )
        electricity_cost_per_kwh_inr = st.number_input(
            "Your Electricity Cost per kWh (₹)",
            min_value=0.0, value=7.0, step=0.50, format="%.2f",
            help="Check your bill. India average: ~₹5-8/kWh."
        )

    st.markdown("<br>", unsafe_allow_html=True) 
    st.markdown("<h3>Labor & Operational Costs</h3>", unsafe_allow_html=True)
    
    op_costs_col1, op_costs_col2 = st.columns([0.4, 1.6]) 

    with op_costs_col1:
        include_labor = st.radio("Include Labor Costs?", ("Yes", "No"), index=1, key="labor_radio_themed")

    labor_cost_for_print_inr = 0.0
    if include_labor == "Yes":
        with op_costs_col2: 
            lab_hr_col, lab_rate_col = st.columns(2)
            with lab_hr_col:
                labor_hours = st.number_input("Total Labor Hours", min_value=0.0, value=0.5, step=0.25, format="%.2f")
            with lab_rate_col:
                labor_hourly_rate_inr = st.number_input("Hourly Labor Rate (₹)", min_value=0.0, value=150.0, step=10.0, format="%.2f")
            labor_cost_for_print_inr = labor_hours * labor_hourly_rate_inr
    
    other_costs_per_print_inr = st.number_input(
        "Other Fixed Costs per Print (₹)",
        min_value=0.0, value=20.0, step=5.0, format="%.2f",
        help="Wear & tear, consumables, software amortization per print."
    )

    st.markdown("<div class='slashy-hr'></div>", unsafe_allow_html=True)

    # --- Calculations ---
    cost_per_gram_pla = (pla_spool_cost_inr / 1000) if pla_spool_cost_inr > 0 else 0
    material_cost_for_print_inr = cost_per_gram_pla * material_used_grams

    kwh_used = (printer_wattage_p1s / 1000) * print_duration_hours
    electricity_cost_for_print_inr = kwh_used * electricity_cost_per_kwh_inr

    total_cost_for_print_inr = (
        material_cost_for_print_inr +
        electricity_cost_for_print_inr +
        labor_cost_for_print_inr +
        other_costs_per_print_inr
    )
    profit_for_print_inr = selling_price_inr - total_cost_for_print_inr
    profit_margin_percentage = (profit_for_print_inr / selling_price_inr * 100) if selling_price_inr > 0 else 0

    # --- Display Results ---
    st.markdown("<h2>RESULTS DASHBOARD</h2>", unsafe_allow_html=True)
    
    res_col1, res_col2, res_col3 = st.columns(3)
    with res_col1:
        st.metric(label="Total Selling Price", value=f"₹{selling_price_inr:,.2f}")
    with res_col2:
        st.metric(label="Total Cost for Print", value=f"₹{total_cost_for_print_inr:,.2f}")
    with res_col3:
        delta_value = f"{profit_margin_percentage:,.1f}%" 
        if profit_for_print_inr >= 0:
            st.metric(label="Estimated Profit", value=f"₹{profit_for_print_inr:,.2f}", delta=delta_value)
        else:
            st.metric(label="Estimated Loss", value=f"₹{profit_for_print_inr:,.2f}", delta=delta_value, delta_color="inverse")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3>Detailed Cost Breakdown</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="cost-breakdown">
        <ul>
            <li>Material Cost (PLA): <strong>₹{material_cost_for_print_inr:,.2f}</strong></li>
            <li>Electricity Cost: <strong>₹{electricity_cost_for_print_inr:,.2f}</strong></li>
            <li>Labor Cost: <strong>₹{labor_cost_for_print_inr:,.2f}</strong> (Included: {include_labor})</li>
            <li>Other Fixed Costs: <strong>₹{other_costs_per_print_inr:,.2f}</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='slashy-hr'></div>", unsafe_allow_html=True)
    # Updated "Made by" line
    st.markdown(f"<div class='footer'>Made by Vedaa B</div>", unsafe_allow_html=True)
    st.caption("Disclaimer: This calculator provides estimates. Actual costs/profits may vary. Consider print failures, market demand, and full overheads for business analysis.")

if __name__ == "__main__":
    run_streamlit_calculator_themed()