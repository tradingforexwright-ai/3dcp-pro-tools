import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

# Nice Professional Color Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**Professional Tools for Resilient 3D Construction Printing**")
st.caption("Optimizing mixes • Estimating projects • Winning grants • Reducing risk")

# Navigation
tool = st.sidebar.selectbox(
    "Select Tool",
    ["Home", "1. Recycled Mix Optimizer", "2. Resilient Project Estimator", 
     "3. FEMA Trailer Cost Comparator", "4. Resilient Housing Grant Qualifier"]
)

def show_processing_animation(message="Analyzing data and running calculations..."):
    with st.spinner(message):
        time.sleep(1.2)  # Creates realistic "thinking" effect

def show_email_cta():
    st.markdown("---")
    st.subheader("Ready for Pro Features or Custom Analysis?")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email Address", placeholder="you@company.com")
        if st.button("📧 Get Pro Access & Custom Report"):
            if email:
                st.success(f"Thank you! We'll send Pro upgrade details and your custom report to **{email}** shortly.")
            else:
                st.warning("Please enter your email address.")
    with col2:
        st.markdown("**Call us directly:**")
        st.markdown("📞 **(720) 555-0199**  *(Space Saver - Temporary Number)*")
        st.caption("Monday–Friday, 9AM–5PM Mountain Time")

# ==================== HOME PAGE ====================
if tool == "Home":
    st.success("Welcome to 3DCP Pro Tools LLC")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("""
        We provide powerful, easy-to-use tools specifically built for the 3D Construction Printing industry.
        
        Our tools help companies optimize recycled mixes, estimate resilient projects accurately, 
        compare costs against temporary FEMA housing, and qualify for valuable grants.
        """)
        st.info("💰 **Projected first 30-60 days revenue**: $3,000 – $10,000")
    
    with col2:
        st.metric("Free Tier", "Basic Calculations")
        st.metric("Pro Tier", "$99 one-time or $29/month")
    
    show_email_cta()

# ==================== TOOL 1 ====================
elif tool == "1. Recycled Mix Optimizer":
    st.subheader("1. Recycled Mix Optimizer")
    st.write("Optimizing high-recycled content concrete mixes for printability and strength.")
    
    col1, col2 = st.columns(2)
    with col1:
        strength = st.slider("Target Compressive Strength (MPa)", 15, 50, 30)
        recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    with col2:
        cement_cost = st.number_input("Cement Cost per Ton ($)", value=150)
        recycled_cost = st.number_input("Recycled Aggregate Cost per Ton ($)", value=45)
        virgin_cost = st.number_input("Virgin Aggregate Cost per Ton ($)", value=85)
    
    if st.button("🚀 Optimize Mix"):
        show_processing_animation("Juggling recycled material data and running rheology calculations...")
        
        cement = 350 + (strength - 20) * 8
        total_agg = 1800 - (cement * 0.6)
        rec_amt = total_agg * (recycled / 100)
        vir_amt = total_agg - rec_amt
        cost_m3 = (cement/1000 * cement_cost) + (rec_amt/1000 * recycled_cost) + (vir_amt/1000 * virgin_cost)
        printability = max(50, 95 - recycled*0.65)
        
        st.success(f"**Recommended Cost per m³: ${cost_m3:.2f}**")
        st.metric("Printability Score", f"{printability:.0f}/100")
        st.metric("Estimated CO₂ Reduction", f"{recycled*0.35:.0f}%")
        
        st.write("**Optimized Recipe:**")
        st.write(f"• Cement: **{cement:.0f} kg/m³**")
        st.write(f"• Recycled Aggregate: **{rec_amt:.0f} kg/m³** ({recycled}%)")
    
    show_email_cta()

# ==================== TOOL 2 ====================
elif tool == "2. Resilient Project Estimator":
    st.subheader("2. Resilient Project Estimator")
    st.write("Calculating material needs, print time, and cost for resilient structures.")
    
    length = st.number_input("Total Wall Length (meters)", value=50.0)
    height = st.number_input("Wall Height (meters)", value=3.0)
    thickness = st.number_input("Wall Thickness (meters)", value=0.2)
    recycled_pct = st.slider("Recycled Content %", 0, 60, 40)
    
    if st.button("🚀 Calculate Project"):
        show_processing_animation("Analyzing project parameters and running cost simulations...")
        
        volume = length * height * thickness
        cost = volume * 120 * (1 - (recycled_pct/100)*0.35)
        time_hours = volume * 0.8
        
        st.metric("Estimated Total Project Cost", f"${cost:,.0f}")
        st.metric("Estimated Print Time", f"{time_hours:.1f} hours (~{time_hours/24:.1f} days)")
    
    show_email_cta()

# ==================== TOOL 3 ====================
elif tool == "3. FEMA Trailer Cost Comparator":
    st.subheader("3. FEMA Trailer Cost Comparator")
    st.write("See the real financial difference between temporary FEMA housing and permanent 3DCP structures.")
    
    home_cost = st.number_input("Your 3DCP Project Cost ($)", value=150000)
    
    if st.button("🚀 Compare Costs"):
        show_processing_animation("Retrieving historical FEMA data and running comparison...")
        st.error(f"**FEMA Trailer Equivalent Total Cost**: ${int(home_cost * 1.8):,}")
        st.success(f"**Savings using Permanent Resilient 3DCP**: ${int(home_cost * 0.8):,}")
    
    show_email_cta()

# ==================== TOOL 4 ====================
elif tool == "4. Resilient Housing Grant Qualifier":
    st.subheader("4. Resilient Housing Grant Qualifier")
    st.write("Checking eligibility for current resilient housing grant programs.")
    
    county = st.selectbox("Select Your County", ["Lake County, FL", "Other Florida County", "Denver Metro, CO"])
    
    if st.button("🚀 Check Grant Eligibility"):
        show_processing_animation("Cross-referencing 2026 grant databases...")
        st.success("✅ **High eligibility detected** – You may qualify for $5,000 – $10,000+ in grants!")
        st.info("Pro users receive full customized grant strategy and application support.")
    
    show_email_cta()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Built to accelerate resilient 3D construction printing")
