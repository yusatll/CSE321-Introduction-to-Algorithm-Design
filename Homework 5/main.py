# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 1                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def optimumPlan(ny, sf, m):
    best_cost_N = [0]
    best_cost_S = [0]
    for i in range(1, len(ny) + 1):
        best_cost_N.append(ny[i - 1] + minimum(best_cost_N[i - 1], m + best_cost_S[i - 1]))
        best_cost_S.append(sf[i - 1] + minimum(best_cost_S[i - 1], m + best_cost_N[i - 1]))

    return minimum(best_cost_N[len(best_cost_N) - 1], best_cost_S[len(best_cost_N) - 1])


def minimum(a, b):
    return a if a < b else b


def Part1():
    print("PART 1")
    M = 10
    print("Moving Cost:", M)
    NY1 = [1, 3, 20, 30]
    SF1 = [50, 20, 2, 4]
    plan1 = optimumPlan(NY1, SF1, M)
    print("NY:", NY1, "SF:", SF1)
    print("Optimum Plan 1:  ", plan1)
    print("")

    NY2 = [12, 3, 5, 3]
    SF2 = [3, 17, 2, 4]
    plan2 = optimumPlan(NY2, SF2, M)
    print("NY:", NY2, "SF:", SF2)
    print("Optimum Plan 2:  ", plan2)
    print("")
    print("")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 2                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def sortstart(s, f):
    # insertion sort
    for i in range(1, len(s)):
        key = s[i]
        key2 = f[i]
        j = i - 1
        while j >= 0 and key < s[j]:
            s[j + 1] = s[j]
            f[j + 1] = f[j]
            j -= 1
        s[j + 1] = key
        f[j + 1] = key2

    return s, f


def OptimalListOfSessions(start, finish):
    n = len(start)
    # start, finish = zip(*sorted(zip(start, finish)))
    start, finish = sortstart(start, finish)

    total = n * [1]
    k = 0
    listeler = [[] for _ in range(n)]

    for i in range(0, len(start)):
        # print("İLK", start[i], "başladı", finish[i], "de bitecek ")
        listeler[k].append(start[i])
        for j in range(1, len(start)):
            # print("start[j]", start[j], "finish[i]", finish[i])
            if start[j] >= finish[i]:
                # print(start[j], "başladı", finish[j], "de bitecek >= finish[i]", finish[i])
                total[k] += 1
                listeler[k].append(start[j])
                i = j
        k += 1

    print("Max activity start:", listeler[total.index(max(total))])


def Part2():
    print("PART 2")
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print("Activities Start  Time", start)
    print("Activities Finish Time", finish)
    OptimalListOfSessions(start, finish)
    print("")
    print("")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 3                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def sumSubset(liste):
    if not liste:
        return [[]], {0}
    result = sumSubset(liste[1:])

    if type(result) is not tuple:
        # result bulundu
        return result
    else:
        sub, sumSet = result

    for s in sub[:]:
        newSub = [liste[0]] + s
        newSum = sum(newSub)
        if newSum == 0:
            return newSub
        elif newSum not in sumSet:
            sub.append(newSub)
            sumSet.add(newSum)

    # for i, s in enumerate(sub):
    #     print(i, s, sum(s))
    # print("-------------")
    return sub, sumSet


def Part3():
    S = [-1, 6, 4, 2, 3, -7, -5]
    print("PART 3")

    values = [10, 3, 9, -5, 4, 2, -7, 8]
    subs = sumSubset(values)
    print("Array:", values)
    print("Subset:", subs, "Total:", sum(subs))
    print("")
    subs = sumSubset(S)
    print("Array:", S)
    print("Subset:", subs, "Total:", sum(subs))
    print("")
    print("")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 4                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def alignmentSeq(seq1, seq2):
    match = 0
    match_score = 2
    mistmatch = 0
    mistmatch_score = -2
    gap = 0
    gap_score = -1

    if len(seq1) < len(seq2):
        seq1, seq2 = seq2, seq1

    checkAlign = False
    while len(seq1) > 0 and len(seq2) > 0:
        broken = False
        matched = False
        for i in range(len(seq1)):
            for j in range(len(seq2)):
                # print("s1i", seq1[i], "s2j", seq2[j])
                if seq1[i] == seq2[j]:
                    checkAlign = True
                    match += 1
                    seq1 = seq1[i + 1:]
                    seq2 = seq2[j + 1:]
                    # print("seq1", seq1, "seq2", seq2)
                    broken = True
                    matched = True
                    break

            if not matched and checkAlign:
                # print("gap:", seq1[i])
                gap += 1
            if not checkAlign:
                # print("mistmatch: ",seq1[i])
                mistmatch += 1

            if broken:
                break

    print("Match:", match, "Gap:", gap, "Mistmatch:", mistmatch)
    cost = (match * match_score) + (mistmatch * mistmatch_score) + (gap * gap_score)
    print("Cost:", cost)


