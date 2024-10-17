import streamlit as st

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyBDxUlnYEBlNVobE8h-7ctodpWfFUnja3A",
    "authDomain": "validation-4f73d.firebaseapp.com",
    "projectId": "validation-4f73d",
    "storageBucket": "validation-4f73d.appspot.com",
    "messagingSenderId": "28069701249",
    "appId": "1:28069701249:web:777360b088dd3764e60f80",
    "measurementId": "G-CJGTJTBTSB",
}

# HTML and JavaScript for Firebase Authentication
html_code = f"""
<script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js"></script>
<script>
  const firebaseConfig = {firebase_config};
  firebase.initializeApp(firebaseConfig);
  
  function signUp(email, password) {{
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {{
        const user = userCredential.user;
        window.alert("Successfully signed up: " + user.email);
      }})
      .catch((error) => {{
        const errorMessage = error.message;
        window.alert("Sign Up failed: " + errorMessage);
      }});
  }}

  function signIn(email, password) {{
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((userCredential) => {{
        const user = userCredential.user;
        window.alert("Welcome " + user.email + "!");
      }})
      .catch((error) => {{
        const errorMessage = error.message;
        window.alert("Sign In failed: " + errorMessage);
      }});
  }}
</script>
"""

# Streamlit app layout
st.title("Firebase Authentication Example")
st.components.v1.html(html_code, height=0)

# User inputs
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Sign Up button
if st.button("Sign Up"):
    if email and password:
        st.components.v1.html(f'<script>signUp("{email}", "{password}");</script>', height=0)
    else:
        st.warning("Please enter both email and password.")

# Sign In button
if st.button("Sign In"):
    if email and password:
        st.components.v1.html(f'<script>signIn("{email}", "{password}");</script>', height=0)
    else:
        st.warning("Please enter both email and password.")
