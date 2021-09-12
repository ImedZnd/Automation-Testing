import pytest


def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Gmail.com"

    print("Beginning")
    assert expected_title == actual_title, "Titles Not Matches"
    assert "Google" in actual_title
    assert False, "force failing the test"
    print("Ending")
