# Data Transfer Objects:
class Vaccine:
    def __init__(self, vaccine_id, date, supplier, quantity):
        self.vaccine_id = vaccine_id
        self.date = date
        self.supplier = supplier
        self.quantity = quantity


class Supplier:
    def __init__(self, supplier_id, supplier_name, logistic):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.logistic = logistic


class Clinic:
    def __init__(self, clinic_id, location, demand, logistic):
        self.clinic_id = clinic_id
        self.location = location
        self.demand = demand
        self.logistic = logistic


class Logistic:
    def __init__(self, logistic_id, logistic_name, count_sent, count_received):
        self.logistic_id = logistic_id
        self.logistic_name = logistic_name
        self.count_sent = count_sent
        self.count_received = count_received
