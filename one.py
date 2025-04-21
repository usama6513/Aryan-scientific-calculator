import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify, factor, pi, sin, cos, tan, simplify
from sympy.core.sympify import SympifyError

# Page Config
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# Inject Custom CSS
st.markdown("""
<style>
/* Your existing CSS stays same */
body {
    background-color: #f0f8ff;
    font-family: 'Roboto', sans-serif;
    color: #333333;
}
h1, h2 {
    color: #2e86de;
    text-align: center;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 6px;
    padding: 10px 18px;
    transition: 0.3s ease;
    margin-top: 10px;
}
.stButton>button:hover {
    background-color: #2e7d32;
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
.footer {
    margin-top: 50px;
    color: #888;
    text-align: center;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# Custom trig functions
def cot(x): return 1 / math.tan(x)
def sec(x): return 1 / math.cos(x)
def cosec(x): return 1 / math.sin(x)
def arccot(x): return math.atan(1/x)
def arcsec(x): return math.acos(1/x)
def arccosec(x): return math.asin(1/x)

# Title
st.title("🧮 Scientific Calculator")

# ---------------- Trigonometric Functions ----------------
st.subheader("📐 Trigonometric Functions")
shift = st.checkbox("Shift (Inverse Functions)")
angle_input = st.number_input("Enter angle in degrees:", value=0.0)
angle_rad = math.radians(angle_input)
if st.button("💾 Compute Trigonometric Values"):
    try:

       if shift:
           st.write(f"arcsin(sin({angle_input}°)) = {math.degrees(math.asin(math.sin(angle_rad))):.4f}°")
           st.write(f"arccos(cos({angle_input}°)) = {math.degrees(math.acos(math.cos(angle_rad))):.4f}°")
           st.write(f"arctan(tan({angle_input}°)) = {math.degrees(math.atan(math.tan(angle_rad))):.4f}°")
           st.write(f"arccot(cot({angle_input}°)) = {math.degrees(arccot(cot(angle_rad))):.4f}°")
           st.write(f"arcsec(sec({angle_input}°)) = {math.degrees(arcsec(sec(angle_rad))):.4f}°")
           st.write(f"arccosec(cosec({angle_input}°)) = {math.degrees(arccosec(cosec(angle_rad))):.4f}°")
       else:
           st.write(f"sin({angle_input}°) = {math.sin(angle_rad):.4f}")
           st.write(f"cos({angle_input}°) = {math.cos(angle_rad):.4f}")
           st.write(f"tan({angle_input}°) = {math.tan(angle_rad):.4f}")
           st.write(f"cot({angle_input}°) = {cot(angle_rad):.4f}")
           st.write(f"sec({angle_input}°) = {sec(angle_rad):.4f}")
           st.write(f"cosec({angle_input}°) = {cosec(angle_rad):.4f}")
    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- Matrix Operations ----------------
st.subheader("🔢 Matrix Operations")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix 1:")
st.write(matrix_1)
st.write("Matrix 2:")
st.write(matrix_2)

operation = st.selectbox("Select matrix operation", ["Add", "Sub", "Divide", "Multiply", "Determinent", "Inverse"])

if st.button("💾 Perform Matrix Operation"):
    try:
        if operation == "Add":
            result = np.add(matrix_1, matrix_2)
        elif operation == "Sub":
            result = np.subtract(matrix_1, matrix_2)
        elif operation == "Multiply":
            result = np.dot(matrix_1, matrix_2)
        elif operation == "Divide":
            result = np.divide(matrix_1, matrix_2)
        elif operation == "Determinent":
            result = np.linalg.det(matrix_1)
        elif operation == "Inverse":
            result = np.linalg.inv(matrix_1)
        else:
            result = "Invalid operation"
        st.success("✅ Matrix Result:")
        st.write(result)
    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- Derivatives, Integrals, Factorization ----------------
st.subheader("🧠 Calculus & Algebra")

expression_input = st.text_input("Enter expression (e.g., sin(x), x^2 + 2*x + 1):", "x^2 + 2*x + 1")
variables_input = st.text_input("Enter variable(s) (e.g., x, y, theta):", "x")
operation_type = st.selectbox("Choose operation", ["Derivative", "Indefinite Integral", "Definite Integral", "Factor"])

try:
    variables = symbols(variables_input)
    expr = sympify(expression_input)

    if operation_type == "Derivative":
        var_to_diff = st.selectbox("Differentiate with respect to:", variables)
        if st.button("🦾 Calculate Derivative"):
            result = diff(expr, var_to_diff)
            st.success("✅ Derivative:")
            st.latex(f"\\frac{{d}}{{d{var_to_diff}}}({expression_input}) = {result}")

    elif operation_type == "Indefinite Integral":
        var_to_integrate = st.selectbox("Integrate with respect to:", variables)
        if st.button("💻 Calculate Indefinite Integral"):
            result = integrate(expr, var_to_integrate)
            st.success("✅ Indefinite Integral:")
            st.latex(f"\\int {expression_input} \\, d{var_to_integrate} = {result} + C")

    elif operation_type == "Definite Integral":
        var_to_integrate = st.selectbox("Variable for definite integral:", variables)
        lower_limit_raw = st.text_input(f"Lower limit for {var_to_integrate} (e.g., 0, pi):", "0")
        upper_limit_raw = st.text_input(f"Upper limit for {var_to_integrate} (e.g., pi):", "pi")
        if st.button("🤖 Calculate Definite Integral"):
            try:
                lower_limit = sympify(lower_limit_raw)
                upper_limit = sympify(upper_limit_raw)
                result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
                st.success("✅ Definite Integral:")
                st.latex(f"\\int_{{{lower_limit_raw}}}^{{{upper_limit_raw}}} {expression_input} \\, d{var_to_integrate} = {result}")
            except SympifyError:
                st.error("❌ Invalid limits.")

    elif operation_type == "Factor":
        if st.button("🧩 Factor Expression"):
            result = factor(expr)
            st.success("✅ Factorized Expression:")
            st.latex(f"{expression_input} = {result}")

except SympifyError as e:
    st.error(f"Invalid expression: {e}")

# Footer
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif</div>", unsafe_allow_html=True)
