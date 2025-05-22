import json
from s3 import filename, bucket_name, s3_client


# loading vocab file
def load_vocab(filename):
    with open(filename, "r", encoding="utf-8") as f:
        vocab = json.load(f)
    return vocab


vocab = load_vocab(filename)


# saving vocab file
def save_vocab(s3_client, vocab, filename, bucket_name):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)
    s3_client.upload_file(filename, bucket_name, filename)
    return None
