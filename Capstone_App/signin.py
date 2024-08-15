import streamlit as st

# Function to check if user data exists (authentication)
def authenticate_user(username, password):
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_password, _, _ = user.strip().split(",")
                if stored_username == username and stored_password == password:
                    return True
    except FileNotFoundError:
        return False
    return False

def main():
    st.title("Sign In Page")
    st.header("Log into your account")

    # Input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Sign-in button
    if st.button("Sign In"):
        if authenticate_user(username, password):
            st.success("Signed in successfully")
            # Redirect to home page
            st.experimental_set_query_params(page="home")
        else:
            st.error("Invalid username or password")

# if __name__ == "__main__":
#     main()
