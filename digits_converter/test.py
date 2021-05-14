
import pytest

from digits_converter import DigitsConvert

def test_no_digits():
    converter = DigitsConvert()
    display = converter.convert_number_to_7seg_display('')
    assert display == ''


def test_with_number_zero():
    converter = DigitsConvert()
    display = converter.convert_number_to_7seg_display('0')
    expected = ' _ \n' \
               '| |\n' \
               '|_|\n'
    print()
    print(expected)
    print()
    print(display)

    assert expected == display


def test_with_number_one():
    converter = DigitsConvert()
    display = converter.convert_number_to_7seg_display('1')
    expected = '   \n' \
               '  |\n' \
               '  |\n'
    print()
    print(expected)
    print()
    print(display)

    assert expected == display


@pytest.mark.parametrize('input,expected',
    [
        ('23',
        ' _   _ \n' \
        ' _|  _|\n' \
        '|_   _|\n' \
        ),
        ('54',
        ' _     \n' \
        '|_  |_|\n' \
        ' _|   |\n' \
        ),
        ('89',
        ' _   _ \n' \
        '|_| |_|\n' \
        '|_|  _|\n' \
        ),
        ('67',
        ' _   _ \n' \
        '|_    |\n' \
        '|_|   |\n' \
        ),
        ('10',
        '     _ \n' \
        '  | | |\n' \
        '  | |_|\n'
        )
    ]
)
def test_with_multi_digit_number_parametrize(input, expected):
    converter = DigitsConvert()
    display = converter.convert_number_to_7seg_display(input)

    print()
    print(expected)
    print()
    print(display)

    assert expected == display


def test_with_multiple_numbers():
    converter = DigitsConvert()
    display = converter.convert_number_to_7seg_display('0123456789')
    expected = ' _       _   _       _   _   _   _   _ \n' \
               '| |   |  _|  _| |_| |_  |_    | |_| |_|\n' \
               '|_|   | |_   _|   |  _| |_|   | |_|  _|\n'
    print()
    print(expected)
    print()
    print(display)

    assert expected == display


def test_create_converter_with_custom_size():
    converter = DigitsConvert(length=5, height=5)
    assert converter.length == 5
    assert converter.height == 5


@pytest.mark.parametrize('length, height, input, expected', [
    (3, 5, '8', 
               ' _ \n' \
               '| |\n' \
               '|_|\n' \
               '| |\n' \
               '|_|\n'
    ), 

    (5, 3, '8', 
               ' ___ \n' \
               '|___|\n' \
               '|___|\n'
    ), 

    (6, 3, '8', 
               ' ____ \n' \
               '|____|\n' \
               '|____|\n'
    ), 

    (6, 4, '8', 
               ' ____ \n' \
               '|____|\n' \
               '|    |\n' \
               '|____|\n'
    ),

])
def test_digit_with_different_size(length, height, input, expected):
    converter = DigitsConvert(length, height)
    display = converter.convert_number_to_7seg_display(input)

    print()
    print(expected)
    print()
    print(display)

    assert expected == display