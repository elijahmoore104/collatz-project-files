def getHailstoneSequence(n):
    """
        A Collatz Path is defined as a Path that follows:
        Take some number n:
            if n is even,  path(i+1) = path(i)/2
            if n is odd, path (i+1) = 3*path(i) + 1
    """
    path = []
    while n != 1:
        path.append(n)

        if n % 2 == 1:
            n = 3*n+1
        elif n < 1: 
            break
        else:
            n = n/2

    path.append(1)
    return path

def getReverseCollatzPath(max_depth):
    """
        Parameter 'depth' that determines the depth of the Collatz path

        In a similar fashion to Collatz, we can construct a reverse Collatz path using:
        for any i, r_path(i+1)[1] = r_path(i)*2
        for (i-1)%3 = 0, then r_path(i+1)[2] = (r_path(i)-1)/3
    """
    r_path = []
    start_num = 1

    for i in range(0, max_depth): # i is the current level of the reverse path
        level_arr = []

        if i == 0:
            level_arr.append(start_num)
        elif i > 0: #skip the first iteration, otherwise IOOR exception
            for j in range(0, len(r_path[i-1])): # j is how many items are in the arr
                curr_num = r_path[i-1][j]

                if j < len(r_path[i-1]):
                    level_arr.append(curr_num*2)

                if (curr_num-1) % 3 == 0 and (curr_num-1)/3 > 1:
                    level_arr.append((curr_num-1)/3)
        r_path.append(level_arr)

    return r_path


def getCollatzDepth(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            return i
        else:    
            pass
    return 0

def getIndexPositions(arr, item):
    outarr = []
    for i in range(len(arr)):
        if arr[i] == item:
            outarr.append(i)
    return outarr

def plotArr(arr, display_str="-bo", display_str2="or"):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.plot(arr, display_str)
    ax.plot([arr.index(max(arr))], [max(arr)], display_str2)

    plt.show()

