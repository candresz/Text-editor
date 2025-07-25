from collections import Counter

text_file: str = "text.txt"

with open(text_file, "r") as f:
    text = f.read()

# --------------------
# Counting function
# --------------------


def AllWordCount():
    counting = Counter(text.split())
    top_5 = counting.most_common(5)
    for word, count in top_5:
        print(f"{word}: {count}")


# -----------------------
# Single word function
# -----------------------


def SingleWordCount():
    word = input("Please write a single word: ").lower()
    counting = Counter(text.lower().split())
    single_word = counting[word]
    print(f"{word}: {single_word}")


# -----------------------
# Replace word function
# -----------------------


def ReplaceWord():
    global text
    while True:
        word = input("Please write a word to find: ").lower()
        words = text.lower().split()

        if word in words:
            new_word = input("Please write a word to replace it: ").lower()
            count = 0
            updated_words = []

            for w in text.split():
                if w.lower() == word:
                    updated_words.append(new_word)
                    count += 1
                else:
                    updated_words.append(w)

            text = " ".join(updated_words)
            print(f"We have replaced '{word}' with '{new_word}' {count} times.")
            break
        else:
            print(f'We could not find the word "{word}", try again please.\n')


# ---------------------
# Text function
# ---------------------


def AddText():
    global text
    new_text = input("Please write new text to update: ").lower()
    text += " " + new_text
    print("New text has been added.")


# ---------------------
# Delete function
# ---------------------


def DeleteText():
    global text
    target = input("Please enter the exact text to delete: ")
    position = text.find(target)
    if position != -1:
        text = text[:position] + text[position + len(target) :]
        print(f"The first occurrence of '{target}' was deleted.")
    else:
        print(f"The text '{target}' was not found.")


# ------------------------
# Highlight function
# ------------------------


def HighLight():
    word = input("Please enter a word to highlight: ").lower()
    highlighted = []

    for w in text.split():
        if w.lower() == word:
            highlighted.append(f"**{w}**")
        else:
            highlighted.append(w)

    print(" ".join(highlighted))


# ------------------------
# Read text function
# ------------------------


def readTextFile():
    global text
    with open(text_file, "r") as f:
        text = f.read()
    print("Text loaded successfully.")


# ------------------------
# Save text function
# ------------------------


def saveTextFile():
    with open(text_file, "w") as f:
        f.write(text)
    print("Text saved successfully.")


# ------------------------
# Main
# ------------------------


def main():
    while True:
        print("\n=== Edit Menu ===")
        print("1: Top 5 most common words")
        print("2: Single Word Frequency")
        print("3: Replace a word")
        print("4: Add Text")
        print("5: Delete Text")
        print("6: Highlight Text")
        print("7: Save changes")
        print("8: Reload text from file")
        print("9: Exit")
        print("=================")

        choice = input("Select an option (1–9): ")

        if choice == "1":
            AllWordCount()
        elif choice == "2":
            SingleWordCount()
        elif choice == "3":
            ReplaceWord()
        elif choice == "4":
            AddText()
        elif choice == "5":
            DeleteText()
        elif choice == "6":
            HighLight()
        elif choice == "7":
            saveTextFile()
        elif choice == "8":
            readTextFile()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
