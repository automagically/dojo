from typing import List

BASE_POINTS_STRIKE_OR_SPARE = 10

def calculate_total_points(frames: str) -> int:
    frames = frames.split(' ')
    points = 0
    for i in range(10):
        frame = frames[i]
        if is_strike(frame):
            StrikeFrame(frame)
            iterator = iter(frames[i+1:i+3])
            points += calculate_strike_points(iterator)
        elif is_spare(frame):
            points += calculate_spare_points(frames[i + 1])
        else:
            points += pins_knocked(frame)
    return points
    
def     calculate_strike_points(iterator):
        next_frame = next(iterator)
    total_points = BASE_POINTS_STRIKE_OR_SPARE + pins_knocked(next_frame)
    
    if next_frame == 'x':
        total_points  += pins_knocked(next(iterator)[0])
    
    return total_points

def calculate_spare_points(next_frame: str):
    return BASE_POINTS_STRIKE_OR_SPARE + pins_knocked(next_frame[0])

def pins_knocked(frame: str) -> int:
    if is_strike(frame) or is_spare(frame):
        return 10

    total_pins = 0
    for i in frame:
        is_miss = i == '-'
        if is_miss:
            continue

        total_pins += int(i)

    return total_pins

def is_strike(frame: str) -> bool:
    return frame == 'x'

def is_spare(frame: str) -> bool:
    return '/' in frame