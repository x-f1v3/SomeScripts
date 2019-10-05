### 栅栏

e = 'string'

elen = len(e)
print elen
field=[]
for i in range(2,elen):
            if(elen%i==0):
                field.append(i)

for f in field:
    b = elen / f
    result = {x:'' for x in range(b)}
    for i in range(elen):
        a = i % b
        result.update({a:result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print str(f)+'\t'+str(d)



### 培根

import re

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

first_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"]

second_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","baabb","babaa","babab","babba","babbb"]

def encode(s):
    upper_flag = False 
    string = s
    if string.isupper():
        upper_flag = True
        string = string.lower()
    e_string1 = ""
    e_string2 = ""
    for index in string:
        for i in range(0,26):
            if index == alphabet[i]:
                e_string1 += first_cipher[i]
                e_string2 += second_cipher[i]
                break
    if upper_flag:
        e_string1 = e_string1.upper()
        e_string2 = e_string2.upper()
    print "first encode method result is:\n"+e_string1
    print "second encode method result is:\n"+e_string2
    return


def decode(s):
    upper_flag = False 
    e_string = s
    if e_string.isupper():
        upper_flag = True
        e_string = e_string.lower()
    e_array = re.findall(".{5}",e_string)
    d_string1 = ""
    d_string2 = ""
    for index in e_array:
        for i in range(0,26):
            if index == first_cipher[i]:
                d_string1 += alphabet[i]
            if index == second_cipher[i]:
                d_string2 += alphabet[i]
    if upper_flag:
        d_string1 = d_string1.upper()
        d_string2 = d_string2.upper()
    # print "first decode method result is:\n"+d_string1
    # print "second decode method result is:\n"+d_string2
    return d_string1,d_string2



def decode2(s):
    decode_string1 = ""
	decode_string2 = ""
	mask=""
	for index in s:
		if index.isupper():
			mask = mask + "b"   # up = b
		else:
			mask = mask + "a"   # low =a
	print(mask)
	tmp1,tmp2= decode(mask)
	decode_string1 +=tmp1
	decode_string2 +=tmp2

	print "first decode method result is:\n"+decode_string1
	print "second decode method result is:\n"+decode_string2




### ASCII 移位 decode
encode="string"

for i in xrange(1,120):
    decode=""
    for x in encode:
        char=ord(x)
        decode=decode+chr(char+i)
    print decode
    print '*'*20

### ASCII 移位 encode
text="string"

encode=""
for x in text:
    char=ord(x)
    encode=encode+chr(char-6)
print encode
print '*'*20


