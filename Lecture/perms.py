def perms(s):
	'''(str) -> list of str
	Return all permutations of s.
	'''
	if  s == '':
		return ['']
	smaller = perms(s[1:])
	bigger = []
	for p in smaller:
		for i in range(len(p) + 1):
			new_perm = p[:i] + s[0] + p[i:]
			bigger.append(new_perm)
	return bigger

    
