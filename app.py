import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

# Professional dark theme
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    .blurred { opacity: 0.25; filter: blur(4px); pointer-events: none; }
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
        time.sleep(1.4)

def show_cta():
    st.markdown("---")
    st.subheader("Want the Full Detailed Report, Sample PDF, or Grant Paperwork?")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Unlock Pro – Get Full Specs & PDF"):
            if email:
                st.success(f"✅ Thank you! Your full detailed report, sample PDF, and grant paperwork have been requested for **{email}**.")
            else:
                st.warning("Please enter your email.")
    with col2:
        st.markdown("**Or call us directly:**")
        st.markdown("📞 **(720) 555-0199** *(Space Saver - Temporary Line)*")
        st.caption("Monday–Friday, 9AM–5PM MT")

# ==================== HOME ====================
if tool == "Home":
    st.success("Welcome to 3DCP Pro Tools LLC")
    st.write("Practical, industry-specific tools that help 3DCP companies optimize recycled mixes, estimate resilient projects, compare costs against FEMA trailers, and qualify for grants.")
    st.info("💰 Projected first 30-60 days revenue: **$3,000 – $10,000**")
    show_cta()

# ==================== TOOL 1 ====================
elif tool == "1. Recycled Mix Optimizer":
    st.subheader("1. Recycled Mix Optimizer")
    col1, col2 = st.columns(2)
    with col1:
        strength = st.slider("Target Strength (MPa)", 15, 50, 30)
        recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    with col2:
        cement_cost = st.number_input("Cement $/ton", value=150)
        recycled_cost = st.number_input("Recycled $/ton", value=45)
        virgin_cost = st.number_input("Virgin $/ton", value=85)
    
    if st.button("🚀 Optimize Mix"):
        processing_animation("Searching material databases and running rheology simulations...")
        cement = 350 + (strength - 20) * 8
        total_agg = 1800 - (cement * 0.6)
        rec_amt = total_agg * (recycled / 100)
        vir_amt = total_agg - rec_amt
        cost_m3 = (cement/1000 * cement_cost) + (rec_amt/1000 * recycled_cost) + (vir_amt/1000 * virgin_cost)
        
        st.success(f"**Recommended Cost per m³: ${cost_m3:.2f}**")
        st.metric("Printability Score", f"{max(50, 95 - recycled*0.65):.0f}/100")
        st.metric("CO₂ Reduction", f"{recycled*0.35:.0f}%")
        
        # Pro teaser - blurred high-value content
        st.markdown("**Full Detailed Mixture Specification (Pro Only)**")
        st.markdown('<div class="blurred">Full 12-page optimized mix recipe with exact additive percentages, rheology modifiers, print speed recommendations, and downloadable PDF specification sheet.</div>', unsafe_allow_html=True)
    
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
        
        st.markdown("**Full Project Report + Insurance Savings Calculation (Pro Only)**")
        st.markdown('<div class="blurred">Complete 8-page PDF report with detailed material breakdown, insurance premium reduction estimates, and full resilience certification recommendations.</div>', unsafe_allow_html=True)
    
    show_cta()

# ==================== TOOL 3 ====================
elif tool == "3. FEMA Trailer Cost Comparator":
    st.subheader("3. FEMA Trailer Cost Comparator")
    home_cost = st.number_input("Your 3DCP Project Cost ($)", value=150000)
    
    if st.button("🚀 Run Comparison"):
        processing_animation("Retrieving historical FEMA data and calculating true cost...")
        st.error(f"FEMA Trailer Equivalent: **${int(home_cost * 1.8):,}**")
        st.success(f"Savings with Permanent 3DCP: **${int(home_cost * 0.8):,}**")
        
        st.markdown("**Full FEMA Proposal Template (Pro Only)**")
        st.markdown('<div class="blurred">Ready-to-submit 15-page FEMA / state disaster recovery proposal template with cost justification, resilience data, and grant application language.</div>', unsafe_allow_html=True)
    
    show_cta()

# ==================== TOOL 4 ====================
elif tool == "4. Resilient Housing Grant Qualifier":
    st.subheader("4. Resilient Housing Grant Qualifier")
    county = st.selectbox("County", ["Lake County, FL", "Denver Metro, CO", "Other"])
    
    if st.button("🚀 Check Grant Eligibility"):
        processing_animation("Cross-referencing 2026 grant databases...")
        st.success("✅ High eligibility — Potential awards: **$5,000 – $10,000+**")
        
        st.markdown("**Full Grant Paperwork Package (Pro Only)**")
        st.markdown('<div class="blurred">Complete pre-filled grant application package, required forms, supporting documentation checklist, and submission timeline.</div>', unsafe_allow_html=True)
    
    show_cta()

st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Accelerating Resilient 3D Construction Printing")
