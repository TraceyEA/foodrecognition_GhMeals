import streamlit as st

#  save user data 
def save_user_data(username, password, email, number):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password},{email},{number}\n")

# check if email is valid 
def is_valid_email(email):
    return "@" in email  

# check if phone number is valid 
def is_valid_number(number):
    return len(number) == 10 and number.isdigit() 

def main():
    st.title("Sign Up Page")
    st.header("New user, Create a new account 🌟")

    # Input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    email = st.text_input("Email")
    number = st.text_input("Phone Number")


    # Sign-up 
    if st.button("Sign Up"):
        if not username or not password or not email or not number:
            st.error("Please fill in all fields")
        elif not is_valid_email(email):
            st.error("Please enter a valid email address")
        elif not is_valid_number(number):
            st.error("Please enter a valid phone number")
        elif password != confirm_password:
            st.error("Passwords do not match")
        else:
            save_user_data(username, password, email, number)
            st.success("Account created successfully")
            # Redirect to sign-in page after a delay (not recommended, see note below)
            st.experimental_set_query_params(page="signin")

    st.write("Already a User, <span style='color: blue;'>Sign In</span> instead.", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
