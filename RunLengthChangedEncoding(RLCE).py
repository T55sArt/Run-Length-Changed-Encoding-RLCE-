#RLE but RL is only defined when RL changes, making <= Item length as traditional RLE. Encoded list count should be just as big as RLE results
#(unless input data has similar formatting, making this robust & flexible)
#Example:
#Data: ['a', 'a', 'b', 'b', 'a', 'b', 'c', 'd', 'd', '3#s', '3', '3', '5_t', '7#e', '7#e', '#a', 'a#'], Delim: "#"
#Returned: ['2#a', 'b', '1#a', 'b', 'c', '2#d', '1#3#s', '2#3', '1#5_t', '2#7#e', '1##a', 'a#']

from collections import namedtuple

def ParseRLE(Item: str, Delimiter: str):
    a = Item.split(Delimiter, 1)
    Success = a[0].isdigit() and Delimiter in Item
    result = namedtuple('ParseRLEresult', ['RunLength', 'Data', 'Success'])
    Result = result(int(a[0]) if Success else -1, a[1] if Success else Item, Success)
    return Result

def Encode(Data: list, Delimiter: str):
    Encoded: list[str] = []
    prevInput = str(Data[0])
    prevRunLength = 0
    curRunLength = 0

    dataHasSimilarFormatting = False
    for i in Data:
        i = str(i)
        if i == prevInput:
            curRunLength = curRunLength + 1
        else:
            Encoded.append(str(curRunLength) + Delimiter + prevInput if dataHasSimilarFormatting or not curRunLength == prevRunLength else prevInput)
            prevInput = i
            prevRunLength = curRunLength
            curRunLength = 1
            dataHasSimilarFormatting = ParseRLE(i, Delimiter).Success

    Encoded.append(str(curRunLength) + Delimiter + prevInput if ParseRLE(i, Delimiter).Success or not curRunLength == prevRunLength else prevInput)

    return Encoded

def Decode(ToType, Data: list[str], Delimiter: str):
    Decoded = []
    curRunLength = 0
    prevRunLength = 0

    for i in Data:
        cur = ParseRLE(i, Delimiter)
        setNewRunLength = cur.Success
        curRunLength = cur.RunLength if setNewRunLength else prevRunLength
        Item = cur.Data if setNewRunLength else i
        if not curRunLength == prevRunLength:
            prevRunLength = curRunLength
        for _ in range(prevRunLength):
            Decoded.append(ToType(Item))

    return Decoded