# Data Access Objects:
# All of these are meant to be singletons
from DTO import Vaccine, Logistic, Supplier, Clinic


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    # must
    def insert(self, vaccine):
        self._conn.execute("""
               INSERT INTO vaccines (id, date, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id FROM vaccines WHERE id = ?
        """, [vaccine_id])
        # return tapel
        return Vaccine(*c.fetchone())

    def get_max_id(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT MAX(id) FROM vaccines;
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
                 DELETE FROM vaccines WHERE id = ?
            """, [vaccine_id])

    def decrease_quantity(self, vaccine_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE vaccines SET quantity = quantity-(?) WHERE id=(?)
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
                INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.logistic])

    def find_by_name(self, supplier_name):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM suppliers WHERE name = ?
            """, [supplier_name])
        return c.fetchone()


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
            INSERT INTO clinics (id, location, demand, logistic) VALUES (?, ?, ?, ?)
        """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find_by_location(self, location):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM clinics WHERE location = ?
                """, [location])
        return c.fetchone()

    def decrease_demand(self, clinic_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE clinics SET demand = demand-(?) WHERE id=(?)
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
            INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)
        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def find(self, logistic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM logistics WHERE id = ?
        """, [logistic_id])
        return Logistic(*c.fetchone())

    def increase_count_received(self, logistic_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE logistics SET count_received = count_received+(?) WHERE id=(?)
            """, [amount, logistic_id])

    def increase_count_sent(self, logistic_id, amount):
        c = self._conn.cursor()
        c.execute("""
                 UPDATE logistics SET count_sent = count_sent+(?) WHERE id=(?)
            """, [amount, logistic_id])

    def get_received_sent_sum(self):
            c = self._conn.cursor()
            c.execute("""
                SELECT SUM(count_received), SUM(count_sent) FROM logistics
            """, )
            return c.fetchone()
