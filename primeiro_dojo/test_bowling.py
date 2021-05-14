from bowling import calculate_total_points

def test_when_missed_all_the_total_should_be_zero():
    input = '-- -- -- -- -- -- -- -- -- --'
    assert calculate_total_points(input) == 0

def test_all_strikes_should_sum_up_to_300():
    input = 'x x x x x x x x x x x x'
    assert calculate_total_points(input) == 300

def test_given_no_strikes_nor_spares_should_sum_up_to_the_number_of_pins_knocked_out():
    input = '9- 9- 9- 9- 9- 9- 9- 9- 9- 9-'
    assert calculate_total_points(input) == 90

    input = '9- 5- -9 9- 9- -7 9- 9- 3- 9-'
    assert calculate_total_points(input) == 78

    input = '-- -- 1- 1- -- -- 1- -1 -1 --'
    assert calculate_total_points(input) == 5

    input = '3- 24 53 -6 -7 8- -9 -- 13 9-'
    assert calculate_total_points(input) == 60

    input = '1- 2- -3 -4 5- 6- -7 -8 9- 1-'
    assert calculate_total_points(input) == 46

def test_given_no_strikes_should_sum_up_to_the_number_of_pins_knocked_out():
    input = '5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5'
    assert calculate_total_points(input) == 150

    input = '5/ 6/ 4/ 5/ 8/ 5/ 5/ 9/ 5/ 5/ 1'
    assert calculate_total_points(input) == 153

def test_happy_path():
    input = '1/ 9- x x x 2/ -6 -- x x 9-'
    #        19 9  30 22 20 10 6  0  29 19
    #        19 28 58 80 100 110 116 116 145 164
    assert calculate_total_points(input) == 164