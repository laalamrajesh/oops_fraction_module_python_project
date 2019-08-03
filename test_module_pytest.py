import math

import pytest

from fraction_definition import Fraction


#default constructor


def test_fraction_default_contructor_return_zero():
    #Arrange
    fraction = Fraction()

    #Assert
    assert fraction.numerator == 0

def test_fraction_single_argument_numeric_constructor_return_same_number():
    #Arrange
    fraction = Fraction(1)

    #Assert
    assert fraction.numerator == 1

def test_fraction_dual_arguments_numeric_constructor_return_same_values():
    #Arrange
    fraction = Fraction(1,2)

    #Assert
    assert fraction.numerator == 1
    assert fraction.denominator == 2

def test_fraction_dual_arguments_negetive_denominator_constructor_return_negetive_fracion():
    #Arrange
    fraction = Fraction(1,-2)

    #Assert
    assert fraction.numerator == -1
    assert fraction.denominator == 2

def test_fraction_dual_arguments_numeric_constructor_return_reduction_fraction_values():
    #Arrange
    fraction = Fraction(50,100)

    #Assert
    assert fraction.numerator == 1
    assert fraction.denominator == 2

def test_fraction_single_argument_float_constructor_retrun_fraction_value():
    #Arrange
    fraction = Fraction(0.5)

    # Assert
    assert fraction.numerator == 1
    assert fraction.denominator == 2

def test_fraction_single_argument_float_as_string_constructor_retrun_fraction_value():
    #Arrange
    fraction = Fraction ( "0.5" )

    # Assert
    assert fraction.numerator == 1
    assert fraction.denominator == 2

def test_fraction_single_argument_fraction_as_string_constructor_retrun_fraction_value():
    #Arrange
    fraction = Fraction ( "1/2" )

    # Assert
    assert fraction.numerator == 1
    assert fraction.denominator == 2

def test_fraction_single_argument_fraction_as_string_constructor_retrun_reduction_fraction_value():
    #Arrange
    fraction = Fraction ( "75/25" )

    # Assert
    assert fraction.numerator == 3
    assert fraction.denominator == None

def test_fraction_eq_another_fraction():
    #Arrange
    left_fraction = Fraction(0.5)
    right_fraction = Fraction(1/2)

    #Assert
    assert left_fraction == right_fraction

def test_fraction_eq_another_fraction_by_reduction():
    #Arrange
    left_fraction = Fraction(25/125)
    right_fraction = Fraction(100/500)

    #Assert
    assert left_fraction == right_fraction


def test_fraction_lt_another_fraction() :
    # Arrange
    left_fraction = Fraction ( 1/5 )
    right_fraction = Fraction ( 1/4 )

    # Assert
    assert left_fraction < right_fraction


def test_fraction_lt_another_fraction_by_reduction() :
    # Arrange
    left_fraction = Fraction ( 25 , 150 )
    right_fraction = Fraction ( 100, 500 )

    # Assert
    assert left_fraction < right_fraction


def test_fraction_gt_another_fraction() :
    # Arrange
    left_fraction = Fraction ( 1/4 )
    right_fraction = Fraction ( 1/5 )

    # Assert
    assert left_fraction > right_fraction


def test_fraction_gt_another_fraction_by_reduction() :
    # Arrange
    left_fraction = Fraction ( 100 , 500 )
    right_fraction = Fraction ( 25, 150)

    # Assert
    assert left_fraction > right_fraction


def test_fraction_str_representation():
    # Arrange
    fraction = Fraction(1/2)

    #Assert
    assert str(fraction) == "1/2"


def test_fraction_str_representation_by_reduction():
    # Arrange
    fraction = Fraction(100,1000)

    #Assert
    assert str(fraction) == "1/10"

def test_fraction_add_another_fraction_return_fraction():
    #Arrange
    left_fraction = Fraction ( 1, 5 )
    right_fraction = Fraction ( 1, 6 )

    #Art
    addition = left_fraction + right_fraction

    #Assert
    assert addition.numerator == 11
    assert addition.denominator == 30


def test_fraction_add_another_fraction_return_fraction_by_reduction():
    #Arrange
    left_fraction = Fraction ( 1, 6 )
    right_fraction = Fraction ( 1, 6 )

    #Art
    addition = left_fraction + right_fraction

    #Assert
    assert addition.numerator == 1
    assert addition.denominator == 3


def test_fraction_sub_another_fraction_return_fraction():
    #Arrange
    left_fraction = Fraction ( 1, 5 )
    right_fraction = Fraction ( 1, 6 )

    #Art
    addition = left_fraction - right_fraction

    #Assert
    assert addition.numerator == 1
    assert addition.denominator == 30


def test_fraction_sub_another_fraction_return_fraction_by_reduction():
    #Arrange
    left_fraction = Fraction ( 1, 6 )
    right_fraction = Fraction ( 1, 6 )

    #Art
    addition = left_fraction - right_fraction

    #Assert
    assert addition.numerator == 0
    assert addition.denominator == None

def test_fraction_mul_another_fraction_return_fraction():
    #Arrange
    left_fraction = Fraction ( 1, 5 )
    right_fraction = Fraction ( 1, 6 )

    #Art
    addition = left_fraction * right_fraction

    #Assert
    assert addition.numerator == 1
    assert addition.denominator == 30


def test_fraction_mul_another_fraction_return_fraction_by_reduction():
    #Arrange
    left_fraction = Fraction ( 1, 6 )
    right_fraction = Fraction ( 3, 6 )

    #Art
    addition = left_fraction * right_fraction

    #Assert
    assert addition.numerator == 1
    assert addition.denominator == 12

def test_fraction_div_another_fraction_return_fraction():
    #Arrange
    left_fraction = Fraction ( 1, 5 )
    right_fraction = Fraction ( 1, 6 )

    #Art
    addition = left_fraction / right_fraction

    #Assert
    assert addition.numerator == 6
    assert addition.denominator == 5


def test_fraction_div_another_fraction_return_fraction_by_reduction():
    #Arrange
    left_fraction = Fraction ( 2, 6 )
    right_fraction = Fraction ( 4, 12 )

    #Art
    addition = left_fraction / right_fraction

    #Assert
    assert addition.numerator == 1
    assert addition.denominator == None

def test_fraction_abs_retrun_fraction():
    #Arrange
    fraction = Fraction(-1)

    #Assert
    assert abs(fraction.numerator) == 1

def test_fraction_floor_retrun_fraction():
    #Arrange
    fraction = math.floor(Fraction(1/2))

    #Assert
    assert fraction.numerator == 0


def test_fraction_ceil_retrun_fraction():
    #Arrange
    fraction = math.ceil(Fraction(1/2))

    #Assert
    assert fraction.numerator == 1




