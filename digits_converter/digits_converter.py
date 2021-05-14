import math
from typing import List

class DigitsConvert():
    """Converts a sequence of digits into a display of multi-line characters."""

    def __init__(self, length: int = 3, height: int = 3):
        self.length = length
        self.height = height
        self.digit_bool_list = []


    def convert_number_to_7seg_display(self, value):
        if value == '':
            return ''

        is_line_size_even = self.height % 2 == 0

        temp = [self._generate_digit(v, is_line_size_even) for v in value]
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

    
    def _generate_digit(self, digit, is_line_size_even):       
        self.digit_bool_list = self._convert_digit_to_7seg_bool(digit)
        return self._render_digit()
    
    
    def _convert_digit_to_7seg_bool(self, digit: str) -> List[int]:
        """
         0   _  
        561 |_|
        432 |_|
        """
        digit_as_7seg_bool_list = {'0': [1, 1, 1, 1, 1, 1, 0], 
                       '1': [0, 1, 1, 0, 0, 0, 0], 
                       '2': [1, 1, 0, 1, 1, 0, 1],
                       '3': [1, 1, 1, 1, 0, 0, 1],
                       '4': [0, 1, 1, 0, 0, 1, 1],
                       '5': [1, 0, 1, 1, 0, 1, 1],
                       '6': [1, 0, 1, 1, 1, 1, 1],
                       '7': [1, 1, 1, 0, 0, 0, 0],
                       '8': [1, 1, 1, 1, 1, 1, 1],
                       '9': [1, 1, 1, 1, 0, 1, 1]}
        return digit_as_7seg_bool_list[digit]


    def _render_digit(self):
        """
         0   _ 
        561 |_|
        432 |_|
        """
         
        top = self._generate_top_of_digit()
        between_top_and_middle = self._generate_between_top_and_middle_of_digit()
        middle = self._generate_middle_of_digit()
        between_middle_and_bottom = self._generate_between_middle_and_bottom_of_digit()
        bottom = self._generate_bottom_of_digit()

        return [top, *between_top_and_middle, middle, *between_middle_and_bottom, bottom]
    

    def _generate_top_of_digit(self):
        return self._render_segment(False, self.digit_bool_list[0], False)


    def _generate_between_top_and_middle_of_digit(self):
        top_middle_size = math.floor((self.height - 3) / 2)
        return self._generate_filler(top_middle_size, self.digit_bool_list[5], self.digit_bool_list[1])


    def _generate_middle_of_digit(self):
        return self._render_segment(self.digit_bool_list[5], self.digit_bool_list[6], self.digit_bool_list[1])


    def _generate_between_middle_and_bottom_of_digit(self):
        bottom_middle_size = math.ceil((self.height - 3) / 2)
        return self._generate_filler(bottom_middle_size, self.digit_bool_list[4], self.digit_bool_list[2])


    def _generate_bottom_of_digit(self):
        return self._render_segment(self.digit_bool_list[4], self.digit_bool_list[3], self.digit_bool_list[2])


    def _generate_filler(self, size, start_with_pipe, ends_with_pipe):

        generate_filler_list = []

        for _ in range(size):
            generate_filler_list.append(self._render_segment(start_with_pipe, False, ends_with_pipe))
        return generate_filler_list


    def _render_segment(self, start_with_pipe, has_middle, ends_with_pipe):
        #"|_|"
        first_pipe = "|" if start_with_pipe else " "
        middle_character = "_" if has_middle else " "
        second_pipe = "|" if ends_with_pipe else " "

        middle_character = middle_character * (self.length - 2)

        return first_pipe + middle_character + second_pipe