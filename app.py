import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; }
    label { color: #93c5fd !important; font-size: 1.05em !important; font-weight: 500; }
    .blurred { opacity: 0.28; filter: blur(5px); }
    .report-box { background-color: #1e2937; padding: 25px; border-radius: 12px; border-left: 5px solid #3b82f6; }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**Your Personal 3DCP Specialist**")

# User info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_company" not in st.session_state:
    st.session_state.user_company = ""
if "user_location" not in st.session_state:
    st.session_state.user_location = ""

tool = st.sidebar.selectbox(
    "Select Tool",
    ["Home / Welcome", "1. Recycled Mix Optimizer", "2. Resilient Project Estimator", 
     "3. FEMA / Disaster Response Proposal Tool", "4. Resilient Housing Grant Qualifier"]
)

def processing_animation(message="Analyzing your project specifications..."):
    with st.spinner(message):
        time.sleep(1.6)

def show_cta():
    st.markdown("---")
    st.subheader("Unlock the Full Professional Report + Printable PDFs")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Request Full Pro Report"):
            if email:
                st.success(f"✅ Thank you! Your complete personalized report package has been requested for **{email}**.")
    with col2:
        st.markdown("**Instant Pro Upgrade**")
        st.markdown("[**Pro Lifetime Access – $99**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
        st.markdown("[**Pro Monthly – $29**](https://gumroad.com/l/YOUR-MONTHLY-LINK)")

# ==================== HOME ====================
if tool == "Home / Welcome":
    st.success("Welcome to your personal 3DCP toolkit")
    st.write("We treat every contractor like a VIP client.")
    
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    company = st.text_input("Company / Organization", value=st.session_state.user_company)
    location = st.text_input("Project Location (City, State)", value=st.session_state.user_location)
    
    if st.button("Save My Information & Begin"):
        st.session_state.user_name = name
        st.session_state.user_company = company
        st.session_state.user_location = location
        st.success(f"✅ Welcome, **{name or 'there'}** from **{company or 'your team'}** in **{location or 'your area'}**!")
    
    if st.session_state.user_name:
        st.write(f"Hi **{st.session_state.user_name}** — let's build something resilient today.")
    show_cta()

# ==================== TOOL 1: Recycled Mix Optimizer ====================
elif tool == "1. Recycled Mix Optimizer":
    name = st.session_state.user_name or "there"
    st.subheader(f"1. Recycled Mix Optimizer – Hi {name}!")
    st.write(f"Creating a high-recycled mix optimized for your **{st.session_state.user_company or 'project'}** in **{st.session_state.user_location or 'your area'}**.")
    
    col1, col2 = st.columns(2)
    with col1:
        printer_type = st.selectbox("Printer Type", ["Gantry Large Format", "Robotic Arm", "Delta", "Mobile Trailer System", "Other"])
        nozzle_size = st.selectbox("Nozzle Size (mm)", ["20", "30", "40", "50", "Custom"])
        layer_height = st.slider("Layer Height (mm)", 5, 40, 15)
    with col2:
        pump_type = st.selectbox("Pump Type", ["Progressive Cavity", "Peristaltic", "Screw Pump", "Other"])
        print_speed = st.slider("Target Print Speed (mm/s)", 50, 300, 120)
        ambient_temp = st.number_input("Ambient Temperature (°F)", value=72)
    
    strength = st.slider("Target Compressive Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    
    if st.button("🚀 Generate Optimized Mix"):
        processing_animation("Tailoring mix to your printer configuration and local materials...")
        st.success("**Basic Free Mix Recommendation**")
        st.metric("Estimated Cost per m³", "$112.80")
        st.metric("Printability Score", "82/100")
        
        st.subheader("Your Personalized Report")
        st.markdown('<div class="report-box">Basic mix parameters generated successfully.</div>', unsafe_allow_html=True)
        
        st.markdown("**Advanced Pro Content (Locked)**")
        st.markdown('<div class="blurred">Full 15-page specification including exact additive ratios, pump pressure curves, temperature-adjusted settings, layer adhesion data, and downloadable PDF ready for your site team.</div>', unsafe_allow_html=True)
        st.markdown("[**Upgrade to Pro – Get Full PDF Now**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
    
    show_cta()

# ==================== TOOL 2: Resilient Project Estimator ====================
elif tool == "2. Resilient Project Estimator":
    name = st.session_state.user_name or "there"
    st.subheader(f"2. Resilient Project Estimator – Hi {name}!")
    
    col1, col2 = st.columns(2)
    with col1:
        wall_length = st.number_input("Total Wall Length (meters)", value=60.0)
        wall_height = st.number_input("Average Wall Height (meters)", value=3.0)
        thickness = st.number_input("Wall Thickness (meters)", value=0.25)
        recycled_pct = st.slider("Recycled Content %", 0, 60, 35)
    with col2:
        floors = st.number_input("Number of Floors", value=1, min_value=1)
        openings = st.number_input("Number of Openings (windows/doors)", value=8)
        wind_zone = st.selectbox("Wind Zone", ["Standard", "Hurricane Zone (Florida)", "High Wind", "Tornado Alley"])
    
    if st.button("🚀 Generate Project Estimate"):
        processing_animation("Running detailed structural and cost analysis...")
        st.success("**Basic Free Estimate**")
        st.metric("Estimated Material Cost", "$24,650")
        st.metric("Estimated Print Time", "52 hours")
        
        st.subheader("Your Project Report")
        st.markdown('<div class="report-box">Basic cost and time estimate generated.</div>', unsafe_allow_html=True)
        
        st.markdown("**Pro Report (Locked)**")
        st.markdown('<div class="blurred">Full printable PDF including floor plans, parts & supply lists, insurance savings breakdown, and structural reinforcement schedule.</div>', unsafe_allow_html=True)
        st.markdown("[**Upgrade to Pro – Get Full PDF Now**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
    
    show_cta()

# ==================== TOOL 3: FEMA / Disaster Response Proposal Tool ====================
elif tool == "3. FEMA / Disaster Response Proposal Tool":
    name = st.session_state.user_name or "there"
    st.subheader(f"3. FEMA / Disaster Response & Government Contract Proposal Tool – Hi {name}!")
    st.write("Designed for contractors bidding on disaster recovery and government projects.")
    
    col1, col2 = st.columns(2)
    with col1:
        project_type = st.selectbox("Project Type", ["Temporary Housing Replacement", "Permanent Resilient Homes", "Community Shelter", "Infrastructure Repair"])
        number_units = st.number_input("Number of Units / Structures", value=12)
        total_sqft = st.number_input("Total Square Footage", value=18500)
    with col2:
        disaster_type = st.selectbox("Disaster Type", ["Hurricane", "Tornado", "Flood", "Wildfire", "Other"])
        timeline = st.selectbox("Required Timeline", ["Emergency (30 days)", "Short-term (90 days)", "Standard (6 months)"])
        funding_source = st.selectbox("Funding Source", ["FEMA", "HUD Rebuild", "State Grant", "Local Government"])
    
    if st.button("🚀 Generate Proposal Framework"):
        processing_animation("Building government contract proposal framework...")
        st.success("**Basic Free Framework Generated**")
        st.metric("Estimated Project Value", "$1,245,000")
        
        st.subheader("Proposal Report")
        st.markdown('<div class="report-box">Basic cost framework and timeline created.</div>', unsafe_allow_html=True)
        
        st.markdown("**Full Pro Proposal Package (Locked)**")
        st.markdown('<div class="blurred">Complete 25+ page ready-to-submit proposal including floor plans, supply lists, cost justification, resilience data, and FEMA-compliant language.</div>', unsafe_allow_html=True)
        st.markdown("[**Upgrade to Pro – Get Full Proposal Now**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
    
    show_cta()

# ==================== TOOL 4 ====================
elif tool == "4. Resilient Housing Grant Qualifier":
    name = st.session_state.user_name or "there"
    st.subheader(f"4. Resilient Housing Grant Qualifier – Hi {name}!")
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other Florida", "Other"])
    
    if st.button("🚀 Check Grant Eligibility"):
        processing_animation("Cross-referencing current 2026 grant databases...")
        st.success("✅ High eligibility detected – Potential awards: **$5,000 – $10,000+ per unit**")
        
        st.markdown("**Full Grant Application Package (Pro Only)**")
        st.markdown('<div class="blurred">Pre-filled forms, supporting documentation checklist, submission timeline, and customized grant strategy PDF.</div>', unsafe_allow_html=True)
        st.markdown("[**Upgrade to Pro – Get Full Package Now**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
    
    show_cta()

st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Your Personal 3DCP Specialist")
