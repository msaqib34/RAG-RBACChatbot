import streamlit as st
import requests

st.title("RAG RBAC Chatbot")

# 1. Initialize session state for authentication
if "auth" not in st.session_state:
    st.session_state["auth"] = None
    st.session_state["role"] = None

# 2. LOGIN UI (Only show if not logged in)
if st.session_state["auth"] is None:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.get(
            "http://127.0.0.1:8000/login",
            auth=(username, password)
        )
        
        if response.status_code == 200:
            st.session_state["auth"] = (username, password)
            st.session_state["role"] = response.json()["role"]
            st.rerun()  # Refresh the page to hide login and show chat
        else:
            st.error("Invalid credentials")

# 3. CHAT UI (Only show if logged in)
else:
    st.write(f"Logged in as: **{st.session_state['role']}**")
    
    if st.button("Logout"):
        st.session_state["auth"] = None
        st.rerun()

    message = st.text_input("Ask something:")
    
    if st.button("Send"):
        res = requests.post(
            "http://127.0.0.1:8000/chat",
            params={"message": message},
            auth=st.session_state["auth"]
        )
        
        if res.status_code == 200:
            data = res.json()
            st.write("### Response:")
            st.write(data.get("response"))
            st.write("### Sources:")
            st.write(data.get("sources"))
        else:
            st.error(f"Error: {res.status_code}")
