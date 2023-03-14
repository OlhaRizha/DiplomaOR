import sqlite3


class Database:
    """
    A class to interact with a SQLite database
    """

    def __init__(self):
        """
        Creates a connection to the database and a cursor
        """
        self.connection = sqlite3.connect('c://Users//Lenovo//DiplomaOR'+r'//become_qa_auto.db')
        self.cursor = self.connection.cursor()


    def test_connection(self):
        """
        Sends a SELECT query to the database to get its version 
        and prints the result
        """
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()

        print(f"Connected successfully SQLite Database Version is: {record}")


    def get_all_users(self):
        """
        Sends a SELECT query to the database to get all the users 
        in the customers table and returns the result
        """
        query = "SELECT name,address,city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    def get_user_address_by_name(self, name):
        """
        Sends a SELECT query to the database to get the address of a user 
        with a given name and returns the result
        """
        query=f"SELECT address, city, postalCode, country \
            FROM customers WHERE name='{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def update_product_qnt_by_id(self, product_id, qnt):
        """
        Sends an UPDATE query to the database to update 
        the quantity of a product with a given id
        """
        query = f"UPDATE products SET quantity={qnt} WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def select_product_qnt_by_id(self,product_id):
        """
        Sends a SELECT query to the database to get the quantity 
        of a product with a given id and returns the result
        """
        query = f"SELECT quantity FROM products WHERE id={product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def insert_product(self, product_id, name, description, qnt):
        """
        Sends an INSERT OR REPLACE INTO query to the database 
        to create or replace a product
        """
        query = f"INSERT OR REPLACE INTO products (id,name,description,quantity) VALUES ({product_id},'{name}','{description}',{qnt})"
        self.cursor.execute(query)
        self.connection.commit()


    def delete_product_by_id(self, product_id):
        """
        Sends a DELETE query to the database 
        to delete a product with a given id
        """
        query = f"DELETE FROM products WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def get_detailed_orders(self):
        """
        Sends a SELECT-FROM-JOIN query to the database to get 
        a detailed list of orders, customers, products and returns the result
        """
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
        FROM orders \
        JOIN customers ON orders.customer_id=customers.id\
        JOIN products ON orders.product_id=products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record







