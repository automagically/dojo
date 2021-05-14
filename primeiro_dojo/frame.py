class Frame:
    def pins_knocked(self, frame: str) -> int:
        if is_strike(frame) or is_spare(frame):
            return 10

        total_pins = 0
        for i in frame:
            is_miss = i == '-'
            if is_miss:
                continue

            total_pins += int(i)

        return total_pins

class StrikeFrame(Frame):
    pass

def calculate_strike_points(iterator):
    next_frame = next(iterator)
    total_points = BASE_POINTS_STRIKE_OR_SPARE + pins_knocked(next_frame)

    if next_frame == 'x':
        total_points  += pins_knocked(next(iterator)[0])

    return total_points


class SpareFrame(Frame):
    pass

    def calculate_spare_points(next_frame: str):
        return BASE_POINTS_STRIKE_OR_SPARE + pins_knocked(next_frame[0])