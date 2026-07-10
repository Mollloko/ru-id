from ru_id.exceptions import ValidationError


def digits_only(value: str, *, field: str) -> str:
    cleaned = "".join(ch for ch in value if ch.isdigit())
    if not cleaned:
        raise ValidationError(f"{field}: значение не содержит цифр", field=field)
    return cleaned


def check_length(value: str, allowed: tuple[int, ...], *, field: str) -> None:
    if len(value) not in allowed:
        sizes = ", ".join(str(size) for size in allowed)
        raise ValidationError(
            f"{field}: ожидается {sizes} цифр, получено {len(value)}",
            field=field,
        )


def checksum(digits: list[int], coefficients: list[int]) -> int:
    total = sum(d * c for d, c in zip(digits, coefficients))
    return total % 11 % 10
