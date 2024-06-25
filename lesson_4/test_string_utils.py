
import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""
#1 вариант

def test_capitalize():
    """POSITIVE"""
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("333")=="333"
    """NEGATIVE"""
    assert utils.capitalize("")==""
    assert utils.capitalize("  ")=="  " 
    assert utils.capitalize("12345тест") == "12345тест"

#2 вариант  
  
@pytest.mark.parametrize("input_string,expected_output",[
        ("skypro","Skypro"),
        ("hello world", "Hello world"),
        ("123", "123"),
        ("", ""),
        (" "," "),
        ("12345тест","12345тест")
    ])
def test_capitalize(input_string,expected_output):
    assert utils.capitilize(input_string) == expected_output

"""trim"""
def test_trim():
     """POSITIVE"""
     assert utils.trim(" skypro") == "skypro"
     assert utils.trim(" hello word ") == "hello word "
     assert utils.trim(" SKY ") == "SKY "
     """NEGATIVE"""
     assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_input():
    assert utils.trim(" SKY ") == " SKY"


"""contains"""

@pytest.mark.parametrize('string, symbol, result',[
    ("банан","б", True),
    (" гвоздь","д", True),
    ("мир ","р", True),
    ("диван-кровать","-", True),
    ("145","1", True),
    ("","", True),
    ("Москва", "м", False),
    ("привет", "з", False),
    ("кот", "№", False),
    ("", "з", False),
    ("12345", "h", False)
    #("hello","", False)# ошибка системы не корректно работает со строкой которая не содержит ни одного символа
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

    """delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
    ("корень", "к", "орень"),
    ("Женя", "н", "Жея"),
    ("Море", "М", "оре"),
    ("123", "1", "23"),
    ("Красная Площадь", " ", "КраснаяПлощадь"),

    ("ножик", "з", "ножик"),
    ("", "", ""),
    ("", "с", ""),
    ("кофе", "", "кофе"),
    ("зелень ", " ", "зелень")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

"""starts_with"""

@pytest.mark.parametrize('string, symbol, result',[
    
    ("светофор", "с", True),
    ("", "", True),
    ("Москва", "М", True),
    ("Film", "F", True),
    ("Мира-Зина", "М", True),
    ("123", "1", True),

    ("Ваня", "в", False),
    ("мир", "М", False),
    ("", "@", False),
    ("плащ", "ж", False),
    ("зверь", "н", False)
])    
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

"""end_with"""

@pytest.mark.parametrize('string, symbol, result',[

    ("Мария", "я", True),
    ("ТОРТИК", "К", True),
    ("", "", True),
    ("собака", "", True),
    ("67", "7", True),
    ("ONE-TWo", "o", True),
    ("Пётр1", "1", True),
    ("БаобаБ", "Б", True),

    ("природа", "л", False),
    ("тигр", "с", False),
    ("дверь", "ь", False),
    ("", "*", False)
    
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

"""is_empty"""
@pytest.mark.parametrize('string, result',[
    ("", True),
    (" ", True),
    ("  ", True),

    ("не пусто", False),
    ("не пусто с пробелом", False),
    ("345", False),

])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result    

"""list_to_string"""

@pytest.mark.parametrize('lst, joiner, result',[
    (["s","o","s"], ",", "s,o,s"),
    ([1,2,3,4,5], None, "1,2,3,4,5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
    (["в", "у", "з"], "","вуз"),

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
        assert res == result
