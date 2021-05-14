from typing import List

class Bowling():
    def __init__(self, ):
        self.__frames = []
        self._rolls = []
        self._index_score = 0
        self._score = 0

    def add_frame(self, *args) -> None:
        for i in args:
            self._rolls.append(i)

    def calculate_score(self) -> int:
        self._index_score = 0
        self._score = 0

        for _ in range(10):
            if self._is_strike():
                self._add_strike_score()
                continue

            if self._is_spare():
                self._add_spare_score()
                continue

            self._add_normal_score()

        return self._score
    
    def _is_strike(self) -> bool:
        return self._rolls[self._index_score] == 10
    
    def _is_spare(self) -> bool:
        return self._rolls[self._index_score] + self._rolls[self._index_score + 1] == 10
            
    def _add_strike_score(self):
        self._score += 10 + self._rolls[self._index_score + 1] + self._rolls[self._index_score + 2]
        self._index_score += 1

    def _add_spare_score(self):
        self._score += 10 + self._rolls[self._index_score + 2]
        self._index_score += 2
        
    def _add_normal_score(self):
        self._score += self._rolls[self._index_score] + self._rolls[self._index_score + 1]
        self._index_score += 2
