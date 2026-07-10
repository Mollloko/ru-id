from ru_id._utils import check_length, digits_only
from ru_id.bik import validate_bik
from ru_id.exceptions import ValidationError

_ACCOUNT_COEFFICIENTS = (7, 1, 3)
_CORRESPONDENT_PREFIXES = ("301", "302", "303", "304", "305", "306", "307", "308", "309")


def is_valid_account(account: str, bik: str) -> bool:
    try:
        validate_account(account, bik)
    except ValidationError:
        return False
    return True


def validate_account(account: str, bik: str) -> str:
    """Проверить расчётный или корреспондентский счёт (20 цифр) вместе с БИК."""
    account_digits = digits_only(account, field="account")
    check_length(account_digits, (20,), field="account")

    bik_digits = validate_bik(bik)
    bik_suffix = bik_digits[-3:]

    if account_digits[:3] in _CORRESPONDENT_PREFIXES:
        composite = "0" + bik_suffix + account_digits
    else:
        composite = bik_suffix + account_digits

    total = 0
    for index, digit_char in enumerate(composite):
        coefficient = _ACCOUNT_COEFFICIENTS[index % 3]
        total += int(digit_char) * coefficient

    if total % 10 != 0:
        raise ValidationError(
            "account: неверная контрольная сумма для указанного БИК",
            field="account",
        )

    return account_digits
