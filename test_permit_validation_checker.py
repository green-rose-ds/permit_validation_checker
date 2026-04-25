from permit_validation_checker import permit_format_check

def test_pytest():
    assert 1+1 == 2

def test_permit_number_given_unhappy():
    assert permit_format_check("") == False

def test_permit_number_is_8_characters_unhappy():
    assert permit_format_check("1234567") == False
    assert permit_format_check("123456789") == False

def test_permit_number_correct_format_unhappy():
    assert permit_format_check("ab12345c") == False

def test_permit_number_letters_are_upper_unhappy():
    assert permit_format_check("aB1234Cd") == False