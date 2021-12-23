str1 = 'разработка'
str2 = 'администрирование'
str3 = 'protocol'
str4 = 'standard'

enc_str1 = str1.encode('utf-8')
enc_str2 = str2.encode('utf-8')
enc_str3 = str3.encode('utf-8')
enc_str4 = str4.encode('utf-8')

print(str1, enc_str1)
print(str2, enc_str2)
print(str3, enc_str3)
print(str4, enc_str4)

dec_str1 = enc_str1.decode('utf-8')
dec_str2 = enc_str2.decode('utf-8')
dec_str3 = enc_str3.decode('utf-8')
dec_str4 = enc_str4.decode('utf-8')

print(str1 == dec_str1)
print(str2 == dec_str2)
print(str3 == dec_str3)
print(str4 == dec_str4)
