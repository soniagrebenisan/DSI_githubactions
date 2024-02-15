###### area of square test ######

def test_calc_area_square():
    from calc_area_3 import calc_area_square
    input_numbers = [0, 1, 4, 100]
    output_numbers = [0, 1, 16, 10000]
    # output_number = calc_area_square(input_number) # replacing this with zip
    assert len(input_numbers) == len(output_numbers)

    # option 1
    for input, output in zip(input_numbers, output_numbers):
        assert calc_area_square(input) == output

    # assert output_number == 4 # not flexible
    
    # option 2
    for i in range(len(input_numbers)):
        this_input = input_numbers[i]
        this_exp_out = output_numbers[i]

        assert calc_area_square(this_input) == this_exp_out

###### are of circle test ######
from pytest import approx, raises

def test_calc_area_circle_errors():
    from calc_area_3 import calc_area_circle

    with raises(ValueError):
        calc_area_circle(-1)

    with raises(TypeError):
        calc_area_circle('this is not a number')