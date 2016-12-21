import pytest
from pyramid import testing

@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request

@pytest.fixture
def testapp():
    """Fixture to test."""
    from webtest import TestApp 
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)

def test_home_page_has_list(testapp):
    """Test."""
    response = testapp.get("/", status=200)
    inner_html = response.html



def test_list_route_for_home_page_renders_file_data(req):
    """My list view returns html data."""
    from .views import list
    response = list(req)
    assert "<!DOCTYPE html>" in response

# class ViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()

#     def tearDown(self):
#         testing.tearDown()

#     def test_my_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'learning_journal_basic')


# class FunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from learning_journal_basic import main
#         app = main({})
#         from webtest import TestApp
#         self.testapp = TestApp(app)

#     def test_root(self):
#         res = self.testapp.get('/', status=200)
#         self.assertTrue(b'Pyramid' in res.body)
