import streamlit as st
from transformers import pipeline

chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

# # Load the chatbot model
# # chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")


# # Define the Streamlit app
# def main():
#     st.title("Chatbot Demo")
#     st.write("Welcome to the chatbot demo! Type your message below.")

#     # User input text box
#     user_input = st.chat_input("You:")
#     if user_input:
#         st.write(f"User has sent the following prompt: {user_input}")

#     # if st.button("Send"):
#     #     if user_input.strip() != "":
#     #         try:
#     #             # Create a conversation object
#     #             conversation = Conversation(user_input)
#     #             # Get chatbot response
#     #             bot_response = chatbot(conversation)
#     #             response_text = bot_response.generated_responses[0]
#     #             st.text_area("Chatbot:", value=response_text, height=200)
#     #         except Exception as e:
#     #             st.error(f"An error occurred: {e}")

# # Run the app
# if __name__ == "__main__":
#     main()
