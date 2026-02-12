def RotateTemp(Vect, k):
    n = len(Vect)

    if n == 0:
        return

    k = k % n

    Temp = [None] * n

    for i in range(0, n):
        Temp[(i + k) % n] = Vect[i]

    for i in range(0, n):
        Vect[i] = Temp[i]

    return Vect


def RotateOneByOne(Vect, k):
    n = len(Vect)

    if n == 0:
        return

    k = k % n

    for step in range(1, k + 1):
        last = Vect[n - 1]

        for i in range(n - 1, 0, -1):
            Vect[i] = Vect[i - 1]

        Vect[0] = last

    return Vect

def Reverse(Vect, left, right):
    while left < right:
        temp = Vect[left]
        Vect[left] = Vect[right]
        Vect[right] = temp

        left = left + 1
        right = right - 1


def RotateReverse(Vect, k):
    n = len(Vect)

    if n == 0:
        return

    k = k % n

    Reverse(Vect, 0, n - 1)
    Reverse(Vect, 0, k - 1)
    Reverse(Vect, k, n - 1)
    
    return Vect