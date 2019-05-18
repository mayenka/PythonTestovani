#test driven development - nejprve píšu test, pak funkci
import pytest
from fizzbuzz import fizzbuzz

def test_fb_is_callable_with_1_argument():
    fizzbuzz(1)

def test_fb_returns_str():
    assert isinstance(fizzbuzz(1), str)

def test_fb_1_is_1():
    assert fizzbuzz(1) == '1'

@pytest.mark.parametrize('num', [1, 2, 4])
def test_fb_regular_is_self(num):
    assert int(fizzbuzz(num)) == num

@pytest.mark.parametrize('num', [3, 6, 9])
def test_fb_tree_is_fizz(num):
    assert fizzbuzz(num) == 'fizz'

@pytest.mark.parametrize('num', [5, 20, 50])
def test_fb_five_is_buzz(num):
    assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [15, 30, 3000])
def test_fb_five_and_three_is_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'

@pytest.mark.parametrize('num', ['', 1.5, [], 4+3j])
def test_fb_raises_typerror_on_nonint(num):
    '''ověří, že kód vevnitř v bloku vyhodí vyjímku uvedenou v závorce'''
    with pytest.raises(TypeError):
        fizzbuzz(num)

@pytest.mark.parametrize('num', ['', 1.5, [], 4+3j])
def test_fb_raises_typerror_on_nonint(num):
    with pytest.raises(TypeError):
        fizzbuzz(num)

@pytest.mark.parametrize('num', [0, -1, -30])
def test_fb_raises_typerror_on_nonpositive(num):
    with pytest.raises(ValueError):
        fizzbuzz(num)
