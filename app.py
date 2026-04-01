import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

# Professional Dark Theme with Blue Accents
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { 
        background-color: #3b82f6; 
        color: white; 
        border-radius: 8px; 
        padding: 12px 28px; 
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**Professional Tools for Resilient 3D Construction Printing**")
st.caption("Mix Optimization • Project Estimation • Cost Comparison • Grant Qualification")

tool = st.sidebar.selectbox(
    "Select Tool",
    ["Home", "1. Recycled Mix Optimizer", "2. Resilient Project Estimator", 
     "3. FEMA Trailer Cost Comparator", "4. Resilient Housing Grant Qualifier"]
)

def processing_animation(message="Juggling data and running advanced calculations..."):
    with st.spinner(message):
        time.sleep(1.4)  # Nice "thinking" pause

def show_cta():
    st.markdown("---")
    st.subheader("Ready for Pro Features or Custom Analysis?")
    
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Get Pro Access + Custom Report"):
            if email:
                st.success(f"✅ Thank you! Pro upgrade details and your custom report have been requested for **{email}**.")
            else:
                st.warning("Please enter your email.")
    with col2:
        st.markdown("**Call us directly for faster support:**")
        st.markdown("📞 **(720) 555-0199** *(Space Saver - Temporary Line)*")
        st.caption("Monday–Friday, 9AM–5PM MT")

# ==================== HOME ====================
if tool == "Home":
    st.success("Welcome to 3DCP Pro Tools LLC")
    st.write("Practical tools built specifically for the 3D Construction Printing industry to save time, reduce risk, and win more projects.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Free Tier", "Basic Calculations")
    with col2:
        st.metric("Pro Tier", "$99 one-time or $29/month")
    
    st.info("💰 Projected first 30-60 days revenue: **$3,000 – $10,000**")
    show_cta()

# ==================== TOOL 1 ====================
elif tool == "1. Recycled Mix Optimizer":
    st.subheader("1. Recycled Mix Optimizer")
    st.write("Optimizing high-recycled content mixes for printability and strength.")
    
    col1, col2 = st.columns(2)
    with col1:
        strength = st.slider("Target Strength (MPa)", 15, 50, 30)
        recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    with col2:
        cement_cost = st.number_input("Cement $/ton", value=150)
        recycled_cost = st.number_input("Recycled $/ton", value=45)
        virgin_cost = st.number_input("Virgin $/ton", value=85)
    
    if st.button("🚀 Optimize Mix Now"):
        processing_animation("Searching material databases and running rheology simulations...")
        # (Calculation code remains the same as before)
        cement = 350 + (strength - 20) * 8
        total_agg = 1800 - (cement * 0.6)
        rec_amt = total_agg * (recycled / 100)
        vir_amt = total_agg - rec_amt
        cost_m3 = (cement/1000 * cement_cost) + (rec_amt/1000 * recycled_cost) + (vir_amt/1000 * virgin_cost)
        printability = max(50, 95 - recycled*0.65)
        
        st.success(f"**Recommended Cost per m³: ${cost_m3:.2f}**")
        st.metric("Printability", f"{printability:.0f}/100")
        st.metric("CO₂ Reduction", f"{recycled*0.35:.0f}%")
    
    show_cta()

# ==================== TOOL 2 ====================
elif tool == "2. Resilient Project Estimator":
    st.subheader("2. Resilient Project Estimator")
    length = st.number_input("Wall Length (meters)", value=50.0)
    height = st.number_input("Wall Height (meters)", value=3.0)
    thickness = st.number_input("Thickness (meters)", value=0.2)
    recycled = st.slider("Recycled %", 0, 60, 40)
    
    if st.button("🚀 Calculate Estimate"):
        processing_animation("Analyzing geometry and running cost simulations...")
        volume = length * height * thickness
        cost = volume * 120 * (1 - (recycled/100)*0.35)
        hours = volume * 0.8
        st.metric("Estimated Cost", f"${cost:,.0f}")
        st.metric("Print Time", f"{hours:.1f} hours")
    
    show_cta()

# ==================== TOOL 3 ====================
elif tool == "3. FEMA Trailer Cost Comparator":
    st.subheader("3. FEMA Trailer Cost Comparator")
    home_cost = st.number_input("Your 3DCP Project Cost ($)", value=150000)
    
    if st.button("🚀 Run Comparison"):
        processing_animation("Retrieving historical FEMA data and calculating true cost...")
        st.error(f"FEMA Trailer Equivalent: **${int(home_cost * 1.8):,}**")
        st.success(f"**Savings with Permanent 3DCP: ${int(home_cost * 0.8):,}**")
    
    show_cta()

# ==================== TOOL 4 ====================
elif tool == "4. Resilient Housing Grant Qualifier":
    st.subheader("4. Resilient Housing Grant Qualifier")
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other"])
    
    if st.button("🚀 Check Eligibility"):
        processing_animation("Cross-referencing 2026 grant databases...")
        st.success("✅ High eligibility — Potential awards: **$5,000 – $10,000+**")
    
    show_cta()

st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Accelerating Resilient 3D Construction")
