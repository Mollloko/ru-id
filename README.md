# ru-id

Валидация российских идентификаторов с проверкой контрольных сумм.

## Что делает библиотека

`ru-id` проверяет корректность российских реквизитов и документов:

| Функция | Что проверяет |
|---------|---------------|
| `validate_inn()` | ИНН юрлица (10 цифр) и физлица/ИП (12 цифр) |
| `validate_snils()` | СНИЛС (страховой номер) |
| `validate_ogrn()` | ОГРН (13 цифр) и ОГРНИП (15 цифр) |
| `validate_kpp()` | КПП (9 цифр) |
| `validate_bik()` | БИК банка (9 цифр) |
| `validate_account()` | Расчётный/корреспондентский счёт вместе с БИК |

Две формы API:

- `validate_*()` — возвращает очищенную строку из цифр или выбрасывает `ValidationError`
- `is_valid_*()` — возвращает `True` / `False`

## Установка

```bash
pip install ru-id
```

## Использование

```python
from ru_id import validate_inn, validate_snils, is_valid_inn, ValidationError

# Вернёт строку только из цифр
inn = validate_inn("7707 083 893")  # "7707083893"

# Быстрая проверка
if is_valid_inn("7707083893"):
    print("ИНН корректен")

# СНИЛС с дефисами и пробелом тоже принимается
snils = validate_snils("112-233-445 95")

# Ошибка с понятным текстом
try:
    validate_inn("1234567890")
except ValidationError as error:
    print(error)  # inn: неверная контрольная сумма
```

## Разработка

```bash
git clone https://github.com/YOUR_USERNAME/ru-id.git
cd ru-id
pip install -e ".[dev]"
pytest
```

## Публикация на GitHub

### 1. Создай репозиторий

1. Зайди на [github.com/new](https://github.com/new)
2. Имя: `ru-id`
3. Описание: `Валидация российских идентификаторов (ИНН, СНИЛС, ОГРН...)`
4. Публичный репозиторий, без README (он уже есть локально)

### 2. Залей код

```bash
cd C:\Users\Матвей\Desktop\library
git init
git add .
git commit -m "Initial release: ru-id validators"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ru-id.git
git push -u origin main
```

Замени `YOUR_USERNAME` на свой логин GitHub.

### 3. Обнови ссылки

В `pyproject.toml` замени `YOUR_USERNAME` на свой логин в секции `[project.urls]`.

## Публикация на PyPI

### 1. Аккаунты

- [pypi.org](https://pypi.org/account/register/) — основной PyPI
- [test.pypi.org](https://test.pypi.org/account/register/) — тестовый PyPI (сначала проверь здесь)

### 2. API-токен

1. Зайди в Account Settings → API tokens
2. Create token → scope: Entire account (или только проект `ru-id`)
3. Сохрани токен — он показывается один раз

### 3. Сборка пакета

```bash
pip install build twine
python -m build
```

Появится папка `dist/` с файлами `.tar.gz` и `.whl`.

### 4. Загрузка на TestPyPI (рекомендуется сначала)

```bash
python -m twine upload --repository testpypi dist/*
```

Логин: `__token__`  
Пароль: твой API-токен TestPyPI

Проверка установки:

```bash
pip install -i https://test.pypi.org/simple/ ru-id
```

### 5. Загрузка на основной PyPI

```bash
python -m twine upload dist/*
```

Логин: `__token__`  
Пароль: API-токен PyPI

После этого любой сможет установить:

```bash
pip install ru-id
```

### 6. Обновление версии

При каждом релизе:

1. Подними версию в `pyproject.toml` и `src/ru_id/__init__.py`
2. Запусти тесты: `pytest`
3. Собери и загрузи заново:

```bash
python -m build
python -m twine upload dist/*
```

Удаляй старые файлы из `dist/` перед новой сборкой или используй `--skip-existing`.

## Лицензия

MIT
