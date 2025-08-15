# 🎲 Pytzee - A Python Yahtzee Variant

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## 📌 Overview
**Pytzee** is a **Python-based console game** inspired by the classic dice game **Yahtzee**, with a few rule changes and customizations.  
The goal is to roll dice and score points across various categories, aiming for the highest score possible.

---

## 🎮 How to Play
- The game rolls **5 dice** each round.
- You choose a **category** to score your roll:
  - Singles (1's, 2's, 3's, 4's, 5's, 6's)
  - Three of a Kind
  - Four of a Kind
  - Full House (25 pts)
  - Small Straight (30 pts)
  - Large Straight (40 pts)
  - Pytzee (Yahtzee) (50 pts, extra 100 pts for additional Pytzees)
  - Chance (sum of all dice)
- If a category is already taken, you must choose another.
- Upper section bonus: **+35 points** if 1's–6's sum to 63 or more.
- The winner is the player (or you) with the **highest total score** after all rounds.

---

## 🛠️ Controls
- After each roll, type your scoring choice:
  - `"count 1"` → Score all 1's in the roll
  - `"full house"` → Score as a full house if possible
  - `"pytzee"` → Score as a Yahtzee (Pytzee)
  - `"chance"` → Score sum of all dice
  - `"skip"` → Skip scoring this round
- Input can be **full text** or abbreviations like `"3 of a kind"`.

---

## 📂 Project Structure
```
yahtzee.py   # Main game code
```

---

## 🛠️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/pytzee.git
   cd pytzee
   ```

2. **Run the game**
   ```bash
   python3 cmsc201_proj1_yahtzee.py
   ```

---

## 📖 Example Gameplay
```plaintext
What is the number of rounds that you want to play? 3
Enter the seed or 0 to use a random seed: 42
***** Beginning round 1 *****
Your score is: 0
[3, 5, 2, 3, 1]
How would you like to count this roll? full house
You have a full house and get 25 points.
|Full House : 25|
...
Your final score is: 115
```

---

## ⚙️ Requirements
- Python **3.x**
- No external libraries required

---

## 📜 License
This project is licensed under the **MIT License** — free to use, modify, and share.

---

## 👨‍💻 Author
**Ali Amir**  
📧 codepirate2028@gmail.com
