def ec(s,key):
	output = []
	while len(key)<len(s):
		key +=key
	for i in range(len(s)):
		output.append(ord(s[i])+ord(key[i]))
		output[i] = chr(output[i])
	output = "".join(output)
	print output
	return output

def dc(s,key):
	output = []
	while len(key)<len(s):
		key +=key
	for i in range(len(s)):
		output.append(ord(s[i])-ord(key[i]))
		output[i] = chr(output[i])
	output = "".join(output)
	return output



dc(ec("abasdfasdfasdf","abasdf"),"abasdf")