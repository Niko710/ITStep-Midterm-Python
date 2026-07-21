import json, os
from pathlib import Path


LANGUAGES = ("geo-eng", "eng-geo")


def read_json(filename: str | Path):
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
    

def translate(to_translate: list[str], dictionary: dict, filename: str | Path) -> str:
    # Translation which will be outputed
    translated_words = []

    # Search user inputed words in dictionary
    for i in to_translate:
        t = dictionary.get(i.lower())

        if t:
            translated_words.append(t)
        # if translation was not found, users have choice to add it in dictionary
        else:
            choice = input(f"Word '{i}' was not found in dictionary, if you want to add it enter 'yes': ")
            
            if choice.strip().lower() == "yes":
                word = add_word(i, filename, dictionary)
                translated_words.append(word)
            else:
                translated_words.append(f"'{i.lower()}'")
    
    return " ".join(translated_words)


def add_word(word: str, filename: str | Path, data: dict) -> str:
    translation = input(f"Please, input translation for word '{word}': ").strip().lower()
    data[word.lower()] = translation
    tmp_filename = Path(__file__).parent/"tmp.json"
    
    try:
        with open(tmp_filename, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    # if writing crashes, old dictionary wont be affected
    except Exception:
        print(f"Error while updating dictionary! Program continues working!")
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)
        return translation

    # if no errors caught, replace json with updated tmp json
    os.replace(tmp_filename, filename)
    return translation
    
        

def main():
    # Listing all available options
    for i, o in enumerate(LANGUAGES):
        print(f"{i} - {o}")

    # User inputs choice
    user_language = input("Please, choose translating languages (Enter index): ")

    # Validation of user choice, must be decimal
    if not user_language.isdigit():
        print("Index must be strictly integer type, listed in list above!")
        return

    user_language = int(user_language)
    
    # Validation if language choice is out of range
    if user_language < 0 or user_language >= len(LANGUAGES):
        print("Error! Index is out of range!")
        return
    
    # User inputs word/text, we convert it to list for convenience using split() method
    user_text = input("Please, input the the text or word, which needs to be translated: ").split()

    # Read translate data from json file
    filename = Path(__file__).parent/f"{LANGUAGES[user_language]}.json"

    try:
        language_dictionary = read_json(filename)
    except FileNotFoundError:
        print(f"File {filename} was not found!")
        return

    final_output = translate(user_text, language_dictionary, filename)

    print(final_output)


if __name__ == "__main__":
    main()