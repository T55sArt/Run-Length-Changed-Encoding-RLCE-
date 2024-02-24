from collections import namedtuple

def ParseRLE(Item:str, Delimiter:str):
    """
    Takes in a string "Input" formatted by the string "Delimiter"
    (divider/seperator/splitter) & returns tuple with attributes:\n
    * int   : Run Length (-1    when unsuccessful)\n
    * string: Data       (Item  when unsuccessful)\n
    * bool  : Success    (False when unsuccessful)
    """
    a = Item.split(Delimiter, 1)
    Success = a[0].isdigit() and Delimiter in Item
    rleFormat = namedtuple('ParseRLEresult',['RunLength','Data','Success'])
    result = rleFormat(int(a[0]) if Success else -1, a[1] if Success else Item, Success)
    return result

def Encode(Data:list, Delimiter:str):
    """
    Takes in a List of any "Data" with string "Delimiter"
    (divider/seperator/splitter) & returns Data Run Length
    Changed Ecoded (RLCE).\n
    Like Run Length Encoding (RLE),
    it encodes by Run Length, but only when it changes\n
    (with the exception of data with similar formatting so it's
    able to support that type of data, making very robust).\n
    Overall this effciently compacts lists of data like RLE, with
    the primary difference of also saving on item size a bit
    instead of definiing run length everytime.\n
    * Example (Handleing Run Lengths changing everytime (behaves like RLE)):\n
    Data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]\n
    Encode(Data, '#') = [1#1,2#2,3#3,4#4,5#5]\n
    > So overall, not loosing anything here, just RLE\n
    * Example (Handleing Repeated Run Lengths):\n
    Data = [1,1,2,2,3,4,5,6,6,7,7,7,8,8,8]\n
    Encode(Data, '#') = [2#1,2,1#3,4,5,2#6,3#7,8]\n
    > Saves on item size
    * Example (Handleing data with similar formatting):\n
    Data = [1,1,1#e,1#e,4#,#8,a,b]\n
    Encode(Data, '#') = [2#1,2#1#e,1#4#,1##8,a,b]\n
    > Once again, not loosing anything besides from reaching
    its true potential, which is at least still less than RLE
    """
    #Initialization
    Encoded:list[str] = []
    prevInput = str(Data[0])
    prevRunLength = 0
    curRunLength = 0
    hasSimilarFormat = False

    #Loop:
    for i in Data:
        i = str(i)
        if i == prevInput:
            curRunLength += 1
        else:
            Encoded.append(f'{curRunLength}{Delimiter}{prevInput}' if hasSimilarFormat or not curRunLength == prevRunLength else prevInput)
            prevInput = i
            prevRunLength = curRunLength
            curRunLength = 1
            hasSimilarFormat = ParseRLE(i, Delimiter).Success #Handle Similar formatting
    Encoded.append(f'{curRunLength}{Delimiter}{prevInput}' if ParseRLE(i, Delimiter).Success or not curRunLength == prevRunLength else prevInput)

    #Return:
    return Encoded

def Decode(ToType, Data:list[str], Delimiter:str):
    """
    Takes in any "ToType", List of string "Data" (Encoded in RLCE), &
    string "Delimiter" (divider/seperator/splitter) & returns Data to
    its usual self as type of ToType\n
    """
    #Initialization:
    Decoded = []
    Item = Data[0]
    runLength = ParseRLE(Item, Delimiter).RunLength

    #Loop:
    for i in Data:
        cur = ParseRLE(i, Delimiter)
        setNewRunLength = cur.Success
        if setNewRunLength:
            runLength = cur.RunLength
        Item = cur.Data if setNewRunLength else i
        Decoded.extend([ToType(Item) for _ in range(runLength)])

    #Return:
    return Decoded