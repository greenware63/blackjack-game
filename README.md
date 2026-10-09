# 🃏 Terminal Blackjack Game

A classic command-line Blackjack (21) game built in Python, featuring colorful ASCII terminal art and standard casino rules.

---

## 📋 Features

- **Stylized Terminal Art**: Custom ASCII logo and banner with ANSI terminal colors (`art.py`).
- **Standard Card Values & Rules**:
  - Ace counts as **11** or **1** (automatically adjusting to prevent busting).
  - Face cards (King, Queen, Jack) and 10s count as **10**.
  - Cards 2–9 count at face value.
- **Natural Blackjack Detection**: Instant check for opening 21 on both the player and dealer hands.
- **Interactive Gameplay**:
  - Choose to **Hit (`h`)** to draw another card.
  - Choose to **Stand (`s`)** to hold your hand.
- **Dealer AI**: The computer/dealer automatically draws cards until reaching a score of at least 17.
- **Score Calculation & Outcome Handling**:
  - Handles busts (> 21) for both player and computer.
  - Automatically compares hands and determines win, loss, or draw (push).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+ (No external third-party packages required — uses only standard library modules).

### Installation & Running

1. **Clone the repository**:
   ```bash
   git clone https://github.com/greenware63/blackjack-game.git
   cd blackjack-game
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

---

## 🎮 How to Play

1. When the game starts, you and the dealer will each be dealt two random cards. One of the dealer's cards remains hidden.
2. If neither side has a natural Blackjack (21), you can choose your next move:
   - Type **`h`** to **Hit** (take another card).
   - Type **`s`** to **Stand** (end your turn).
3. If you stand, the dealer will draw cards until their score is 17 or higher.
4. The winner is determined based on who is closest to 21 without going over!

---

## 📂 Project Structure

```text
blackjack-game/
├── art.py        # ASCII banners, glyphs, and ANSI terminal color definitions
├── main.py       # Core game loop, card dealing, scoring, and input handling
├── .gitignore    # Git ignore rules for Python virtual environments and IDEs
└── README.md     # Project documentation
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
