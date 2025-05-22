from handle_vocab_file import vocab, filename
import time
import msvcrt
import random


# Def: show words random
def show_random(vocab, unit):
    words_list = vocab[unit][:]
    random.shuffle(words_list)
    return words_list


# Def: time for answering on each word
def wait_or_enter(timeout):
    start = time.time()
    while time.time() - start < timeout:
        if msvcrt.kbhit() and msvcrt.getch() == b"\r":
            return None
        time.sleep(0.1)
    print()


# Def: train a whole unit
def train_whole_unit(timeout, repeat_count, unit):
    while repeat_count > 0:
        print(f"\n{repeat_count} repeats left")
        print(
            f"\nFor answer: press enter or wait {timeout} seconds", end="\n", flush=True
        )
        words_list = show_random(vocab, unit)
        for defin in words_list:
            print(f"{defin['word']} =")
            wait_or_enter(timeout)
            print(f"{defin['meaning'][::-1]}\n")
        repeat_count -= 1
    return None


# Def: validating word range in a specific unit
def validate_word_range(vocab, unit, start_word, end_word):
    words_list = []
    for defin in vocab[unit]:
        words_list.append(defin["word"].lower())
    start_word = start_word.lower().strip()
    end_word = end_word.lower().strip()

    if start_word not in words_list:
        print(f"Start word '{start_word}' not found in {unit}")
        return None, None

    if end_word not in words_list:
        print(f"End word '{end_word}' not found in {unit}")
        return None, None

    start_index = words_list.index(start_word)
    end_index = words_list.index(end_word)

    if start_index >= end_index:
        print("Start word must come before end word.")
        return None, None

    return start_index, end_index


# Def: train a words range in unit
def train_words_range(vocab, repeat_count, timeout, unit, start_index, end_index):
    while repeat_count > 0:
        print(f"\n{repeat_count} repeats left")
        print(
            f"\nFor answer: press enter or wait {timeout} seconds", end="\n", flush=True
        )
        words_subset = vocab[unit][start_index : end_index + 1]
        random.shuffle(words_subset)
        for defin in words_subset:
            print(f"{defin['word']} =")
            wait_or_enter(timeout)
            print(f"{defin['meaning'][::-1]}\n")
        repeat_count -= 1
    return None
