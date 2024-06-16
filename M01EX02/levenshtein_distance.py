def levenshtein_distance(source, target):
    distance_table = [[0]*(len(target)+1) for _ in range(len(source)+1)]
    for i in range(len(source)+1):
        distance_table[i][0] = i
    for j in range(len(target)+1):
        distance_table[0][j] = j
    a = 0
    b = 0
    c = 0
    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if (source[i-1] == target[j-1]):
                distance_table[i][j] = distance_table[i-1][j-1]
            else:
                a = distance_table[i][j-1] +1 # insert
                b = distance_table[i-1][j]+1  # delete
                c = distance_table[i-1][j-1]  +1# substitution
                distance_table[i][j] = min(a,b,c)

    distance = distance_table[len(source)][len(target)]
    return distance


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))
