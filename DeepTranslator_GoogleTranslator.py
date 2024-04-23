from deep_translator import GoogleTranslator


def translate_and_validate(word, target_language):
    # Translate from English to the target language
    translated_to_target = GoogleTranslator(source='en', target=target_language).translate(word)
    print(f"Translated to {target_language.upper()}: [ {translated_to_target} ]")

    # Translate back from the target language to English
    translated_to_english = GoogleTranslator(source=target_language, target='en').translate(translated_to_target)
    print(f"Translated back to English:[ {translated_to_english} ]")

    # Validate if the word has changed
    if word.lower() == translated_to_english.lower():
        print("The word has not changed.")
    else:
        print("The word has changed.")


# Main Code here
word_to_translate = "Hello"
translate_and_validate(word_to_translate, 'de')
