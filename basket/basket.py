class Basket:
    """
    A base Basket class providing some default
    behaviours taht can be inherited or overwritted as necessary
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("session_key")
        if "session_key" not in request.session:
            basket = self.session["session_key"] = {"number":12345}
        self.basket = basket