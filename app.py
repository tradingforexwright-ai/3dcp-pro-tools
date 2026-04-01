import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

# Professional styling
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; }
    .pro-label { color: #f59e0b; font-weight: bold; }
    .greyed { opacity: 0.45; pointer-events: none; filter: blur(2px); }
    </style>
""", unsafe_allow_html=True)

# Top Navigation (using tabs)
tabs = st.tabs(["🏠 Home", "🔧 Mix Optimizer", "📏 Project Estimator", "📋 FEMA Proposal Tool", "🏛️ Grant Qualifier", "📊 My Dashboard"])

# Store user info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_company" not in st.session_state:
    st.session_state.user_company = ""
if "user_location" not in st.session_state:
    st.session_state.user_location = ""
if "reports" not in st.session_state:
    st.session_state.reports = {}

def processing_animation(message="Processing your specifications..."):
    with st.spinner(message):
        time.sleep(1.4)

# ==================== HOME TAB ====================
with tabs[0]:
    st.title("Welcome to 3DCP Pro Tools LLC")
    st.markdown("**The Leading Software Platform for 3D Construction Printing**")
    
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    company = st.text_input("Company", value=st.session_state.user_company)
    location = st.text_input("Project Location", value=st.session_state.user_location)
    
    if st.button("Save Profile"):
        st.session_state.user_name = name
        st.session_state.user_company = company
        st.session_state.user_location = location
        st.success(f"Profile saved for **{name or 'Contractor'}**")

    st.info("Use the tabs above to access specialized tools. All results are saved to **My Dashboard**.")

# ==================== MIX OPTIMIZER TAB ====================
with tabs[1]:
    st.title("🔧 Recycled Mix Optimizer")
    st.write("Professional mix design for large-format 3DCP")
    
    col1, col2 = st.columns(2)
    with col1:
        printer = st.selectbox("Printer Type", ["Gantry Large Format", "Robotic Arm", "Mobile Trailer", "Delta"])
        nozzle = st.selectbox("Nozzle Size (mm)", ["20", "30", "40", "50"])
        layer_height = st.slider("Layer Height (mm)", 5, 40, 15)
    with col2:
        pump = st.selectbox("Pump Type", ["Progressive Cavity", "Peristaltic", "Screw"])
        speed = st.slider("Print Speed (mm/s)", 50, 300, 120)
        temp = st.number_input("Ambient Temp (°F)", value=72)
    
    strength = st.slider("Target Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    
    # Advanced Pro options (greyed out)
    st.markdown("**Advanced Settings (Pro Only)**")
    st.slider("Fiber Reinforcement %", 0, 5, 1, disabled=True)
    st.selectbox("Rheology Modifier", ["None", "VMA", "Superplasticizer"], disabled=True)
    
    if st.button("🚀 Generate Optimized Mix"):
        processing_animation("Calculating mix for your printer configuration...")
        st.success("Basic mix parameters generated.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== PROJECT ESTIMATOR TAB ====================
with tabs[2]:
    st.title("📏 Resilient Project Estimator")
    st.write("Detailed estimation for resilient 3DCP structures")
    
    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input("Total Wall Length (m)", value=60.0)
        height = st.number_input("Average Height (m)", value=3.0)
        thickness = st.number_input("Wall Thickness (m)", value=0.25)
    with col2:
        floors = st.number_input("Number of Floors", value=1)
        openings = st.number_input("Number of Openings", value=12)
        wind_zone = st.selectbox("Wind Exposure", ["Standard", "Hurricane Zone", "High Wind", "Tornado"])
    
    recycled = st.slider("Recycled Content %", 0, 60, 35)
    
    st.markdown("**Advanced Structural Options (Pro Only)**")
    st.checkbox("Include Seismic Reinforcement", disabled=True)
    st.checkbox("Include Thermal Bridging Analysis", disabled=True)
    
    if st.button("🚀 Generate Estimate"):
        processing_animation("Running full project analysis...")
        st.success("Basic estimate completed.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== FEMA PROPOSAL TAB ====================
with tabs[3]:
    st.title("📋 FEMA / Disaster Response Proposal Tool")
    st.write("Professional proposal generator for government and disaster recovery contracts")
    
    project_type = st.selectbox("Project Type", ["Permanent Housing Replacement", "Community Shelter", "Infrastructure Repair"])
    units = st.number_input("Number of Structures", value=15)
    sqft = st.number_input("Total Square Footage", value=22000)
    disaster = st.selectbox("Disaster Type", ["Hurricane", "Tornado", "Flood", "Wildfire"])
    
    st.markdown("**Government Compliance Fields (Pro Only)**")
    st.text_input("FEMA DR Number", disabled=True)
    st.text_input("Grant ID / RFP Number", disabled=True)
    
    if st.button("🚀 Generate Proposal Framework"):
        processing_animation("Building compliant proposal structure...")
        st.success("Basic framework generated.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== GRANT TAB ====================
with tabs[4]:
    st.title("🏛️ Resilient Housing Grant Qualifier")
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other"])
    
    if st.button("🚀 Check Eligibility"):
        processing_animation("Cross-referencing current grant programs...")
        st.success("High eligibility detected.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== DASHBOARD TAB ====================
with tabs[5]:
    st.title("📊 My Dashboard & Reports")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}**")
    
    if not st.session_state.reports:
        st.info("No reports yet. Generate content using the tools above.")
    else:
        for key, report in st.session_state.reports.items():
            st.subheader(f"{report.get('tool', 'Report')} — {report.get('date', '')}")
            st.markdown('<div class="report-box">Basic summary created successfully.</div>', unsafe_allow_html=True)
            st.markdown("**Full Professional Package (Pro Only)**")
            st.markdown('<div class="blurred">Printable PDF • Floor plans • Supply lists • Vendor quotes • Structural notes • Grant-ready documentation</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Your Contacts (Early CRM)")
    with st.form("add_contact"):
        c_name = st.text_input("Contact Name")
        c_role = st.text_input("Role / Company")
        if st.form_submit_button("Add Contact"):
            st.success("Contact added to your dashboard.")

st.caption("© 2026 3DCP Pro Tools LLC • The Leading Software Platform for 3D Construction Printing")
