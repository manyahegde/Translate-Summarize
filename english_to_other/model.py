from translate import Translator

def english_to_hindi(text):
    try:
        translator = Translator(to_lang="hi", from_lang="en")
        chunk_size = 1000
        translated_chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size]
            translated_chunk = translator.translate(chunk)
            translated_chunks.append(translated_chunk)
        return " ".join(translated_chunks)
    except Exception as e:
        print("Translation to Hindi failed:", e)
        return None

def english_to_kannada(text):
    try:
        translator = Translator(to_lang="kn", from_lang="en")
        chunk_size = 1000
        translated_chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size]
            translated_chunk = translator.translate(chunk)
            translated_chunks.append(translated_chunk)
        return " ".join(translated_chunks)
    except Exception as e:
        print("Translation to Kannada failed:", e)
        return None
