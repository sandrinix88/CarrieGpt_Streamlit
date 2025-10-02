import streamlit as st
from model_config import llm, trim_to_sentence, MAX_TOKENS

# Streamlit page setup
st.set_page_config(page_title="CarrieGPT", page_icon="💋")
st.title("CarrieGPT 💄")
st.caption("Ask me anything, darling. Life, love, or Louboutins — I’ve got you.")

# Input box
user_input = st.text_input("Your question:")
submitted = st.button("Submit")

# Response logic
if submitted and user_input:
    if user_input.lower() in ["bye", "exit", "quit"]:
        st.markdown("**Carrie:** Bye honey, talk soon! And remember — heartbreak is just fashion waiting to happen. 💋")
    else:
        prompt = f"User: {user_input}\nCarrie:"
        response = llm.invoke(prompt).strip()
        final_response = trim_to_sentence(response, MAX_TOKENS)
        st.markdown(f"**Carrie:** {final_response}")
        st.caption("Is that all, darling? You can ask me another question… or we can say goodbye and chase sales at Manolo Blahnik. 💋")