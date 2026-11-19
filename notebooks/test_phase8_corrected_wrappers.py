
import sys
from pathlib import Path
from unittest.mock import Mock, patch

EXPECTED_API = Path(
    r"C:\Users\Tushti Gupta\AI_Software_Engineering_Agent"
    r"\data\raw_repositories\requests\src\requests\api.py"
)

# Prioritize the extracted production source.
REQUESTS_SRC = EXPECTED_API.parent.parent
sys.path.insert(0, str(REQUESTS_SRC))

# Remove any previously cached requests modules so Python reloads
# the package from the extracted source directory.
for module_name in list(sys.modules):
    if module_name == "requests" or module_name.startswith("requests."):
        del sys.modules[module_name]

import requests.api as api


# Ensure tests run against the project's extracted production source.
assert Path(api.__file__).resolve() == EXPECTED_API.resolve(), (
    f"Wrong requests module imported: {api.__file__}"
)


def test_get_forwards_arguments_and_returns_result():
    expected_response = Mock()

    with patch.object(api, "request", return_value=expected_response) as mocked:
        result = api.get(
            "https://example.com",
            params={"page": 2},
            timeout=5
        )

    mocked.assert_called_once_with(
        "get",
        "https://example.com",
        params={"page": 2},
        timeout=5
    )
    assert result is expected_response


def test_options_forwards_arguments_and_returns_result():
    expected_response = Mock()

    with patch.object(api, "request", return_value=expected_response) as mocked:
        result = api.options(
            "https://example.com",
            timeout=3,
            headers={"X-Test": "true"}
        )

    mocked.assert_called_once_with(
        "options",
        "https://example.com",
        timeout=3,
        headers={"X-Test": "true"}
    )
    assert result is expected_response


def test_request_delegates_to_session():
    expected_response = Mock()
    session_instance = Mock()
    session_instance.__enter__ = Mock(return_value=session_instance)
    session_instance.__exit__ = Mock(return_value=False)
    session_instance.request.return_value = expected_response

    with patch.object(api.sessions, "Session", return_value=session_instance):
        result = api.request(
            "get",
            "https://example.com",
            timeout=4
        )

    session_instance.request.assert_called_once_with(
        method="get",
        url="https://example.com",
        timeout=4
    )
    assert result is expected_response
