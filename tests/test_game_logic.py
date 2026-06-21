from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high_outcome():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_high_says_lower():
    # When guess > secret, hint must tell the player to go LOWER
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_guess_too_low_outcome():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_too_low_says_higher():
    # When guess < secret, hint must tell the player to go HIGHER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_one_below_secret_says_higher():
    _, message = check_guess(49, 50)
    assert "HIGHER" in message


def test_one_above_secret_says_lower():
    _, message = check_guess(51, 50)
    assert "LOWER" in message
