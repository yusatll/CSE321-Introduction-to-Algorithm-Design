# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 1                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#  decrease-and-conquer
from random import random
from re import split


def DAC(row, mixed):
    if row:
        mixed.append(row[0])
        mixed.append(row[-1])
        DAC(row[1:-1], mixed)
        return mixed
    return row


def Part1():
    # 1 -> black
    # 0 -> white
    print("$$$ PART 1 $$$")
    print("Black - White Boxes")
    print("1 -> Black\n0 -> White")
    WB = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mixed = []
    print("First Box:", WB)
    mixed = DAC(WB, mixed)
    print("Mixed Box:", mixed)
    print("\n\n")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 2                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# hafif agirlikta olan listeyi bulur
def weighbridge(liste1, liste2):
    if sum(liste1) > sum(liste2):
        return liste2
    elif sum(liste1) < sum(liste2):
        return liste1
    else:  # iki tarafta ayni agirlikta ise uzun olani dondur
        return liste1 if len(liste1) > len(liste2) else liste2


def list_split(liste):
    half = len(liste) // 2
    return liste[:half], liste[half:]


def fakeFinder(fake, eleman):
    if len(fake) != 1:
        firstHalf, secondHalf = list_split(fake)
        # print("first Half:",firstHalf,"Second Half:", secondHalf)
        fake = weighbridge(firstHalf, secondHalf)
        if len(fake) == 1:
            if fake[0] != 0:
                return -1
            eleman = fake[0]
            return eleman
        eleman = fakeFinder(fake, eleman)

    return eleman


def Part2():
    print("$$$ PART 2 $$$")
    print("Find Fake Coin in list.")
    fake = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
    fakecoin = -1
    print("1 -> Coin\n0 -> Fake")
    print("Coins List:", fake)
    print("List Length:",len(fake))
    faker = fakeFinder(fake, fakecoin)
    if faker != -1:
        index = fake.index(0)
        print("Fake Coin's Index:", index)
    else:
        print("There is no fake coin.")
    print("\n\n")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 3                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# INSERTION SORT
def InstertionSort(unsorted):
    swap = 0
    for i in range(1, len(unsorted)):
        key = unsorted[i]
        j = i - 1
        while j >= 0 and key < unsorted[j]:
            unsorted[j + 1] = unsorted[j]
            j -= 1
            swap += 1
        unsorted[j + 1] = key
    return swap


# QUICK SORT
def Partition(unsorted, left, right):
    i = left - 1
    pivot = unsorted[right]
    swap = 0
    for j in range(left, right):
        if unsorted[j] <= pivot:
            i += 1
            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
            swap += 1
    unsorted[i + 1], unsorted[right] = unsorted[right], unsorted[i + 1]
    swap += 1
    return (i + 1, swap)

def QuickSort(unsorted, left, right):
    swap = 0
    if left < right:
        pi, swap = Partition(unsorted, left, right)
        QuickSort(unsorted, left, pi - 1)
        QuickSort(unsorted, pi + 1, right)

    return swap


def Part3():
    print("$$$ PART 3 $$$")
    print("Insertion - Quick Sort Discuss")

    arr1 = [10, 9, 8, 7, 6, 5]
    arr2 = [5, 6, 7, 8, 9, 10]
    arr3 = [5, 10, 6, 9, 7, 8]

    print("First Array ", arr1)
    print("Second Array", arr2)
    print("Third Array ", arr3)

    si1 = InstertionSort(arr1)
    si2 = InstertionSort(arr2)
    si3 = InstertionSort(arr3)

    sq1 = QuickSort(arr1, 0, len(arr1) - 1)
    sq2 = QuickSort(arr2, 0, len(arr2) - 1)
    sq3 = QuickSort(arr3, 0, len(arr3) - 1)
    print("First Array Results:")
    print("Swap Insertion 1:", si1, "Swap Quick 1:", sq1)

    print("Second Array Results:")
    print("Swap Insertion 2:", si2, "Swap Quick 2:", sq2)

    print("Third Array Result:")
    print("Swap Insertion 3:", si3, "Swap Quick 3:", sq3)
    print("\n\n")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 4                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def Part4():
    print("$$$ PART 4 $$$")
    print("Unsorted Array - Median")
    median = [12, 9, 2, 13, 20, 1, 17, 10, 7, 22, 11, 30]
    print("Unsorted Array:", median)
    InstertionSort(median)
    l = len(median)
    if l % 2 == 0: # even
        print("Median:", (median[int(l / 2)] + median[int(l / 2) - 1]) / 2)
    else: # odd
        print("Median:", median[int(l / 2)])
    print("\n\n")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                                      PART 5                                   $
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# A listesindeki TÜM sublist leri buluyoruz.
# bu listelerin elemanlarının toplamını bulmak için
# diğer fonksiyona gönderiyoruz.
def findSubLists(liste):
    if not liste:
        return [[]]
    sub = findSubLists(liste[1:])
    return sub + [[liste[0]] + i for i in sub]


# subliste içindeki listelerin toplamlarının büyüklüğünü kontrol ediyoruz
# olması gerekenden küçük olanları eliyoruz.
def totalCheck(sublist, maxsum):
    sublists = []
    for i in sublist:
        if sum(i) >= maxsum:
            sublists.append(i)
    return sublists


# gelen sublists ler içindeki elemanların çarpımlarını
# bulup. en küçük çarpımı olan listenin indexini
# geri gönderir.
# find the minimum number of multiplication of items in the
# sub-array.
def findMultiplications(sublists):
    mult = []
    t = 1
    for i in range(0, len(sublists)):
        for j in range(0, len(sublists[i])):
            t *= sublists[i][j]
        mult.append(t)
        t = 1
    return mult.index(min(mult))


def Part5():
    print("$$$ PART 5 $$$")
    print("Optimal Sub-Array")
    A = [2, 4, 7, 5, 22, 11]
    maxsum = (max(A) + min(A)) * (len(A) / 4)
    print("An Array:", A, "\nMinimum sum:", maxsum)
    allsublists = findSubLists(A)
    sublists = totalCheck(allsublists, maxsum)
    minindex = findMultiplications(sublists)
    print("Optimal list:", sublists[minindex])


Part1()
Part2()
Part3()
Part4()
Part5()
