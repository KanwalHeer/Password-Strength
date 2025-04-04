import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

# Title
st.title("🔐 Password Strength Meter")
st.write("""
Check how strong your password is and get suggestions to improve it.
""")

# Password input
password = st.text_input("Enter your password:", type="password")

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Common password check
    common_passwords = ["password", "123456", "qwerty", "letmein", "welcome"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a very common password that's easy to guess.")
    
    return score, feedback

def generate_strong_password():
    import random
    import string
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    
    # Ensure we have at least one of each character type
    strong_pass = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest randomly
    for _ in range(8):  # Total length will be 12 characters
        strong_pass.append(random.choice(lowercase + uppercase + digits + special))
    
    random.shuffle(strong_pass)
    return ''.join(strong_pass)

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        # Display strength meter
        st.subheader("Password Strength")
        
        if score == 0:
            st.error("Very Weak")
            st.progress(0)
        elif score == 1:
            st.error("Weak")
            st.progress(25)
        elif score == 2:
            st.warning("Fair")
            st.progress(50)
        elif score == 3:
            st.warning("Moderate")
            st.progress(75)
        elif score == 4:
            st.success("Strong!")
            st.progress(100)
        
        # Display feedback
        if feedback:
            st.subheader("Suggestions:")
            for item in feedback:
                st.write(item)
        
        # Common password warning
        common_passwords = ["password", "123456", "qwerty", "letmein", "welcome"]
        if password.lower() in common_passwords:
            st.error("Warning: This password is in the list of most common passwords!")
    else:
        st.warning("Please enter a password to check")

# Password generator section
st.header("🔧 Need a strong password?")
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.code(strong_password)
    st.success("Here's a strong password for you! Copy it to a safe place.")

# Signature at the Bottom
st.write("\n")
st.write("Created with ❤️ by **Kanwal Heer**.")