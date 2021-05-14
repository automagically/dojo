import pytest
from bowling import Bowling

def test_zero_points():
    bowling = Bowling()

    _add_frames(bowling, 10, (0, 0))

    assert bowling.calculate_score() == 0
    
def test_knock_some_pins():
    bowling = Bowling()

    _add_frames(bowling, 10, (6, 0))

    expected_score = 60
    assert bowling.calculate_score() == expected_score

def test_frame_with_spare():
    bowling = Bowling()

    _add_frames(bowling, 9, (1, 9))
    _add_frames(bowling, 1, (1, 9, 1))

    expected_score = 110
    assert bowling.calculate_score() == expected_score

def test_frame_with_perfect_strike():
    bowling = Bowling()

    _add_frames(bowling, 9, (10,))
    _add_frames(bowling, 1, (10, 10, 10))

    expected_score = 300
    assert bowling.calculate_score() == expected_score

def test_frame_with_strike():
    bowling = Bowling()
    
    # 10 10 10 10 10 10 10 10 10 000
    # 30 30 30 30 30 30 30 20 10 0
    

    _add_frames(bowling, 9, (10,))
    _add_frames(bowling, 1, (0, 0))

    expected_score = 240
    assert bowling.calculate_score() == expected_score


def _add_frames(bowling: Bowling, num_frames: int, score: tuple):
    for frame in range(num_frames):
        bowling.add_frame(*score)
