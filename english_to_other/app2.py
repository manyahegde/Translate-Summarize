import streamlit as st
from model import english_to_kannada, english_to_hindi

from summa.summarizer import summarize  # Importing the summarize function directly

def main():
    st.title("Translation and Summarization App")

    # Sidebar
    st.sidebar.header("Translation Options")
    translation_option = st.sidebar.selectbox(
        "Select Translation Option",
        ("English to Kannada", "English to Hindi")
    )

    # Input text area
    text = st.text_area("Enter Text", "")

    # Translate and summarize
    if st.button("Translate and Summarize"):
        if translation_option == "English to Kannada":
            translated_text = english_to_kannada(text)
        elif translation_option == "English to Hindi":
            translated_text = english_to_hindi(text)
        
        if translated_text:
            summary = summarize(translated_text, ratio=0.3)
            
            # Display translated text and summary
            st.subheader("Translated Text:")
            st.write(translated_text)

            st.subheader("Summary:")
            st.write(summary)
        else:
            st.write("Translation failed. Please try again.")

if __name__ == "__main__":
    main()
