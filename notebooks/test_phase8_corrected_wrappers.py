
import sys
from pathlib import Path
from unittest.mock import Mock, patch


# ============================================================
# 1. PROJECT PATH CONFIGURATION
# Cross-platform: Windows + Linux (Streamlit Cloud)
# ============================================================

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

assert EXPECTED_API.is_file(), (
    f"Expected production source file not found: {EXPECTED_API}"
)


# ============================================================
# 2. IMPORT EXTRACTED PRODUCTION SOURCE
# ============================================================

REQUESTS_SRC = EXPECTED_API.parent.parent

sys.path.insert(0, str(REQUESTS_SRC))

# Clear previously cached Requests modules.
for module_name in list(sys.modules):
    if module_name == "requests" or module_name.startswith("requests."):
        del sys.modules[module_name]

import requests.api as api


# ============================================================
# 3. VERIFY CORRECT PRODUCTION MODULE
# ============================================================

ACTUAL_API = Path(api.__file__).resolve()

assert ACTUAL_API == EXPECTED_API.resolve(), (
    f"Wrong requests module imported!\n"
    f"Expected: {EXPECTED_API.resolve()}\n"
    f"Actual:   {ACTUAL_API}"
)


# ============================================================
# TEST 1: GET WRAPPER
# ============================================================

def test_get_forwards_arguments_and_returns_result():

    expected_response = Mock()

    with patch.object(
        api,
        "request",
        return_value=expected_response
    ) as mocked:

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


# ============================================================
# TEST 2: OPTIONS WRAPPER
# ============================================================

def test_options_forwards_arguments_and_returns_result():

    expected_response = Mock()

    with patch.object(
        api,
        "request",
        return_value=expected_response
    ) as mocked:

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


# ============================================================
# TEST 3: REQUEST DELEGATION TO SESSION
# ============================================================

def test_request_delegates_to_session():

    expected_response = Mock()
    session_instance = Mock()

    session_instance.__enter__ = Mock(
        return_value=session_instance
    )

    session_instance.__exit__ = Mock(
        return_value=False
    )

    session_instance.request.return_value = expected_response

    with patch.object(
        api.sessions,
        "Session",
        return_value=session_instance
    ):

        result = api.request(
            "get",
            "https://example.com",
            timeout=4
        )

    # Production code uses keyword arguments.
    session_instance.request.assert_called_once_with(
        method="get",
        url="https://example.com",
        timeout=4
    )

    assert result is expected_response
