import streamlit as st
from sympy import sympify, pi, N, sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc, diff, symbols, integrate, factor, Matrix

import math

# Set page config
st.set_page_config(page_title="Advanced Calculator", page_icon="📐", layout="wide")
st.title("🧠 Advanced Calculator ")

# Add Custom Styles for a Stylish UI
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            color: #4CAF50;
        }
        .stRadio>label {
            font-size: 20px;
            font-weight: bold;
        }
        .stTextInput>label {
            font-size: 20px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            font-weight: bold;
        }
        .stTextArea>label {
            font-size: 20px;
        }
        .answer_button {
            background-color: #008CBA;
            color: white;
            padding: 10px 15px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Angle Unit Selection (Radians / Degrees)
unit = st.radio("Select angle unit", ["Radians", "Degrees"], horizontal=True)

# Input Type Selection (Decimal / π-form)
mode = st.radio("Input mode", ["Decimal", "π-form"], horizontal=True)

# Handle input (Decimal or π-form)
if mode == "Decimal":
    angle = st.number_input("Enter angle", value=0.0, format="%.4f")
    if unit == "Degrees":
        angle_rad = math.radians(angle)
    else:
        angle_rad = angle
    angle_sym = angle_rad  # for compatibility

else:
    expr = st.text_input("Enter angle in π-form (e.g. pi/3, 3*pi/4)", value="pi/2")
    try:
        angle_sym = sympify(expr)
        if unit == "Degrees":
            angle_sym = N(angle_sym * 180 / pi)  # convert to degrees
            angle_rad = math.radians(angle_sym)
        else:
            angle_rad = N(angle_sym)
    except Exception as e:
        st.error(f"Invalid input: {e}")
        st.stop()

# Trigonometric Calculations
st.subheader("📊 Trigonometric Values")
try:
    st.write(f"✅ Angle in radians (decimal): `{angle_rad:.4f}`")

    st.markdown(f"""
    | Function        | Value              |
    |-----------------|--------------------|
    | sin(θ)          | {round(math.sin(angle_rad), 6)} |
    | cos(θ)          | {round(math.cos(angle_rad), 6)} |
    | tan(θ)          | {round(math.tan(angle_rad), 6)} |
    | cot(θ)          | {round(1/math.tan(angle_rad), 6) if math.tan(angle_rad) != 0 else "∞"} |
    | sec(θ)          | {round(1/math.cos(angle_rad), 6) if math.cos(angle_rad) != 0 else "∞"} |
    | csc(θ)          | {round(1/math.sin(angle_rad), 6) if math.sin(angle_rad) != 0 else "∞"} |
    | arcsin(θ)       | {round(N(asin(angle_rad)), 6) if -1 <= angle_rad <= 1 else "Undefined"} |
    | arccos(θ)       | {round(N(acos(angle_rad)), 6) if -1 <= angle_rad <= 1 else "Undefined"} |
    | arctan(θ)       | {round(N(atan(angle_rad)), 6)} |
    | arccot(θ)       | {round(N(acot(angle_rad)), 6)} |
    | arcsec(θ)       | {round(N(asec(angle_rad)), 6) if abs(angle_rad) >= 1 else "Undefined"} |
    | arccsc(θ)       | {round(N(acsc(angle_rad)), 6) if abs(angle_rad) >= 1 else "Undefined"} |
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Math error: {e}")

# Derivative Section
st.subheader("🔢 Derivative Calculator")
x = symbols('x')  # x is the variable for derivatives
func_input = st.text_input("Enter a function to differentiate (e.g. x**2, sin(x), cos(x))", value="x**2")

if func_input:
    try:
        func_expr = sympify(func_input)  # Convert to sympy expression
        derivative = diff(func_expr, x)  # Take the derivative
        st.write(f"Function: {func_expr}")
        st.write(f"Derivative: {derivative}")
        
        # If the user asks for the evaluated value at the angle, evaluate the derivative
        if angle_sym:
            derivative_value = derivative.evalf(subs={x: angle_rad})
            st.write(f"Derivative at angle ({angle_rad:.4f}): {derivative_value:.4f}")
        
    except Exception as e:
        st.error(f"Invalid function for derivative: {e}")

# Factorization Section
st.subheader("🔠 Factorization of Polynomials")

polynomial_input = st.text_input("Enter polynomial (e.g. x**2 - 4, x**2 + 5*x + 6)", value="x**2 - 4")

if polynomial_input:
    try:
        poly_expr = sympify(polynomial_input)
        factorized = factor(poly_expr)
        st.write(f"Polynomial: {poly_expr}")
        st.write(f"Factorized Form: {factorized}")
    except Exception as e:
        st.error(f"Invalid polynomial input: {e}")

# Matrix Operations
st.subheader("🧮 Matrix Operations")
matrix_input = st.text_area("Enter Matrix (comma-separated rows, e.g. [[1, 2], [3, 4]])", value="[[1, 2], [3, 4]]")

if matrix_input:
    try:
        matrix_expr = sympify(matrix_input)
        matrix_obj = Matrix(matrix_expr)

        determinant = matrix_obj.det()
        inverse = matrix_obj.inv() if matrix_obj.det() != 0 else "Inverse not possible"
        
        st.write(f"Matrix: {matrix_obj}")
        st.write(f"Determinant: {determinant}")
        st.write(f"Inverse: {inverse}")
        
    except Exception as e:
        st.error(f"Invalid matrix input: {e}")

# Integral Section
st.subheader("🔗 Integral Calculator")
integral_input = st.text_input("Enter function to integrate (e.g. x**2, sin(x))", value="x**2")
lower_limit = st.number_input("Enter lower limit for definite integral", value=0.0)
upper_limit = st.number_input("Enter upper limit for definite integral", value=1.0)

if integral_input:
    try:
        func_expr = sympify(integral_input)  # Convert to sympy expression
        indefinite_integral = integrate(func_expr, x)  # Calculate indefinite integral
        
        # Calculate definite integral
        definite_integral = integrate(func_expr, (x, lower_limit, upper_limit))
        
        # Display the results
        st.write(f"Function: {func_expr}")
        st.write(f"Indefinite Integral: {indefinite_integral}")
        
        st.write(f"Definite Integral from {lower_limit} to {upper_limit}: {definite_integral}")
        
        # Add Answer Buttons
        st.markdown(f"<button class='answer_button'>{definite_integral}</button>", unsafe_allow_html=True)
        st.markdown(f"<button class='answer_button'>{indefinite_integral}</button>", unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Invalid function for integral: {e}")
