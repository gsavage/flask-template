from app import create_app


def test_a0_01():
    """Ensure home page is rendered"""
    app = create_app({"TESTING": True})
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Flask Template</h1>" in response.data
