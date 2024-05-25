import streamlit as st
from transformers import pipeline

# Load the chatbot model
chatbot = pipeline(model="facebook/blenderbot-400M-distill")

# Define the Streamlit app
def main():
    st.title("Chatbot Demo")
    st.write("Welcome to the chatbot demo! Type your message below.")

    # User input text box
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        # Get chatbot response
        try:
            bot_response = chatbot(user_input)[0]['generated_text']
            st.text_area("Chatbot:", value=bot_response, height=200)
        except Exception as e:
            st.write(e)
# Run the app
if __name__ == "__main__":
    main()
