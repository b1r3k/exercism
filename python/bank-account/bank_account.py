from threading import Lock


class BankAccount:
    def __init__(self):
        self._balance = 0
        self._open = None
        self._lock = Lock()

    def verify_account_state(self):
        if self._open != True:
            raise ValueError('Account closed')

    def get_balance(self):
        self.verify_account_state()
        return self._balance

    def open(self):
        if self._open:
            raise ValueError('Account already open')
        self._open = True

    def deposit(self, amount):
        self.verify_account_state()
        if amount < 0:
            raise ValueError('Invalid amount')
        with self._lock:
            self._balance += amount

    def withdraw(self, amount):
        self.verify_account_state()
        if amount < 0:
            raise ValueError('Invalid amount')
        if amount > self._balance:
            raise ValueError('Insufficient balance')
        with self._lock:
            self._balance -= amount

    def close(self):
        self.verify_account_state()
        self._open = False
        self._balance = 0
