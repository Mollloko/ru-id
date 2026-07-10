# ru-id

Валидация российских идентификаторов с проверкой контрольных сумм.

## Установка

```bash
pip install ru-id
```

## Быстрый старт

```python
from ru_id import validate_inn, validate_snils, is_valid_inn, ValidationError

# Проверка + очистка ввода (убирает пробелы и дефисы)
inn = validate_inn("7707 083 893")      # → "7707083893"
snils = validate_snils("112-233-445 95")  # → "11223344595"

# Быстрая проверка без исключений
if is_valid_inn("7707083893"):
    print("ИНН корректен")

# Понятная ошибка при неверных данных
try:
    validate_inn("7707083890")
except ValidationError as error:
    print(error)  # inn: неверная контрольная сумма
```

## API

| Функция | Что проверяет |
|---------|---------------|
| `validate_inn()` | ИНН юрлица (10 цифр) или физлица/ИП (12 цифр) |
| `validate_snils()` | СНИЛС |
| `validate_ogrn()` | ОГРН (13 цифр) и ОГРНИП (15 цифр) |
| `validate_kpp()` | КПП (9 цифр) |
| `validate_bik()` | БИК банка (9 цифр) |
| `validate_account(account, bik)` | Расчётный или корреспондентский счёт |

Для каждого идентификатора есть две функции:

- `validate_*()` — возвращает очищенную строку из цифр или выбрасывает `ValidationError`
- `is_valid_*()` — возвращает `True` / `False`

## Пример: проверка формы

```python
from ru_id import ValidationError, validate_inn, validate_kpp, validate_ogrn, validate_bik, validate_account

def validate_company_form(data: dict[str, str]) -> list[str]:
    checks = [
        ("ИНН", lambda: validate_inn(data["inn"])),
        ("КПП", lambda: validate_kpp(data["kpp"])),
        ("ОГРН", lambda: validate_ogrn(data["ogrn"])),
        ("БИК", lambda: validate_bik(data["bik"])),
        ("Счёт", lambda: validate_account(data["account"], data["bik"])),
    ]

    errors = []
    for label, check in checks:
        try:
            check()
        except ValidationError as error:
            errors.append(f"{label}: {error}")
    return errors
```


## Лицензия

MIT
