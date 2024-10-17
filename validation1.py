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

# JavaScript code to initialize Firebase and handle authentication
html_code = f"""
<script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js"></script>
<script>
  const firebaseConfig = {firebase_config};
  firebase.initializeApp(firebaseConfig);

  function isValidEmail(email) {{
    const re = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;  // Simple regex for email validation
    return re.test(email);
  }}

  function signUp(firstName, lastName, email, password) {{
    if (!isValidEmail(email)) {{
      alert("Please enter a valid email address.");
      return;
    }}
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {{
        const user = userCredential.user;
        alert("Successfully signed up: " + firstName + " " + lastName);
        window.location.reload();  // Reload the page to update UI
      }})
      .catch((error) => {{
        const errorMessage = error.message;
        if (errorMessage.includes("The email address is badly formatted")) {{
          alert("Invalid email format.");
        }} else if (errorMessage.includes("password")) {{
          alert("Password does not meet the requirements: " + errorMessage);
        }} else {{
          alert("Sign Up failed: " + errorMessage);
        }}
      }});
  }}

  function signIn(email, password) {{
    if (!isValidEmail(email)) {{
      alert("Please enter a valid email address.");
      return;
    }}
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((userCredential) => {{
        const user = userCredential.user;
        alert("Welcome back, " + user.email + "!");
        window.location.reload();  // Reload the page to update UI
      }})
      .catch((error) => {{
        const errorMessage = error.message;
        if (errorMessage.includes("There is no user record corresponding to this identifier.")) {{
          alert("No account found with this email.");
        }} else if (errorMessage.includes("password")) {{
          alert("Password is incorrect or does not meet the requirements: " + errorMessage);
        }} else {{
          alert("Sign In failed: " + errorMessage);
        }}
      }});
  }}
</script>
"""

# Streamlit app layout
st.title("Firebase Authentication Example")
st.components.v1.html(html_code, height=0)

# Main app logic
if 'show_sign_up' not in st.session_state:
    st.session_state.show_sign_up = False
if 'show_sign_in' not in st.session_state:
    st.session_state.show_sign_in = False

# Function to handle the Sign Up process
def handle_sign_up():
    st.session_state.show_sign_up = True
    st.session_state.show_sign_in = False

# Function to handle the Sign In process
def handle_sign_in():
    st.session_state.show_sign_in = True
    st.session_state.show_sign_up = False

# Display buttons for Sign In and Sign Up
if not st.session_state.show_sign_up and not st.session_state.show_sign_in:
    st.button("Sign Up", on_click=handle_sign_up)
    st.button("Sign In", on_click=handle_sign_in)

# Sign Up Form
if st.session_state.show_sign_up:
    st.header("Sign Up")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        if first_name and last_name and email and password:
            st.components.v1.html(f'<script>signUp("{first_name}", "{last_name}", "{email}", "{password}");</script>', height=0)
        else:
            st.warning("Please fill in all fields.")

# Sign In Form
if st.session_state.show_sign_in:
    st.header("Sign In")
    email = st.text_input("Email", key="sign_in_email")
    password = st.text_input("Password", type="password", key="sign_in_password")

    if st.button("Sign In"):
        if email and password:
            st.components.v1.html(f'<script>signIn("{email}", "{password}");</script>', height=0)
        else:
            st.warning("Please enter both email and password.")
