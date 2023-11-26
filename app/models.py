from database import queries 
import click 

   
class Customer():
    def __init__(self):
        self.table_name = 'customer' 
    def create_table(self):
        columns =   [
                        ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
                        ('name', 'VARCHAR(50)'),
                        ('mobile_no', 'VARCHAR(50)'),
                        ('address', 'VARCHAR(250)')
                    ]   
        if queries.create_table(self.table_name,columns):
            return True 
        else:
            return False 

class Vehicle():
    def __init__(self):
        self.table_name = 'vehicle' 
        
    def create_table(self):
        columns =   [
                        ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
                        ('type', 'VARCHAR(50)'),
                        ('rent_rate', 'FLOAT'),
                    ]   
        if queries.create_table(self.table_name,columns):
            return True 
        else:
            return False 
    
    
class Booking:
    def __init__(self):
        self.table_name = 'booking'
    def create_table(self):
        columns = [
            ('id', 'INT AUTO_INCREMENT PRIMARY KEY'),
            ('customer_id', 'INT'),
            ('vehicle_id', 'INT'),
            ('booking_date', 'DATETIME'),
            ('return_date','DATETIME'),
            ('payment','float')

        ]
        
        foreign_keys = '''
                        FOREIGN KEY (customer_id) REFERENCES customer(id),
                        FOREIGN KEY (vehicle_id) REFERENCES vehicle(id)
                       '''
        
        if queries.create_table(self.table_name,columns,foreign_keys):
            return True
        else:
            return False



def init_models_first_time():
    customer_instance = Customer()
    customer_instance.create_table()

    vehicle_instance = Vehicle()
    vehicle_instance.create_table()

    booking_instance = Booking()
    booking_instance.create_table()
