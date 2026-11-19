import sys
from pathlib import Path
from unittest.mock import Mock, patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_API = (
    PROJECT_ROOT
    / "data"
    / "raw_repositories"
    / "requests"
    / "src"
    / "requests"
    / "api.py"
)

REQUESTS_SRC = EXPECTED_API.parent.parent
sys.path.insert(0, str(REQUESTS_SRC))

# Ensure the extracted Requests package is imported.
for module_name in list(sys.modules):
    if module_name == "requests" or module_name.startswith("requests."):
        del sys.modules[module_name]

import requests.api as api

assert Path(api.__file__).resolve() == EXPECTED_API.resolve(), (
    f"Wrong Requests module imported: {api.__file__}"
)


def test_get_delegates_to_request():
    expected_response = Mock()

    with patch.object(
        api, "request", return_value=expected_response
    ) as mocked:
        result = api.get(
            "https://example.com",
            params={"page": 1},
            timeout=5
        )

    assert result is expected_response
    mocked.assert_called_once_with(
        "get",
        "https://example.com",
        params={"page": 1},
        timeout=5
    )


def test_options_delegates_to_request():
    expected_response = Mock()

    with patch.object(
        api, "request", return_value=expected_response
    ) as mocked:
        result = api.options(
            "https://example.com",
            timeout=5
        )

    assert result is expected_response
    mocked.assert_called_once_with(
        "options",
        "https://example.com",
        timeout=5
    )
