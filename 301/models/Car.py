from PyQt6.QtWidgets import QMessageBox
from datetime import datetime


class Car:
    def __init__(self,data):
        self.id = data['id'].decode('utf-8')
        self.year = data['year'].decode('utf-8')
        self.make = data['make'].decode('utf-8')
        self.model = data['model'].decode('utf-8')
        self.country = data['country'].decode('utf-8')
        self.price = data['price'].decode('utf-8')
        self.created_at = data['created_at'].decode('utf-8')
        self.updated_at = data['updated_at'].decode('utf-8')

    def get_id(self):
        return self.id

    def display_list_data(self):
        return f'{self.year} {self.model} - ${self.price} |{self.id}'

    def display_full_data(self):
        return f"""
    YEAR: {self.year}
    MAKE: {self.make}
    MODEL: {self.model}
    COUNTRY: {self.country}
    Price: ${self.price}
    Car ID: {self.id}
    Created: {self.created_at[:10]}
    Last Update: ${self.updated_at[:10]}
    """

    @classmethod
    def create_car(cls,db,form_data):
        query = """
        INSERT INTO cars(year,make,model,country,price)
        VALUES('%s','%s','%s','%s','%s');
        """ % (
            ''.join(str(form_data['year'])),
            ''.join(form_data['make']),
            ''.join(form_data['model']),
            ''.join(form_data['country']),
            ''.join(str(form_data['price']))
        )
        db.query(query)

    @classmethod
    def get_all_cars(cls,db):
        query = "SELECT * FROM cars;"
        db.query(query)
        results = db.store_result()
        all_cars_tuple = results.fetch_row(0,1)
        all_cars_dict = {}
        for i in range(len(all_cars_tuple)):
            this_car = cls(all_cars_tuple[i])
            all_cars_dict[i] = this_car
        return all_cars_dict

    @classmethod
    def get_car_by_id(cls,db,id):
        query = f"""
        SELECT * 
        FROM cars
        WHERE id = {id};
        """
        db.query(query)
        results = db.store_result()
        this_car = results.fetch_row(1,1)
        return cls(this_car[0])

    @classmethod
    def update_car(cls,db,form_data):
        query = f"""
        UPDATE cars
        SET year = '{form_data["year"]}',
        make = '{form_data["make"]}',
        model = '{form_data["model"]}',
        country = '{form_data["country"]}',
        price = '{form_data["price"]}'
        WHERE id = {form_data['id']}
        """
        try:
            db.query(query)
            return [True, form_data['id']]
        except Exception as e:
            return [False, e]

    @classmethod
    def delete_car(cls,db,id):
        query = f"DELETE FROM cars WHERE id = {id};"
        try:
            db.query(query)
            return [True,id]
        except Exception as e:
            return [False,e]