# Lux Bank - CLI Banking System

A simple command-line interface (CLI) banking application built with Python that allows users to perform basic banking operations.

## Features

- ✅ Create a bank account with a default balance of Kshs 10,000
- 💰 Check account balance
- 📥 Deposit cash
- 📤 Withdraw cash
- ✨ Input validation for all transactions
- 🔄 Interactive menu system

## Project Structure

```
lux-bank/
│
├── account.py          # Account class with banking operations
├── main.py            # Main application with CLI interface
└── README.md          # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lux-bank.git
   cd lux-bank
   ```

2. **Requirements**
   - Python 3.6 or higher
   - No external dependencies required

## Usage

Run the application from the command line:

```bash
python main.py
```

### Menu Options

When you run the application, you'll be greeted with an interactive menu:

1. **Check Balance** - View your current account balance
2. **Deposit Cash** - Add funds to your account
3. **Withdraw Cash** - Remove funds from your account (with sufficient balance check)
4. **Exit Service** - Exit the application

### Example Session

```
What is your Name: John Doe

Welcome John Doe, to Lux Bank:
What would you like to do(1-4)?
1. Check Balance
2. Deposit Cash
3. Withdraw Cash
4. Exit Service
> 1

Your Account Balance is: Kshs 10000

Welcome John Doe, to Lux Bank:
What would you like to do(1-4)?
1. Check Balance
2. Deposit Cash
3. Withdraw Cash
4. Exit Service
> 2

Enter Amount to Deposit: Kshs 5000
You have deposited Kshs 5000
New Account Balance: Kshs 15000
```

## Code Overview

### Account Class (`account.py`)

The `Account` class handles all banking operations:

- **`__init__(name, amount=10000)`** - Initialize account with name and starting balance
- **`check_balance()`** - Returns current account balance
- **`deposit_amount(deposit)`** - Adds money to the account
- **`withdraw_amount(withdraw)`** - Removes money from the account

### Main Application (`main.py`)

The main application provides:
- User input handling
- Menu navigation
- Transaction validation
- Error handling for invalid inputs

## Validation Rules

- **Deposits**: Must be Kshs 1 or more
- **Withdrawals**: 
  - Must be Kshs 1 or more
  - Cannot exceed current account balance
- **Menu Selection**: Must be a valid option (1-4)

## Future Enhancements

Potential features for future versions:

- [ ] Multiple account support
- [ ] Transaction history
- [ ] Account authentication (PIN/Password)
- [ ] Save/load account data to file
- [ ] Transfer between accounts
- [ ] Interest calculation
- [ ] Account types (Savings, Current, Fixed Deposit)
- [ ] Currency conversion
- [ ] GUI interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Wams**

## Acknowledgments

- Built as a learning project to demonstrate OOP principles in Python
- Inspired by basic banking system requirements

---

**Note**: This is a demonstration project for educational purposes. It does not include security features required for real banking applications.
