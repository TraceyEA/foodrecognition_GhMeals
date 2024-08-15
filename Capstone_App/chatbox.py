

import streamlit as st
import openai

# # Set the OpenAI API key securely
api_key = " " #can't type my API key here for secuirity reasons
client = openai.OpenAI(api_key=api_key)

# Function to interact with OpenAI GPT
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def app():
    st.title("Interactive Chatbox")
    st.write("Please ask any pending questions")

    # Input box for user
    user_input = st.text_area("You:", "")

    if st.button("Ask"):
        if user_input:
            # Generate response using OpenAI
            response = ask_gpt(user_input)
            st.text_area("Chatbot:", value=response, height=200, readonly=True)

# Run the app
if __name__ == '__main__':
    app()
