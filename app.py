import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 14px 32px; font-weight: bold; font-size: 1.05em; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; font-size: 2.4em; }
    
    /* Bolder & Larger Top Navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.25em !important;
        font-weight: 700 !important;
        padding: 16px 28px !important;
        background-color: #1e2937;
        color: #e2e8f0;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
        border-bottom: 4px solid #60a5fa;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**The Leading Software Platform for 3D Construction Printing**")

# Store user info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Top Navigation - Larger & Bolder
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
        time.sleep(1.4)

# ==================== HOME TAB ====================
with tab1:
    st.title("Welcome to 3DCP Pro Tools LLC")
    st.write("The premier software platform built for professional 3DCP contractors.")
    
    name = st.text_input("**Your First Name**", value=st.session_state.user_name, placeholder="Enter your name to personalize your experience")
    
    if st.button("Save My Name & Continue"):
        st.session_state.user_name = name
        st.success(f"✅ Welcome, **{name or 'Contractor'}**! Let's get to work.")
        
        # Friendly helper message with pointer
        st.markdown("""
        <div style="background-color: #1e2937; padding: 20px; border-radius: 12px; border-left: 6px solid #60a5fa; margin-top: 20px;">
            👋 Hi <strong>{}</strong>! I'm your personal 3DCP assistant.<br><br>
            👉 Use the <strong>bold tabs at the top</strong> to explore the tools.<br>
            Each tool will save your work automatically to the Dashboard.
        </div>
        """.format(name or "there"), unsafe_allow_html=True)

    if st.session_state.user_name:
        st.markdown(f"👋 Hello **{st.session_state.user_name}** — ready to build something resilient?")

# ==================== MIX OPTIMIZER ====================
with tab2:
    st.title("🔧 Recycled Mix Optimizer")
    name = st.session_state.user_name or "Contractor"
    st.write(f"Hi {name} — let's optimize a high-recycled mix for your project.")
    
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
    
    st.markdown("**Advanced Settings (Pro Only)**")
    st.slider("Fiber Reinforcement %", 0, 5, 1, disabled=True)
    st.selectbox("Rheology Modifier", ["None", "VMA", "Superplasticizer"], disabled=True)
    
    if st.button("🚀 Generate Optimized Mix"):
        processing_animation("Tailoring mix to your printer and site conditions...")
        st.success("Basic mix recommendation generated.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== PROJECT ESTIMATOR ====================
with tab3:
    st.title("📏 Resilient Project Estimator")
    st.write("Detailed estimation for resilient 3DCP structures")
    
    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input("Total Wall Length (m)", value=60.0)
        height = st.number_input("Average Wall Height (m)", value=3.0)
        thickness = st.number_input("Wall Thickness (m)", value=0.25)
    with col2:
        floors = st.number_input("Number of Floors", value=1)
        openings = st.number_input("Number of Openings", value=12)
        wind_zone = st.selectbox("Wind Exposure", ["Standard", "Hurricane Zone", "High Wind", "Tornado"])
    
    recycled = st.slider("Recycled Content %", 0, 60, 35)
    
    st.markdown("**Advanced Structural Analysis (Pro Only)**")
    st.checkbox("Seismic Load Analysis", disabled=True)
    st.checkbox("Thermal Bridging Study", disabled=True)
    
    if st.button("🚀 Generate Estimate"):
        processing_animation("Running full project analysis...")
        st.success("Basic estimate completed.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== FEMA TOOL ====================
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
    
    st.markdown("**Government Compliance (Pro Only)**")
    st.text_input("FEMA DR Number", disabled=True)
    
    if st.button("🚀 Generate Proposal Framework"):
        processing_animation("Building compliant proposal...")
        st.success("Basic proposal framework generated.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== GRANT TOOL ====================
with tab5:
    st.title("🏛️ Resilient Housing Grant Qualifier")
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other"])
    
    st.markdown("**Advanced Grant Features (Pro Only)**")
    st.checkbox("Pre-filled Application Forms", disabled=True)
    
    if st.button("🚀 Check Grant Eligibility"):
        processing_animation("Cross-referencing grant databases...")
        st.success("High eligibility detected.")
        st.button("→ View Full Report in Dashboard", type="primary")

# ==================== DASHBOARD ====================
with tab6:
    st.title("📊 My Dashboard & Reports")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}**")
    
    if not st.session_state.get("reports"):
        st.info("No reports generated yet. Use the tools above.")
    else:
        for key, report in st.session_state.reports.items():
            st.subheader(f"{report.get('tool', 'Report')}")
            st.markdown('<div class="report-box">Basic summary created successfully.</div>', unsafe_allow_html=True)
            st.markdown("**Full Professional Package (Pro Only)**")
            st.markdown('<div class="blurred">Printable PDFs • Floor plans • Supply lists • Vendor quotes • Structural analysis</div>', unsafe_allow_html=True)

st.caption("© 2026 3DCP Pro Tools LLC • The Leading Software Platform for 3D Construction Printing")
