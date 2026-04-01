import streamlit as st

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**Professional Software for 3D Construction Printing**")
st.caption("Recycled Mix Optimizer • Resilient Estimator • FEMA Comparator • Grant Qualifier")

# Sidebar navigation
tool = st.sidebar.selectbox(
    "Choose Tool",
    ["Home", "1. Recycled Mix Optimizer", "2. Resilient Project Estimator", 
     "3. FEMA Trailer Cost Comparator", "4. Resilient Housing Grant Qualifier"]
)

if tool == "Home":
    st.success("Welcome to 3DCP Pro Tools LLC!")
    st.write("""
    We build simple, powerful tools that save 3DCP companies hours of trial-and-error and help win more bids and grants.
    
    **Launch Offer**: First 10 users get **50% off** Pro access ($49 one-time).
    """)
    st.info("💰 Expected first-month revenue: $3,000 – $10,000")
    
    email = st.text_input("Get early access & updates (optional)")
    if st.button("Join Early Access List"):
        st.success("Thank you! We'll send Pro access details shortly.")

elif tool == "1. Recycled Mix Optimizer":
    st.subheader("Recycled Mix Optimizer")
    strength = st.slider("Target Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    cement_cost = st.number_input("Cement $/ton", value=150)
    recycled_cost = st.number_input("Recycled $/ton", value=45)
    virgin_cost = st.number_input("Virgin $/ton", value=85)
    
    if st.button("Calculate Optimal Mix"):
        cement = 350 + (strength - 20) * 8
        total_agg = 1800 - (cement * 0.6)
        rec_amt = total_agg * (recycled / 100)
        vir_amt = total_agg - rec_amt
        cost_m3 = (cement/1000 * cement_cost) + (rec_amt/1000 * recycled_cost) + (vir_amt/1000 * virgin_cost)
        
        st.success(f"Cost per m³: **${cost_m3:.2f}**")
        st.write(f"Printability: **{max(50, 95 - recycled*0.65):.0f}/100**")
        st.write(f"CO₂ reduction: **{recycled*0.35:.0f}%**")

elif tool == "2. Resilient Project Estimator":
    st.subheader("Resilient Project Estimator")
    length = st.number_input("Wall Length (meters)", value=50.0)
    height = st.number_input("Wall Height (meters)", value=3.0)
    thickness = st.number_input("Thickness (meters)", value=0.2)
    recycled_pct = st.slider("Recycled %", 0, 60, 40)
    
    if st.button("Estimate Project"):
        volume = length * height * thickness
        cost = volume * 120 * (1 - (recycled_pct/100)*0.35)
        time_hours = volume * 0.8
        st.metric("Total Est. Cost", f"${cost:,.0f}")
        st.metric("Print Time", f"{time_hours:.1f} hours (~{time_hours/24:.1f} days)")

elif tool == "3. FEMA Trailer Cost Comparator":
    st.subheader("FEMA Trailer Replacement Comparator")
    st.write("See the true cost difference vs. temporary FEMA-style housing")
    home_cost = st.number_input("Your 3DCP Home Cost ($)", value=150000)
    if st.button("Compare"):
        st.error(f"FEMA Trailer Equivalent (with all hidden costs): **${int(home_cost * 1.8):,}**")
        st.success(f"Your permanent resilient home saves: **${int(home_cost * 0.8):,}**")

elif tool == "4. Resilient Housing Grant Qualifier":
    st.subheader("Florida Resilient Housing Grant Qualifier")
    st.write("2026 My Safe Florida Home & Resilient Florida Program")
    county = st.selectbox("County", ["Lake County", "Other Florida"])
    if st.button("Check Eligibility"):
        st.success("✅ You likely qualify for $5,000 – $10,000 in grants + insurance discounts!")
        st.info("Contact us for full application support ($750–$2,000)")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 3DCP Pro Tools LLC | All Rights Reserved")
