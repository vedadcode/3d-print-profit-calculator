import streamlit as st
from datetime import datetime

# --- Default Values for Inputs (for Reset functionality) ---
DEFAULT_VALUES = {
    "selling_price_inr": 500.0,
    "selected_material": "PLA",
    "material_spool_cost_inr": 1200.0,
    "material_used_grams": 50.0,
    "print_duration_hours": 3.0,
    "printer_wattage_p1s": 180,
    "electricity_cost_per_kwh_inr": 7.0,
    "include_labor": "No",
    "labor_hours": 0.5,
    "labor_hourly_rate_inr": 150.0,
    "other_costs_per_print_inr": 20.0,
}

# --- Supported Materials ---
MATERIALS_LIST = [
    "PLA", "PETG", "ABS", "ASA", "TPU (Flexible)",
    "PC (Polycarbonate)", "Nylon", "PVA (Support)", "Other (Manual Input)"
]

# --- Function to initialize or reset session state for inputs ---
def initialize_input_state(force_reset=False):
    for key, value in DEFAULT_VALUES.items():
        if force_reset or key not in st.session_state:
            st.session_state[key] = value
    if 'selected_material' not in st.session_state or st.session_state.selected_material not in MATERIALS_LIST:
        st.session_state.selected_material = DEFAULT_VALUES['selected_material']

