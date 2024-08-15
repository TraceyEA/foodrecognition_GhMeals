import streamlit as st
from streamlit_option_menu import option_menu
import signup
import signin
import chatbox
import home
# import side_bar

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Menu",
                options=['Sign Up', 'Sign In', 'Home'],
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        for item in self.apps:
            if app == item['title']:
                item['function']()

# Instantiate the app
app = MultiApp()

# Add your pages to the app
app.add_app("Sign Up", signup.main)
app.add_app("Sign In", signin.main)
app.add_app("Home", home.main)

# Run the app
app.run()
