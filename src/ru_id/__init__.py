"""Валидация российских идентификаторов: ИНН, СНИЛС, ОГРН, КПП, БИК, расчётный счёт."""

from ru_id.account import is_valid_account, validate_account
from ru_id.bik import is_valid_bik, validate_bik
from ru_id.exceptions import ValidationError
from ru_id.inn import is_valid_inn, validate_inn
from ru_id.kpp import is_valid_kpp, validate_kpp
from ru_id.ogrn import is_valid_ogrn, validate_ogrn
from ru_id.snils import is_valid_snils, validate_snils

__version__ = "0.1.0"

__all__ = [
    "ValidationError",
    "__version__",
    "is_valid_account",
    "is_valid_bik",
    "is_valid_inn",
    "is_valid_kpp",
    "is_valid_ogrn",
    "is_valid_snils",
    "validate_account",
    "validate_bik",
    "validate_inn",
    "validate_kpp",
    "validate_ogrn",
    "validate_snils",
]
