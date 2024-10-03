import os
import streamlit as st
from streamlit_option_menu import option_menu

from gemini_utility import (load_gemini_pro_model, gemini_pro_response)

# set the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))
print(working_dir)

# Creating the User Interface
# Set Page Configurations
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered",
)

# Create a SideBar
with st.sidebar:
    selected = option_menu('Gemini AI',
                           ['ChatBot',
                            'Image Captioning',
                            'Embed text',
                            'Ask me anything'],
                           menu_icon='robot', icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0
                           )


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if selected == "Ask me anything":

    st.title("❓ Ask me a question")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Ask me anything...")

    if st.button("Get Response"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)

# RESEARCH ON
# STREAMLIT TECHNOLOGY(USER INTERFACE FOR AI APPLICATIONS)
# FINE TUNING: Modifying a Pre-Trained Large Language Model for a Particular Domain
# E,g Esheria, Marketting, Education, Healthcare, Climate...
# DEEP LEARNING(ARTIFICIAL NEURAL NETWORK)