import sqlite3

#Створення класу DataBase
class Database:

#Створення конструктора класу, що забезпечить зв'язок з Базою Даних та виконання потрібних команд у ній
    def __init__(self):
        self.connection=sqlite3.connect('c://Users//Lenovo//DiplomaOR'+r'//become_qa_auto.db')
        self.cursor=self.connection.cursor()

#Створення методу об'єкту класу DataBase, що відправляє запит SELECT до БД про її версію та повертає результат
#а також виводить на друк інформацію про успішний конект з БД
    def test_connection(self):
        sqlite_select_Query="SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record=self.cursor.fetchall()

        print(f"Connected successfully SQLite Database Version is: {record}")

#Створення методу об'єкту класу DataBase, що відправляє запит SELECT до БД 
# про надання певної інформації з таблиці customers та повертає результат
    def get_all_users(self):
        query="SELECT name,address,city FROM customers"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record

#Створення методу об'єкту класу DataBase, що відправляє запит SELECT з критерієм WHERE до БД 
# про надання певної інформації з таблиці customers та повертає результат
    def get_user_address_by_name(self,name):
        query=f"SELECT address,city,postalCode,country \
            FROM customers WHERE name='{name}'"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record

#Створення методу об'єкту класу DataBase, що відправляє запит UPDATE з критерієм WHERE до БД 
# про зміну певної інформації в таблиці products та повертає результат
    def update_product_qnt_by_id(self,product_id,qnt):
        query=f"UPDATE products SET quantity={qnt} WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

#Створення методу об'єкту класу DataBase, що відправляє запит SELECT з критерієм WHERE до БД 
# про надання певної інформації з таблиці products та повертає результат
#(перевіряє виконання методу update_product_qnt_by_id)
    def select_product_qnt_by_id(self,product_id):
        query=f"SELECT quantity FROM products WHERE id={product_id}"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record

#Створення методу об'єкту класу DataBase, що відправляє запит INSERT OR REPLACE INTO до БД 
# про створення або заміни певної інформації з таблиці products 
    def insert_product(self,product_id,name,description,qnt):
        query=f"INSERT OR REPLACE INTO products (id,name,description,quantity) VALUES ({product_id},'{name}','{description}',{qnt})"
        self.cursor.execute(query)
        self.connection.commit()

#Створення методу об'єкту класу DataBase, що відправляє запит DELETE з критерієм WHERE до БД 
# про видалення певної інформації з таблиці products
    def delete_product_by_id(self,product_id):
        query=f"DELETE FROM products WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

#Створення методу об'єкту класу DataBase, що відправляє запит SELECT-FROM-JOIN до БД 
# про об'єднання певної інформації з таблиць orders, customers, products та повертає результат
    def get_detailed_orders(self):
        query="SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
        FROM orders \
        JOIN customers ON orders.customer_id=customers.id\
        JOIN products ON orders.product_id=products.id"
        self.cursor.execute(query)
        record=self.cursor.fetchall()
        return record







