from decimal import Decimal
from inventory.models import Product

class Basket:
    """
    A base Basket class providing some default
    behaviours taht can be inherited or overwritted as necessary
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] += qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}
        self.session.modified = True

    def __len__(self):
        return sum(item["qty"] for item in self.basket.values())

    def __iter__(self):
        """
            The session has the data but we cannot iterate over the session
            we have to iter over the database
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy() #Since we need to add some more data that we
        # dont want to get added in the main session data

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal((item["price"]))
            item["total_price"] = item["price"] * item["qty"]
            yield item