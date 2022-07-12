class DrinkMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "水": 1000,
            "ミルク": 1000,
            "コーヒー豆": 300,
            "砂糖": 300,
            "クリーム": 500,
            "抹茶ソース": 500,
            "ほうじ茶ソース": 500,
            "キャラメルソース": 500,
            "チョコレートソース": 500,
        }
        self.count = []

    def report(self):
        """Prints a report of all resources."""
        print("☆残りの材料")
        print(f"水: {self.resources['水']}ml")
        print(f"ミルク: {self.resources['ミルク']}ml")
        print(f"コーヒー豆: {self.resources['コーヒー豆']}g")
        print(f"砂糖: {self.resources['砂糖']}g")
        print(f"クリーム: {self.resources['クリーム']}g")
        print(f"抹茶ソース: {self.resources['抹茶ソース']}g")
        print(f"ほうじ茶ソース: {self.resources['ほうじ茶ソース']}g")
        print(f"キャラメルソース: {self.resources['キャラメルソース']}g")
        print(f"チョコレートソース: {self.resources['チョコレートソース']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"申し訳ありません。{drink.name}を作るための{item}が足りません。")
                can_make = False
                store_resource = int(input(f"{item}を補充する必要があります。"))
                self.resources[item] += store_resource
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"美味しい{order.name} ☕️が出来上がりました。")
