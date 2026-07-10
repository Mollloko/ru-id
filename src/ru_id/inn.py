from ru_id._utils import check_length, checksum, digits_only
from ru_id.exceptions import ValidationError

_INN10_COEFFICIENTS = [2, 4, 10, 3, 5, 9, 4, 6, 8]
_INN11_COEFFICIENTS = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
_INN12_COEFFICIENTS = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]


def is_valid_inn(value: str) -> bool:
    try:
        validate_inn(value)
    except ValidationError:
        return False
    return True


def validate_inn(value: str) -> str:
    """Проверить ИНН юрлица (10 цифр) или физлица/ИП (12 цифр)."""
    digits = digits_only(value, field="inn")
    check_length(digits, (10, 12), field="inn")

    numbers = [int(ch) for ch in digits]

    if len(numbers) == 10:
        if checksum(numbers[:9], _INN10_COEFFICIENTS) != numbers[9]:
            raise ValidationError("inn: неверная контрольная сумма", field="inn")
    elif checksum(numbers[:10], _INN11_COEFFICIENTS) != numbers[10]:
        raise ValidationError("inn: неверная 11-я контрольная цифра", field="inn")
    elif checksum(numbers[:11], _INN12_COEFFICIENTS) != numbers[11]:
        raise ValidationError("inn: неверная 12-я контрольная цифра", field="inn")

    return digits
