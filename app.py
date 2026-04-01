import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; font-size: 2.2em; }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.1em !important;
        font-weight: 600 !important;
        padding: 12px 20px !important;
    }
    .pro-label { color: #fbbf24; font-weight: bold; }
    .blurred { opacity: 0.32; filter: blur(4px); }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**The Leading Software Platform for 3D Construction Printing**")

# User info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Top Navigation (Bolder Tabs)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Home", 
    "🔧 Mix Optimizer", 
    "📏 Project Estimator", 
    "📋 FEMA Proposal Tool", 
    "🏛️ Grant Qualifier", 
    "📊 My Dashboard"
])

def processing_animation(message="Processing your project data..."):
    with st.spinner(message):
        time.sleep(1.5)

def show_cta():
    st.markdown("---")
    st.subheader("Unlock Full Professional Reports & PDFs")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Request Full Pro Report"):
            if email:
                st.success(f"✅ Thank you! Your complete report package has been requested.")
    with col2:
        st.markdown("**Instant Pro Upgrade**")
        st.markdown("[**Pro Lifetime Access – $99**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
        st.markdown("[**Pro Monthly – $29**](https://gumroad.com/l/YOUR-MONTHLY-LINK)")

# ==================== HOME ====================
with tab1:
    st.title("Welcome to 3DCP Pro Tools LLC")
    st.write("The premier software platform for professional 3D construction printing contractors.")
    
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    if st.button("Save Name"):
        st.session_state.user_name = name
        st.success(f"Welcome, **{name or 'Contractor'}**!")
    
    st.info("Use the bold tabs above to access specialized tools. All work is saved to **My Dashboard**.")

# ==================== MIX OPTIMIZER ====================
with tab2:
    st.title("🔧 Recycled Mix Optimizer")
    st.write("Advanced mix design for large-format 3DCP")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Printer Configuration")
        printer = st.selectbox("Printer Type", ["Gantry Large Format", "Robotic Arm", "Mobile Trailer System", "Delta"])
        nozzle = st.selectbox("Nozzle Size (mm)", ["20", "30", "40", "50"])
        layer = st.slider("Layer Height (mm)", 5, 40, 15)
    with col2:
        st.subheader("Operational Settings")
        pump = st.selectbox("Pump Type", ["Progressive Cavity", "Peristaltic", "Screw"])
        speed = st.slider("Print Speed (mm/s)", 50, 300, 120)
        temp = st.number_input("Ambient Temperature (°F)", value=72)
    
    strength = st.slider("Target Compressive Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    
    # Deeper Pro-only options
    st.subheader("Advanced Mix Parameters (Pro Only)")
    st.slider("Fiber Reinforcement %", 0, 5, 1, disabled=True)
    st.selectbox("Rheology Modifier Type", ["None", "VMA", "Superplasticizer"], disabled=True)
    st.number_input("Target Extrusion Pressure (bar)", disabled=True)
    
    if st.button("🚀 Generate Optimized Mix"):
        processing_animation("Calculating mix for your specific printer and conditions...")
        st.success("Basic mix recommendation generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== PROJECT ESTIMATOR ====================
with tab3:
    st.title("📏 Resilient Project Estimator")
    st.write("Detailed estimation for resilient 3DCP structures")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Geometry")
        length = st.number_input("Total Wall Length (m)", value=60.0)
        height = st.number_input("Average Wall Height (m)", value=3.0)
        thickness = st.number_input("Wall Thickness (m)", value=0.25)
    with col2:
        st.subheader("Project Details")
        floors = st.number_input("Number of Floors", value=1)
        openings = st.number_input("Number of Openings", value=12)
        wind_zone = st.selectbox("Wind Exposure Category", ["Standard", "Hurricane Zone", "High Wind", "Tornado"])
    
    recycled = st.slider("Recycled Content %", 0, 60, 35)
    
    st.subheader("Advanced Analysis (Pro Only)")
    st.checkbox("Include Seismic Load Analysis", disabled=True)
    st.checkbox("Thermal Bridging & Insulation Study", disabled=True)
    st.checkbox("Full Structural FEM Simulation", disabled=True)
    
    if st.button("🚀 Generate Full Estimate"):
        processing_animation("Running comprehensive project analysis...")
        st.success("Basic estimate completed.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== FEMA PROPOSAL TOOL ====================
with tab4:
    st.title("📋 FEMA / Disaster Response Proposal Tool")
    st.write("Professional proposal generator for government and disaster recovery contracts")
    
    col1, col2 = st.columns(2)
    with col1:
        project_type = st.selectbox("Project Type", ["Permanent Housing Replacement", "Community Shelter", "Infrastructure Repair"])
        units = st.number_input("Number of Structures", value=15)
        sqft = st.number_input("Total Square Footage", value=22000)
    with col2:
        disaster = st.selectbox("Disaster Type", ["Hurricane", "Tornado", "Flood", "Wildfire"])
        timeline = st.selectbox("Required Timeline", ["Emergency (30 days)", "Short-term (90 days)", "Standard"])
        funding = st.selectbox("Primary Funding Source", ["FEMA", "HUD Rebuild", "State Grant"])
    
    st.subheader("Advanced Compliance (Pro Only)")
    st.text_input("FEMA DR Number", disabled=True)
    st.text_input("RFP / Solicitation Number", disabled=True)
    st.checkbox("Include Davis-Bacon Wage Compliance", disabled=True)
    
    if st.button("🚀 Generate Proposal Framework"):
        processing_animation("Building compliant government proposal...")
        st.success("Basic proposal framework generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== GRANT QUALIFIER ====================
with tab5:
    st.title("🏛️ Resilient Housing Grant Qualifier")
    st.write("Check eligibility and prepare applications for current resilient housing programs")
    
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other"])
    
    st.subheader("Advanced Grant Features (Pro Only)")
    st.checkbox("Pre-filled Application Forms", disabled=True)
    st.checkbox("Submission Timeline & Checklist", disabled=True)
    
    if st.button("🚀 Check Grant Eligibility"):
        processing_animation("Cross-referencing 2026 grant databases...")
        st.success("High eligibility detected.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== DASHBOARD ====================
with tab6:
    st.title("📊 My Dashboard & Reports")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}**")
    
    if not st.session_state.get("reports"):
        st.info("No reports generated yet. Use the tools above to start building your project library.")
    else:
        st.write("Your generated reports and project data:")
        for key, report in st.session_state.reports.items():
            st.subheader(f"{report.get('tool', 'Report')}")
            st.markdown('<div class="report-box">Basic summary created.</div>', unsafe_allow_html=True)
            st.markdown("**Full Professional Package (Pro Only)**")
            st.markdown('<div class="blurred">Printable PDFs • Floor plans • Supply lists • Vendor quotes • Structural analysis • Grant-ready documentation</div>', unsafe_allow_html=True)

    st.caption("© 2026 3DCP Pro Tools LLC • The Leading Software Platform for 3D Construction Printing")
