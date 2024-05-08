# Summarization and Translation of Text

This Streamlit app provides options to summarize and translate text.

## Setup

1. Install the required dependencies:
    ```sh
    pip install streamlit googletrans==4.0.0-rc1 nltk
    ```
   
2. Run the app:
    ```sh
    streamlit run app.py
    ```

## Features

### Summarize only
- Select this option to summarize the text without translation.
- Click the "Summarize" button to generate the summary.

### Translate only
- Select this option to translate the text without summarization.
- Choose the target language from the dropdown.
- Click the "Translate" button to translate the text.

### Summarize and translate
- Select this option to summarize and translate the text.
- Choose the target language from the dropdown.
- Click the "Summarize and Translate" button to generate the summary and translate it.

## How to use
1. Choose an option from the dropdown menu: "Summarize only", "Translate only", or "Summarize and translate".
2. Enter the text you want to process in the text area provided.
3. Click the corresponding button to perform the selected action.

## Built with
- [Streamlit](https://streamlit.io/)
- [Googletrans](https://pypi.org/project/googletrans/)
- [NLTK](https://www.nltk.org/)


