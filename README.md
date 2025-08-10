# 📈 CodeAlpha - Stock Portfolio Tracker

## Overview
This project is part of my **Python Programming Internship** at **CodeAlpha**.  
The **Stock Portfolio Tracker** lets users enter stock symbols and quantities, calculates the **total investment value** using hardcoded prices, and optionally saves the summary to a `.txt` file.

---

## Features
- Hardcoded stock prices for quick testing  
- Interactive console input/output  
- Calculates individual stock value and total portfolio value  
- Option to save summary to a text file (`portfolio_summary.txt`)  
- Built with plain Python (no external libraries required)

---

## Technologies Used
- Python 3  
- Dictionaries, loops, conditionals  
- Basic file handling

---

## Folder Structure
    CodeAlpha_StockPortfolioTracker/
    ├── stock_tracker.py           # Main Python script
    ├── README.md                  # Project description (this file)
    └── portfolio_summary.txt      # Generated after saving results

---

## Sample Output
    === Stock Portfolio Tracker ===
    Available stocks and prices:
    AAPL: $180
    TSLA: $250
    GOOG: $120
    MSFT: $300
    AMZN: $140

    Enter stock symbol (or 'done' to finish): AAPL
    Enter quantity of AAPL: 10
    ✅ Added 10 shares of AAPL

    Enter stock symbol (or 'done' to finish): TSLA
    Enter quantity of TSLA: 5
    ✅ Added 5 shares of TSLA

    === Portfolio Summary ===
    AAPL - 10 shares - Value: $1800
    TSLA - 5 shares - Value: $1250

    💰 Total Investment Value: $3050

    Do you want to save this summary to a file? (y/n): y
    📄 Summary saved to portfolio_summary.txt

---

## How to Run
1. Ensure **Python 3** is installed.
2. Clone the repo:
       git clone https://github.com/YourUsername/CodeAlpha_StockPortfolioTracker.git
3. Change directory:
       cd CodeAlpha_StockPortfolioTracker
4. Run the script:
       python stock_tracker.py
   (or `python3 stock_tracker.py` on some systems)
5. Follow the on-screen prompts to enter stock symbols and quantities. Type `done` when finished.

---

## Internship Details
- **Repository name:** `CodeAlpha_StockPortfolioTracker`  
- **Task:** Stock Portfolio Tracker  
- **Mentor / Organization:** CodeAlpha (https://www.codealpha.tech)

---

## Author
**Nagula Lahari**  
Python Programming Intern @ CodeAlpha

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
