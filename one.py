import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify, pi, sin, cos, tan


# Page Configuration (This should be one of the first commands)
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# ✅ Inject Custom CSS (right after imports)
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
        }
        .stButton>button:hover {
            background-color: #2e7d32;  /* Darker green on hover */
        }
        .stTextInput>div>input {
            background-color: #ffffff;
            border: 1px solid #ddd;  /* Light border for text inputs */
            border-radius: 4px;
            padding: 8px;
            margin: 6px 0;
        }
        .stTextArea>div>textarea {
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 8px;
            margin: 6px 0;
        }
        .stSelectbox>div>div>input {
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 8px;
            margin: 6px 0;
        }
        .footer {
            margin-top: 50px;
            color: #888;
            text-align: center;
            font-size: 13px;
        }
        .stAlert {
            background-color: #f9c2c2;  /* Light red for alerts */
            border: 1px solid #f2a1a1;
            color: #d40000;
            padding: 12px;
            border-radius: 4px;
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
elif operation_type == "Definite Integral":
    if st.button("Calculate Definite Integral"):
        try:
            var_to_integrate = st.selectbox("Select variable to integrate with respect to:", variables)
            lower_limit = st.number_input(f"Enter lower limit for {var_to_integrate}:", value=0.0)
            upper_limit = st.number_input(f"Enter upper limit for {var_to_integrate}:", value=1.0)
            integral_result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
            st.write(f"✅ Definite Integral of {expression_input} with respect to {var_to_integrate} from {lower_limit} to {upper_limit}:")
            st.latex(f"∫_{{{lower_limit}}}^{{{upper_limit}}} ({expression_input}) d{var_to_integrate} = {integral_result}")
        except Exception as e:
            st.write(f"Error: {e}")

# Footer
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif</div>", unsafe_allow_html=True)
