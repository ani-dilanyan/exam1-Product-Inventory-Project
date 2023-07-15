from Money import Money
from MyExceptions import ProductTypeError, ProductValueError


class Product:
    def __init__(self, _id, title, price, quantity):
        try:
            if type(title) != str:
                raise ProductTypeError("product title", title)
            elif type(price) != Money:
                raise ProductTypeError("product price", price)
            elif type(_id) != int:
                raise ProductTypeError("id", id)
            elif type(quantity) != int:
                raise ProductTypeError("product quantity", quantity)

            if _id <= 0:
                raise ProductValueError("Unsupported negative value for id", _id)
            elif quantity < 0:
                raise ProductValueError("Unsupported negative value for product quantity", quantity)
        except (ProductTypeError, ProductValueError) as error:
            print(error)
        else:
            self.id = _id
            self.title = title
            self.price = price
            self.quantity = quantity

    def __repr__(self):
        try:
            return "Id:{} Title:{} Price:{} Quantity:{}".format(self.id, self.title, self.price, self.quantity)
        except AttributeError:
            return "Object is empty"

    def buy(self, purchase_quantity):
        try:
            if type(purchase_quantity) != int:
                raise ProductTypeError("purchase quantity", purchase_quantity)

            if purchase_quantity > self.quantity:
                raise ProductValueError("No enough quantity in inventory", purchase_quantity)
            elif purchase_quantity < 0:
                raise ProductValueError("Unsupported negative value for purchase quantity", purchase_quantity)

        except (ProductValueError, ProductTypeError) as purchase_error:
            return purchase_error
        else:
            self.quantity -= purchase_quantity
            return "Purchase completed successfully"
