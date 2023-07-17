class Bank:
    def _init_(self):
        self.users = {}

    def create_acc(self,naam):
        if naam in self.users:
            print("Acc already exists.")
        else:
            self.users[naam] = User(naam)
            print("Acc created successfully.")

    def get_user(self, naam):
        if naam in self.users:
            return self.users[naam]
        else:
            return None


class User:
    def _init_(self, naam):
        self.naam = naam
        self.bl = 0
        self.TR_details= []

    def insert(self, tk):
        if tk <= 0:
            print("Invalid amount.Enter tk is  greater than 0.")
        else:
            self.bl += tk
            self.TR_details.append(f"Deposit: +{tk}")

    def withdraw(self, tk):
        if tk<= 0:
            print("Invalid amount. Withdrawal amount greater than sufficient.")
        elif tk > self.bl:
            print("Insufficient bl.")
        else:
            self.bl -= tk
            self.TR_details.append(f"Withdrawal: -{tk}")

    def transfer(self,tk, recipient):
        if tk<= 0:
            print("Invalid tk. Transfer tk is more than zero.")
        elif tk> self.bl:
            print("Insufficient balance.")
        elif recipient is None:
            print("acceptence account not found.")
        else:
            self.bl -= tk
            self.TR_details.append(f"Transfer to {recipient.naam}: -{tk}")
            recipient.bl += tk
            recipient.TR_details.append(f"Transfer from {self.naam}: +{tk}")

    def check_bl(self):
        return self.bl

    def get_TR_history(self):
        return self.TR_details

    def receive_LN(self):
        LN_tk = 2 * self.bl
        self.bl += LN_tk
        self.TR_details.append(f"Loan: +{LN_tk}")


# Usage example:

bank = Bank()

# Create accounts
bank.create_acc("Asma")
bank.create_acc("Armin")

# Get user objects
asma = bank.get_user("Asma")
armin = bank.get_user("Armin")

# Deposit money
asma.insert(1000)
armin.insert(500)

# Withdraw money
asma.withdraw(200)
armin.withdraw(100)

# Transfer money
asma.transfer(300, armin)

# Check balance
print(f"Asma's bl: {asma.check_bl()}")
print(f"Armin's bl: {armin.check_bl()}")

# Check transaction history
print("Asma's TR history:")
print(asma.get_TR_history())

print("Armin's TR history:")
print(armin.get_TR_history())

# Take a loan
asma.receive_LN()
print(f"Asma's balance after loan: {asma.check_bl()}")