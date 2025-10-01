import streamlit as st
import untitled5 
users = {
    "risk_user": {"password": "risk123", "role": "Risk"},
    "ias19_user": {"password": "ias19123", "role": "IAS19"},
    "admin": {"password": "admin123", "role": "Admin"}
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.role = username
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")
else:
    untitled5.run_app(st.session_state.role)
