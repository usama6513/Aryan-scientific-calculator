 # Scientific Calculator


#✅ Features Included

#- Trigonometric Functions: sin, cos, tan
#- Inverse Trigonometric Functions: arcsin, arccos, arctan
#- Shift Button: Toggle between trigonometric and inverse functions
#- Matrix Operations: Addition and Multiplication
#- Derivatives: Compute derivatives with respect to any variable
#- Integrals:
 # - Indefinite Integrals
 # - Definite Integrals
#- Multiple Variables Support: Handle expressions with multiple variables
#- Custom CSS:
 ## - Roboto Font
  #- Hover Effects on Buttons
#- HTML Unsafe Allowed: To enable custom styling

#---

#📁 Project Structure




#plaintext
#scientific_calculator/
#├── app.py
#└── assets/
#    └── style.css





#---

#🧮 app.py – Main Application Code




#```python
import streamlit as st
import numpy as np
import math
from sympy import symbols, diff, integrate, sympify

st

# Custom CSS for enhanced UI (UI ko behtr bnane k lie custom styling)
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px; 
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        color: #00c9ff;
        border-radius: 10px;
        margin: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Page configuration
st.set_page_config(page_title="Scientific Calculator", layout="centered")

#Functions
def radian_to_degree(radian):
    return radian * (180 / math.pi)
def degree_to_radian(degree):
    return degree * (math.pi / 180)

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

#Title
st.title("🧮 Scientific Calculator")

#Trigonometric Functions
st.subheader("Trigonometric Functions")
shift = st.checkbox("Shift (Inverse Functions)")
angle_input = st.number_input("Enter angle in degrees:", value=0.0)

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

#Matrix Operations
st.subheader("Matrix Operations")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

st.write("Matrix 1:")
st.write(matrix_1)
st.write("Matrix 2:")
st.write(matrix_2)

operation = st.selectbox("Select matrix operation", ["Add", "Multiply"])

if st.button("Perform Matrix Operation"):
    result = matrix_operations(matrix_1, matrix_2, operation)
    st.write(f"✅ Result of Matrix {operation}:")
    st.write(result)

#Derivatives and Integrals
st.subheader("Derivatives and Integrals")
expression_input = st.text_input("Enter a mathematical expression (e.g., x*2 + y*2):", "x*2 + y*2")
variables_input = st.text_input("Enter variables separated by commas (e.g., x,y):", "x,y")
operation_type = st.selectbox("Choose operation", ["Derivative", "Indefinite Integral", "Definite Integral"])

variables = symbols(variables_input)
expr = sympify(expression_input)

if operation_type == "Derivative":
    var_to_diff = st.selectbox("Select variable to differentiate with respect to:", variables)
    derivative_result = diff(expr, var_to_diff)
    st.write(f"✅ Derivative of {expression_input} with respect to {var_to_diff}:")
    st.latex(f"\%s/%sd{{d{var_to_diff}}}({expression_input}) = {derivative_result}")
elif operation_type == "Indefinite Integral":
    var_to_integrate = st.selectbox("Select variable to integrate with respect to:", variables)
    integral_result = integrate(expr, var_to_integrate)
    st.write(f"✅ Indefinite Integral of {expression_input} with respect to {var_to_integrate}:")
    st.latex(f"\∫expression_input \\, d{var_to_integrate} = {integral_result} + C")
elif operation_type == "Definite Integral":
    var_to_integrate = st.selectbox("Select variable to integrate with respect to:", variables)
    lower_limit = st.number_input(f"Enter lower limit for {var_to_integrate}:", value=0.0)
    upper_limit = st.number_input(f"Enter upper limit for {var_to_integrate}:", value=1.0)
    integral_result = integrate(expr, (var_to_integrate, lower_limit, upper_limit))
    st.write(f"✅ Definite Integral of {expression_input} with respect to {var_to_integrate} from {lower_limit} to {upper_limit}:")
    st.latex(f"\\int_{{{lower_limit}}}^{{{upper_limit}}} ({expression_input}) \\, d{var_to_integrate} = {integral_result}")

    # Footer (footer message)
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif </div>", unsafe_allow_html=True)













    
