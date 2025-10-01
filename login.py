
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Define allowed users and roles
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "ias19_user": {"password": "ias19123", "role": "IAS19"},
    "risk_user": {"password": "risk123", "role": "Risk"},
    "esg_user": {"password": "esg123", "role": "ESG"},
    "reserving_user": {"password": "res123", "role": "Reserving"},
}

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users and users[username]["password"] == password:
        st.session_state.authenticated = True
        st.session_state.role = users[username]["role"]
        st.success(f"Welcome {username}, role: {st.session_state.role}")
        st.switch_page("untitled5")  # go to main app
    else:
        st.error("Invalid credentials")