def wateramca(seq1, seq2):
    match = 0
    match_score = 2
    mistmatch = 0
    mistmatch_score = -2
    gap = 0
    gap_score = -1
    m = len(seq1) + 1
    n = len(seq2) + 1
    # table = [[0] * m] * n
    table = [[0 for x in range(m)] for y in range(n)]

    for i in range(1, len(seq2)+1):   # [0,9]
        for j in range(1, len(seq1)+1):   # [0,5]
            maxi = max(table[i-1][j], table[i][j-1])
            if seq1[j-1] == seq2[i-1]:
                table[i][j] = maxi + match_score
            else:
                if maxi <= 0:
                    table[i][j] = 0
                elif maxi > 0:
                    table[i][j] = maxi + gap_score


    for a in table:
        print(a)

    matchedChar = []
    mistedChar = []
    gapIndex = []
    for i in range(1, len(table)):
        maxElement = max(table[i])
        indexes = findMaxIndex(table[i])
        if maxElement == 0:
            # print("mistmatch", table[i])
            # print("mist", seq1[i-1], seq2[i-1])
            mistedChar.append(seq1[i-1])
            mistedChar.append(seq2[i-1])
            mistmatch += 1
        elif len(indexes) > 1:      # iki tane index var
            # print(indexes, i)
            if (table[i][indexes[0]-1] + table[i-1][indexes[0]]) < (table[i][indexes[1]-1] + table[i-1][indexes[1]]):
                gapIndex.append(indexes[0])
                matchedChar.append(seq1[indexes[0]])
            else:
                gapIndex.append(indexes[1])
                matchedChar.append(seq1[indexes[1]-1])
        if len(indexes) == 1:
            gapIndex.append(indexes[0])
            matchedChar.append(seq1[indexes[0]-1])

    print("Misted Characters: ", mistedChar)
    print("Matched Characters:",matchedChar)
    for i in range(len(gapIndex)-1):
        if gapIndex[i] + 1 != gapIndex[i+1]:
            gap = abs(gapIndex[i] + 1 - gapIndex[i+1])

    cost = ((len(matchedChar)//2) * match_score) + (len(mistedChar) * mistmatch) + (gap * gap_score)
    # print("Gap:",gap)
    print("Cost:", cost)


def findMaxIndex(table):
    maxi = -1
    indexes = []
    for i in range(len(table)):
        if maxi <= table[i] != 0:
            maxi = table[i]

    for i in range(len(table)):
        if maxi == table[i]:
            indexes.append(i)

    return indexes


def Part4():
    print("PART 4")
    seqA = "ALIGNMENT"
    seqB = "SLIME"
    print("Sequence A:", seqA, "Sequence B:", seqB)
    # alignmentSeq(seqA, seqB)
    wateramca(seqA, seqB)

    print("")
    print("")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 5                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def findTwoMins(a):
    arr = a[:3]
    min1 = min(arr)
    arr.remove(min1)
    min2 = min(arr)

    a.remove(min1)
    a.remove(min2)
    return min1, min2


def Part5():
    print("PART 5")
    array = [1, 4, 5, 7, 3, 4, 8, 2]
    a = array[:]
    total = 0
    operation = 0
    while len(array) >= 3:
        min1, min2 = findTwoMins(array)
        total += min1
        operation += total
        total += min2
        operation += total

    if len(array) == 2:
        lastm1, lastm2 = array
        if lastm1 < lastm2:
            total += lastm1
            operation += total
            total += lastm2
            operation += total
        else:
            total += lastm2
            operation += total
            total += lastm1
            operation += total
    else:
        lastm1, = array
        total += lastm1
        operation += total

    print("Array:", a)
    print("Operation Count:", operation)
    print("Total:", total)


def main():
    Part1()
    Part2()
    Part3()
    Part4()
    Part5()


if __name__ == '__main__':
    main()
