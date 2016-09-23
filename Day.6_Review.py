for i in range(int(input())):
    S = input()
    # Even-indexed (::2) and odd-indexed (1::2)
    print(S[::2], S[1::2])
