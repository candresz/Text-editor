# 📝 Text Editor (Python Console App)

A simple interactive text editor built in Python that allows users to load, modify, and save text files through a menu-based console interface.

---

## 📌 Features

- ✅ View top 5 most frequent words in the text
- ✅ Count the number of times a single word appears
- ✅ Replace a word and track how many times it was changed
- ✅ Add new text to the file
- ✅ Delete the **first occurrence** of a string
- ✅ Highlight all instances of a word using `**word**`
- ✅ Read text from a file and save changes back to file

---

## 🚀 How It Works

Upon running the program, users are presented with a menu of options. Based on input, the program calls the corresponding function to manipulate the text stored in memory. All changes can be saved to the original file.

---

## 🧠 Functions Overview

| Function           | Description |
|--------------------|-------------|
| `AllWordCount()`   | Displays the top 5 most common words using `Counter` |
| `SingleWordCount()`| Asks the user for a word and prints how many times it appears |
| `ReplaceWord()`    | Replaces all instances of a word with another, reports count |
| `AddText()`        | Appends new user-provided text to the document |
| `DeleteText()`     | Removes the first exact match of a given string |
| `HighLight()`      | Highlights all matches of a word by surrounding with `**` |
| `readTextFile()`   | Reloads the file content into memory |
| `saveTextFile()`   | Writes the current text back into the file |

---

## 🛠 Technologies

- **Python 3.10+**
- Built-in libraries: `collections`, `os` (optional)

---
