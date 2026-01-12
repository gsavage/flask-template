from app import create_app

from lib.calc import Calc

def test_a0_02():
    """Utah tax rate"""
    c = Calc()

    total = c.calc(2, 3, "UT")

    assert total["total"] == 6.411 # First item is the result
    assert total["number_of_items"] == 2 # Next is the number of items
    assert total["price_per_item"] == 3 # Next is the price per item
    assert total["state_code"] == "UT" # Finally, here is the state code

def test_a0_03():
    """California tax rate"""
    c = Calc()

    total = c.calc(2, 3, "CA")

    assert total["total"] == 6.495 # First item is the result
    assert total["number_of_items"] == 2 # Next is the number of items
    assert total["price_per_item"] == 3 # Next is the price per item
    assert total["state_code"] == "CA" # Finally, here is the state code

def test_a0_04():
    """Large numbers get a percentage discount"""
    c = Calc()

    total = c.calc(20000, 3, "CA")

    assert total["total"] == 55207.5 # First item is the result
    assert total["number_of_items"] == 20000 # Next is the number of items
    assert total["price_per_item"] == 3 # Next is the price per item
    assert total["state_code"] == "CA" # Finally, here is the state code