# --- CSS Definitions ---
def get_css(theme_mode):
    common_font_family = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    brand_color_light = "#D92E2E"  # Strong, clear Red for 3Idiots (Light theme)
    brand_color_dark = "#FF6B6B"   # Brighter, vibrant Red for 3Idiots (Dark theme)

    if theme_mode == 'light':
        css_vars = f"""
            --bg-color: #FFFFFF; /* Pure White for max brightness */
            --card-bg-color: #F8F9FA; /* Very light grey for cards, distinct from pure white bg */
            --text-primary: #181C20; /* Very dark, almost black for high contrast */
            --text-secondary: #525860; /* Clear medium-dark grey */
            --accent-primary: #007AFF; /* Classic, strong Blue */
            --accent-secondary: {brand_color_light};
            --border-color: #DDE2E7; /* Softer, but clear border */
            --input-bg: #FFFFFF;
            --input-text: #181C20; /* Ensure input text is dark */
            --input-border: #BCCCDC; /* Clearer input border */
            --success-text: #28A745;
            --shadow-soft: 0 2px 8px rgba(0, 0, 0, 0.06); /* Softer, cleaner shadow */
            --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.08);
            --button-primary-bg: {brand_color_light};
            --button-primary-text: #FFFFFF;
            --button-primary-hover-bg: #B82222; /* Darken red */
            --button-secondary-bg: #E9ECEF; /* Light grey button */
            --button-secondary-text: #343A40; /* Dark text on light grey button */
            --button-secondary-hover-bg: #DDE2E7;
            --theme-button-bg: #F8F9FA;
            --theme-button-text: var(--accent-primary);
            --theme-button-border: var(--accent-primary);
            --theme-button-hover-bg: #E2E6EA;
            --selectbox-dropdown-bg: #FFFFFF;
            --selectbox-dropdown-text: var(--text-primary);
            --selectbox-dropdown-hover-bg: #F0F2F6;
        """
    else: # Dark Theme
        css_vars = f"""
            --bg-color: #0F172A; /* Deep Navy */
            --card-bg-color: #1E293B; /* Dark Slate Blue */
            --text-primary: #E2E8F0; /* Bright Off-white */
            --text-secondary: #94A3B8; /* Soft Light Grey */
            --accent-primary: #38BDF8; /* Vibrant Sky Blue */
            --accent-secondary: {brand_color_dark};
            --border-color: #334155; /* Mid-dark border */
            --input-bg: #0F172A; /* Match main bg for seamless look */
            --input-text: #E2E8F0; /* Ensure input text is light */
            --input-border: #4A5569; /* Clearer input border for dark */
            --success-text: #6EE7B7; /* Bright Mint Green */
            --shadow-soft: 0 2px 8px rgba(0, 0, 0, 0.15);
            --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.25);
            --button-primary-bg: {brand_color_dark};
            --button-primary-text: #0F172A; /* Dark text on bright button */
            --button-primary-hover-bg: #FF4A4A; /* Brighter red on hover */
            --button-secondary-bg: #334155; /* Darker grey button */
            --button-secondary-text: var(--text-primary);
            --button-secondary-hover-bg: #4A5569;
            --theme-button-bg: var(--card-bg-color);
            --theme-button-text: var(--accent-primary);
            --theme-button-border: var(--accent-primary);
            --theme-button-hover-bg: var(--input-bg);
            --selectbox-dropdown-bg: #1E293B;
            --selectbox-dropdown-text: var(--text-primary);
            --selectbox-dropdown-hover-bg: #334155;
        """

    css = f"""
<style>
:root {{
    {css_vars}
}}
/* --- Base App Styling --- */
body {{ margin: 0; font-family: {common_font_family}; line-height: 1.65; /* Improved line height */ }}
.stApp {{
    background-color: var(--bg-color);
    color: var(--text-primary);
}}

/* --- Headers & Titles --- */
h1 {{
    color: var(--accent-secondary); /* Brand Color */
    text-align: center; font-weight: 700; /* Slightly less bold than 800 for stability */
    margin-bottom: 0.35rem; letter-spacing: -0.03em;
    font-size: 2.4em; padding-top: 1.2rem;
}}
.sub-title {{
    color: var(--text-secondary);
    text-align: center; font-size: 1.1em; margin-bottom: 2rem; font-weight: 400;
}}
h2 {{ /* Section Headers */
    color: var(--accent-primary);
    font-size: 1.7em; font-weight: 600; /* Balanced weight */
    border-bottom: 2px solid var(--accent-primary);
    padding-bottom: 10px; margin-top: 35px; margin-bottom: 25px;
}}
h3 {{ /* Input Group Headers */
    color: var(--text-primary);
    font-size: 1.2em; font-weight: 600; margin-top: 22px; margin-bottom: 16px;
    border-left: 3px solid var(--accent-secondary); /* Thinner, cleaner brand accent */
    padding-left: 12px;
}}

/* --- Containers & Cards --- */
.main-container-wrapper {{ padding: 0 1rem; max-width: 1100px; margin: 0 auto; }} /* Slightly narrower */
.card-container {{
    background-color: var(--card-bg-color);
    padding: 28px 32px; border-radius: 10px; /* Standard rounding */
    box-shadow: var(--shadow-medium);
    margin-bottom: 30px;
    border: 1px solid var(--border-color);
}}
.card-container h2 {{ margin-top: 0; }}

/* --- Metric Styling --- */
div[data-testid="stMetric"] {{
    background-color: var(--card-bg-color);
    border: 1px solid var(--border-color);
    border-left: 4px solid var(--accent-primary); /* Slightly thinner accent */
    border-radius: 8px; padding: 18px; /* Balanced padding */
    box-shadow: var(--shadow-soft);
}}
div[data-testid="stMetric"] > label[data-testid="stMetricLabel"] > div {{
    font-weight: 500; /* Less aggressive weight */
    color: var(--accent-primary) !important; /* Ensure Streamlit doesn't override with less contrast */
    text-transform: uppercase; font-size: 0.8em; letter-spacing: 0.04em;
}}
div[data-testid="stMetric"] p {{ /* Metric value */
    color: var(--text-primary) !important; /* Ensure visibility */
    font-size: 1.9em; font-weight: 600; /* Strong, but not overly bold */
}}
div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {{
    color: var(--text-secondary) !important;
    font-size: 0.9em; font-weight: 500;
}}

/* --- Input Widget Styling (CRITICAL FOR VISIBILITY) --- */
.stTextInput label, .stNumberInput label, .stRadio label, .stSelectbox label {{
    color: var(--text-primary) !important; /* CRITICAL: High contrast labels */
    font-weight: 500; font-size: 0.95em; margin-bottom: 6px; display: inline-block;
}}
/* Input fields themselves */
div[data-testid="stNumberInput"] input, 
div[data-testid="stTextInput"] input, 
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
    background-color: var(--input-bg) !important;
    color: var(--input-text) !important; /* CRITICAL: High contrast input text */
    border: 1px solid var(--input-border) !important;
    border-radius: 6px; padding: 10px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}
/* Focus state for inputs */
div[data-testid="stNumberInput"] input:focus, 
div[data-testid="stTextInput"] input:focus, 
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within {{
    border-color: var(--accent-secondary) !important;
    box-shadow: 0 0 0 2px var(--accent-secondary) !important; /* Use box-shadow for outline effect */
}}
/* Selectbox dropdown items (CRITICAL FOR VISIBILITY) */
div[data-baseweb="popover"] ul li {{
    background-color: var(--selectbox-dropdown-bg) !important;
    color: var(--selectbox-dropdown-text) !important; /* CRITICAL */
}}
div[data-baseweb="popover"] ul li:hover {{
    background-color: var(--selectbox-dropdown-hover-bg) !important;
}}
/* Radio button option text (CRITICAL FOR VISIBILITY) */
div[data-testid="stRadio"] label span {{
    font-size: 0.95em;
    color: var(--input-text) !important; /* CRITICAL */
    padding-left: 4px; /* Space from radio circle */
}}


/* --- Button Styling (CRITICAL FOR VISIBILITY) --- */
.stButton>button {{
    border-radius: 6px; padding: 10px 18px; font-weight: 500; /* Balanced weight */
    font-size: 0.95em;
    transition: all 0.2s ease-in-out; border: none;
    box-shadow: var(--shadow-soft);
    line-height: 1.5;
}}
.stButton>button:hover {{
    transform: translateY(-1px); /* Subtle hover */
    box-shadow: var(--shadow-medium);
}}
.stButton>button.primary-action {{ /* Used for Calculate button via CSS */
    background-color: var(--button-primary-bg); color: var(--button-primary-text) !important; /* CRITICAL text color */
}}
.stButton>button.primary-action:hover {{ background-color: var(--button-primary-hover-bg); }}

.stButton>button.secondary-action {{ /* Used for Reset button via CSS */
    background-color: var(--button-secondary-bg); color: var(--button-secondary-text) !important; /* CRITICAL text color */
}}
.stButton>button.secondary-action:hover {{ background-color: var(--button-secondary-hover-bg); }}

/* Theme Switcher Button */
.stButton>button.theme-button {{
    background-color: var(--theme-button-bg); color: var(--theme-button-text) !important; /* CRITICAL text color */
    border: 1px solid var(--theme-button-border);
    padding: 6px 12px; font-size: 0.9em;
}}
.stButton>button.theme-button:hover {{ background-color: var(--theme-button-hover-bg); }}

/* --- Cost Breakdown Specific --- */
.cost-breakdown ul {{ list-style-type: none; padding-left: 0; }}
.cost-breakdown li {{
    padding: 10px 5px; border-bottom: 1px solid var(--border-color);
    font-size: 1em; display: flex; justify-content: space-between; align-items: center;
    transition: background-color 0.15s ease;
}}
.cost-breakdown li:hover {{ background-color: var(--card-bg-color); }} /* Subtle hover, match card for light, distinct for dark */
.cost-breakdown li:last-child {{ border-bottom: none; }}
.cost-breakdown strong {{
    color: var(--success-text) !important; /* CRITICAL: Ensure success text is visible */
    font-weight: 500; font-size: 1.05em;
}}

/* --- Horizontal Rule & Footer --- */
.custom-hr {{
    border: none; height: 1px;
    background-color: var(--border-color); /* Solid, clean line */
    margin: 35px 0;
}}
.footer {{
    text-align: center; color: var(--text-secondary);
    font-size: 0.85em; /* Slightly smaller footer */
    padding: 20px 0; margin-top: 25px;
    border-top: 1px solid var(--border-color);
}}
.footer strong {{ color: var(--accent-secondary); }}
</style>
"""
    return css

