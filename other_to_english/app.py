import streamlit as st
from model_prep import kannada_to_english, hindi_to_english, summarizer

def main():
    st.title("Translation and Summarization App")

    # Sidebar
    st.sidebar.header("Translation Options")
    translation_option = st.sidebar.selectbox(
        "Select Translation Option",
        ("Kannada to English", "Hindi to English")
    )

    # Input text area
    text = st.text_area("Enter Text", "")

    # Translate and summarize
    if st.button("Translate and Summarize"):
        if translation_option == "Kannada to English":
            translated_text = kannada_to_english(text)
        elif translation_option == "Hindi to English":
            translated_text = hindi_to_english(text)
        
        summary = summarizer(translated_text)

        # Display translated text and summary
        st.subheader("Translated Text:")
        st.write(translated_text)

        st.subheader("Summary:")
        st.write(summary)

if __name__ == "__main__":
    main()
