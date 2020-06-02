import base64
import pathlib
import tempfile

from django.contrib.auth.models import AnonymousUser
from django.core.files import File
from django.core.files.base import ContentFile
from django.urls import reverse

import pytest

from config.schema import schema as default_schema
from faker import config
from pytest_factoryboy import register
from requests_mock import MockerCore

config.DEFAULT_LOCALE = "pl_PL"
register(UserFactory)


@pytest.fixture(scope="session")
def faker_locale():
    return "pl_PL"


@pytest.fixture(scope="session")
def setup_view():
    """Returns function able to setup Django's view.

    Mimic as_view() returned callable, but returns view instance.
    args and kwargs are the same you would pass to ``reverse()``

    Examples
    ========
    `setup_view` should be used as normal pytest's fixture::

        def test_hello_view(setup_view):
            name = 'django'
            request = RequestFactory().get('/fake-path')
            view = HelloView(template_name='hello.html')
            view = setup_view(view, request, name=name)

            # Example test ugly dispatch():
            response = view.dispatch(view.request, *view.args, **view.kwargs)
    """

    def _inner_setup_view(view, request, *args, **kwargs):
        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    return _inner_setup_view


@pytest.yield_fixture(scope="session")
def requests_mock():
    mock = MockerCore()
    mock.start()
    yield mock
    mock.stop()


@pytest.fixture
def user_instance(user_factory):
    return user_factory.build()


@pytest.fixture
def admin_user_instance(user_factory):
    return user_factory.build(is_staff=True, is_superuser=True)
