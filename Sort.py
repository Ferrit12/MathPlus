import random
import time
import threading
import Basic

def Rearrange(lst, OrderLst):
    OutLst = []
    for i in range(len(lst)):
        OutLst.append(lst[OrderLst[i]])
    return OutLst

def RandomList(Len, Min, Max):
    Out = []
    for i in range(Len):
        Out.append(random.randrange(Min, Max))
    return Out

def isSorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True

def LinearSort(lst):
    Out = []
    for i in range(len(lst)):
        Out.append(min(lst))
        lst.remove(min(lst))
    return Out

def BogoSort(lst):
    while not isSorted(lst):
        random.shuffle(lst)
    return lst.copy()

def StalinSort(lst):
    lastNum = float("-inf")
    Out = []
    for i in range(len(lst)):
        if lst[i] > lastNum:
            Out.append(lst[i])
            lastNum = lst[i]
    return Out

def BubbleSort(lst):
    while not isSorted(lst):
        for i in range(len(lst) - 1):
            if lst[i + 1] < lst[i]:
                New = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = New
    return lst.copy()

def SleepThenAppend(time):
    time.sleep(time)
    Out.append(time)

def SleepSort(lst):
    global Out
    Out = []

    # Create a list to hold the thread objects
    threads = []

    # Start a thread for each element in the list
    for value in lst:
        thread = threading.Thread(target=SleepThenAppend, args=(value,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return Out

def WhySort(lst):
    Existing = []
    Curr = []
    for i in range(len(lst)):
        Curr = RandomList(len(lst), min(lst), max(lst))
        if not Curr in Existing:
            Existing.append(Curr)
        else:
            while not Curr in Existing:
                Curr = RandomList(len(lst), min(lst), max(lst))
    for j in range(len(Existing)):
        if isSorted(Existing[j]):
            return Existing[j]
