import app

def test_calculate_current_age():
    """
    GIVEN a user enters the year they were born WHEN that 
    year is passed to this function then the user age is depicted
    """
assert app.calculate_current_age(2000) == 22 ##will chaange


def test_calculate_future_age():
    """
    GIVEN a user age WHEN that age 
    is passed to this function then 10 years are added to age
    """
assert app.calculate_future_age(20) == 30 ##will chaange

def test_calculate_past_age():
    """
    GIVEN a user age WHEN that age is passed to this function then 
    10 years are subtracted from users age
    """
assert app.calculate_past_age(20) == 10 ##will chaange