class Basket:
    """
    A base Basket class providing some default
    behaviours taht can be inherited or overwritted as necessary
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("session_key")
        if "session_key" not in request.session:
            basket = self.session["session_key"] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = product.id
        if product_id not in self.basket:
            self.basket['product_id'] = {"price": str(product.price),
                                         "qty":qty}

        self.session.modified = True