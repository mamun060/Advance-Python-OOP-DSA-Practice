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


def _check_checkout(payment_gateway: PaymentGateway, amount: float):
    result = payment_gateway.pay(amount)
    print(result) 

_check_checkout(StripeGateway(), 100.0)
_check_checkout(PayPalGateway(), 200.0)
_check_checkout(BkashGateway(), 300.0)