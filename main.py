import random

class Bank:
    """
    Represents a Bank that can manage branches and accounts.

    Attributes:
        name (str): The name of the bank.
        branches (list): A list of branch names associated with the bank.
    """

    def __init__(self, name):
        """
        Initializes a new Bank instance with the provided name.

        Args:
            name (str): The name of the bank.
        """
        self.name = name
        self.branches = []

    def add_branch(self, branch_name):
        """
        Adds a new branch to the bank.

        Args:
            branch_name (str): The name of the branch to be added.
        """
        self.branches.append(branch_name)

    def delete_branch(self, branch_name):
        """
        Deletes a branch from the bank.

        Args:
            branch_name (str): The name of the branch to be removed.
        """
        if branch_name in self.branches:
            self.branches.remove(branch_name)
            print(branch_name, 'was removed successfully')
        else:
            print('Branch does not exist')

    def get_branches(self):
        """
        Prints the list of branches associated with the bank.
        """
        for branch in self.branches:
            print(branch)


class Branch:
    """
    Represents a Branch within a bank.

    Attributes:
        name (str): The name of the branch.
        accounts (list): A list of account names associated with the branch.
    """

    def __init__(self, name):
        """
        Initializes a new Branch instance with the provided name.

        Args:
            name (str): The name of the branch.
        """
        self.name = name
        self.accounts = []

    def add_account(self, account_name):
        """
        Adds a new account to the branch.

        Args:
            account_name (str): The name of the account to be added.
        """
        self.accounts.append(account_name)

class Account:
    """
    Represents a bank account.

    Attributes:
        account_name (str): The name of the account holder.
        account_number (str): A randomly generated account number.
        balance (float): The current balance of the account.
    """

    def __init__(self, account_name, balance):
        """
        Initializes a new Account instance.

        Args:
            account_name (str): The name of the account holder.
            balance (float): The initial balance of the account.
        """
        self.account_name = account_name
        self.account_number = self.generate_account_number()
        self.balance = balance

    def generate_account_number(self):
        """
        Generates a random 8-digit account number for the account.

        Returns:
            str: The generated account number.
        """
        return str(random.randint(10000000, 99999999))

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount (float): The amount to be deposited.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws money from the account.

        Args:
            amount (float): The amount to be withdrawn.
        """
        if amount > self.balance:
            print(f'{self.account_name} has low balance, try again')
        else:
            self.balance -= amount
            print(f'Withdrawal of {amount} from {self.account_name} was successful')

# Create an HSBC bank instance
hsbc_bank = Bank("HSBC")

# Test adding London branches
hsbc_bank.add_branch("London Main Branch")
hsbc_bank.add_branch("London Oxford Street Branch")

# Display the list of branches
print("List of HSBC Branches:")
hsbc_bank.get_branches()

# Create accounts for London Main Branch
london_main_account1 = Account("Alice", 1000.0)
london_main_account2 = Account("Bob", 1500.0)

# Add accounts to the London Main Branch
for branch in hsbc_bank.branches:
    if branch == "London Main Branch":
        branch_obj = Branch(branch)
        branch_obj.add_account(london_main_account1)
        branch_obj.add_account(london_main_account2)

# Display the list of accounts for the London Main Branch
print("\nList of Accounts at London Main Branch:")
for branch in hsbc_bank.branches:
    if branch == "London Main Branch":
        branch_obj = Branch(branch)
        for account in branch_obj.accounts:
            print(f"Account Name: {account.account_name}, Account Number: {account.account_number}, Balance: {account.balance}")

# Test account deposit and withdrawal
london_main_account1.deposit(500.0)
london_main_account2.withdraw(200.0)

# Display updated account balances
print("\nUpdated Account Balances:")
print(f"Account 1 - Name: {london_main_account1.account_name}, Balance: {london_main_account1.balance}")
print(f"Account 2 - Name: {london_main_account2.account_name}, Balance: {london_main_account2.balance}")

# Add a new branch
hsbc_bank.add_branch("London West End Branch")

# Display the list of branches (including the new branch)
print("\nUpdated List of HSBC Branches:")
hsbc_bank.get_branches()

# Create an account for London West End Branch
london_west_end_account = Account("Charlie", 2000.0)

# Add the account to the London West End Branch
for branch in hsbc_bank.branches:
    if branch == "London West End Branch":
        branch_obj = Branch(branch)
        branch_obj.add_account(london_west_end_account)