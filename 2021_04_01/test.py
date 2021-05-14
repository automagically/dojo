import pytest

class DigitsConvert():
    """Converts a sequence of digits into a display of multi-line characters."""

    def __init__(self, length: int = 3, heigth: int =3):
        self.length = length
        self.heigth = heigth
        self.digits = {

            '0': [
                    ' _ ',
                    '| |',
                    '|_|',
                 ],

            '1': [
                    '   ',
                    '  |',
                    '  |',
                ],

             '2': [
                    ' _ ',
                    ' _|',
                    '|_ ',
                ],

            '3': [
                    ' _ ',
                    ' _|',
                    ' _|',
                ],

            '4': [
                    '   ',
                    '|_|',
                    '  |',
                ],

            '5': [
                    ' _ ',
                    '|_ ',
                    ' _|',
                ],

            '6': [
                    ' _ ',
                    '|_ ',
                    '|_|',
                ],

            '7': [
                    ' _ ',
                    '  |',
                    '  |',
                ],

            '8': [
                    ' _ ',
                    '|_|',
                    '|_|',
                ],

            '9': [
                    ' _ ',
                    '|_|',
                    ' _|',
                ]
        }

    def digits_to_display(self, value):
        if value == '':
            return ''

        temp = [self.digits.get(v) for v in value]
        result = ''
        """
        [
            [' _ ',' _ '],
            [' _|',' _|'],
            ['|_ ',' _|'],
        ]
        """
        for linha in zip(*temp):
            result += ' '.join(linha) + '\n'

        return result


def test_no_digits():
    converter = DigitsConvert()
    display = converter.digits_to_display('')
    assert display == ''


def test_with_number_zero():
    converter = DigitsConvert()
    display = converter.digits_to_display('0')
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
    display = converter.digits_to_display('1')
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
def test_with_number_parametrize(input, expected):
    converter = DigitsConvert()
    display = converter.digits_to_display(input)

    print()
    print(expected)
    print()
    print(display)

    assert expected == display


def test_with_multiple_number():
    converter = DigitsConvert()
    display = converter.digits_to_display('0123456789')
    expected = ' _       _   _       _   _   _   _   _ \n' \
               '| |   |  _|  _| |_| |_  |_    | |_| |_|\n' \
               '|_|   | |_   _|   |  _| |_|   | |_|  _|\n'
    print()
    print(expected)
    print()
    print(display)

    assert expected == display


def test_create_converter_with_custom_size():
    converter = DigitsConvert(length=5, heigth=5)
    assert converter.length == 5
    assert converter.heigth == 5


def test_number_with_size_3x5():

    '8': [
            ' _ ',
            '|_|',
            '|_|',
        ],
