import json

filename = "vocab_hebrew.json"


# loading vocab file
def load_vocab(filename):
    vocab = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                vocab = json.loads(content)
            else:
                print(
                    f"{filename} is empty or contains only whitespace. Starting with empty database."
                )
    except Exception as e:
        print(f"Unexpected error while reading {filename}: {e}")
    return vocab


vocab = load_vocab(filename)


# saving vocab file
def save_vocab(vocab, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)
    return None
