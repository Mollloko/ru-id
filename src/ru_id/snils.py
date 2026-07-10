from ru_id._utils import check_length, digits_only
from ru_id.exceptions import ValidationError

_SNILS_CHECKSUM_THRESHOLD = 1_001_998


def is_valid_snils(value: str) -> bool:
    try:
        validate_snils(value)
    except ValidationError:
        return False
    return True


def validate_snils(value: str) -> str:
    """Проверить СНИЛС в формате XXX-XXX-XXX YY или только цифры."""
    digits = digits_only(value, field="snils")
    check_length(digits, (11,), field="snils")

    number = int(digits[:9])
    check_digit = int(digits[9:])

    if number <= _SNILS_CHECKSUM_THRESHOLD:
        return digits

    total = 0
    for index, ch in enumerate(reversed(digits[:9]), start=1):
        total += int(ch) * (index % 10 or 10)

    if total < 100:
        expected = total
    elif total in (100, 101):
        expected = 0
    else:
        expected = total % 101
        if expected == 100:
            expected = 0

    if check_digit != expected:
        raise ValidationError("snils: неверная контрольная сумма", field="snils")

    return digits
