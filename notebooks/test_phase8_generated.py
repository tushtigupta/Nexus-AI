
import os
import sys
import pytest
from pathlib import Path

# Load Requests from the extracted project repository.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_PACKAGE = (
    PROJECT_ROOT
    / "data"
    / "raw_repositories"
    / "requests"
    / "src"
    / "requests"
    / "__init__.py"
)

REQUESTS_SRC = EXPECTED_PACKAGE.parent.parent
sys.path.insert(0, str(REQUESTS_SRC))

# Clear previously imported Requests modules.
for module_name in list(sys.modules):
    if module_name == "requests" or module_name.startswith("requests."):
        del sys.modules[module_name]

import requests
from requests import PreparedRequest
from requests.adapters import _urllib3_request_context

assert Path(requests.__file__).resolve() == EXPECTED_PACKAGE.resolve(), (
    f"Wrong Requests package imported: {requests.__file__}"
)


class DummyPoolManager:
    pass


def make_request(url="https://example.com/path"):
    request = PreparedRequest()
    request.prepare(method="GET", url=url)
    return request


def test_verify_false_disables_certificate_verification():
    request = make_request()

    host_params, pool_kwargs = _urllib3_request_context(
        request, False, None, DummyPoolManager()
    )

    assert pool_kwargs["cert_reqs"] == "CERT_NONE"
    assert "ca_certs" not in pool_kwargs
    assert "ca_cert_dir" not in pool_kwargs


def test_verify_string_file_path():
    request = make_request()
    ca_file = os.path.join(os.getcwd(), "ca-test-file.pem")

    host_params, pool_kwargs = _urllib3_request_context(
        request, ca_file, None, DummyPoolManager()
    )

    assert pool_kwargs["ca_certs"] == ca_file
    assert pool_kwargs["cert_reqs"] == "CERT_REQUIRED"


def test_verify_string_directory_path(tmp_path):
    request = make_request()
    ca_dir = str(tmp_path)

    host_params, pool_kwargs = _urllib3_request_context(
        request, ca_dir, None, DummyPoolManager()
    )

    assert pool_kwargs["ca_cert_dir"] == ca_dir
    assert "ca_certs" not in pool_kwargs


def test_client_cert_tuple():
    request = make_request()
    client_cert = ("client.crt", "private.key")

    host_params, pool_kwargs = _urllib3_request_context(
        request, True, client_cert, DummyPoolManager()
    )

    assert pool_kwargs["cert_file"] == "client.crt"
    assert pool_kwargs["key_file"] == "private.key"


def test_client_cert_string():
    request = make_request()
    client_cert = "client.crt"

    host_params, pool_kwargs = _urllib3_request_context(
        request, True, client_cert, DummyPoolManager()
    )

    assert pool_kwargs["cert_file"] == "client.crt"
    assert "key_file" not in pool_kwargs


def test_host_parameters_are_parsed_correctly():
    request = make_request("https://example.com:8443/path")

    host_params, pool_kwargs = _urllib3_request_context(
        request, True, None, DummyPoolManager()
    )

    assert host_params == {
        "scheme": "https",
        "host": "example.com",
        "port": 8443,
    }
