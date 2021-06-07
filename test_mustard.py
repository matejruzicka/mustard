import pytest

from api import API


@pytest.fixture
def api():
    return API()


def test_basic_route(api):
    @api.route("/home")
    def home(req):
        return "YOLO"


def test_route_overlap_throws_exception(api):
    @api.route("/home")
    def home(req):
        return "YOLO"

    with pytest.raises(AssertionError):
        @api.route("/home")
        def home2(req):
            return "YOLO"
