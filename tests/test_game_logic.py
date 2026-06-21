import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess
from app import parse_guess, update_score


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


# ---------------------------------------------------------------------------
# parse_guess — decimal inputs
# ---------------------------------------------------------------------------

def test_decimal_truncates_down():
    ok, val, _ = parse_guess("3.9")
    assert ok is True
    assert val == 3  # int(float("3.9")) == 3, not 4


def test_decimal_exactly_half():
    ok, val, _ = parse_guess("50.5")
    assert ok is True
    assert val == 50


def test_decimal_close_to_boundary():
    ok, val, _ = parse_guess("99.99")
    assert ok is True
    assert val == 99


def test_decimal_negative():
    ok, val, _ = parse_guess("-1.7")
    assert ok is True
    assert val == -1  # int(float("-1.7")) == -1


# ---------------------------------------------------------------------------
# parse_guess — boundary and extreme integers
# ---------------------------------------------------------------------------

def test_parse_lower_boundary():
    ok, val, _ = parse_guess("1")
    assert ok is True and val == 1


def test_parse_upper_boundary():
    ok, val, _ = parse_guess("100")
    assert ok is True and val == 100


def test_parse_zero():
    ok, val, _ = parse_guess("0")
    assert ok is True and val == 0


def test_parse_negative_integer():
    ok, val, _ = parse_guess("-5")
    assert ok is True and val == -5


def test_parse_very_large_number():
    ok, val, _ = parse_guess("999999")
    assert ok is True and val == 999999


def test_parse_very_large_negative():
    ok, val, _ = parse_guess("-999999")
    assert ok is True and val == -999999


# ---------------------------------------------------------------------------
# parse_guess — invalid / malformed inputs
# ---------------------------------------------------------------------------

def test_parse_none_input():
    ok, val, err = parse_guess(None)
    assert ok is False
    assert val is None
    assert err is not None


def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert err is not None


def test_parse_plain_letters():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert "number" in err.lower()


def test_parse_mixed_alphanum():
    ok, val, err = parse_guess("12abc")
    assert ok is False


def test_parse_double_negative():
    # "--5" is not a valid number
    ok, val, err = parse_guess("--5")
    assert ok is False


def test_parse_whitespace_only():
    ok, val, err = parse_guess("   ")
    assert ok is False


def test_parse_scientific_notation():
    # "1e3" has no "." so it hits the int() branch and raises
    ok, val, err = parse_guess("1e3")
    assert ok is False


def test_parse_leading_trailing_spaces():
    # int(" 42 ") succeeds in Python, so parse_guess should accept it
    ok, val, _ = parse_guess(" 42 ")
    assert ok is True and val == 42


def test_parse_plus_prefix():
    # int("+10") == 10 in Python
    ok, val, _ = parse_guess("+10")
    assert ok is True and val == 10


# ---------------------------------------------------------------------------
# check_guess — boundary and extreme secrets
# ---------------------------------------------------------------------------

def test_check_guess_at_min_boundary():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"


def test_check_guess_at_max_boundary():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"


def test_check_guess_zero_secret_one():
    outcome, msg = check_guess(0, 1)
    assert outcome == "Too Low"
    assert "HIGHER" in msg


def test_check_guess_above_range():
    outcome, msg = check_guess(200, 100)
    assert outcome == "Too High"
    assert "LOWER" in msg


def test_check_guess_negative_secret_positive():
    outcome, msg = check_guess(-10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg


def test_check_guess_both_negative_equal():
    outcome, _ = check_guess(-7, -7)
    assert outcome == "Win"


def test_check_guess_both_negative_too_low():
    outcome, msg = check_guess(-20, -5)
    assert outcome == "Too Low"
    assert "HIGHER" in msg


def test_check_guess_both_negative_too_high():
    outcome, msg = check_guess(-3, -10)
    assert outcome == "Too High"
    assert "LOWER" in msg


# ---------------------------------------------------------------------------
# update_score — scoring logic and the asymmetry quirk
# ---------------------------------------------------------------------------

def test_score_win_first_attempt():
    # attempt_number=1 → points = 100 - 10*1 = 90
    score = update_score(0, "Win", 1)
    assert score == 90


def test_score_win_late_attempt_clamped_to_10():
    # attempt_number=10 → 100 - 100 = 0 → clamped to 10
    score = update_score(0, "Win", 10)
    assert score == 10


def test_score_win_floor_adds_to_existing():
    score = update_score(50, "Win", 100)
    assert score == 60  # 50 + 10 (floor)


def test_score_too_low_subtracts_5():
    score = update_score(50, "Too Low", 1)
    assert score == 45


def test_score_too_low_same_on_any_attempt():
    for attempt in range(1, 6):
        score = update_score(100, "Too Low", attempt)
        assert score == 95


def test_score_too_high_subtracts_5():
    # Fixed: "Too High" now consistently subtracts 5 regardless of attempt parity
    score = update_score(50, "Too High", 2)
    assert score == 45


def test_score_too_high_odd_attempt_subtracts_5():
    score = update_score(50, "Too High", 1)
    assert score == 45


def test_score_unknown_outcome_no_change():
    score = update_score(77, "Draw", 3)
    assert score == 77


def test_score_can_go_negative():
    score = update_score(3, "Too Low", 1)
    assert score == -2
