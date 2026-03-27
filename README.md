# AI Rock-Paper-Scissors Predictor

This project is a part of the **Machine Learning with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/). It features an intelligent bot that learns and predicts opponent moves using a **Multi-level Markov Chain** algorithm.

## 🚀 Live Demo
You can play against the AI here: [https://rock-paper-sciapprs.streamlit.app/](https://rock-paper-sciapprs.streamlit.app/)

## 🧠 How it Works
Unlike simple random bots, this AI analyzes the history of the game to find patterns in your gameplay.
* **Pattern Matching:** It tracks sequences of moves (lengths 3 to 6) to predict what you will play next.
* **Confidence Scoring:** It evaluates multiple possible patterns and chooses the one with the highest statistical probability.
* **Frequency Analysis:** If not enough data is available (initial moves), it falls back to basic frequency analysis to maintain a winning edge.

## 📊 Performance
The bot successfully passes the freeCodeCamp challenge by maintaining over a **60% win rate** against four different test bots:
- **Quincy:** ~99%
- **Abbey:** ~65%
- **Kris:** ~75%
- **Murgatroid:** ~85%

## 🛠️ Tech Stack
- **Language:** Python 3
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **Algorithm:** Markov Chain / N-gram Pattern Recognition

## 📂 Project Structure
- `RPS.py`: The core AI logic.
- `app.py`: The web interface built with Streamlit.
- `main.py`: Local testing script.
- `RPS_game.py`: Environment and opponent bot definitions.
- `requirements.txt`: Dependencies for deployment.

## 📖 Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/anwarhossen57/Rock-Paper-Scissors.git](https://github.com/anwarhossen57/Rock-Paper-Scissors.git)

   ## What I Learned from this Project
In this project, I explored the world of **Game Theory** and **Pattern Matching**. I learned how to build a bot that predicts an opponent's next move based on historical data. Working with sequences and developing an algorithm that can counter multiple strategies (like Quincy, Mrugesh, and Kris) gave me deep insights into how to handle dynamic datasets and logic-based decision making.
