from handle_vocab_file import vocab, save_vocab, s3_client, filename, bucket_name
from validation import input_formatting


# DEF: adding a word
def add_word(vocab, unit, word, meaning):
    unit = input_formatting(unit)
    word = input_formatting(word)
    new_word = {"word": word, "meaning": meaning}
    if unit not in vocab:
        vocab[unit] = []
    for defin in vocab[unit]:
        if defin["word"] == word:
            print(f"The word '{word}' already exists in {unit}")
            return None
    vocab[unit].append(new_word)
    save_vocab(s3_client, vocab, filename, bucket_name)
    print(f"Added '{word}' to {unit}")


# DEF: deleting a word
def delete_word(vocab, unit, word):
    unit = input_formatting(unit)
    word = input_formatting(word)
    if unit not in vocab:
        print(f"Unit '{unit}' does not exist.")
        return None
    for words in vocab[unit]:
        if word == words["word"]:
            vocab[unit].remove(words)
            save_vocab(s3_client, vocab, filename, bucket_name)
            print(f"{word} deleted from {unit}")
            return
    print(f"{word} not found in {unit}")


# DEF: updating a word
def update_word(vocab, unit, old_word, new_word, new_meaning):
    unit = input_formatting(unit)
    old_word = input_formatting(old_word)
    new_word = input_formatting(new_word)
    if unit not in vocab:
        print(f"Unit '{unit}' does not exist.")
        return None
    for words in vocab[unit]:
        if old_word == words["word"]:
            print(f"Modifying {old_word} in {unit}")
            words["word"] = new_word
            words["meaning"] = new_meaning
            save_vocab(s3_client, vocab, filename, bucket_name)
            return
    print(f"{old_word} not found in {unit}")


# DEF: List words
def list_words(vocab, unit):
    if unit not in vocab:
        print(f"Unit '{unit}' does not exist.")
        return None

    if not vocab[unit]:
        print(f"No words found in {unit}")
        return None

    for words in vocab[unit]:
        word = words["word"]
        meaning = words["meaning"]
        print(f"{word} - {meaning}")


def search_word(vocab, word):
    word = input_formatting(word)
    found = False
    for unit, words_list in vocab.items():
        for words in words_list:
            if input_formatting(words["word"]) == word:
                print(f"{words['word']} found in {unit}")
                found = True

    if not found:
        print(f"Word '{word}' not found in any unit.")
    return None
