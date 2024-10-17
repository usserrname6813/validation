import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, db

# Initialize Firebase
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")  # Use your actual service account key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://validation-39585-default-rtdb.firebaseio.com/'
})

# Streamlit app layout
st.title("Firebase Authentication Example")

# Sign Up Functionality
def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.success(f'Successfully signed up: {user["email"]}')
    except Exception as e:
        st.error(f'Sign Up failed: {str(e)}')

# Sign Up Form
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    if email and password:
        sign_up(email, password)
    else:
        st.warning("Please enter both email and password.")
