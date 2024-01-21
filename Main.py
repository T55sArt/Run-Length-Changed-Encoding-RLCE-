import RunLengthChangedEncoding as rlce

data = ['a', 'a', 'a', 'a', 'a', ]
delimiter = '#'

print('Original: ' + str(data) + '\nDelimiter: ' + delimiter)
print('')
print('Parse Example: 3#a = ' + str(rlce.ParseRLE("3#a" , delimiter)))
print('')
encodedData = rlce.Encode(data, delimiter)
print('Encoded: ' + str(encodedData) + '\nData Saved: ' + str(round(100 - ((len(encodedData) / len(data)) * 100), 3)) + '%, Orginal Count: ' + str(len(data)) + ', Encoded Count: ' + str(len(encodedData)))
print('')
decodedData = rlce.Decode(str, encodedData, delimiter)
print('Decoded: ' + str(decodedData) + '\nDecode Success: ' + str(data == decodedData))