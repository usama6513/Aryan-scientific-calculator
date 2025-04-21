import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify, factor, pi, sin, cos, tan
from sympy.core.sympify import SympifyError

# --- Page Config ---
st.set_page_config(page_title="Scientific Calculator", layout="centered")

# --- Custom Trigonometric Functions ---
def cot(x): return 1 / math.tan(x)
def sec(x): return 1 / math.cos(x)
def cosec(x): return 1 / math.sin(x)
def arccot(x): return math.atan(1/x)
def arcsec(x): return math.acos(1/x)
def arccosec(x): return math.asin(1/x)

# --- Title ---
st.title("🧮 Scientific Calculator")

# ------------------ Trigonometric Functions ------------------
st.subheader("📐 Trigonometric Functions")
angle = st.number_input("Enter angle (in degrees):", value=0.0)
shift = st.checkbox("Use Inverse Functions")
if st.button("💾 Compute Trigonometric Values"):
    angle_rad = math.radians(angle)
    try:
        if shift:
            st.write(f"arcsin(sin({angle}°)) = {math.degrees(math.asin(math.sin(angle_rad))):.4f}°")
            st.write(f"arccos(cos({angle}°)) = {math.degrees(math.acos(math.cos(angle_rad))):.4f}°")
            st.write(f"arctan(tan({angle}°)) = {math.degrees(math.atan(math.tan(angle_rad))):.4f}°")
            st.write(f"arccot(cot({angle}°)) = {math.degrees(arccot(cot(angle_rad))):.4f}°")
            st.write(f"arcsec(sec({angle}°)) = {math.degrees(arcsec(sec(angle_rad))):.4f}°")
            st.write(f"arccosec(cosec({angle}°)) = {math.degrees(arccosec(cosec(angle_rad))):.4f}°")
        else:
            st.write(f"sin({angle}°) = {math.sin(angle_rad):.4f}")
            st.write(f"cos({angle}°) = {math.cos(angle_rad):.4f}")
            st.write(f"tan({angle}°) = {math.tan(angle_rad):.4f}")
            st.write(f"cot({angle}°) = {cot(angle_rad):.4f}")
            st.write(f"sec({angle}°) = {sec(angle_rad):.4f}")
            st.write(f"cosec({angle}°) = {cosec(angle_rad):.4f}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ------------------ Matrix Operations ------------------
st.subheader("🔢 Matrix Operations")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix A:")
st.write(matrix_1)
st.write("Matrix B:")
st.write(matrix_2)

matrix_op = st.selectbox("Choose matrix operation:", ["Add", "Subtract", "Multiply", "Inverse of A", "Determinant of A"])

if st.button("💾 Compute Matrix Operation"):
    try:
        if matrix_op == "Add":
            result = np.add(matrix_1, matrix_2)
        elif matrix_op == "Subtract":
            result = np.subtract(matrix_1, matrix_2)
        elif matrix_op == "Multiply":
            result = np.dot(matrix_1, matrix_2)
        elif matrix_op == "Inverse of A":
            result = np.linalg.inv(matrix_1)
        elif matrix_op == "Determinant of A":
            result = np.linalg.det(matrix_1)
        else:
            result = "Unknown operation"
        st.success("✅ Result:")
        st.write(result)
    except Exception as e:
        st.error(f"⚠️ Matrix error: {e}")

# ------------------ Calculus & Algebra ------------------
st.subheader("🧠 Calculus & Algebra")

expression = st.text_input("Enter expression (e.g. x^2 + 2*x + 1):", "x^2 + 2*x + 1")
variable_input = st.text_input("Enter variable(s) (comma-separated if more):", "x")
calc_option = st.selectbox("Choose operation:", ["Derivative", "Indefinite Integral", "Definite Integral", "Factor"])

try:
    vars = symbols(variable_input)
    expr = sympify(expression)

    if calc_option == "Derivative":
        var = st.selectbox("Differentiate with respect to:", vars)
        if st.button("🦾 Compute Derivative"):
            result = diff(expr, var)
            st.success("✅ Derivative:")
            st.latex(f"\\frac{{d}}{{d{var}}}({expression}) = {result}")

    elif calc_option == "Indefinite Integral":
        var = st.selectbox("Integrate with respect to:", vars)
        if st.button("💻 Compute Indefinite Integral"):
            result = integrate(expr, var)
            st.success("✅ Indefinite Integral:")
            st.latex(f"\\int {expression} \\, d{var} = {result} + C")

    elif calc_option == "Definite Integral":
        var = st.selectbox("Integrate from lower to upper limit (with respect to):", vars)
        lower = st.text_input("Lower Limit:", "0")
        upper = st.text_input("Upper Limit:", "pi")
        if st.button("🤖 Compute Definite Integral"):
            lower_val = sympify(lower)
            upper_val = sympify(upper)
            result = integrate(expr, (var, lower_val, upper_val))
            st.success("✅ Definite Integral:")
            st.latex(f"\\int_{{{lower}}}^{{{upper}}} {expression} \\, d{var} = {result}")

    elif calc_option == "Factor":
        if st.button("🧩 Factor Expression"):
            result = factor(expr)
            st.success("✅ Factorized Form:")
            st.latex(f"{expression} = {result}")

except SympifyError as e:
    st.error(f"❌ Invalid Expression: {e}")
except Exception as e:
    st.error(f"⚠️ Error: {e}")

# ------------------ Footer ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: grey;'>Created with 💖 by Usama Sharif</div>", unsafe_allow_html=True)
