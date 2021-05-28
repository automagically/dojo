from typing import List

class Minesweeper:
    
    def __init__(self):
        self.count = 0
        self.lines = 0
        self.columns = 0
        self.field = 0
        
    def parse_field(self, lines: int, columns: int, field: List[List[str]]) -> str:
        is_invalid_input = (lines == 0  and columns == 0)
        if is_invalid_input:
            return ''

        self.lines = lines
        self.columns = columns
        self.field = field

        result = self._process()
        return self._generate_response(result)
    
    def _process(self):
        result = [[0]*self.columns for _ in range(self.lines)]
        
        for current_line in range(self.lines):
            for current_column in range(self.columns):
                is_bomb = self.field[current_line][current_column] == "*"
                if is_bomb:
                    self._process_bombs(result, current_line, current_column)
        return result

    def _process_bombs(self, result, current_line, current_column):
        result[current_line][current_column] = "*"

        delta = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        for line_delta, column_delta in delta:
            updated_line = current_line + line_delta  
            if not self._is_valid_line(updated_line):
                continue

            updated_column = current_column + column_delta
            if updated_column < 0 or updated_column >= self.columns:
                continue

            if self.field[updated_line][updated_column] == '.':
                result[updated_line][updated_column] += 1

    def _is_valid_line(self, index):
        return  0 <= index < self.lines
    
    def _generate_response(self, result):                            
        self._update_count()
        converted_result = self._convert_result_to_string(result)
        return self._format_response(converted_result)
    
    def _update_count(self):
        self.count += 1

    def _format_response(self, converted_result):
        result_string = f'Field #{self.count}:\n' + "\n".join([''.join(i) for i in converted_result]) + '\n'
        return result_string

    def _convert_result_to_string(self, result):
        return [[str(item) for item in lin] for lin in result]