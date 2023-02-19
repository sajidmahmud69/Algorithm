def validString (my_list):
    res = []

    for element in my_list:
        hashMap = {}

        keyword = element.split (' ')[0]
        occurence = element.split (' ')[1]
        string = element.split (' ')[2]

        for c in string:
            if c not in hashMap:
                hashMap [c] = 1
            else:
                hashMap [c] += 1

        if occurence == hashMap[keyword]:
            res.append ('valid')
        else:
            res.append ('invalid')

    return res


my_list = ['a 1: cat',
            'aa 2: Aadhaar',
            'c 5: bat',
            'z 2: zebra']

print (validString(my_list))


