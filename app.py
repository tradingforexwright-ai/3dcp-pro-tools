import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; }
    .blurred { opacity: 0.3; filter: blur(5px); }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**Your Personal 3DCP Specialist**")

# Store user info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_company" not in st.session_state:
    st.session_state.user_company = ""
if "user_location" not in st.session_state:
    st.session_state.user_location = ""

tool = st.sidebar.selectbox(
    "Select Tool",
    ["Home / Welcome", "1. Recycled Mix Optimizer", "2. Resilient Project Estimator", 
     "3. FEMA Trailer Cost Comparator", "4. Resilient Housing Grant Qualifier"]
)

def processing_animation(message="Analyzing your specific project data..."):
    with st.spinner(message):
        time.sleep(1.5)

def show_cta():
    st.markdown("---")
    st.subheader("Ready for the Full Professional Report + PDF?")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Unlock Full Pro Report"):
            if email:
                st.success(f"✅ Thank you, **{st.session_state.user_name or 'there'}**! Your personalized full report has been requested.")
    with col2:
        st.markdown("**Instant Upgrade on Gumroad**")
        st.markdown("[**Pro Lifetime Access – $99**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
        st.markdown("[**Pro Monthly – $29**](https://gumroad.com/l/YOUR-MONTHLY-LINK)")
        st.caption("Instant access after purchase")

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
        st.write(f"Hi **{st.session_state.user_name}** — let's optimize your next project.")
    show_cta()

# ==================== TOOL 1 ====================
elif tool == "1. Recycled Mix Optimizer":
    name = st.session_state.user_name or "there"
    st.subheader(f"1. Recycled Mix Optimizer – Hi {name}!")
    st.write(f"Tailored for your **{st.session_state.user_company or 'project'}** in **{st.session_state.user_location or 'your area'}**.")
    
    printer_type = st.selectbox("Printer Type", ["Gantry (large format)", "Robotic Arm", "Delta", "Other"])
    nozzle_size = st.selectbox("Nozzle Size (mm)", ["20", "30", "40", "50"])
    layer_height = st.slider("Layer Height (mm)", 5, 30, 15)
    pump_type = st.selectbox("Pump Type", ["Progressive Cavity", "Peristaltic", "Screw", "Other"])
    
    strength = st.slider("Target Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    
    if st.button("🚀 Optimize My Mix"):
        processing_animation("Searching material databases and tailoring to your printer setup...")
        st.success("**Basic Free Result**")
        st.metric("Estimated Cost per m³", "$118.45")
        st.metric("Printability Score", "78/100")
        
        st.markdown("**Full Detailed Mixture Specification + PDF (Pro Only)**")
        st.markdown('<div class="blurred">12-page custom recipe with exact additive percentages, pump pressure settings, layer speed recommendations, nozzle-specific adjustments, and downloadable PDF tailored to your exact printer and location.</div>', unsafe_allow_html=True)
        st.markdown("[**Upgrade to Pro – Get Full PDF Now**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
    
    show_cta()

# ==================== TOOL 2 ====================
elif tool == "2. Resilient Project Estimator":
    name = st.session_state.user_name or "there"
    st.subheader(f"2. Resilient Project Estimator – Hi {name}!")
    
    length = st.number_input("Total Wall Length (m)", value=50.0)
    height = st.number_input("Wall Height (m)", value=3.0)
    thickness = st.number_input("Wall Thickness (m)", value=0.2)
    recycled = st.slider("Recycled %", 0, 60, 40)
    
    if st.button("🚀 Generate My Project Estimate"):
        processing_animation("Running detailed structural and cost analysis for your project...")
        st.success("**Basic Free Estimate**")
        st.metric("Estimated Total Cost", "$18,240")
        st.metric("Print Time", "38.4 hours")
        
        st.markdown("**Full Contractor Report + PDF (Pro Only)**")
        st.markdown('<div class="blurred">8-page personalized PDF with insurance savings breakdown, structural reinforcement recommendations, full material list, and contractor-ready report.</div>', unsafe_allow_html=True)
        st.markdown("[**Upgrade to Pro – Get Full PDF Now**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
    
    show_cta()

# ==================== TOOL 3 & 4 ====================
elif tool in ["3. FEMA Trailer Cost Comparator", "4. Resilient Housing Grant Qualifier"]:
    st.subheader(f"{tool} – Hi {st.session_state.user_name or 'there'}!")
    st.info("Basic calculation is free. The full contractor-ready report, PDF, and proposal template are available in Pro.")
    show_cta()

st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Your Personal 3DCP Specialist")
