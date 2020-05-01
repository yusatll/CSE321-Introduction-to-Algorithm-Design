# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$           Ahmet Yuşa Telli         $$$$$
# $$$$$             151044092              $$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PART 1 ££££££££££££££££££££££££££££££££££
# £££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££

def Part1():
    print("Part 1 ")
    A = [[10, 17, 13, 28, 23],
         [17, 22, 16, 29, 23],
         [24, 28, 22, 34, 24],
         [11, 13, 6, 17, 7],
         [45, 44, 32, 37, 23],
         [36, 33, 19, 21, 6],
         [75, 66, 51, 53, 34]]

    for a in A:
        print(a)

    print("m x n : ",len(A), "x", len(A[0]))
    isSpacialArray(A)
    found = findMinElement(A) # part C
    min = [row[0] for row in found]
    index = [row[1] for row in found]
    print("Minimum Elements in each row:", min)
    print("Minimum Elements indexes: ", index)
    print("")
    print("")

# Part B
def isSpacialArray(arr):
    m = len(arr)
    n = len(arr[0])
    indexes = []
    for i in range(1,m):                    # 1 < i < m
        for j in range(1, n):               # 1 < j < n
            for k in range(i+1, m):         # i + 1 < k < m
                for l in range(j+1, n):     # j + 1 < l < n
                    t1 = arr[i][j] + arr[k][l]      #  A[i, j ] +  A[k, l]
                    t2 = arr[i][l] + arr[k][j]      #  A[i, l ] +  A[k, j ]
                    if t2 < t1:             # push the list
                        indexes.append((i, j))
                        indexes.append((k, l))
                        indexes.append((i, l))
                        indexes.append((k, j))

                        # return False
    # return True
    if indexes:
        print("It is not a Special Array.")
        findIncorrectIndex(indexes)
    else:
        print("It is a Special Array.")
# Part B
def findIncorrectIndex(indexes):
    freq = {}
    for item in indexes:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    v = 0
    wrongIndex = ()
    for key, value in freq.items():
        # print("{} : {}".format(key,value))
        if v < value:
            v = value
            wrongIndex = key
    print("The Wrong value is in this index:", wrongIndex)


# Part C
def findMinElement(a):
    if not a:
        return []

    s, index = minimum(a[0])
    # index = a[0].index(s)
    a = findMinElement(a[1:])
    a.insert(0, (s, index))
    return a

def minimum(a):
    minElement = 9999999
    minIndex = -1
    for i in range(len(a)):
        if minElement > a[i]:
            minIndex = i
            minElement = a[i]
    return minElement, minIndex


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PART 2 ££££££££££££££££££££££££££££££££££
# £££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££

def Part2():
    # find the kth element
    print("PART 2")
    A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    B = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    C = [1, 2, 3, 7, 8, 11, 12]
    D = [4, 5, 6, 9, 10, 14, 15]

    a = [1, 3, 5, 6, 7, 8, 9, 11]
    b = [2, 4, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22]

    k = 18
    print("A",a)
    print("B",b)
    print("Find the",k,"'th element in A, B arrays.")
    kth = findElement(a, b, 0, 0, len(a), len(b), k)
    if kth == -1:
        print("The",k,"value is not in these arrays.(start from 1)")
    else:
        print("The", k, "value is :",kth)

    print("")
    print("")

def findElement(A, B, leftA, leftB, rightA, rightB, k):
    #print("A:", A[leftA:rightA], "\nB:", B[leftB:rightB], "k", k)
    if k > len(A) + len(B):
        return -1

    if leftA >= rightA:
        return B[leftB + k - 1]
    if leftB >= rightB:
        return A[leftA + k - 1]

    midA = int((leftA + rightA) / 2)
    midB = int((leftB + rightB) / 2)
    forA = midA - leftA + 1
    forB = midB - leftB + 1

    if forA + forB > k:
        if A[midA] > B[midB]:
            rightA = midA - 1
        else:
            rightB = midB - 1
    else:
        if A[midA] < B[midB]:
            leftA = midA + 1
            k = k - forA
        else:
            leftB = midB + 1
            k = k - forB

    return findElement(A, B, leftA, leftB, rightA, rightB, k)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PART 3 ££££££££££££££££££££££££££££££££££
# £££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££

def Part3():
    print("PART 3")
    # for i in range(2,10,1): # [2:10) 2 3 .. 9
    #     print(i)
    # print("")
    # for j in range(10,2,-1):    # (2:10] 10 9 .. 3
    #     print(j)

    A = [5, -6, 6, 7, -6, 7, -4, 3]
    print("A:",A)
    max_sum = findSubArray(A, 0, len(A) - 1)
    print("Largest Total is:", max_sum)
    print("")
    print("")

def splitArray(arr, left, mid, right):
    return summation(arr, mid, left, -1) + summation(arr, mid + 1, right + 1, 1)


