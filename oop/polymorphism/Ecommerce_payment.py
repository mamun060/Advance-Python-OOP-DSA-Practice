class Payment:
    def pay(self, amount: float):
        raise NotImplementedError("Subclasses must implement this method")
    

class BkashPayment(Payment):
    def pay(self, amount: float):
        print(f"Processing Bkash payment of {amount}")

class PaypalPayment(Payment):
    def pay(self, amount: float):
        print(f"Processing PayPal payment of {amount}")

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Processing Credit Card payment of {amount}")

payments = [BkashPayment(), PaypalPayment(), CreditCardPayment()]

for payment in payments:
    payment.pay(100.0)