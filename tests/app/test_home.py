from app import create_app

from lib.calc import Calc


def test_a0_01():
    """Ensure home page is rendered"""
    app = create_app({"TESTING": True})
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Flask Template</h1>" in response.data

def test_a0_02():
    """Returns price * count"""
    c = Calc()

    total = c.calc(2, 3, "UT")

    assert total[0] == 5.87675 # First item is the result
    assert total[1] == 2 # Next is the number of items
    assert total[2] == 3 # Next is the price per item
    assert total[3] == "UT" # Finally, here is the state code

def test_a0_03():
    """Returns price * count"""
    c = Calc()

    total = c.calc(2, 3, "CA")

    assert total[0] == 5.95375 # First item is the result
    assert total[1] == 2 # Next is the number of items
    assert total[2] == 3 # Next is the price per item
    assert total[3] == "CA" # Finally, here is the state code

def test_a0_04():
    """Returns price * count"""
    c = Calc()

    total = c.calc(20000, 3, "CA")

    assert total[0] == 55207.5 # First item is the result
    assert total[1] == 20000 # Next is the number of items
    assert total[2] == 3 # Next is the price per item
    assert total[3] == "CA" # Finally, here is the state code
