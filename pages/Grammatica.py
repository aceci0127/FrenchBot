import streamlit as st
from beckend import perform_response_grammatica

# Set the page configuration
st.set_page_config(page_title="Chat with FrenchBot ", page_icon="🇫🇷")

# Title for the Streamlit app
st.title("FrenchBot - Grammatica🇫🇷")

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# User input
if prompt := st.chat_input("Ask frenchbot anything..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Append user message to conversation
    st.session_state.conversation.append({"role": "user", "content": prompt})

    # Generate response
    response = perform_response_grammatica(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    # Append assistant response to conversation
    st.session_state.conversation.append({"role": "assistant", "content": response})