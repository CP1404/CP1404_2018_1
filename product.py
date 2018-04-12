"""..."""


class Product:
    """Product class for ..."""

    def __init__(self, name="", price=0.0, is_on_sale=False):
        """Construct a Product."""
        self._name = name
        self.__price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = " (on sale)"
        return "{} ${:.2f}{}".format(self._name.title(), self.__price, on_sale_string)

    def __repr__(self):
        return self.__str__()

    def put_on_sale(self, discount_rate=0.0):
        self.is_on_sale = True
        self.__price -= self.__price * discount_rate
