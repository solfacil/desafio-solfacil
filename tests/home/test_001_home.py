from fastapi.testclient import TestClient

from src.app.main import __version__, app

client = TestClient(app)


class TestHome:

    @classmethod
    def setup_class(cls):
        ...

    @classmethod
    def teardown_class(cls):
        ...

    def setup_method(self):
        ...

    def teardown_method(self):
        ...

    def test_home(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {'status': "running", "version": __version__}
