import streamlit as st

# Set Page Config
st.set_page_config(page_title="MechConverter & Density Checker", layout="centered")

# --- HEADER SECTION ---
st.title("Mechanical Unit Converter & Material Density Checker")
st.markdown(f"""
**Developer:** Muzammil Khan  
**Roll Number:** 25-ME-100  
---
""")

# --- SIDEBAR / NAVIGATION ---
option = st.sidebar.selectbox("Select Function", ["Unit Converter", "Material Density Checker"])

if option == "Unit Converter":
    st.header("⚖️ Mechanical Unit Converter")
    
    conv_type = st.selectbox("Select Conversion Type", ["Length", "Pressure", "Force"])
    
    col1, col2 = st.columns(2)
    
    if conv_type == "Length":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Meters", "Millimeters", "Inches", "Feet"])
        with col2:
            unit_to = st.selectbox("To", ["Meters", "Millimeters", "Inches", "Feet"])
            
        # Conversion Factors to Meters
        factors = {"Meters": 1, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
        result = val * (factors[unit_from] / factors[unit_to])
        st.success(f"**Result:** {result:.4f} {unit_to}")

    elif conv_type == "Pressure":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere"])
        with col2:
            unit_to = st.selectbox("To", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere"])
            
        factors = {"Pascal (Pa)": 1, "Bar": 100000, "PSI": 6894.76, "Atmosphere": 101325}
        result = val * (factors[unit_from] / factors[unit_to])
        st.success(f"**Result:** {result:.4f} {unit_to}")

    elif conv_type == "Force":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
        with col2:
            unit_to = st.selectbox("To", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
            
        factors = {"Newton (N)": 1, "Kilonewton (kN)": 1000, "Pound-force (lbf)": 4.44822}
        result = val * (factors[unit_from] / factors[unit_to])
        st.success(f"**Result:** {result:.4f} {unit_to}")

else:
    st.header("🏗️ Material Density Checker")
    
    # Dictionary of Materials and Densities (kg/m^3)
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Concrete": 2400,
        "Water": 1000,
        "Lead": 11340
    }
    
    selected_material = st.selectbox("Select Material", list(densities.keys()))
    density_val = densities[selected_material]
    
    st.info(f"The density of **{selected_material}** is approximately **{density_val} kg/m³**.")
    
    # Simple Mass Calculation Feature
    st.subheader("Mass Estimator")
    volume = st.number_input("Enter Volume (m³)", value=1.0, min_value=0.0)
    mass = volume * density_val
    st.write(f"Estimated Mass: **{mass:.2f} kg**")

st.markdown("---")
st.caption("2026 Mechanical Engineering Project | Powered by Streamlit")
