from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass 

class StripeGateway(PaymentGateway):
    def pay(self, amount: float):
        return (f"Processing payment of ${amount} through Stripe.")

class PayPalGateway(PaymentGateway):
    def pay(self, amount: float):
        return (f"Processing payment of ${amount} through PayPal.")

class BkashGateway(PaymentGateway):
    def pay(self, amount: float):
        return (f"Processing payment of ${amount} through Bkash.")


def checkout(payment_gateway: PaymentGateway, amount: float):
    result = payment_gateway.pay(amount)
    print(result) 

checkout(StripeGateway(), 100.0)
checkout(PayPalGateway(), 200.0)
checkout(BkashGateway(), 300.0)