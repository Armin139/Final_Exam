class Account:
    def _init_(self, account_NUM,BL):
        self.account_NUM = account_NUM
        self.BL = BL


class Bank:
    def _init_(self):
        self.accounts = []
        self.LN_AM = 0
        self.LN_on= True

    def create_account(self, account_NUM, starting_BL):
        account = Account(account_NUM, starting_BL)
        self.accounts.append(account)

    def count_total_BL(self):
        total_BL= sum(account.BL for account in self.accounts)
        return total_BL

    def count_LN_AM(self):
        return self.LN_AM

    def enable_LN(self):
        self.LN_on = True

    def disable_LN(self):
        self.LN_on = False


class Admin:
    def _init_(self, bank):
        self.bank = bank

    def create_account(self, account_NUM, initial_BL):
        self.bank.create_account(account_NUM, initial_BL)

    def count_total_BL(self):
        return self.bank.count_total_BL()

    def count_LN_AM(self):
        return self.bank.count_LN_AM()

    def enable_LN_atribute(self):
        self.bank.enable_LN()

    def disable_LN_atribute(self):
        self.bank.disable_LN()


# Usage example:
bank = Bank()
admin = Admin(bank)

# Create accounts
admin.create_account(1001, 1000)
admin.create_account(1002, 2000)
admin.create_account(1003, 3000)

# Check total balance
total_BL= admin.count_total_BL()
print("Total BL:", total_BL)

# Check loan amount
LN_AM= admin.count_LN_AM()
print("Loan Amount:", LN_AM)

# Disable loan feature
admin.disable_LN_atribute()
print("Loan Feature Enabled:", bank.LN_on)

# Enable loan feature
admin.enable_LN_atribute()
print("Loan Feature Enabled:", bank.LN_on)