import pytest
from modules.common.database import Database

#Створення теста з міткою database, що створює екземпляр класу DataBase db та перевіряє чи відбулось з'єднання з БД
@pytest.mark.database
def test_database_connection():
    db=Database()
    db.test_connection()

#Створення теста з міткою database, що створює екземпляр класу DataBase db, 
#перевіряє можливість отримання певних даних з БД та виводить результат на екран
@pytest.mark.database
def test_check_all_users():
    db=Database()
    users=db.get_all_users()

    print(users)    

#Створення теста з міткою database, що створює екземпляр класу DataBase db, 
#перевіряє можливість отримання певної інформації за певним критерієм в БД
# та перевіряє чи результат такий як очікується
@pytest.mark.database
def test_check_user_sergii():
    db=Database()
    user=db.get_user_address_by_name('Sergii')

    assert user[0][0]=='Maydan Nezalezhnosti 1'
    assert user[0][1]=='Kyiv'
    assert user[0][2]=='3127'
    assert user[0][3]=='Ukraine'

#Створення теста з міткою database, що створює екземпляр класу DataBase db, 
#перевіряє можливість зміни певної інформації за певним критерієм в БД, 
#перевіряє що зміни відбулись та чи результат такий як очікується
@pytest.mark.database
def test_product_qnt_update():
    db=Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt=db.select_product_qnt_by_id(1)

    assert water_qnt[0][0]==25

#Створення теста з міткою database, що створює екземпляр класу DataBase db, 
#перевіряє можливість створення або заміни певної інформації за певним критерієм в БД, 
#перевіряє що зміни відбулись та чи результат такий як очікується
@pytest.mark.database
def test_product_insert():
    db=Database()
    db.insert_product(4,'печиво','солодке',30)
    water_qnt=db.select_product_qnt_by_id(4)

    assert water_qnt[0][0]==30

#Створення теста з міткою database, що створює екземпляр класу DataBase db, 
#перевіряє можливість видалення певної інформації за певним критерієм в БД, 
#перевіряє що зміни відбулись та чи результат такий як очікується
@pytest.mark.database
def test_product_delete():
    db=Database()
    db.insert_product(99,'тестові','дані',999)
    db.delete_product_by_id(99)
    qnt=db.select_product_qnt_by_id(99)

    assert len(qnt)==0

#Створення теста з міткою database, що створює екземпляр класу DataBase db, 
#перевіряє можливість обєднання певної інформації за певним критерієм в БД в одну таблицю, 
#перевіряє що зміни відбулись та чи результат такий як очікується
@pytest.mark.database
def test_detailed_orders():
    db=Database()
    orders=db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders)==1

    assert orders[0][0]==1
    assert orders[0][1]=='Sergii'
    assert orders[0][2]=='солодка вода'
    assert orders[0][3]=='з цукром'




