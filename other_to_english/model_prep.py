from translate import Translator
from summa.summarizer import summarize

def kannada_to_english(text):
    translator = Translator(to_lang="en", from_lang="kn")
    translation = translator.translate(text)
    return translation

def hindi_to_english(text):
    translator = Translator(to_lang="en", from_lang="hi")
    translation = translator.translate(text)
    return translation

def summarizer(text):
    summary = summarize(text, ratio=0.3)  # Adjust the ratio as needed
    return summary
