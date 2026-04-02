import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

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
        padding: 12px 28px; 
        font-weight: bold; 
    }
    .stButton>button:hover { background-color: #2563eb; }

    /* Extra large title */
    h1 { 
        color: #60a5fa; 
        font-size: 3.8em !important; 
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }

    /* Much larger top navigation */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.45em !important;
        font-weight: 700 !important;
        padding: 18px 28px !important;
        margin: 0 8px !important;
        letter-spacing: 0.5px;
    }

    /* Creative cursive lattice sentence */
    .lattice {
        font-family: 'Georgia', serif;
        font-size: 1.35em;
        font-style: italic;
        color: #94a3b8;
        text-align: center;
        margin: 8px 0 25px 0;
        letter-spacing: 1.5px;
        opacity: 0.85;
    }
    </style>
""", unsafe_allow_html=True)

st.title("3DCP Pro Tools LLC")

# Creative lattice sentence under the title
st.markdown('<p class="lattice">Empowering the future of resilient 3D construction • One precise layer at a time</p>', unsafe_allow_html=True)

# Top Navigation - Very Bold & Large
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Home", 
    "🔧 Mix Optimizer", 
    "📏 Project Estimator", 
    "📋 FEMA Proposal Tool", 
    "🏛️ Grant Qualifier", 
    "📊 My Dashboard"
])

# User info persistence
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
                st.success(f"✅ Thank you! Your complete report package has been requested.")
    with col2:
        st.markdown("**Instant Pro Upgrade**")
        st.markdown("[**Pro Lifetime Access – $99**](https://gumroad.com/l/YOUR-LIFETIME-LINK)")
        st.markdown("[**Pro Monthly – $29**](https://gumroad.com/l/YOUR-MONTHLY-LINK)")

# ==================== HOME TAB ====================
with tab1:
    st.title("Welcome to 3DCP Pro Tools LLC")
    st.write("The premier software platform for professional 3D construction printing contractors.")
    
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    
    if st.button("Save My Name & Get Started"):
        st.session_state.user_name = name
        st.success(f"✅ Welcome, **{name or 'Contractor'}**!")
        st.markdown(f"""
            <div style="background-color:#1e2937; padding:20px; border-radius:12px; margin:20px 0;">
                👋 Hi <strong>{name or 'there'}</strong>! I'm your personal 3DCP specialist.<br>
                <span style="font-size:1.8em;">👉</span> Use the bold tabs above to explore the tools. 
                Everything you create will be saved in <strong>My Dashboard</strong>.
            </div>
        """, unsafe_allow_html=True)

# ==================== MIX OPTIMIZER TAB ====================
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
    
    st.subheader("Advanced Mix Parameters (Pro Only)")
    st.slider("Fiber Reinforcement %", 0, 5, 1, disabled=True)
    st.selectbox("Rheology Modifier", ["None", "VMA", "Superplasticizer"], disabled=True)
    
    if st.button("🚀 Generate Optimized Mix"):
        processing_animation("Tailoring mix to your printer...")
        st.success("Basic mix recommendation generated.")
        st.button("→ View in My Dashboard", type="primary")

# (Other tabs follow the same pattern - shortened here for brevity)

with tab6:
    st.title("📊 My Dashboard & Reports")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}**")
    st.info("Your generated reports will appear here once you use the tools above.")

st.caption("© 2026 3DCP Pro Tools LLC • The Leading Software Platform for 3D Construction Printing")
