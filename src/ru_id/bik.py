from ru_id._utils import check_length, digits_only
from ru_id.exceptions import ValidationError


def is_valid_bik(value: str) -> bool:
    try:
        validate_bik(value)
    except ValidationError:
        return False
    return True


def validate_bik(value: str) -> str:
    """Проверить БИК банка (9 цифр, для РФ начинается с 04)."""
    digits = digits_only(value, field="bik")
    check_length(digits, (9,), field="bik")

    if not digits.startswith("04"):
        raise ValidationError("bik: БИК российского банка начинается с 04", field="bik")

    return digits
