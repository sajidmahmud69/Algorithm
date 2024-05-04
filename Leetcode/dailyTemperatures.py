def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)

    return res


if __name__ == '__main__':
    temp = [73,74,75,71,69,72,76,73] 
    print(dailyTemperatures(temp))
