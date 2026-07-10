from ru_id._utils import check_length, digits_only
from ru_id.exceptions import ValidationError


def is_valid_kpp(value: str) -> bool:
    try:
        validate_kpp(value)
    except ValidationError:
        return False
    return True


def validate_kpp(value: str) -> str:
    """Проверить КПП (9 цифр)."""
    digits = digits_only(value, field="kpp")
    check_length(digits, (9,), field="kpp")

    if digits == "0" * 9:
        raise ValidationError("kpp: недопустимое значение", field="kpp")

    return digits