def findSubArray(arr, left, right):
    if left == right:
        return arr[left]
    mid = int((left + right) / 2)

    max1 = findSubArray(arr, left, mid)
    max2 = findSubArray(arr, mid + 1, right)
    max3 = splitArray(arr, left, mid, right)
    if max1 > max2 and max1 > max3:
        return max1
    elif max2 > max1 and max2 > max3:
        return max2
    else:
        return max3

def summation(arr, a, b, t):
    temp = 0
    total = -1000
    for i in range(a, b, t):
        temp += arr[i]
        if temp > total:
            total = temp
    return total


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PART 4 ££££££££££££££££££££££££££££££££££
# £££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££

def Part4():
    print("PART 4")
    graph = [[0, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 0, 1, 0]
             ]

    graph2 = [[0, 1, 2, 3],
             [4, 5, 6, 7],
             [8, 9, 10, 11],
             [12, 13, 14, 15]
             ]

    graph3 = [[0, 1, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0]
             ]

    graph4 = [[0, 1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0]
              ]

    # EXAMPLE ONE #########
    color = [-1] * len(graph3)
    color[0] = 1
    q = [0]

    print("The Graph is:")
    for a in graph3:
        print(a)

    if checkBipartition(graph3, color, q):
        print("Yes It is a bipartite graph.")
    else:
        print("No It is not a bipartite graph.")

    print("")

    # EXAMPLE TWO #########
    colors = [-1] * len(graph4)
    colors[0] = 1
    q2 = [0]
    print("The Graph is:")
    for a in graph4:
        print(a)

    if checkBipartition(graph4, colors, q2):
        print("Yes It is a bipartite graph.")
    else:
        print("No It is not a bipartite graph.")

    print("")
    print("")

def checkBipartition(g, colors, q):
    if not q:
        return True

    u = q.pop()
    if g[u][u] == 1:
        return False

    for v in range(len(g)):
        if g[u][v] == 1:
            if colors[v] == -1:     # if not colored before
                colors[v] = 1 - colors[u]
                q.append(v)
            elif colors[v] == colors[u]:    # if colored before
                return False

    return checkBipartition(g, colors, q)
"""
for v in range(len(g)):
    if g[u][v] == 1 and colors[v] == -1:
        colors[v] = 1 - colors[u]
        q.append(v)
    elif g[u][v] == 1 and colors[v] == colors[u]:
        return False
"""


# sol alt üçgen ve sağ üst üçgen kontrolü için yazılmış kod.
# bu part için sonradan uygun bulunamamıştır. Kullanılmayacaktır.

# def deneme2(graph, left, right):
#     g1 = graph[:1] # ilk satır
#
#     if left >= right:
#         return False
#
#     g1 = [row[left] for row in graph]
#     g2 = [row[right] for row in graph]
#     print(g1)
#     print(g2)
#     if check(g1,g2):
#         deneme1(graph,left+1,right-1)
#         print("yes")
#     else:
#         print("no")
#         return False
#     return True
#
# def deneme1(graph, left, right):
#     g1 = graph[:1] # ilk satır
#
#     while left <= right:
#         g1 = [row[left] for row in graph]
#         g2 = [row[right] for row in graph]
#         print(g1)
#         print(g2)
#         if check(g1,g2):
#             #deneme1(graph[1:-1],0,len(graph)-1)
#             left+=1
#             right-=1
#             print("yes")
#         else:
#             print("no")
#             return False
#
#     return True
#
# def check(g1,g2):
#     print(g1[0],g2[-1])
#     if len(g1) == 1:
#         if g1 == g2:
#             return True
#         else:
#             return False
#
#     if g1[0] == g2[-1]:
#         return check(g1[1:], g2[:-1])
#     else:
#         return False




# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PART 5 ££££££££££££££££££££££££££££££££££
# £££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££

def Part5():
    C = [5, 11, 2, 21, 5, 7, 8, 12, 13, '-']
    P = ['-', 7, 9, 5, 21, 7, 13, 10, 14, 20]
    print("PART - 5")
    print("Calculate Maximum Gain")
    print("Cost list:", C, "\nPrice list", P)
    P.remove(P[0])
    C.remove(C[len(C) - 1])
    maxG, p, c = maxGain(C, P)
    print("Maximum Gain is:", maxG)
    print("Max Gain's Cost is:", c)
    print("Max Gain's Price is:", p)
    print("The index in Cost:", C.index(c))
    print("The index in Price:", P.index(p)+1)


def maxGain(A, B):
    if len(A) == 1:
        if B[0] <= A[0]:
            print(B[0], "liraya alınan ürünü", A[0], "liraya satarak", B[0]-A[0],"lira zarar ettik.")
        return B[0] - A[0], B[0], A[0]

    t1, b1, a1 = maxGain(A[int(len(A) / 2):], B[int(len(B) / 2):])
    t2, b2, a2 = maxGain(A[:int(len(A) / 2)], B[:int(len(B) / 2)])

    if t1 > t2:
        return t1, b1, a1
    else:
        return t2, b2, a2

def main():
    Part1()
    Part2()
    Part3()
    Part4()
    Part5()


if __name__ == '__main__':
    main()
