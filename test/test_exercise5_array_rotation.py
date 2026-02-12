from exercise5_array_rotation import *

## Test cases
t1_Vect1 = [1, 2, 3, 4, 5, 6, 7] 
t2_Vect1 = [1, 2, 3, 4, 5, 6, 7]
t3_Vect1 = [1, 2, 3, 4, 5, 6, 7]
t1_k1 = 10
t2_k1 = 10
t3_k1 = 10
t1_Output1 = [5, 6, 7, 1, 2, 3, 4]
t2_Output1 = [5, 6, 7, 1, 2, 3, 4]
t3_Output1 = [5, 6, 7, 1, 2, 3, 4]

t1_Vect2 = [1]
t2_Vect2 = [1]
t3_Vect2 = [1]
t1_k2 = 5
t2_k2 = 5
t3_k2 = 5
t1_Output2 = [1]
t2_Output2 = [1]
t3_Output2  = [1]


def test_RotateTemp():
    assert RotateTemp(t1_Vect1, t1_k1) == t1_Output1
    assert RotateTemp(t1_Vect2, t1_k2) == t1_Output2


def test_RotateOneByOne():
    assert RotateOneByOne(t2_Vect1, t2_k1) == t2_Output1
    assert RotateOneByOne(t2_Vect2, t2_k2) == t2_Output2

def test_RotateReverse():
    assert RotateReverse(t3_Vect1, t3_k1) == t3_Output1
    assert RotateReverse(t3_Vect2, t3_k2) == t3_Output2
