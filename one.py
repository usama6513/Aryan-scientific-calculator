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
import streamlit as st
import numpy as np

st.title("Matrix Input App (Flexible Size)")

# Matrix size selection
st.sidebar.header("Matrix Size Selector")
rows = st.sidebar.selectbox("Select number of rows", [2, 3, 4])
cols = st.sidebar.selectbox("Select number of columns", [2, 3, 4])

st.subheader(f"Enter values for Matrix 1 ({rows}x{cols})")
matrix_1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = st.number_input(f"Matrix 1 [{i+1}][{j+1}]", key=f"m1_{i}_{j}", format="%.2f")
        row.append(val)
    matrix_1.append(row)
matrix_1 = np.array(matrix_1)
st.write("Matrix 1:")
st.write(matrix_1)

st.subheader(f"Enter values for Matrix 2 ({rows}x{cols})")
matrix_2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = st.number_input(f"Matrix 2 [{i+1}][{j+1}]", key=f"m2_{i}_{j}", format="%.2f")
        row.append(val)
    matrix_2.append(row)
matrix_2 = np.array(matrix_2)
st.write("Matrix 2:")
st.write(matrix_2)

# Optional: Add operations
st.subheader("Matrix Operations")
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply Element-wise"])

if st.button("Calculate"):
    if operation == "Add":
        result = matrix_1 + matrix_2
    elif operation == "Subtract":
        result = matrix_1 - matrix_2
    elif operation == "Multiply Element-wise":
        result = matrix_1 * matrix_2
    else:
        result = "Invalid operation"
    
    st.success(f"Result of {operation}:")
    st.write(result)

   
          
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
