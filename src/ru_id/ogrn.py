from ru_id._utils import check_length, digits_only
from ru_id.exceptions import ValidationError


def is_valid_ogrn(value: str) -> bool:
    try:
        validate_ogrn(value)
    except ValidationError:
        return False
    return True


def validate_ogrn(value: str) -> str:
    """Проверить ОГРН (13 цифр) или ОГРНИП (15 цифр)."""
    digits = digits_only(value, field="ogrn")
    check_length(digits, (13, 15), field="ogrn")

    if len(digits) == 13:
        body = int(digits[:12])
        expected = body % 11 % 10
        if expected != int(digits[12]):
            raise ValidationError("ogrn: неверная контрольная цифра", field="ogrn")
    else:
        body = int(digits[:14])
        expected = body % 13 % 10
        if expected != int(digits[14]):
            raise ValidationError("ogrn: неверная контрольная цифра ОГРНИП", field="ogrn")

    return digits
