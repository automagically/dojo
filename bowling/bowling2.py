class Bowling():
    def __init__(self, ):
        self.__frames = []
        self.__multiplier = 1
        self.__multiplier = 1


    def add_frame(self, first_roll: int, second_roll: int, third_roll: int = None) -> None:
        self.__frames.append((first_roll, second_roll, third_roll))


    def calculate_score(self) -> int:
        MAX_TOTAL_PINS = 10
        points = 0
        LAST_FRAME = 9
        should_add_spare_bonus = False
        counter_strike = 0

        """
        strike seguido nao strike
        - somar o next frame
        strike seguido por strike
        - se for o penultimo
        -- considerar o segundo roll do next frame
        - se for o ultimo
        -- considerar o segundo e o terceiro roll do frame atual
        """
        for iteration, frame in enumerate(self.__frames):

            first_roll, second_roll, third_roll = frame
            total_pins_knocked = first_roll + second_roll 

            if first_roll == 10:
                points += self._calculate_strike_score(iteration)
                continue
                    
            if total_pins_knocked == 10:
               points += self._calculate_spare_score(iteration)

            points += total_pins_knocked

        return points


    def _calculate_strike_score(self, iteration: int) -> int:
        score = 10
        if iteration == 9:
            first_roll, second_roll, third_roll = self.__frames[iteration]
            score += second_roll + third_roll
        else:
            first_roll, second_roll, _ = self.__frames[iteration + 1]
            score += first_roll
            if first_roll == 10 and iteration < 8:
                first_roll, _, _ = self.__frames[iteration + 2]
                score += first_roll
            else:
                score += second_roll
        
        return score

    def _calculate_spare_score(self, iteration: int) -> int:
        score = 0
        if iteration == 9:
            _, _, third_roll = self.__frames[iteration]
            score += third_roll
        else:
            next_frame = self.__frames[iteration + 1]
            first_roll, _, _ = next_frame
            score += first_roll
        return score
