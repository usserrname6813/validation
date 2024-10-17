import streamlit as st
import pyrebase

# Firebase configuration
config = {
    "apiKey": "AIzaSyBDxUlnYEBlNVobE8h-7ctodpWfFUnja3A",
    "authDomain": "validation-4f73d.firebaseapp.com",
    "projectId": "validation-4f73d",
    "storageBucket": "validation-4f73d.appspot.com",
    "messagingSenderId": "28069701249",
    "appId": "1:28069701249:web:777360b088dd3764e60f80",
    "measurementId": "G-CJGTJTBTSB",
}

# Initialize Firebase
try:
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
except Exception as e:
    st.error(f"Failed to initialize Firebase: {e}")

# Streamlit app
st.title("Firebase Auth with Streamlit")

# Function to sign up users
def sign_up():
    st.subheader("Sign Up")
    email = st.text_input("Email", "")
    password = st.text_input("Password", "", type="password")
    
    if st.button("Sign Up"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            # Save user data to Firestore
            user_data = {
                "email": email,
                "created_at": str(st.timestamp()),  # Save the timestamp
            }
            db.child("users").child(user['localId']).set(user_data)
            st.success("Sign up successful! Please log in.")
        except Exception as e:
            st.error(f"Error during sign up: {e}")

# Function to sign in users
def sign_in():
    st.subheader("Sign In")
    email = st.text_input("Email", "")
    password = st.text_input("Password", "", type="password")
    
    if st.button("Sign In"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Sign in successful!")
            # Fetch user data from Firestore
            user_data = db.child("users").child(user['localId']).get().val()
            if user_data:
                st.write("User Data:", user_data)
            else:
                st.write("No user data found.")
        except Exception as e:
            st.error(f"Error during sign in: {e}")

# Main function to toggle between sign-up and sign-in
def main():
    choice = st.sidebar.selectbox("Select Action", ["Sign Up", "Sign In"])
    
    if choice == "Sign Up":
        sign_up()
    else:
        sign_in()

if __name__ == "__main__":
    main()
