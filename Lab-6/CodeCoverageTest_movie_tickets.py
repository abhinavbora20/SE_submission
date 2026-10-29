import pytest

from movie_tickets import ticket_price, group_discount, snack_combo


def test_ticket_prices_for_all_seats():
    assert ticket_price("regular", 25, 15, False) == 150
    assert ticket_price("premium", 25, 15, False) == 250
    assert ticket_price("recliner", 25, 15, False) == 400


def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_show_time(hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, hour, False)


def test_morning_price():
    assert ticket_price("regular", 25, 11, False) == 100


def test_evening_price():
    assert ticket_price("regular", 25, 18, False) == 180


def test_weekend_price():
    assert ticket_price("regular", 25, 15, True) == 190


def test_child_under_three():
    assert ticket_price("premium", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_senior_discount():
    assert ticket_price("recliner", 60, 15, False) == 200


def test_invalid_ticket_count():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_group_discount_tiers():
    assert group_discount(2, False) == 0
    assert group_discount(5, False) == 10
    assert group_discount(10, False) == 15


def test_student_group_discount():
    assert group_discount(5, True) == 15
    assert group_discount(10, True) == 20


def test_snack_prices():
    assert snack_combo("small", False) == 120
    assert snack_combo("medium", False) == 180
    assert snack_combo("large", False) == 250


def test_snack_coupon():
    assert snack_combo("small", True) == 70
    assert snack_combo("medium", True) == 130
    assert snack_combo("large", True) == 200
