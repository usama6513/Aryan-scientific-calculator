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

# Trigonometric Functions st.error(f"⚠️ Invalid input: {e}")
# ---------------- TRIGONOMETRIC FUNCTIONS ----------------
st.subheader("🧮 Trigonometric Functions")

shift = st.checkbox("Shift (Inverse Functions)")
angle_input = st.number_input("Enter angle in degrees:", value=0.0)

if st.button("🧠 Compute Trigonometric Values"):
    angle_rad = math.radians(angle_input)

    if shift:
        try:
       st.markdown(f"""
    <div class='result-box'>
        sin({angle_input}°) = {math.sin(angle_rad):.4f}<br>
        cos({angle_input}°) = {math.cos(angle_rad):.4f}<br>
        tan({angle_input}°) = {math.tan(angle_rad):.4f}
    </div>
""", unsafe_allow_html=True)


        except ValueError:
            st.error("Invalid input for inverse trigonometric functions.")
    else:
        st.markdown(f"""
        <div class='result-box'>
            sin({angle_input}°) = {math.sin(angle_rad):.4f}<br>
            cos({angle_input}°) = {math.cos(angle_rad):.4f}<br>
            tan({angle_input}°) = {math.tan(angle_rad):.4f}
        </div>
        """, unsafe_allow_html=True)


# ---------------- MATRIX OPERATIONS ----------------
st.subheader("🔢 Matrix Operations")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix 1:")
st.write(matrix_1)
st.write("Matrix 2:")
st.write(matrix_2)

operation = st.selectbox("Select matrix operation", ["Add", "Multiply"])

if st.button("📐 Perform Matrix Operation"):
    try:
        result = np.add(matrix_1, matrix_2) if operation == "Add" else np.dot(matrix_1, matrix_2)
        st.success("✅ Matrix Result:")
        st.write(result)
    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- DERIVATIVES AND INTEGRALS ----------------
st.subheader("🧠 Derivatives and Integrals")
expression_input = st.text_input("Enter expression (e.g., sin(x), r*sin(theta))", "3*sin(theta)")
variables_input = st.text_input("Enter variable(s) (e.g., x, y, theta)", "theta")
operation_type = st.selectbox("Choose operation", ["Derivative", "Indefinite Integral", "Definite Integral"])

try:
    variables = symbols(variables_input)
    expr = sympify(expression_input)

    if operation_type == "Derivative":
        var_to_diff = st.selectbox("Differentiate with respect to:", variables)
        if st.button("💻 Calculate Derivative"):
            if var_to_diff in expr.free_symbols:
                derivative_result = diff(expr, var_to_diff)
                st.success("✅ Derivative:")
                st.latex(f"\\frac{{d}}{{d{var_to_diff}}}({expression_input}) = {derivative_result}")
            else:
                st.warning("Variable not found in expression. Derivative = 0.")

    elif operation_type == "Indefinite Integral":
        var_to_integrate = st.selectbox("Integrate with respect to:", variables)
        if st.button("🛰️ Calculate Indefinite Integral"):
            if var_to_integrate in expr.free_symbols:
                integral_result = integrate(expr, var_to_integrate)
                st.success("✅ Indefinite Integral:")
                st.latex(f"\\int {expression_input} \\, d{var_to_integrate} = {integral_result} + C")
            else:
                st.warning("Variable not found in expression. Integral = constant.")

    elif operation_type == "Definite Integral":
        var_to_integrate = st.selectbox("Variable for definite integral:", variables)
        lower_limit_raw = st.text_input(f"Lower limit for {var_to_integrate} (e.g., 0, pi/2):", "0")
        upper_limit_raw = st.text_input(f"Upper limit for {var_to_integrate} (e.g., pi):", "pi")

        if st.button("🤖 Calculate Definite Integral"):
            try:
                lower_limit = sympify(lower_limit_raw)
                upper_limit = sympify(upper_limit_raw)

                if var_to_integrate in expr.free_symbols:
                    definite_result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
                    st.success("✅ Definite Integral:")
                    st.latex(f"\\int_{{{lower_limit_raw}}}^{{{upper_limit_raw}}} {expression_input} \\, d{var_to_integrate} = {definite_result}")
                else:
                    st.warning("Variable not found in expression. Result = 0.")
            except SympifyError:
                st.error("❌ Invalid limit. Use 0, pi, pi/2, etc.")
except SympifyError as e:
    st.error(f"Invalid Expression: {e}")


# Footer
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif</div>", unsafe_allow_html=True)
