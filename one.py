import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify

# Load custom CSS
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ Custom CSS not found. Styling may not apply.")

# Page configuration
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# Functions
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

# Title
st.title("🧮 Scientific Calculator")

# --- Trigonometric Functions ---
st.subheader("Trigonometric Functions")
shift = st.checkbox("Shift (Inverse Functions)")
angle_input = st.number_input("Enter angle in degrees:", value=0.0)
if st.button("Get Trigonometric Answer"):
    if shift:
        try:
            sin_val = math.sin(math.radians(angle_input))
            cos_val = math.cos(math.radians(angle_input))
            tan_val = math.tan(math.radians(angle_input))

            st.write(f"arcsin({sin_val:.4f}) = {math.degrees(math.asin(sin_val)):.4f}°")
            st.write(f"arccos({cos_val:.4f}) = {math.degrees(math.acos(cos_val)):.4f}°")
            st.write(f"arctan({tan_val:.4f}) = {math.degrees(math.atan(tan_val)):.4f}°")
        except ValueError:
            st.error("Invalid input for inverse trigonometric functions.")
    else:
        st.write(f"sin({angle_input}°) = {math.sin(math.radians(angle_input)):.4f}")
        st.write(f"cos({angle_input}°) = {math.cos(math.radians(angle_input)):.4f}")
        st.write(f"tan({angle_input}°) = {math.tan(math.radians(angle_input)):.4f}")

# --- Matrix Operations ---
st.subheader("Matrix Operations")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix 1:")
st.write(matrix_1)
st.write("Matrix 2:")
st.write(matrix_2)

operation = st.selectbox("Select matrix operation", ["Add", "Multiply"])
if st.button("Get Matrix Answer"):
    result = matrix_operations(matrix_1, matrix_2, operation)
    st.write(f"✅ Result of Matrix {operation}:")
    st.write(result)

# --- Derivatives and Integrals ---
st.subheader("Derivatives and Integrals")
expression_input = st.text_input("Enter a mathematical expression (e.g., x*2 + y*2):", "x*2 + y*2")
variables_input = st.text_input("Enter variables separated by commas (e.g., x,y):", "x,y")
operation_type = st.selectbox("Choose operation", ["Derivative", "Indefinite Integral", "Definite Integral"])

if st.button("Get Calculus Answer"):
    try:
        variables = symbols(variables_input)
        expr = sympify(expression_input)

        if operation_type == "Derivative":
            var_to_diff = st.selectbox("Select variable to differentiate with respect to:", variables, key="diff_var")
            derivative_result = diff(expr, var_to_diff)
            st.write(f"✅ Derivative of `{expression_input}` with respect to `{var_to_diff}`:")
            st.latex(f"\\frac{{d}}{{d{var_to_diff}}}({expression_input}) = {derivative_result}")

        elif operation_type == "Indefinite Integral":
            var_to_integrate = st.selectbox("Select variable to integrate with respect to:", variables, key="indef_var")
            integral_result = integrate(expr, var_to_integrate)
            st.write(f"✅ Indefinite Integral of `{expression_input}` with respect to `{var_to_integrate}`:")
            st.latex(f"\\int {expression_input} \\, d{var_to_integrate} = {integral_result} + C")

        elif operation_type == "Definite Integral":
            var_to_integrate = st.selectbox("Select variable to integrate with respect to:", variables, key="def_var")
            lower_limit = st.number_input(f"Enter lower limit for {var_to_integrate}:", value=0.0, key="low_lim")
            upper_limit = st.number_input(f"Enter upper limit for {var_to_integrate}:", value=1.0, key="up_lim")
            integral_result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
            st.write(f"✅ Definite Integral from `{lower_limit}` to `{upper_limit}`:")
            st.latex(f"\\int_{{{lower_limit}}}^{{{upper_limit}}} {expression_input} \\, d{var_to_integrate} = {integral_result}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# Footer
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif</div>", unsafe_allow_html=True)