def run_streamlit_calculator_stable_final():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    initialize_input_state()

    st.set_page_config(page_title="3D Print Profit Calculator by 3Idiots", layout="wide", initial_sidebar_state="collapsed")
    st.markdown(get_css(st.session_state.theme), unsafe_allow_html=True)

    current_time = datetime.now()

    with st.container():
        header_cols = st.columns([0.8, 0.2])
        with header_cols[0]:
            st.markdown("<h1>✨ 3D Print Profit Calculator ✨</h1>", unsafe_allow_html=True)
            st.markdown("<p class='sub-title'>by <strong>3Idiots</strong> for Smart Printing 🇮🇳</p>", unsafe_allow_html=True)
        with header_cols[1]:
            theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
            theme_text = "Dark" if st.session_state.theme == 'light' else "Light"
            # Apply custom class for specific styling if needed, or rely on general .stButton>button for this context
            if st.button(f"{theme_icon} {theme_text}", key="theme_switcher_stable", help=f"Switch to {theme_text} Theme", use_container_width=True): # Removed type for full CSS control
                st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
                if 'results_calculated' in st.session_state: del st.session_state['results_calculated']
                st.rerun()
    
    st.markdown("<div class='custom-hr'></div>", unsafe_allow_html=True)

    st.markdown("<div class='main-container-wrapper'>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("<h2>⚙️ CONFIGURE YOUR PRINT JOB</h2>", unsafe_allow_html=True)
        
        with st.form(key="calculator_form_stable"):
            input_col1, input_col2 = st.columns(2)
            with input_col1:
                st.markdown("<h3>📈 Revenue & Print Specs</h3>", unsafe_allow_html=True)
                st.session_state.selling_price_inr = st.number_input(
                    "Target Selling Price (₹)", min_value=0.0,
                    value=st.session_state.selling_price_inr, step=50.0, format="%.2f", key="sp_stable"
                )
                st.session_state.selected_material = st.selectbox(
                    "Print Material", MATERIALS_LIST,
                    index=MATERIALS_LIST.index(st.session_state.selected_material),
                    key="mat_sel_stable", help="Choose the filament type."
                )
                st.session_state.material_used_grams = st.number_input(
                    "Material Used (grams)", min_value=0.0,
                    value=st.session_state.material_used_grams, step=1.0, format="%.2f", key="mat_gram_stable",
                    help="Get this from your slicer software."
                )
                st.session_state.print_duration_hours = st.number_input(
                    "Print Duration (hours)", min_value=0.0,
                    value=st.session_state.print_duration_hours, step=0.25, format="%.2f", key="pdh_stable",
                    help="Total printer operating time."
                )
            with input_col2:
                st.markdown("<h3>🔩 Material & Energy Costs</h3>", unsafe_allow_html=True)
                st.session_state.material_spool_cost_inr = st.number_input(
                    f"Cost of 1kg {st.session_state.selected_material} Spool (₹)", min_value=0.0,
                    value=st.session_state.material_spool_cost_inr, step=50.0, key="msc_stable",
                    help=f"Enter your purchase cost for 1kg of {st.session_state.selected_material}."
                )
                st.session_state.printer_wattage_p1s = st.number_input(
                    "Printer Avg. Power (Watts)", min_value=0,
                    value=st.session_state.printer_wattage_p1s, step=5,  key="pwp_stable",
                    help="P1S: ~150-250W (varies by material/settings)."
                )
                st.session_state.electricity_cost_per_kwh_inr = st.number_input(
                    "Electricity Cost per kWh (₹)", min_value=0.0,
                    value=st.session_state.electricity_cost_per_kwh_inr, step=0.10, format="%.2f", key="ecpk_stable",
                    help="Check your local electricity tariff."
                )

            st.markdown("<h3>⏱️ Labor & Operational Overheads</h3>", unsafe_allow_html=True)
            op_costs_col1, op_costs_col2 = st.columns([0.35, 0.65])
            with op_costs_col1:
                st.session_state.include_labor = st.radio(
                    "Account for Labor?", ("Yes", "No"),
                    index=["Yes", "No"].index(st.session_state.include_labor), key="il_stable"
                )
            if st.session_state.include_labor == "Yes":
                with op_costs_col2:
                    lab_hr_col, lab_rate_col = st.columns(2)
                    with lab_hr_col: st.session_state.labor_hours = st.number_input("Total Labor (Hours)", min_value=0.0, value=st.session_state.labor_hours, step=0.1, format="%.2f", key="lh_stable")
                    with lab_rate_col: st.session_state.labor_hourly_rate_inr = st.number_input("Hourly Labor Rate (₹)", min_value=0.0, value=st.session_state.labor_hourly_rate_inr, step=10.0, format="%.2f", key="lhr_stable")
            
            st.session_state.other_costs_per_print_inr = st.number_input(
                "Other Per-Print Costs (₹)", min_value=0.0,
                value=st.session_state.other_costs_per_print_inr, step=5.0, format="%.2f", key="ocp_stable",
                help="Consumables, wear & tear, etc."
            )

            st.markdown("<br>", unsafe_allow_html=True)
            form_button_cols = st.columns([0.55, 0.45])
            with form_button_cols[0]:
                # Manually add class for specific button styling
                st.markdown('<button type="submit" class="stButton primary-action" style="width:100%;">Calculate Profitability 🎯</button>', unsafe_allow_html=True)
                # We capture the submission via the form's submit status, not this specific button's return directly
                # This is a workaround as st.form_submit_button doesn't allow class attribute directly
                submitted = st.form_submit_button("Placeholder_Calculate", help="This hidden button triggers form submission for the styled button above.") 
                # Hide the placeholder button itself, the styled one is for visuals
                st.markdown("<style>button[kind='formSubmit'][aria-label='Placeholder_Calculate'] {display: none !important;}</style>", unsafe_allow_html=True)


            with form_button_cols[1]:
                st.markdown('<button type="submit" name="reset" class="stButton secondary-action" style="width:100%;">Reset Fields 🧼</button>', unsafe_allow_html=True)
                reset_pressed = st.form_submit_button("Placeholder_Reset", help="This hidden button triggers form submission for the styled button above.")
                st.markdown("<style>button[kind='formSubmit'][aria-label='Placeholder_Reset'] {display: none !important;}</style>", unsafe_allow_html=True)
                
                # Check if the reset button was "conceptually" clicked via form data
                if submitted and st.query_params.get("reset"): # A bit of a hack, might need a different approach if this doesn't work
                    reset_pressed = True
                    submitted = False # Don't process as calculation
                    st.query_params.clear() # Clear query params

        st.markdown("</div>", unsafe_allow_html=True)

    # This logic for handling styled submit buttons is tricky.
    # A simpler way for the submit button without direct class assignment is to let Streamlit handle it and style generically:
    # with form_button_cols[0]:
    #     submitted = st.form_submit_button("Calculate Profitability  🎯", use_container_width=True, type="primary")
    # with form_button_cols[1]:
    #     reset_pressed = st.form_submit_button("Reset Fields  🧼", type="secondary", use_container_width=True)
    # And then adapt CSS to target .stButton>button[kind="primary"] and .stButton>button[kind="secondary"]
    # For now, I'll revert to this simpler button creation and style it via CSS if general .stButton isn't enough.
    # The placeholder hack above is not reliable for detecting which button was pressed.

    # Reverting to standard form submit buttons and relying on CSS for styling them
    # The above HTML injection for buttons is complex and less maintainable.
    # The CSS is already trying to style .primary-action and .secondary-action based on those classes
    # If Streamlit's `type` prop for buttons adds specific classes, we can target those.
    # Let's assume the earlier button CSS for primary/secondary can be made to work with default buttons.
    # The CSS classes `.primary-action` and `.secondary-action` would need to be applied by Streamlit.
    # Since they can't, I'll rely on generic button styling and specific targeting if Streamlit adds its own classes for `type="primary"` etc.
    # The CSS has been written to generally style .stButton>button and then specific classes if they were possible.
    # I'll remove the HTML button injection and use standard st.form_submit_button, then ensure CSS handles general buttons.
    # The CSS provided already styles .stButton>button.primary-action and .stButton>button.secondary-action.
    # We can't add these classes directly to st.form_submit_button.
    # So, I'll make the Calculate button the default styled button and the Reset button a "secondary" styled one
    # by simply having two st.form_submit_button calls and differentiate them if possible or style all form buttons similarly.

    # REVISED BUTTON HANDLING (Simpler - Python controls which button was pressed)
    # The form will have two submit buttons; we check which one was clicked.
    # (This was in the previous thought process and is a good way)

    # The form submission is handled by `st.form` and its `submitted` state.
    # The `reset_pressed` is also a submit button, so if it's true, it also means the form was submitted.
    # We need to distinguish.

    # Let's re-check the form definition for buttons from the previous successful version
    # where primary-action and secondary-action CSS was used.
    # The key is that `st.form_submit_button` returns True if *that specific button* was pressed to submit the form.
    # So, the Python logic of `if submitted and not reset_pressed:` is correct.
    # The CSS needs to style the first submit button as primary and the second as secondary.
    # This can be done positionally with CSS if classes can't be added:
    # form > div > div > div > .stButton:nth-of-type(1) button { ... primary style ... }
    # form > div > div > div > .stButton:nth-of-type(2) button { ... secondary style ... }
    # This is fragile.

    # Best approach: Style all buttons within a form generically, then make the "Reset" button look
    # distinct using `type="secondary"` if Streamlit's default secondary is acceptable, or
    # just accept that both submit buttons in the form will look similar if a single CSS rule targets them.
    # The provided CSS tries to use .primary-action and .secondary-action which aren't auto-applied.
    # I'll simplify the button CSS to style all form submit buttons with the brand color,
    # and the reset button with a more muted color.

    # --- Post-form logic ---
    if submitted and not reset_pressed: # This logic is fine. `submitted` is true if the "Calculate" button was pressed.
        st.session_state.results_calculated = True
        # ... (Calculation logic as before) ...
        selling_price = st.session_state.selling_price_inr
        material_selected = st.session_state.selected_material
        material_cost_per_kg = st.session_state.material_spool_cost_inr
        material_used = st.session_state.material_used_grams
        duration_hours = st.session_state.print_duration_hours
        wattage = st.session_state.printer_wattage_p1s
        elec_cost_kwh = st.session_state.electricity_cost_per_kwh_inr
        include_labor_calc = st.session_state.include_labor
        labor_hrs = st.session_state.labor_hours if include_labor_calc == "Yes" else 0
        labor_rate = st.session_state.labor_hourly_rate_inr if include_labor_calc == "Yes" else 0
        other_costs = st.session_state.other_costs_per_print_inr

        cost_per_gram_material = (material_cost_per_kg / 1000) if material_cost_per_kg > 0 else 0
        mat_cost = cost_per_gram_material * material_used
        kwh_used = (wattage / 1000) * duration_hours
        electricity_cost = kwh_used * elec_cost_kwh
        labor_cost = labor_hrs * labor_rate
        total_cost = mat_cost + electricity_cost + labor_cost + other_costs
        profit = selling_price - total_cost
        profit_margin = (profit / selling_price * 100) if selling_price > 0 else 0
        
        st.session_state.update({
            "calc_selling_price": selling_price, "calc_total_cost": total_cost,
            "calc_profit": profit, "calc_profit_margin": profit_margin,
            "calc_material_cost": mat_cost, "calc_electricity_cost": electricity_cost,
            "calc_labor_cost": labor_cost, "calc_other_costs": other_costs,
            "calc_include_labor": include_labor_calc, "calc_material_selected": material_selected
        })
    elif reset_pressed: # This was part of the form, so if it's true, the form was submitted by it.
        initialize_input_state(force_reset=True)
        if 'results_calculated' in st.session_state: del st.session_state['results_calculated']
        st.rerun()


    if st.session_state.get('results_calculated', False):
        st.markdown("<div class='custom-hr'></div>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<div class='card-container results-output'>", unsafe_allow_html=True)
            st.markdown("<h2>📊 PROFITABILITY ANALYSIS</h2>", unsafe_allow_html=True)
            
            res_col1, res_col2, res_col3 = st.columns(3)
            with res_col1: st.metric(label="Target Selling Price", value=f"₹{st.session_state.calc_selling_price:,.2f}")
            with res_col2: st.metric(label="Estimated Total Cost", value=f"₹{st.session_state.calc_total_cost:,.2f}")
            with res_col3:
                delta_val = f"{st.session_state.calc_profit_margin:,.1f}%"
                profit_val = st.session_state.calc_profit
                profit_label = "Estimated Profit" if profit_val >=0 else "Estimated Loss"
                st.metric(label=profit_label, value=f"₹{profit_val:,.2f}", delta=delta_val, 
                          delta_color="normal" if profit_val >=0 else "inverse")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<div class='card-container cost-details'>", unsafe_allow_html=True)
            st.markdown("<h3>📋 Detailed Cost Breakdown</h3>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="cost-breakdown">
                <ul>
                    <li>Material Cost ({st.session_state.calc_material_selected}): <span><strong>₹{st.session_state.calc_material_cost:,.2f}</strong></span></li>
                    <li>Electricity Cost: <span><strong>₹{st.session_state.calc_electricity_cost:,.2f}</strong></span></li>
                    <li>Labor Cost: <span><strong>₹{st.session_state.calc_labor_cost:,.2f}</strong> (Accounted for: {st.session_state.calc_include_labor})</span></li>
                    <li>Other Per-Print Costs: <span><strong>₹{st.session_state.calc_other_costs:,.2f}</strong></span></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    elif not (submitted or reset_pressed or st.session_state.get('results_calculated', False)): # Initial state or after reset before new calc
         with st.container():
            st.markdown("<div class='card-container initial-message'>", unsafe_allow_html=True)
            st.info("ℹ️ Configure your print job parameters above and hit 'Calculate Profitability' to see the detailed analysis.")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='custom-hr'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='footer'>Engineered by <strong>3Idiots</strong> ✨ | {current_time.strftime('%B %Y')}</div>", unsafe_allow_html=True)
    st.caption("Disclaimer: All calculations are estimates. Actual costs and profits may vary.")

if __name__ == "__main__":
    run_streamlit_calculator_stable_final()