from googletrans import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import streamlit as st
import nltk

def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')

def summarize_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    # Creating a frequency table to keep the score of each word
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
    
    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentence_value = dict()

    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    sum_values = 0
    for sentence in sentence_value:
        sum_values += sentence_value[sentence]

    # Average value of a sentence from the original text
    average = int(sum_values / len(sentence_value))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

# Function to translate text
def translate_text(text, src_language, dest_language):
    if not text:
        return "Please enter some text."
    translator = Translator()
    translation = translator.translate(text, src=src_language, dest=dest_language)
    return translation.text

def main():
    download_nltk_resources()
    st.title("Text Summarization and Translation App")
    user_text = st.text_area("Enter the text you want to process:")

    option = st.selectbox("Choose an option:", ["Translate only", "Summarize only", "Summarize and translate"])

    if option == "Translate only":
        dest_lang = st.selectbox("Select the language you want to translate to:", ["English", "Kannada", "Hindi"])
        if st.button("Translate"):
            dest_lang_code = {"English": "en", "Kannada": "kn", "Hindi": "hi"}
            translated_text = translate_text(user_text, 'en', dest_lang_code[dest_lang])
            st.subheader("Translated Text:")
            st.write(translated_text)
    elif option == "Summarize only":
        if st.button("Summarize"):
            summary = summarize_text(user_text)
            if summary:
                st.subheader("Summarized Text:")
                st.write(summary)
            else:
                st.write("There is not enough text to summarize.")
    elif option == "Summarize and translate":
        dest_lang = st.selectbox("Select the language you want to translate to:", ["Kannada", "Hindi"])
        if st.button("Summarize and Translate"):
            summary = summarize_text(user_text)
            if not summary:
                st.write("There is not enough text to summarize.")
            else:
                dest_lang_code = {"Kannada": "kn", "Hindi": "hi"}
                translated_summary = translate_text(summary, 'en', dest_lang_code[dest_lang])
                st.subheader("Summarized Text:")
                st.write(summary)
                st.subheader("Translated Text:")
                st.write(translated_summary)

if __name__ == "__main__":
    main()
