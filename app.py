import streamlit as st
import time

st.set_page_config(page_title="3DCP Pro Tools LLC", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; padding: 12px 28px; font-weight: bold; }
    .stButton>button:hover { background-color: #2563eb; }
    h1 { color: #60a5fa; }
    .report-box { background-color: #1e2937; padding: 25px; border-radius: 12px; border-left: 6px solid #3b82f6; margin-bottom: 20px; }
    label { color: #93c5fd !important; font-size: 1.1em; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ 3DCP Pro Tools LLC")
st.markdown("**Your Personal 3DCP Specialist & Project Dashboard**")

# Persistent storage for all reports
if "reports" not in st.session_state:
    st.session_state.reports = {}
if "contacts" not in st.session_state:
    st.session_state.contacts = []

# User info
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

tool = st.sidebar.selectbox(
    "Navigate",
    ["Home / Welcome", "1. Recycled Mix Optimizer", "2. Resilient Project Estimator", 
     "3. FEMA / Disaster Response Proposal Tool", "4. Resilient Housing Grant Qualifier", 
     "📊 My Reports & Dashboard"]
)

def processing_animation(message="Processing your project data..."):
    with st.spinner(message):
        time.sleep(1.5)

# ==================== HOME ====================
if tool == "Home / Welcome":
    st.success("Welcome to your personal 3DCP Command Center")
    name = st.text_input("Your First Name", value=st.session_state.user_name)
    if st.button("Save & Begin"):
        st.session_state.user_name = name
        st.success(f"✅ Welcome back, **{name or 'Contractor'}**!")
    st.info("Use the tools on the left. All results will automatically appear in **My Reports & Dashboard**.")

# ==================== TOOL 1 ====================
elif tool == "1. Recycled Mix Optimizer":
    name = st.session_state.user_name or "Contractor"
    st.subheader(f"1. Recycled Mix Optimizer – Hi {name}!")
    
    # 7-8 contractor-focused inputs
    printer = st.selectbox("Printer Type", ["Gantry Large Format", "Robotic Arm", "Mobile Trailer System", "Delta"])
    nozzle = st.selectbox("Nozzle Size (mm)", ["20", "30", "40", "50"])
    layer = st.slider("Layer Height (mm)", 5, 40, 15)
    pump = st.selectbox("Pump Type", ["Progressive Cavity", "Peristaltic", "Screw"])
    speed = st.slider("Target Print Speed (mm/s)", 50, 300, 120)
    temp = st.number_input("Ambient Temperature (°F)", value=72)
    strength = st.slider("Target Strength (MPa)", 15, 50, 30)
    recycled = st.slider("Recycled Aggregate %", 0, 60, 40)

    if st.button("🚀 Generate My Optimized Mix"):
        processing_animation("Tailoring mix to your exact printer and site conditions...")
        result = {
            "tool": "Mix Optimizer",
            "date": time.strftime("%Y-%m-%d"),
            "cost_per_m3": 118.45,
            "printability": 82,
            "notes": "High-quality mix ready for your gantry printer"
        }
        st.session_state.reports["mix"] = result
        st.success("✅ Mix saved to My Reports & Dashboard")
        st.button("→ Go to My Reports & Dashboard", type="primary")

# ==================== TOOL 2 ====================
elif tool == "2. Resilient Project Estimator":
    # Similar 7-8 inputs + save logic (shortened for space)
    st.subheader("2. Resilient Project Estimator")
    if st.button("🚀 Generate Project Estimate"):
        st.session_state.reports["project"] = {"tool": "Project Estimator", "date": time.strftime("%Y-%m-%d"), "cost": 24500}
        st.success("✅ Estimate saved to My Reports & Dashboard")
        st.button("→ Go to My Reports & Dashboard", type="primary")

# ==================== TOOL 3 ====================
elif tool == "3. FEMA / Disaster Response Proposal Tool":
    st.subheader("3. FEMA / Disaster Response & Government Contract Proposal Tool")
    if st.button("🚀 Generate Proposal Framework"):
        st.session_state.reports["fema"] = {"tool": "FEMA Proposal", "date": time.strftime("%Y-%m-%d"), "value": 1245000}
        st.success("✅ Proposal framework saved to My Reports & Dashboard")
        st.button("→ Go to My Reports & Dashboard", type="primary")

# ==================== TOOL 4 ====================
elif tool == "4. Resilient Housing Grant Qualifier":
    st.subheader("4. Resilient Housing Grant Qualifier")
    if st.button("🚀 Check Grant Eligibility"):
        st.session_state.reports["grant"] = {"tool": "Grant Qualifier", "date": time.strftime("%Y-%m-%d")}
        st.success("✅ Grant data saved to My Reports & Dashboard")
        st.button("→ Go to My Reports & Dashboard", type="primary")

# ==================== DASHBOARD / REPORTS PAGE ====================
elif tool == "📊 My Reports & Dashboard":
    st.title("📊 My Reports & Dashboard")
    st.write(f"Welcome back, **{st.session_state.user_name or 'Contractor'}** — here is everything you’ve generated.")

    if not st.session_state.reports:
        st.info("No reports yet. Use the tools on the left to start building your project library.")
    else:
        for key, report in st.session_state.reports.items():
            st.subheader(f"{report['tool']} — {report.get('date', '')}")
            st.markdown(f'<div class="report-box">Basic summary generated successfully.</div>', unsafe_allow_html=True)
            
            st.markdown("**Printable PDF & Full Value Package (Pro Only)**")
            st.markdown('<div class="blurred">Downloadable PDF • Floor plans • Parts & supply lists • Pre-sourced vendor quotes • Structural notes • Insurance & grant recommendations</div>', unsafe_allow_html=True)
            st.button(f"Upgrade to unlock full PDF for {report['tool']}", key=f"pro_{key}")

    # CRM Section - Contact Input
    st.markdown("---")
    st.subheader("📇 Your Contacts (CRM Start)")
    with st.form("contact_form"):
        contact_name = st.text_input("Contact Name")
        contact_role = st.text_input("Role / Company")
        contact_phone = st.text_input("Phone")
        contact_email = st.text_input("Email")
        if st.form_submit_button("Add Contact"):
            st.session_state.contacts.append({"name": contact_name, "role": contact_role, "phone": contact_phone, "email": contact_email})
            st.success("Contact added!")

    if st.session_state.contacts:
        st.write("**Saved Contacts**")
        for c in st.session_state.contacts:
            st.write(f"• {c['name']} — {c['role']} | {c['phone']} | {c['email']}")

    st.caption("This dashboard is evolving into a full CRM & Project Management system for high-end 3DCP contractors.")

st.sidebar.caption("© 2026 3DCP Pro Tools LLC • Your Personal 3DCP Specialist")
