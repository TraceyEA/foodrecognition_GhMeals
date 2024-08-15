import streamlit as st
from streamlit_option_menu import option_menu
import home, account, chatbox,food_library,image_capture

# Streamlit app
st.set_page_config(
    page_title="Diabetes Monitoring"
)

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
                options=['Home', 'Account','Camera', 'Food Library', 'Chat box'],
                icons=['house-fill', 'person-circle','camera-fill' ,'basket-fill', 'chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if app == 'Home':
            home.app()
        if app == 'Account':
            account.app()
        if app == 'Chat box':
            chatbox.app()
        if app == 'Food Library':
            food_library.app()
        if app=='Camera':
            image_capture.app()


#instantiate the app
app = MultiApp()
#run the app
app.run()

