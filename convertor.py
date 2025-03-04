import streamlit as st 
import time 

st.markdown("<h1>Unit convertor using python and streamlit</h1>", unsafe_allow_html=True) 
st.write("Easily convert between different units of Length, Weight")

conversion_type = st.selectbox("Choose Conversion Type", ["Length", "Weight"])
value = st.number_input("Enter your value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Kilometer", "Meter", "Centimeter", "Millimeter", "Miles", "Yard", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Kilometer", "Meter", "Centimeter", "Millimeter", "Miles", "Yard", "Inches", "Feet"])
   
elif conversion_type == "Weight":
    with col1:  
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounce"])
    with col2:     
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounce"])

def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meter': 1,
        'Kilometer': 0.001, 
        'Centimeter': 100, 
        'Millimeter': 1000, 
        'Miles': 0.000621371, 
        'Yard': 1.09361, 
        'Feet': 3.28, 
        'Inches': 39.37
    } 
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1,  
        'Gram': 100, 
        'Milligram': 1000000, 
        'Pounds': 2.2046, 
        'Ounce': 35.27
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div style='padding: 20px; background-color: #f0f2f6; border-radius: 5px;'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
        