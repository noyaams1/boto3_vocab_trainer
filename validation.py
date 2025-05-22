def input_validation(unit, word, meaning):
    if not unit or not unit.strip():
        print("❌ Unit name cannot be empty.")
        return False

    if not word or not word.strip():
        print("❌ Word cannot be empty.")
        return False

    if not meaning or not meaning.strip():
        print("❌ Meaning cannot be empty.")
        return False

    return True


def input_formatting(input_str):
    return input_str.strip().lower()
