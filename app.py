import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    
    /* Extra large main title */
    h1 { 
        color: #60a5fa; 
        font-size: 3.8em !important; 
        font-weight: 700 !important;
        margin-bottom: 8px !important;
    }
    
    /* Much larger and bolder top navigation */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.65em !important;
        font-weight: 700 !important;
        padding: 22px 32px !important;
        margin: 0 6px !important;
        letter-spacing: 0.8px;
    }
    
    /* Subcategory labels */
    .sub-header { 
        font-size: 1.4em; 
        font-weight: 600; 
        color: #93c5fd; 
        margin: 20px 0 10px 0; 
    }
    </style>
""", unsafe_allow_html=True)

st.title("3DCP Pro Tools LLC")

# Top Navigation - Very Large & Bold
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Home", 
    "🔧 Mix Optimizer", 
    "📏 Project Estimator", 
    "📋 FEMA Proposal Tool", 
    "🏛️ Grant Qualifier", 
    "📊 My Dashboard"
])

# User info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

def processing_animation(message="Analyzing your project data..."):
    with st.spinner(message):
        time.sleep(1.4)

def show_cta():
    st.markdown("---")
    st.subheader("Unlock the Full Professional Report + PDFs")
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
    if st.button("Save My Name & Get Started"):
        st.session_state.user_name = name
        st.success(f"✅ Welcome, **{name or 'Contractor'}**!")

# ==================== MIX OPTIMIZER ====================
with tab2:
    st.title("🔧 Recycled Mix Optimizer")
    st.subheader("Choose a subcategory below")
    sub = st.radio("Subcategory", ["Basic Mix Design", "Advanced Rheology & Additives", "Printer-Specific Optimization", "Material Cost & Sustainability Analysis"], horizontal=True)
    
    if sub == "Basic Mix Design":
        st.write("**Basic Mix Design** – Core parameters for your project")
        # ... (your previous inputs here)
    elif sub == "Advanced Rheology & Additives":
        st.write("**Advanced Rheology & Additives** (Pro Only)")
        st.slider("Fiber Reinforcement %", 0, 5, 1, disabled=True)
    # (other subcategories can be expanded similarly)

    if st.button("🚀 Generate Mix"):
        processing_animation("Calculating...")
        st.success("Basic result generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== PROJECT ESTIMATOR ====================
with tab3:
    st.title("📏 Resilient Project Estimator")
    st.subheader("Choose a subcategory below")
    sub = st.radio("Subcategory", ["Geometry & Basic Estimate", "Structural Analysis", "Insurance & Resilience Modeling", "Full Contractor Report"], horizontal=True)
    # Add your inputs here for each sub

    if st.button("🚀 Generate Estimate"):
        processing_animation("Running analysis...")
        st.success("Basic estimate generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== FEMA PROPOSAL ====================
with tab4:
    st.title("📋 FEMA / Disaster Response Proposal Tool")
    st.subheader("Choose a subcategory below")
    sub = st.radio("Subcategory", ["Basic Framework", "Compliance & Documentation", "Cost Justification", "Full Government Proposal"], horizontal=True)

    if st.button("🚀 Generate Proposal"):
        processing_animation("Building proposal...")
        st.success("Basic framework generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== GRANT QUALIFIER ====================
with tab5:
    st.title("🏛️ Resilient Housing Grant Qualifier")
    st.subheader("Choose a subcategory below")
    sub = st.radio("Subcategory", ["Eligibility Check", "Pre-filled Forms", "Submission Strategy", "Full Application Package"], horizontal=True)

    if st.button("🚀 Check Eligibility"):
        processing_animation("Checking grants...")
        st.success("Eligibility results generated.")
        st.button("→ View in My Dashboard", type="primary")

# ==================== DASHBOARD ====================
with tab6:
    st.title("📊 My Dashboard & Reports")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}**")
    st.info("All your generated reports and project data will appear here.")

st.caption("© 2026 3DCP Pro Tools LLC • The Leading Software Platform for 3D Construction Printing")
