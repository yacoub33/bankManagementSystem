# Bank Management System

A simple Python-based bank management system that allows you to manage bank branches, accounts, deposits, and withdrawals.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create and manage multiple bank branches.
- Add accounts to specific branches.
- Generate random account numbers for accounts.
- Deposit and withdraw money from accounts.
- Handle low balance scenarios.

## Getting Started

### Prerequisites

- Python 3.x
- Git (optional)

### Installation

1. Clone the repository (or download the ZIP file):

   ```bash
   git clone https://github.com/your-username/bank-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd bank-management-system
   ```

3. Run the bank management system:

   ```bash
   python main.py
   ```

## Usage

Follow the on-screen menu to interact with the bank management system. You can add branches, create accounts, and perform deposits and withdrawals.

## Documentation

- [Bank Class](#bank-class)
- [Branch Class](#branch-class)
- [Account Class](#account-class)

### Bank Class

Represents a Bank that can manage branches and accounts.

#### Attributes

- `name (str)`: The name of the bank.
- `branches (list)`: A list of branch names associated with the bank.

#### Methods

- `add_branch(branch_name)`: Adds a new branch to the bank.
- `delete_branch(branch_name)`: Deletes a branch from the bank.
- `get_branches()`: Prints the list of branches associated with the bank.

### Branch Class

Represents a Branch within a bank.

#### Attributes

- `name (str)`: The name of the branch.
- `accounts (list)`: A list of account names associated with the branch.

#### Methods

- `add_account(account_name)`: Adds a new account to the branch.

### Account Class

Represents a bank account.

#### Attributes

- `account_name (str)`: The name of the account holder.
- `account_number (str)`: A randomly generated account number.
- `balance (float)`: The current balance of the account.

#### Methods

- `deposit(amount)`: Deposits money into the account.
- `withdraw(amount)`: Withdraws money from the account.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please open an issue or create a pull request.