def majority(string):
    letters = {}
    for s in string:
        if s not in letters:
            letters[s] = 1
        else:
            letters[s] += 1
    #                                                           x[0] x[1]
    #                v-- list of tuples               v-- e.g. (A   ,13  )
    letters = sorted(letters.items(), key = lambda x: x[1], reverse = True) # !!!
    return letters[0][0]

a1 = "KKKAAAAAAAAAAAFKAAKK"
print(majority(a1))
