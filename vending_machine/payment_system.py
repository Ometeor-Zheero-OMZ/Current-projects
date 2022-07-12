class PaymentSystem:
    CURRENCY = "￥"

    MONEY_VALUES = {
        "10,000": 10000,
        "5,000": 5000,
        "1,000": 1000,
        "500": 500,
        "100": 100,
        "50": 50,
        "10": 10,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print("☆売上高")
        print(self.CURRENCY, self.profit)

        """TODO:コーヒーメーカーの中のお金を勘定する"""
        # for money in self.MONEY_VALUES:
        #     if money == 10000:
        #         print(f"{money}: ")
        #     elif money == 5000:
        #         money /= 2
        #         print(f"{money}: ")


    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        for _ in self.MONEY_VALUES:
            self.money_received += int(input("お金を入れてください。"))
            ask_customer = input("清算しますか？: 'Yes' or 'No': ").lower()
            if ask_customer == "yes":
                return self.money_received
            else:
                print("払い戻しをしました。")
                self.money_received = 0

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"お返しが{self.CURRENCY}{change}になります。")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("恐れ入りますが、金額が足りません。")
            self.money_received = 0
            return False

