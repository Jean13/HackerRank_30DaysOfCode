N = int(input())

# grabbing next input and splitting
info = [input().split() for _ in range(N)]
# creating our dictionary phone book
book = {na: nu for na, nu in info}

# while there's input
while True:
    try:
        name = input()
        if name in book:
            # %s allows us to insert whatever is passed after the % symbol. we use it to insert the name and number
            print("%s=%s" % (name, book[name]))
        else:
            print("Not found")
    except:
        break
