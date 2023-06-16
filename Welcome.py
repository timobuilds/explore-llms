import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="👾",
)
st.write("# Exploring LLMs 🔮")
st.markdown(
    """
   This is a collection of silly AI apps built with Streamlit. 

   
    ### Demo applications:
     **👈 Select these demos from the sidebar** to see some examples
    of what LLMs can do!
    - **Search a PDF**:
    - **LinkBlink**: Upload a URL and summarize the content on the website. 
    - **Speak to Multiple PDFs**: Upload multiple PDFs and ask them questions. 
    - **SciFi StoryTime**: Upload an image, get a story. 
    - **AutoRnD**: An agent that automates the collection and generation of research ideas. 
    - **Presentation Generator**: Build an agent that uses sequential chains of prompts to. 
 
    
    ### Tools used:

    - Streamlit [documentation](https://docs.streamlit.io)
    - OpenAI API [documentation](https://platform.openai.com/docs/introduction)
    - Langchain [documentation](https://python.langchain.com/en/latest/)
    - Llama Index [documentation](https://gpt-index.readthedocs.io/en/latest/)
    - HuggingFace Transformers[https://huggingface.co/docs/transformers/installation]
    - FAISS [documentation][https://github.com/facebookresearch/faiss]

"""
)