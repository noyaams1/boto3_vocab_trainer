from handle_vocab_file import vocab
from menus import editing_menu, training_menu, testing_menu


def main():
    while True:
        print("\n=== Vocabulary Trainer ===")
        print("1. Editing Mode")
        print("2. Training Mode")
        print("3. Testing Mode")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            editing_menu(vocab)
        elif choice == "2":
            training_menu(vocab)
        elif choice == "3":
            testing_menu(vocab)
        elif choice == "4":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")
            break


if __name__ == "__main__":
    main()
