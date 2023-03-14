import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    """
    Test that creates an instance of the Database class and checks if a connection to the database has been established.
    """
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    """Test that creates an instance of the DataBase class 'db',
    checks the possibility of getting specific data from the database,
    and outputs the result to the screen.
    """
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    """Test that creates an instance of the DataBase class 'db',
    checks the possibility of getting specific information for a specific user from the database, 
    and verifies whether the result is as expected.
    """
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    """Test that creates an instance of the DataBase class 'db',
    checks the possibility of updating specific information for a specific product in the database,
    and verifies that the changes have occurred and the result is as expected.
    """
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    """Test that creates an instance of the DataBase class 'db',
    checks the possibility of inserting specific information for a specific product in the database,
    and verifies that the changes have occurred and the result is as expected.
    """
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    """Test that creates an instance of the DataBase class 'db',
    checks the possibility of deleting specific information for a specific product in the database,
    and verifies that the changes have occurred and the result is as expected.
    """
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    """Test that creates an instance of the DataBase class 'db',
    checks the possibility of merging specific information for specific orders in the database into one table,
    and verifies that the changes have occurred and the result is as expected.
    """
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
