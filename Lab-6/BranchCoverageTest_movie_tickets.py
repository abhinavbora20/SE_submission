import pytest

from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price: valid and invalid seats
def test_all_seat_types():
    assert ticket_price("regular", 25, 15, False) == 150
    assert ticket_price("premium", 25, 15, False) == 250
    assert ticket_price("recliner", 25, 15, False) == 400


def test_unknown_seat():
    with pytest.raises(ValueError):
        ticket_price("balcony", 25, 15, False)


# Ticket price: both invalid-time branches
@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_hours(hour):
    with pytest.raises(ValueError):
        ticket_price("regular", 25, hour, False)


# Ticket price: time branches
def test_morning():
    assert ticket_price("regular", 25, 11, False) == 100


def test_midday():
    assert ticket_price("regular", 25, 12, False) == 150


def test_evening():
    assert ticket_price("regular", 25, 18, False) == 180


def test_weekend():
    assert ticket_price("regular", 25, 15, True) == 190


# Ticket price: age branches
def test_free_child():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_adult_full_price():
    assert ticket_price("regular", 25, 15, False) == 150


def test_senior_discount():
    assert ticket_price("recliner", 60, 15, False) == 200


# Group discount: invalid count and all discount tiers
@pytest.mark.parametrize("tickets", [0, -1])
def test_invalid_ticket_counts(tickets):
    with pytest.raises(ValueError):
        group_discount(tickets, False)


def test_group_discount_tiers():
    assert group_discount(2, False) == 0
    assert group_discount(5, False) == 10
    assert group_discount(10, False) == 15


def test_student_discount_branches():
    assert group_discount(2, True) == 0
    assert group_discount(5, True) == 15
    assert group_discount(10, True) == 20


# Snack combo: each size and coupon outcome
@pytest.mark.parametrize(
    "size,expected",
    [("small", 120), ("medium", 180), ("large", 250), ("other", 250)],
)
def test_snack_sizes_without_coupon(size, expected):
    assert snack_combo(size, False) == expected


@pytest.mark.parametrize(
    "size,expected",
    [("small", 70), ("medium", 130), ("large", 200)],
)
def test_snack_sizes_with_coupon(size, expected):
    assert snack_combo(size, True) == expected
