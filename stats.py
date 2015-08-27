def mean(vals):
	total = sum(vals)
	length = len(vals)
	return total/length

def test_mean():
	assert(mean([2,4]) == 3)
test_mean()

def test_float_mean():
	assert(mean([1,2]) == 1.5)
test_float_mean()

#print mean([2,4])

