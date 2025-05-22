from training_func import show_random
from validation import input_formatting


def test(vocab, unit):
    correct_count = 0
    incorrect_words = []
    words = show_random(vocab, unit)
    for word in words:
        print(f"\n * {word['word']}")
        user_ans = input_formatting(input("What is the meaning? "))
        correct_meaning = input_formatting(word["meaning"])

        if user_ans == correct_meaning:
            print("✅ Correct!\n")
            correct_count += 1
        else:
            print(f"❌ Incorrect. Correct answer: {word['meaning']}\n")
            incorrect_words.append((word["word"], word["meaning"]))

    total = len(words)
    percentage = int((correct_count / total) * 100) if total > 0 else 0

    print(f"\n📝 Final Score: {correct_count}/{total} ({percentage}%)")

    if incorrect_words:
        print("\n❗ Words to review:")
        for w, correct in incorrect_words:
            print(f"  * {w} → {correct}")

    get_feedback(percentage)

    return percentage


def get_feedback(score):
    if score in range(85, 101):
        print("🌟 Excellent! Great job remembering your vocabulary")
    elif score in range(60, 85):
        print("👍 Good work! A bit more practice and you'll master it")
    elif score in range(30, 60):
        print("🟡 Keep going! You're getting there, but review needed")
    else:
        print("🧱 Needs improvement. Study the words again and try once more")
