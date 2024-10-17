import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase only if it hasn't been initialized yet
if not firebase_admin._apps:
    cred = credentials.Certificate("validation-39585-firebase-adminsdk-70ppy-e489e5b197.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://validation-39585-default-rtdb.firebaseio.com/'
    })

# Streamlit app layout
st.title("Firebase Authentication Example")

# Function to sign up a user
def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.success(f'Successfully signed up: {user["email"]}')
    except Exception as e:
        st.error(f'Sign Up failed: {str(e)}')

# Function to sign in a user
def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.success(f'Welcome {user["email"]}!')
    except Exception as e:
        st.error(f'Sign In failed: {str(e)}')

# User inputs
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Sign Up button
if st.button("Sign Up"):
    if email and password:
        sign_up(email, password)
    else:
        st.warning("Please enter both email and password.")

# Sign In button
if st.button("Sign In"):
    if email and password:
        sign_in(email, password)
    else:
        st.warning("Please enter both email and password.")
