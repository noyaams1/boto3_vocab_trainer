from validation import input_validation
from editing_mode import add_word, delete_word, update_word, list_words, search_word
from training_func import train_whole_unit, validate_word_range, train_words_range
from testing_func import test


def show_units(vocab):
    if not vocab:
        print("No vocabulary units found.")
        return False

    print("\nAvailable units:")
    for unit in vocab.keys():
        print(f"{unit}")
    print()
    return True


def editing_menu(vocab):

    while True:
        print("\n--- Editing Mode ---")
        print("1. Add word")
        print("2. Delete word")
        print("3. Update word")
        print("4. List words")
        print("5. Search word across units")
        print("6. Back to main menu")

        choice = input("\nChoose an option (1-6): ").strip()
        if choice == "1":
            unit = input("Enter unit name: ").strip()
            word = input("Enter word: ").strip()
            meaning = input("Enter meaning: ").strip()

            if input_validation(unit, word, meaning):
                add_word(vocab, unit, word, meaning)

        elif choice == "2":
            if show_units(vocab):
                unit = input("Enter unit name: ").strip()
                if unit in vocab:
                    word = input("Enter word to delete: ").strip()
                    delete_word(vocab, unit, word)
                else:
                    print(f"Unit '{unit}' does not exist.")

        elif choice == "3":
            if show_units(vocab):
                unit = input("Enter unit name: ").strip()
                if unit in vocab:
                    old_word = input("Enter word to update: ").strip()
                    new_word = input(
                        "Enter new word (leave empty to keep the same): "
                    ).strip()
                    new_meaning = input("Enter new meaning: ").strip()

                    if not new_word:
                        new_word = old_word

                    if input_validation(unit, new_word, new_meaning):
                        update_word(vocab, unit, old_word, new_word, new_meaning)
                else:
                    print(f"Unit '{unit}' does not exist.")

        elif choice == "4":
            if show_units(vocab):
                unit = input("Enter unit name to list: ").strip()
                list_words(vocab, unit)

        elif choice == "5":
            word = input("Enter word to search: ").strip()
            search_word(vocab, word)

        elif choice == "6":
            return

        else:
            print("Invalid option. Please try again.")
            break


def training_menu(vocab):
    while True:
        print("\n--- Training Mode ---")
        print("1. Train whole unit")
        print("2. Train word range")
        print("3. Back to main menu")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            if show_units(vocab):
                unit = input("Enter unit name to train: ").strip()
                if unit in vocab:
                    timeout = int(input("Enter delay time in seconds: ") or 4)
                    repeat_count = int(input("Enter number of repetitions: ") or 7)
                    train_whole_unit(timeout, repeat_count, unit)
                else:
                    print(f"Unit '{unit}' does not exist.")

        elif choice == "2":
            if show_units(vocab):
                unit = input("Enter unit name to train: ").strip()
                if unit in vocab:
                    start_word = input("Enter start word: ").strip()
                    end_word = input("Enter end word: ").strip()

                    start_index, end_index = validate_word_range(
                        vocab, unit, start_word, end_word
                    )
                    if start_index is not None:
                        timeout = int(input("Enter delay time in seconds: ") or 4)
                        repeat_count = int(input("Enter number of repetitions: ") or 7)
                        train_words_range(
                            vocab, repeat_count, timeout, unit, start_index, end_index
                        )
                else:
                    print(f"Unit '{unit}' does not exist.")

        elif choice == "3":
            return

        else:
            print("Invalid option. Please try again.")
            break


def testing_menu(vocab):

    while True:
        print("\n--- Testing Mode ---")
        print("1. Test on a unit")
        print("2. Back to main menu")

        choice = input("\nChoose an option (1-2): ").strip()

        if choice == "1":
            if show_units(vocab):
                unit = input("Enter unit name to test: ").strip()
                if unit in vocab:
                    test(vocab, unit)
                else:
                    print(f"Unit '{unit}' does not exist.")

        elif choice == "2":
            return

        else:
            print("Invalid option. Please try again.")
            break
