# 📈 Stock Portfolio Tracker

A simple Python-based stock tracker that calculates total investment value based on user input and static stock prices. Built as part of an internship project to demonstrate core programming concepts such as dictionaries, input/output, arithmetic operations, and optional CSV file handling.

---

## 🔍 Project Overview

This program allows users to:

- Enter stock symbols and quantities they own
- Calculate total investment value based on hardcoded stock prices
- Display a formatted portfolio summary
- Optionally export the report to a `.csv` file for records

---

## 🛠️ Technologies & Concepts Used

- ✅ Python 3
- ✅ Dictionaries
- ✅ Loops and conditionals
- ✅ User input handling
- ✅ Basic arithmetic operations
- ✅ File writing (CSV)

---

## 💡 Sample Hardcoded Prices

The current version uses the following stock prices (can be easily updated):

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 120,
    "MSFT": 310
}


🚀 How It Works
1. The user is prompted to input stock symbols and the number of shares owned.
2. The program looks up the stock price from a predefined dictionary.
3. It calculates the value of each stock and accumulates the total.
4. Results are printed in a clean tabular format.
5. The user is asked whether to save the report as a CSV file.

📸 Example Output

--- Portfolio Breakdown ---
Stock     Qty       Price     Value     
AAPL      5         $180      $900
TSLA      2         $250      $500
GOOGL     3         $135      $405

Total Investment Value: $1,805

📁 Optional CSV Output
If the user chooses, the portfolio summary can be saved to a file named portfolio_summary.csv.

🤝 Credits
This project was developed by Kacabdev as part of a learning challenge and internship program. The goal was to reinforce Python fundamentals through hands-on project building.

🔗 License
This project is licensed under the MIT License.

