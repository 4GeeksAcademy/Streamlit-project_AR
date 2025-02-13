# Import libraries
import streamlit as st 
import random

# The prediction is based on a random 0 or 1
result = random.randint(0, 1)

if result == 0:
    st.title("You are not hired! You suck!")
else:
    st.title("You are hired! My, my, Mr. Gates!")
    # Create a form to request the email
    with st.form("my_form"):
        st.write("Please enter your email")
        text= st.text_input("Email")

        submitted = st.form_submit_button("Submit")
        if submitted:
            # Write the email
            st.write(text)