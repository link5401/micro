class Customer:
    def __init__(self, id,name,order):
        self.id = id
        self.name = name
        self.order = order

class View:
    def print(self,customer):
        print(f'customer details\nID:{customer.id}\nName: {customer.name}\nDepartment: {customer.order}')
class Controller:
    def __init__(self, model , view):
        self.model = []
        self.model.extend(model)
        self.view = view
    def addCustomer(self, cus):
        self.model.append(cus)
    def removeCustomer(self, id):
        for customer in self.model:
            if customer.id == id:
                self.model.remove(customer)