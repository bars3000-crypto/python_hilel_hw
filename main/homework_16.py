class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount_active = False

    def add_item(self, price: float, quantity: int = 1):
        if price <= 0 or quantity <= 0:
            raise ValueError("Ціна та кількість мають бути більшими за нуль")
        
        total_price = price * quantity
        
        if self.discount_active:
            total_price *= 0.9  # Знижка 10%

        self.items.append(total_price)
        return total_price


def test_shopping_cart_normal_price():
    cart = ShoppingCart()
    result = cart.add_item(100, 2)
    assert result == 200, f"Очікувалося 200, а отримано {result}"


def test_shopping_cart_with_discount():
    cart = ShoppingCart()
    cart.discount_active = True
    result = cart.add_item(100, 2)
    assert result == 180.0, f"Очікувалося 180.0 з урахуванням знижки, а отримано {result}"


def test_shopping_cart_invalid_values():
    cart = ShoppingCart()
    try:
        cart.add_item(-50, 1)
        assert False, "Повинна була виникнути помилка ValueError для від'ємної ціни"
    except ValueError:
        pass  # Тест успішно пройдено, помилка перехоплена


if __name__ == "__main__":
    test_shopping_cart_normal_price()
    test_shopping_cart_with_discount()
    test_shopping_cart_invalid_values()
    print("Усі тести успішно пройдено!")