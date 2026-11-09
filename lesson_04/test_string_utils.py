
import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# --- Тесты для capitalize ---
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123abc", "123abc"),  # числа в строке
    ("04 апреля 2023", "04 апреля 2023"),  # строка с пробелами и цифрами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  # пустая строка
    (" ", " "),  # строка с пробелом
    ("a", "A"),  # строка из одного символа
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# --- Тесты для trim ---
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" sky ", "sky "),  # удаляет только слева
    ("no_spaces", "no_spaces"),
    ("  123", "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  # пустая строка
    (" ", ""),  # строка только из пробела
    ("\t\ttext", "\t\ttext"),  # табуляция не удаляется (дефект BUG-001)
    ("\n\ntest", "\n\ntest"),  # перенос строки не удаляется (дефект BUG-001)
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# --- Тесты для contains ---
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("123", "2", True),
    ("test string", " ", True),  # поиск пробела
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),  # пустая строка
    ("test", "", False),  # поиск пустой подстроки (особенность index)
    ("abc", "abcde", False),  # искомый символ длиннее строки
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


# --- Тесты для delete_symbol ---
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
    ("123-456-789", "-", "123456789"),
    ("test", "z", "test"),  # символа нет, строка не меняется
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),  # пустая строка
    ("   ", " ", ""),  # удаление пробелов из строки пробелов
    ("abc", "", "abc"),  # удаление пустой подстроки
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
