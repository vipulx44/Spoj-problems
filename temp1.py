while True:
    inputStr = input()
    inputStr = inputStr.strip()
    if (inputStr == '0'):
        break
    dp = [0 for i in range(len(inputStr) + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len(inputStr)+1):
        prevDigit = int(inputStr[i-2])
        curDigit = int(inputStr[i-1])
        if (prevDigit >= 3 or prevDigit == 0):
            dp[i] = dp[i-1]
        else:
            # prevDigit == 1 or prevDigit == 2
            if (curDigit == 0):
                dp[i] = dp[i-2]
            else:
                if (prevDigit == 1):
                    dp[i] = dp[i-1] + dp[i-2]
                elif (prevDigit == 2):
                    if (curDigit > 6):
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1] + dp[i-2]
    print(dp[len(inputStr)])
