import streamlit as st

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "ias19_user": {"password": "ias19123", "role": "IAS19"},
    "risk_user": {"password": "risk123", "role": "Risk"},
    "esg_user": {"password": "esg123", "role": "ESG"},
    "reserving_user": {"password": "res123", "role": "Reserving"},
}

st.set_page_config(page_title="Login")

# 🔎 Debug: show session state
st.write("Authenticated:", st.session_state.get("authenticated"))
st.write("Role:", st.session_state.get("role"))

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username in users and users[username]["password"] == password:
        st.session_state.authenticated = True
        st.session_state.role = users[username]["role"]
        st.rerun()
    else:
        st.error("Invalid credentials")

