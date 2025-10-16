import streamlit as st
from utils import matchassignment
from core import calculator_core

# ==============================================
# 🧮 Streamlit Dynamic Calculator App
# ==============================================

# Configure the Streamlit app's title and icon
st.set_page_config(page_title="Calculator", page_icon="🧮")

# ==============================================
#  Setup Streamlit Page and Calculator Instance
# ==============================================

# We use Streamlit's session_state to ensure the calculator
# persists between reruns of the app (since Streamlit refreshes
# the script on every interaction).
if "calc" not in st.session_state:
    st.session_state.calc = calculator_core()

# Store calculator instance reference
calc = st.session_state.calc


# ==============================================
# 🔹 Input Section
# ==============================================

# Display the app title
st.title("🧮 Dynamic Calculator")

# Provide a text input field for the user to type expressions
expr = st.text_input("Enter expression (e.g. 2+3*5, x=10, sqrt(16))")


# ==============================================
#  Expression Evaluation
# ==============================================

if st.button("Evaluate"):
    try:
        result = calc.evaluate(expr)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(str(e))


# ==============================================
# 🔹 Memory Functionality
# ==============================================

c1, c2, c3, c4 = st.columns(4)

if c1.button("M+"):
    calc.m_plus(float(calc.history[0][1]) if calc.history else 0)

if c2.button("M-"):
    calc.m_minus(float(calc.history[0][1]) if calc.history else 0)

if c3.button("MR"):
    st.info(f"Memory: {calc.mr()}")

if c4.button("MC"):
    calc.mc()


# ==============================================
#  History Section
# ==============================================

st.subheader("History")
for ex, val, ts in calc.history:
    st.write(f"[{ts}] {ex} = {val}")


# ==============================================
#  Variables Section
# ==============================================

st.subheader("Vari")
st.json(calc.vari)
