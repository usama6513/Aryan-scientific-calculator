import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify

# ✅ Page configuration MUST be the first Streamlit command
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# ✅ Link to custom CSS file (inside assets folder)
st.markdown('<link href="assets/style.css" rel="stylesheet">', unsafe_allow_html=True)

# Title
st.title("🧮 Scientific Calculator")

# ----------------------------------
# Trigonometric Functions Section
# ----------------------------------
st.subheader("📐 Trigonometric Functions")
shift = st.checkbox("Shift (Inverse Functions)")
angle_input = st.number_input("Enter angle in degrees:", value=0.0)

if st.button("Calculate Trigonometric Functions"):
    if shift:
        try:
            st.write(f"arcsin(sin({angle_input}°)) = {math.degrees(math.asin(math.sin(math.radians(angle_input)))):.4f}°")
            st.write(f"arccos(cos({angle_input}°)) = {math.degrees(math.acos(math.cos(math.radians(angle_input)))):.4f}°")
            st.write(f"arctan(tan({angle_input}°)) = {math.degrees(math.atan(math.tan(math.radians(angle_input)))):.4f}°")
        except ValueError:
            st.write("⚠️ Invalid input for inverse trigonometric functions.")
    else:
        st.write(f"sin({angle_input}°) = {math.sin(math.radians(angle_input)):.4f}")
        st.write(f"cos({angle_input}°) = {math.cos(math.radians(angle_input)):.4f}")
        st.write(f"tan({angle_input}°) = {math.tan(math.radians(angle_input)):.4f}")

# ----------------------------------
# Matrix Operations Section
# ----------------------------------
st.subheader("🧮 Matrix Operations")

matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix 1:")
st.write(matrix_1)

st.write("Matrix 2:")
st.write(matrix_2)

operation = st.selectbox("Select matrix operation", ["Add", "Multiply"])

def matrix_operations(matrix_1, matrix_2, operation):
    try:
        if operation == 'Add':
            return np.add(matrix_1, matrix_2)
        elif operation == 'Multiply':
            return np.dot(matrix_1, matrix_2)
        else:
            return "Unsupported Operation"
    except Exception as e:
        return f"Error: {e}"

if st.button("Calculate Matrix Operation"):
    result = matrix_operations(matrix_1, matrix_2, operation)
    st.write(f"✅ Result of Matrix {operation}:")
    st.write(result)

# ----------------------------------
# Derivatives & Integrals Section
# ----------------------------------
st.subheader("🧠 Derivatives & Integrals")

expression_input = st.text_input("Enter expression (e.g., x**2 + y**2):", "x**2 + y**2")
variables_input = st.text_input("Enter variables separated by commas (e.g., x,y):", "x,y")

operation_type = st.selectbox("Choose operation", ["Derivative", "Indefinite Integral", "Definite Integral"])

variables = symbols(variables_input)
expr = sympify(expression_input)

if operation_type == "Derivative":
    var_to_diff = st.selectbox("Differentiate with respect to:", variables)
    if st.button("Calculate Derivative"):
        derivative_result = diff(expr, var_to_diff)
        st.latex(f"\\frac{{d}}{{d{var_to_diff}}}({expression_input}) = {derivative_result}")

elif operation_type == "Indefinite Integral":
    var_to_integrate = st.selectbox("Integrate with respect to:", variables)
    if st.button("Calculate Indefinite Integral"):
        integral_result = integrate(expr, var_to_integrate)
        st.latex(f"\\int {expression_input} \\, d{var_to_integrate} = {integral_result} + C")

elif operation_type == "Definite Integral":
    var_to_integrate = st.selectbox("Integrate from a to b with respect to:", variables)
    lower_limit = st.number_input(f"Lower limit for {var_to_integrate}:", value=0.0)
    upper_limit = st.number_input(f"Upper limit for {var_to_integrate}:", value=1.0)
    if st.button("Calculate Definite Integral"):
        definite_result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
        st.latex(f"\\int_{{{lower_limit}}}^{{{upper_limit}}} {expression_input} \\, d{var_to_integrate} = {definite_result}")

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("<div class='footer'>🔧 Created with ❤️ by Usama Sharif</div>", unsafe_allow_html=True)
