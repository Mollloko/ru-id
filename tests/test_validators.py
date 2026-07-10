import pytest

from ru_id import (
    ValidationError,
    is_valid_inn,
    is_valid_snils,
    is_valid_ogrn,
    is_valid_kpp,
    is_valid_bik,
    is_valid_account,
    validate_inn,
    validate_snils,
    validate_ogrn,
    validate_kpp,
    validate_bik,
    validate_account,
)


class TestInn:
    def test_valid_inn_10(self):
        assert validate_inn("7707083893") == "7707083893"
        assert is_valid_inn("7707083893")

    def test_valid_inn_12(self):
        assert validate_inn("500100732259") == "500100732259"

    def test_inn_with_spaces(self):
        assert validate_inn("7707 083 893") == "7707083893"

    def test_invalid_inn_checksum(self):
        with pytest.raises(ValidationError, match="контрольная"):
            validate_inn("7707083890")

    def test_invalid_inn_length(self):
        with pytest.raises(ValidationError, match="ожидается"):
            validate_inn("12345")


class TestSnils:
    def test_valid_snils(self):
        assert validate_snils("112-233-445 95") == "11223344595"
        assert is_valid_snils("11223344595")

    def test_snils_low_number_skips_checksum(self):
        assert validate_snils("000-000-001 00") == "00000000100"

    def test_invalid_snils_checksum(self):
        with pytest.raises(ValidationError, match="контрольная"):
            validate_snils("112-233-445 00")


class TestOgrn:
    def test_valid_ogrn(self):
        assert validate_ogrn("1027700132195") == "1027700132195"

    def test_valid_ogrnip(self):
        assert validate_ogrn("304500116000157") == "304500116000157"

    def test_invalid_ogrn(self):
        with pytest.raises(ValidationError, match="контрольная"):
            validate_ogrn("1027700132190")


class TestKpp:
    def test_valid_kpp(self):
        assert validate_kpp("773601001") == "773601001"

    def test_invalid_kpp_zeros(self):
        with pytest.raises(ValidationError):
            validate_kpp("000000000")


class TestBik:
    def test_valid_bik(self):
        assert validate_bik("044525225") == "044525225"

    def test_invalid_bik_prefix(self):
        with pytest.raises(ValidationError, match="04"):
            validate_bik("123456789")


class TestAccount:
    def test_valid_settlement_account(self):
        assert validate_account("40702810000000000007", "044525225") == "40702810000000000007"

    def test_valid_correspondent_account(self):
        assert validate_account("30101810400000000003", "044525225") == "30101810400000000003"

    def test_invalid_account(self):
        assert not is_valid_account("40702810000000000008", "044525225")
