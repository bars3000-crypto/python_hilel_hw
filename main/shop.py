import json
from dataclasses import asdict, dataclass
from pathlib import Path

FREE_DELIVERY_FROM = 1000
BASE_DELIVERY = 50
EXPRESS_EXTRA = 100


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1


class Cart:
    def __init__(self) -> None:
        self._items: dict[str, Item] = {}

    def add(self, name: str, price: float, quantity: int = 1) -> None:
        if price < 0:
            raise ValueError("price must be >= 0")
        if quantity <= 0:
            raise ValueError("quantity must be > 0")
        if name in self._items:
            self._items[name].quantity += quantity
        else:
            self._items[name] = Item(name, price, quantity)

    def remove(self, name: str) -> None:
        if name not in self._items:
            raise KeyError(f"no item {name!r} in cart")
        del self._items[name]

    def __len__(self) -> int:
        return sum(item.quantity for item in self._items.values())

    def total(self) -> float:
        return sum(item.price * item.quantity for item in self._items.values())

    def total_with_discount(self, percent: float) -> float:
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return round(self.total() * (1 - percent / 100), 2)

    def save(self, path: Path) -> None:
        data = [asdict(item) for item in self._items.values()]
        path.write_text(json.dumps(data, indent=2))

    @classmethod
    def load(cls, path: Path) -> Cart:
        cart = cls()
        for row in json.loads(path.read_text()):
            cart.add(row["name"], row["price"], row["quantity"])
        return cart


def delivery_price(total: float, express: bool = False) -> float:
    if total >= FREE_DELIVERY_FROM:
        price = 0
    else:
        price = BASE_DELIVERY
    if express:
        price += EXPRESS_EXTRA
    return price
def discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Некоректний відсоток знижки")
    return price * (1 - percent / 100)