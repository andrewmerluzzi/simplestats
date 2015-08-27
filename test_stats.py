from stats import mean
from nose.tools import assert_equal

def test_mean():
        assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
        assert(mean([1.0,2]) == 1.5)
#test_float_mean()

def test_exercise_mean():
	assert(mean([2,4,6]) == 4)
#test_exercise_mean()
