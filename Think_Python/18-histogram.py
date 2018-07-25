# _*_ encodig:utf-8_*_

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def print_hist(h):
	for c in sorted(h):
		print(c, h[c])

def reverse_lookup(d,v):
	for k in d:
		if d[k] == v:
			return k
	raise LookupError()


def inverse_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse



d = histogram("asasdssfassafgvxkclknskjfjsnklflkjslk")
print(d)
print_hist(d)
k = reverse_lookup(d,6)
print(k)
inverse = inverse_dict(d)
print(inverse)