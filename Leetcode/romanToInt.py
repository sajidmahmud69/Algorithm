# example MCMXCIV => 
def romanToInt (s):
    hashMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    curCharIdx = 0
    answer = 0
    while curCharIdx < len (s):
        nextCharIdx = curCharIdx + 1
        if nextCharIdx >= len (s):
            return answer + hashMap[s[curCharIdx]]
        if hashMap[s[curCharIdx]] < hashMap[s[nextCharIdx]]:
            answer += hashMap[s[nextCharIdx]] - hashMap [s[curCharIdx]]
            curCharIdx += 2

        else:
            answer += hashMap[s[curCharIdx]]
            curCharIdx += 1
    return answer



# Test code

print (romanToInt ('III'))
print (romanToInt ('LVIII'))
print (romanToInt ('MCMXCIV'))


