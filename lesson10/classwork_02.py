from classwork_01 import check_string

if __name__ == "__main__":
    test_phones = []
    assert check_string("+375 (33) 667-14-11") is None
    assert check_string("+375 29 667-14-11 ") is None
    assert check_string("375334451611") is None
    assert check_string("432-23-232-22-32") is None
