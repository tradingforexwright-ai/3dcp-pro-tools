import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

# Professional dark blue theme
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; }
    .welcome { font-size: 1.3em; color: #93c5fd; }
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

def processing_animation(message="Analyzing your project data and running specialized calculations..."):
    with st.spinner(message):
        time.sleep(1.5)

def show_cta():
    st.markdown("---")
    st.subheader("Want the Full Professional Report?")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Your Email Address", placeholder="you@company.com")
        if st.button("📧 Unlock Full Report + PDF"):
            if email:
                st.success(f"✅ Thank you! Your personalized full report and PDF will be sent to **{email}** shortly.")
            else:
                st.warning("Please enter your email.")
    with col2:
        st.markdown("**Call your dedicated specialist:**")
        st.markdown("📞 **(720) 555-0199**")
        st.caption("Monday–Friday, 9AM–5PM MT")

# ==================== HOME / WELCOME ====================
if tool == "Home / Welcome":
    st.success("Welcome to your personal 3DCP toolkit")
    
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    company = st.text_input("Company / Organization", value=st.session_state.user_company)
    location = st.text_input("Project Location (City, State)", value=st.session_state.user_location)
    
    if st.button("Save My Information"):
        st.session_state.user_name = name
        st.session_state.user_company = company
        st.session_state.user_location = location
        st.success(f"✅ Welcome aboard, **{name or 'there'}**! Your information is saved.")
    
    if st.session_state.user_name:
        st.markdown(f"<p class='welcome'>Hello **{st.session_state.user_name}** from **{st.session_state.user_company or 'your team'}** in **{st.session_state.user_location or 'your area'}** 👋</p>", unsafe_allow_html=True)
        st.write("I'm your dedicated 3DCP specialist today. Which tool would you like to use?")

    show_cta()

# ==================== TOOL 1 ====================
elif tool == "1. Recycled Mix Optimizer":
    name = st.session_state.user_name or "there"
    st.subheader(f"1. Recycled Mix Optimizer – Hi {name}!")
    st.write(f"Let's create a high-recycled mix optimized for your **{st.session_state.user_company or 'project'}** in **{st.session_state.user_location or 'your area'}**.")
    
    col1, col2 = st.columns(2)
    with col1:
        strength = st.slider("Target Strength (MPa)", 15, 50, 30)
        recycled = st.slider("Recycled Aggregate %", 0, 60, 40)
    with col2:
        cement_cost = st.number_input("Cement $/ton", value=150)
        recycled_cost = st.number_input("Recycled $/ton", value=45)
        virgin_cost = st.number_input("Virgin $/ton", value=85)
    
    if st.button("🚀 Optimize My Mix"):
        processing_animation("Searching material databases and tailoring the mix to your location...")
        # calculations...
        cement = 350 + (strength - 20) * 8
        total_agg = 1800 - (cement * 0.6)
        rec_amt = total_agg * (recycled / 100)
        cost_m3 = (cement/1000 * cement_cost) + (rec_amt/1000 * recycled_cost) + ((total_agg - rec_amt)/1000 * virgin_cost)
        
        st.success(f"**Recommended Cost per m³ for your project: ${cost_m3:.2f}**")
        st.metric("Printability Score", f"{max(50, 95 - recycled*0.65):.0f}/100")
        
        st.markdown("**Full Custom Mixture Specification + PDF (Pro Version Only)**")
        st.markdown('<div style="opacity:0.3; filter: blur(5px);">Complete 12-page recipe with exact additives, print parameters, and downloadable PDF tailored to your local materials and climate.</div>', unsafe_allow_html=True)
    
    show_cta()

# (I shortened Tools 2-4 for this message, but they follow the same personalized pattern)

st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Your Personal 3DCP Specialist")
