# 🎮 FizzBuzz Quiz Game (Streamlit)

A fun and interactive **FizzBuzz Quiz Game** built with [Streamlit](https://streamlit.io/).  
In this game, the computer shows you a **random number**. You have to select the correct FizzBuzz answer before moving to the next round!

---

## 📝 Rules of the Game
1. If a number is **divisible by 3**, answer → `Fizz`.
2. If a number is **divisible by 5**, answer → `Buzz`.
3. If a number is **divisible by both 3 and 5**, answer → `Fizz Buzz`.
4. Otherwise → say the **number itself**.
5. For each correct answer, your **score increases**.
6. If you select a wrong option → **Game Over**.
7. You can restart anytime.

---

## ✨ Features
- 🔢 Random numbers every round (not in sequence).
- 👀 Shows **previous, current, and next number**.
- 🎯 Multiple-choice answers (with buttons).
- 🏆 Score counter and full game history.
- 🔄 Restart option when the game ends.
- ⚡ Built fully in **Streamlit** with session state.

---

## 📂 Project Structure
fizzbuzz-game/
│── app.py # Main Streamlit app
│── fizzbuzz.py # FizzBuzz logic class
│── game_manager.py # Game state management (score, history, reset)
│── README.md # Documentation


---

## 🚀 How to Run

### 1️⃣ Clone this repository
```bash
git clone https://github.com/hassan271211/fizzbuzz-game.git
cd fizzbuzz-game

⬅️ Previous: 14  
👉 Current: 15  
➡️ Next: 16  

Options: [Fizz, Buzz, Fizz Buzz]



