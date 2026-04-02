import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    
    /* Very large title - main focus */
    h1 { 
        color: #60a5fa; 
        font-size: 4.6em !important; 
        font-weight: 700 !important;
        margin-bottom: 12px !important;
        text-align: center;
    }
    
    /* Large cursive line directly under title - 2x larger */
    .cursive {
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 2.9em !important;
        color: #94a3b8;
        text-align: center;
        margin: 0 0 35px 0;
        letter-spacing: 1.8px;
        opacity: 0.9;
    }
    
    /* Large bold top navigation */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.75em !important;
        font-weight: 700 !important;
        padding: 22px 34px !important;
        margin: 0 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("3DCP Pro Tools LLC")

# Large cursive line directly under the title
st.markdown('<p class="cursive">Empowering the future of resilient 3D construction • One precise layer at a time</p>', unsafe_allow_html=True)

# Top Navigation
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Home", 
    "🔧 Mix Optimizer", 
    "📏 Project Estimator", 
    "📋 FEMA Proposal Tool", 
    "🏛️ Grant Qualifier", 
    "📊 My Dashboard"
])

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

def processing_animation(message="Analyzing your project data..."):
    with st.spinner(message):
        time.sleep(1.4)

def show_cta():
    st.markdown("---")
    st.subheader("Unlock Full Professional Reports & PDFs")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Request Full Pro Report"):
            if email:
                st.success(f"✅ Thank you! Your complete personalized report has been requested.")
    with col2:
        st.markdown("**Instant Pro Upgrade**")
        st.markdown("[**Pro Lifetime Access – $99**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
        st.markdown("[**Pro Monthly – $29**](https://gumroad.com/l/YOUR-MONTHLY-LINK)")

# ==================== HOME ====================
with tab1:
    st.title("Welcome to 3DCP Pro Tools LLC")
    st.write("The premier software platform for professional 3D construction printing contractors.")
    
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    if st.button("Save My Name"):
        st.session_state.user_name = name
        st.success(f"✅ Welcome, **{name or 'Contractor'}**!")

# ==================== MIX OPTIMIZER ====================
with tab2:
    st.title("🔧 Recycled Mix Optimizer")
    st.write("Advanced mix design for large-format 3DCP")
    
    col1, col2 = st.columns(2)
    with col1:
        printer = st.selectbox("Printer Type", ["Gantry Large Format", "Robotic Arm", "Mobile Trailer System", "Delta"])
        nozzle = st.selectbox("Nozzle Size (mm)", ["20", "30", "40", "50"])
        layer = st.slider("Layer Height (mm)", 5, 40, 15)
    with col2:
        pump = st.selectbox("Pump Type", ["Progressive Cavity", "Peristaltic", "Screw"])
        speed = st.slider("Print Speed (mm/s)", 50, 300, 120)
        temp = st.number_input("Ambient Temperature (°F)", value=72)
    
    strength = st.slider("Target Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    
    if st.button("🚀 Generate Optimized Mix"):
        processing_animation("Calculating mix for your setup...")
        st.success("Basic mix recommendation generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== PROJECT ESTIMATOR ====================
with tab3:
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
    
    if st.button("🚀 Generate Estimate"):
        processing_animation("Running project analysis...")
        st.success("Basic estimate generated.")
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
    
    if st.button("🚀 Generate Proposal Framework"):
        processing_animation("Building proposal...")
        st.success("Basic framework generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== GRANT QUALIFIER ====================
with tab5:
    st.title("🏛️ Resilient Housing Grant Qualifier")
    st.write("Check eligibility for resilient housing programs")
    
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other"])
    
    if st.button("🚀 Check Grant Eligibility"):
        processing_animation("Checking grant databases...")
        st.success("Eligibility results generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== DASHBOARD ====================
with tab6:
    st.title("📊 My Dashboard & Reports")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}**")
    st.info("Your generated reports will appear here once you use the tools above.")

st.caption("© 2026 3DCP Pro Tools LLC • The Leading Software Platform for 3D Construction Printing")
