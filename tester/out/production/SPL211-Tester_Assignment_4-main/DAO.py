# Data Access Objects:
# All of these are meant to be singletons
from DTO import Vaccine, Logistic, Supplier, Clinic


class StudentGradeWithName:
    def __init__(self, name, assignment_num, grade):
        self.name = name
        self.assignment_num = assignment_num
        self.grade = grade


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    # must
    def insert(self, vaccine):
        self._conn.execute("""
               INSERT INTO vaccines (vaccine_id, date, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [vaccine.vaccine_id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT vaccine_id FROM vaccines WHERE vaccine_id = ?
        """, [vaccine_id])
        # return tapel
        return Vaccine(*c.fetchone())

    def get_max_id(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT MAX(vaccine_id) FROM vaccines;
        """, )
        return c.fetchone()

    def get_oldest(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM vaccines;
        """)
        return c.fetchone()

    def remove(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
                 DELETE FROM vaccines WHERE vaccine_id = ?
            """, [vaccine_id])

    def decrease_quantity(self, vaccine_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE vaccines SET quantity = quantity-(?) WHERE vaccine_id=(?)
            """, [amount, vaccine_id])

    def get_quantity_sum(self):
        c = self._conn.cursor()
        c.execute("""
                SELECT SUM(quantity) FROM vaccines
        """, )
        return c.fetchone()


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (supplier_id, supplier_name, logistic) VALUES (?, ?, ?)
        """, [supplier.supplier_id, supplier.supplier_name, supplier.logistic])

    def find_by_name(self, supplier_name):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM suppliers WHERE supplier_name = ?
            """, [supplier_name])
        return c.fetchone()


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
            INSERT INTO clinics (clinic_id, location, demand, logistic) VALUES (?, ?, ?, ?)
        """, [clinic.clinic_id, clinic.location, clinic.demand, clinic.logistic])

    def find_by_location(self, location):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM clinics WHERE location = ?
                """, [location])
        return c.fetchone()

    def decrease_demand(self, clinic_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE clinics SET demand = demand-(?) WHERE clinic_id=(?)
            """, [amount, clinic_id])

    def get_demand_sum(self):
        c = self._conn.cursor()
        c.execute("""
                SELECT SUM(demand) FROM clinics
            """, )
        return c.fetchone()


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""
            INSERT INTO logistics (logistic_id, logistic_name, count_sent, count_received) VALUES (?, ?, ?, ?)
        """, [logistic.logistic_id, logistic.logistic_name, logistic.count_sent, logistic.count_received])

    def find(self, logistic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM logistics WHERE logistic_id = ?
        """, [logistic_id])
        return Logistic(*c.fetchone())

    def increase_count_received(self, logistic_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE logistics SET count_received = count_received+(?) WHERE logistic_id=(?)
            """, [amount, logistic_id])

    def increase_count_sent(self, logistic_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE logistics SET count_sent = count_sent+(?) WHERE logistic_id=(?)
            """, [amount, logistic_id])

    def get_received_sent_sum(self):
            c = self._conn.cursor()
            c.execute("""
                SELECT SUM(count_received), SUM(count_sent) FROM logistics
            """, )
            return c.fetchone()
