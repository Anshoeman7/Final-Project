# 🎯 Number Guessing Game

## 📌 Description

This is a terminal-based Number Guessing Game built in Python. The program generates a random number, and the player attempts to guess it based on feedback such as “Too high” or “Too low.”

The game includes multiple difficulty levels, attempt tracking, input validation, and a persistent record system that stores player performance across sessions.

---

## 🚀 Features

* 🎮 Interactive menu system
* 🎯 Random number generation
* 📊 Difficulty levels:

  * Easy (1–50, unlimited attempts)
  * Medium (1–100, 10 attempts)
  * Hard (1–200, 7 attempts)
* 🔢 Input validation (handles invalid and out-of-range inputs)
* ⏳ Attempt tracking with remaining attempts display
* 💾 Persistent player records stored in a file
* 📂 View past game records grouped by player
* 🧠 Object-Oriented Programming using a `GameRecord` class

---

## 🛠️ Technologies Used

* Python 3
* Standard libraries:

  * `random` (for number generation)
  * File handling (`open`, read/write)

---

## ▶️ How to Run the Program

1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python game.py
```

---

## 📁 File Structure

```
.
├── game.py        # Main program file
├── records.txt    # Stores player game history (auto-created)
└── README.md      # Project documentation
```

---

## 📊 Example Output

```
🎯 Welcome to the Number Guessing Game!

1. Play Game
2. View Records
3. Exit

Enter choice: 1

Enter your name: Anshuman
Choose difficulty:
1. Easy
2. Medium
3. Hard

Enter choice: 2

I have selected a number between 1 and 100.
Enter your guess: 50
Too low!
Attempts left: 9
```

---

## 📌 Design Overview

* The program uses a **modular structure** with functions handling different parts of the logic.
* A **dictionary of lists** is used to organize player records.
* A **`GameRecord` class** is used to represent each game entry.
* Data is stored in a **text file (`records.txt`)** to maintain persistence across runs.

---

## ⚠️ Notes

* The `records.txt` file is automatically created when the first game is played.
* Ensure the file is in the same directory as `game.py`.

---

## 👨‍💻 Author

Anshuman Singh

---

## 📄 License

This project is for academic purposes (CMPSC 132 Final Project).
