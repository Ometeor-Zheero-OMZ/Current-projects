class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, sugar, cream, matcha, hojicha, caramel, chocolate, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "水": water,
            "ミルク": milk,
            "コーヒー豆": coffee,
            "砂糖": sugar,
            "クリーム": cream,
            "抹茶ソース": matcha,
            "ほうじ茶ソース": hojicha,
            "キャラメルソース": caramel,
            "チョコレートソース": chocolate
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem(name="ラテ", water=250, milk=150, coffee=24, sugar=48, cream=10, matcha=0, hojicha=0, caramel=0,
                     chocolate=0, cost=350),
            MenuItem(name="エスプレッソ", water=400, milk=0, coffee=26, sugar=22, cream=0, matcha=0, hojicha=0, caramel=0,
                     chocolate=0, cost=300),
            MenuItem(name="カプチーノ", water=300, milk=100, coffee=20, sugar=26, cream=0, matcha=0, hojicha=0, caramel=0,
                     chocolate=0, cost=300),
            MenuItem(name="チョコレートモカ", water=250, milk=150, coffee=30, sugar=48, cream=15, matcha=0, hojicha=0,
                     caramel=0, chocolate=120, cost=450),
            MenuItem(name="抹茶フラペチーノ", water=0, milk=300, coffee=0, sugar=40, cream=100, matcha=100, hojicha=0,
                     caramel=0, chocolate=0, cost=650),
            MenuItem(name="ほうじ茶フラペチーノ", water=0, milk=300, coffee=0, sugar=40, cream=100, matcha=0, hojicha=100,
                     caramel=0, chocolate=0, cost=650),
            MenuItem(name="キャラメルフラペチーノ", water=100, milk=200, coffee=0, sugar=50, cream=100, matcha=0, hojicha=0,
                     caramel=100, chocolate=0, cost=650),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f"申し訳ありません。ご注文頂いた{order_name}はメニューにないか、商品名が間違っています。")
        return False
