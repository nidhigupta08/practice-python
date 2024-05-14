class PaymentMethod:
    def pay(self):
        pass

class CreditCard(PaymentMethod):
    def pay(self):
        return "Paying with Credit Card"

class PayPal(PaymentMethod):
    def pay(self):
        return "Paying with PayPal"

class Bitcoin(PaymentMethod):
    def pay(self):
        return "Paying with Bitcoin"

# Usage
credit_card = CreditCard()
print(credit_card.pay())

paypal = PayPal()
print(paypal.pay())

bitcoin = Bitcoin()
print(bitcoin.pay())
