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
    """Calc exists"""
    c = Calc()
    total = c.calc(1, 2, "UT")
    assert total[0] == 1 # First item is the result
    assert total[1] == 1 # Next is the first input
    assert total[2] == 2 # Next is the second input
    assert total[3] == "UT" # Finally, here is the state code
