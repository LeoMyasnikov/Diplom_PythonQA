import pytest


class Assertions:
    @staticmethod
    def assert_status_code(response, expected_status_code):
        actual_status_code = response.status_code
        if actual_status_code != expected_status_code:
            pytest.fail(f"Status code mismatch: Expected {expected_status_code}, but got {actual_status_code}")

    @staticmethod
    def assert_response_key_exists(response, key):
        try:
            response_json = response.json()
            if key not in response_json:
                pytest.fail(f"Key '{key}' not found in response")
        except ValueError:
            pytest.fail("Response is not in JSON format")

    @staticmethod
    def assert_response_value(response, key, expected_value):
        try:
            response_json = response.json()
            actual_value = response_json.get(key)
            if actual_value != expected_value:
                pytest.fail(f"Value mismatch for key '{key}': Expected {expected_value}, but got {actual_value}")
        except ValueError:
            pytest.fail("Response is not in JSON format")