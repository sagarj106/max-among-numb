def func1(a,b,c):
	if a>b:
		if a>c:
			return a
		else:
			return c
	if b>c:
		return b
	else:
		return c

r=func1(4,5,6)
print(r)
