import RunLengthChangedEncoding as rlce

#Input:
data = ['a', 'a', 'b', 'b', 'a', 'b', 'c', 'd', 'd', '3#s', '3', '4', '5_t', '7#e', '7#e', '#1', '2#']
delimiter = '#'

#Processed by RLCE:
encodedData = rlce.Encode(data, delimiter)
decodedData = rlce.Decode(str, encodedData, delimiter)

#RLE vs RLCE:
traditionalRLE = []
prev = str(data[0])
runLen = 0
for i in data:
    i = str(i)
    if i == prev:
        runLen = runLen + 1
    else:
        traditionalRLE.append(f'{runLen}{delimiter}{prev}')
        prev = i
        runLen = 1
traditionalRLE.append(f'{runLen}{delimiter}{prev}')

#Summing up chars count from RLE & RLCE:
beforeChars = 0
for i in traditionalRLE:
    beforeChars = beforeChars + len(i)
afterChars = 0
for i in encodedData:
    afterChars = afterChars + len(i)

#Statistics:
print(f'Original: {data}\nDelimiter: {delimiter}\n')
print(f'Parse Example: 3#a = {rlce.ParseRLE("3#a", delimiter)}\n')
print(f'Encoded: {encodedData}')
print(f'Data Saved (Count Wise): {round(100-((len(encodedData)/len(data))*100),3)}%, Orginal Count: {len(data)}, Encoded Count: {len(encodedData)}')
print(f'Data Saved (RLE vs RLCE (Char Wise)): {round(100-((afterChars/beforeChars)*100),3)}%, RLE Count: {beforeChars}, RLCE Count: {afterChars}\n')
print(f'Decoded: {decodedData}\nDecode Success: {data == decodedData}')