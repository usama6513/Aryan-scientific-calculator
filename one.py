import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify, pi, sin, cos, tan


# Page Configuration (This should be one of the first commands)
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# ✅ Inject Custom CSS (right after imports)
# Inject Custom CSS (right after imports)
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Light Alice Blue color */
            font-family: 'Roboto', sans-serif;
            color: #333333;  /* Dark gray text for contrast */
        }
        h1, h2 {
            color: #2e86de;  /* Soft Blue color for headers */
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;  /* Green button */
            color: white;
            border-radius: 6px;
            padding: 10px 18px;
            transition: 0.3s ease;
            margin-top: 10px;
        }
        .stButton>button:hover {
            background-color: #2e7d32;  /* Darker green on hover */
        }
        .stTextInput>div>input,
        .stTextArea>div>textarea,
        .stNumberInput>div>input,
        .stSelectbox>div>div>input {
            background-color: #ffffff;
            border: 1px solid #ddd;  /* Light border for text inputs */
            border-radius: 8px;
            padding: 10px;
            margin: 10px 0;
            font-size: 16px;
            transition: border 0.3s ease;
        }
        .stTextInput>div>input:focus,
        .stTextArea>div>textarea:focus,
        .stNumberInput>div>input:focus,
        .stSelectbox>div>div>input:focus {
            border: 1px solid #2e86de;  /* Blue border on focus */
            outline: none;
        }
        .stTextInput>div>input::placeholder,
        .stTextArea>div>textarea::placeholder {
            color: #bbb;  /* Placeholder text color */
        }
        .stTextInput, .stTextArea {
            margin-top: 20px;
        }
        .stAlert {
            background-color: #f9c2c2;  /* Light red for alerts */
            border: 1px solid #f2a1a1;
            color: #d40000;
            padding: 12px;
            border-radius: 4px;
        }
        .stMatrix, .stSelectbox {
            margin-top: 20px;
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #ddd;
        }
        .stMatrix > div, .stSelectbox > div {
            font-size: 14px;
            margin-bottom: 10px;
        }
        .stMatrix button, .stSelectbox button {
            margin: 5px;
        }
        .footer {
            margin-top: 50px;
            color: #888;
            text-align: center;
            font-size: 13px;
        }
        .result-box {
            background-color: #e8f4f9;
            border: 1px solid #2e86de;
            padding: 15px;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .result-box > div {
            padding: 5px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)


# Title
st.title("🧮 Scientific Calculator")

# Trigonometric Functions
st.subheader("Trigonometric Functions")
shift = st.checkbox("Shift (Inverse Functions)")
angle_input = st.number_input("Enter angle in degrees:", value=30.0)

if shift:
    try:
        st.write(f"arcsin({math.sin(math.radians(angle_input))}) = {math.degrees(math.asin(math.sin(math.radians(angle_input)))):.4f}°")
        st.write(f"arccos({math.cos(math.radians(angle_input))}) = {math.degrees(math.acos(math.cos(math.radians(angle_input)))):.4f}°")
        st.write(f"arctan({math.tan(math.radians(angle_input))}) = {math.degrees(math.atan(math.tan(math.radians(angle_input)))):.4f}°")
    except ValueError:
        st.write("Invalid input for inverse trigonometric functions.")
else:
    st.write(f"sin({angle_input}°) = {math.sin(math.radians(angle_input)):.4f}")
    st.write(f"cos({angle_input}°) = {math.cos(math.radians(angle_input)):.4f}")
    st.write(f"tan({angle_input}°) = {math.tan(math.radians(angle_input)):.4f}")

# Matrix Operations (For addition and multiplication)
st.subheader("Matrix Operations")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix 1:")
st.write(matrix_1)
st.write("Matrix 2:")
st.write(matrix_2)

operation = st.selectbox("Select matrix operation", ["Add", "Multiply"])

if st.button("Perform Matrix Operation"):
    try:
        if operation == 'Add':
            result = np.add(matrix_1, matrix_2)
        elif operation == 'Multiply':
            result = np.dot(matrix_1, matrix_2)
        else:
            result = "Unsupported Operation"
        st.write(f"✅ Result of Matrix {operation}:")
        st.write(result)
    except Exception as e:
        st.write(f"Error: {e}")

# Derivatives and Integrals
st.subheader("Derivatives and Integrals")
expression_input = st.text_input("Enter a mathematical expression (e.g., x**2 + y**2):", "x**2 + y**2")
variables_input = st.text_input("Enter variables separated by commas (e.g., x,y):", "x,y")
operation_type = st.selectbox("Choose operation", ["Derivative", "Indefinite Integral", "Definite Integral"])

# Define variables
variables = symbols(variables_input)
expr = sympify(expression_input)

# Derivative button
if operation_type == "Derivative":
    if st.button("Calculate Derivative"):
        try:
            var_to_diff = st.selectbox("Select variable to differentiate with respect to:", variables)
            derivative_result = diff(expr, var_to_diff)
            st.write(f"✅ Derivative of {expression_input} with respect to {var_to_diff}:")
            st.latex(f"\frac{{d}}{{d{var_to_diff}}}({expression_input}) = {derivative_result}")
        except Exception as e:
            st.write(f"Error: {e}")

# Indefinite Integral button
elif operation_type == "Indefinite Integral":
    if st.button("Calculate Indefinite Integral"):
        try:
            var_to_integrate = st.selectbox("Select variable to integrate with respect to:", variables)
            integral_result = integrate(expr, var_to_integrate)
            st.write(f"✅ Indefinite Integral of {expression_input} with respect to {var_to_integrate}:")
            st.latex(f"∫ {expression_input} dx = {integral_result} + C")
        except Exception as e:
            st.write(f"Error: {e}")

# Definite Integral button
from sympy import pi  # make sure pi is imported

lower_limit_str = st.text_input(f"Enter lower limit for {var_to_integrate} (e.g. 0, pi/2):", value="0")
upper_limit_str = st.text_input(f"Enter upper limit for {var_to_integrate} (e.g. pi, 2*pi):", value="pi")

try:
    lower_limit = sympify(lower_limit_str)
    upper_limit = sympify(upper_limit_str)

    if st.button("Compute Definite Integral"):
        integral_result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
        st.markdown(f"<div class='result-box'>✅ Definite Integral of <b>{expression_input}</b> from <b>{lower_limit}</b> to <b>{upper_limit}</b> w.r.t <b>{var_to_integrate}</b>:<br><br><b>{integral_result}</b></div>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"⚠️ Invalid input: {e}")


# Footer
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif</div>", unsafe_allow_html=True)
