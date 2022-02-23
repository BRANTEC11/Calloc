import time
import ast
def initiate():
    # playlistnode.c D:
    songList = []
    lenList = []
    sideLen = input(f"Please input the length of one side of your cassette: ")
    if ((sideLen == '') or ((sideLen.isnumeric() == False) or (int(sideLen) < 0))):
        fullLen = 0
        print("\nError: input was not a valid integer, defaulting to length 0.")
    else:
        fullLen = int(sideLen) * 2
    currLen = 0
    addList = []
    addListSec = []
    numSong = 0
    partition = 0
    choice = 'init'
    while (choice != "q"):
        i = 0
        print("\nCassette Size: " + str(fullLen) + " minutes")
        print("Total Length: " + time.strftime('%H:%M:%S', time.gmtime(currLen))) #str(len2Min(currLen)) + ":" + str(len2Sec(currLen)))
        l = 0
        longestName = 0
        while (l < len(songList)):
            if (len(songList[l]) > longestName):
                longestName = len(songList[l])
            l += 1
        longestPrint = int(len(str(numSong))) + longestName
        while (i < numSong):
            if ((i == partition) and (i != 0)):
                g = 0
                while (g < (int(len(str(numSong))) + 1)):
                    print("-",end='')
                    g += 1
                print("|",end='')
                g = 0
                while (g < (longestName + 2)):
                    print("-",end='')
                    g += 1
                print("|",end='')
                print("---------")
            k = i + 1
            m = int(len(str(numSong)))
            while (int(len(str(k))) != m):
                print("", end=' ')
                k *= 10 
            print(str(i + 1) + " | " + songList[i], end='')
            j = longestTrack(songList) - len(songList[i])
            while (j != 0):
                print("", end=' ')
                j -= 1
            print(" | " + time.strftime('%H:%M:%S', time.gmtime(time2sec(lenList[i])))) #+ " | " + time.strftime('%M:%S', time.gmtime(addList[i])) )
            i += 1
        
        if (partition != 0):
            i = 0
            add = 0
            addSec = 0
            while (i < len(lenList)):
                add += int(lenList[i])
                addSec += time2sec(int(lenList[i]))
              
                addListSec.append(addSec)
                i += 1
            sideA = addListSec[partition-1]
            sideB = addListSec[numSong-1] - addListSec[partition-1]
            print("Side A: " + time.strftime('%H:%M:%S', time.gmtime(sideA)))
            print("Side B: " + time.strftime('%H:%M:%S', time.gmtime(sideB)))


        print("\nMain Menu")
        print("a  - add song(s)")                       #DONE
        print("al - automatically allocate tracks")     #DONE
        print("am - manually allocate tracks")          #DONE
        print("m  - move song")                         #DONE
        print("r  - remove song")                       #DONE
        print("ra - remove ALL songs")                  #DONE
        print("re - rename a song")                     #DONE
        print("cl - change track length")               #DONE
        print("cs - change cassette side length")       #DONE
        print("im - import infoList")                   #DONE
        print("ex - export infoList")                   #DONE
        print("q  - quit\n")                            #DONE
        choice = input()
        if (choice == "q"):
            print("Successfully quit program!")
        if (choice == "a"):
            infoList = addSong(songList,lenList, currLen, numSong, addList)
            songList = infoList[0]
            lenList = infoList[1]
            currLen = infoList[2]
            numSong = infoList[3]
            addList = infoList[4]
            partition = 0
        if (choice == "r"):
            infoList = removeSong(songList,lenList, currLen, numSong, addList)
            songList = infoList[0]
            lenList = infoList[1]
            currLen = infoList[2]
            numSong = infoList[3]
            addList = infoList[4]
            partition = 0
        if (choice == "ra"):
            infoList = removeAllSong(songList,lenList, currLen, numSong, addList)
            songList = infoList[0]
            lenList = infoList[1]
            currLen = infoList[2]
            numSong = infoList[3]
            addList = infoList[4]
            succ = infoList[5]
            if (succ == 1):
                partition = 0
        if (choice == "re"):
            songList = renameTrack(songList,lenList, currLen, numSong, addList)
        if (choice == "cl"):
            infoList = relenTrack(songList,lenList, currLen, numSong, addList)
            songList = infoList[0]
            lenList = infoList[1]
            currLen = infoList[2]
            numSong = infoList[3]
            addList = infoList[4]
            partition = 0
        if (choice == "m"):
            infoList = moveTrack(songList, lenList, numSong)
            songList = infoList[0]
            lenList = infoList[1]
            partition = 0
        if (choice == "cs"):
            sideLen = input(f"Please input the new length of one side of your cassette: ")
            if ((sideLen == '') or ((sideLen.isnumeric() == False) or (int(sideLen) < 0))):
                fullLen = 0
                print("\nError: input was not a valid integer, defaulting to length 0.")
            else:
                fullLen = int(sideLen) * 2
                partition = 0
        if (choice == "al"):
            partition = allocation(songList,lenList, currLen, numSong, addList, fullLen)
        if (choice == "am"):
            partitionN = allocationManual()
            if (partitionN.isnumeric()):
                partitionN = int(partitionN)
                if (partitionN < numSong):  
                    partition = partitionN
                else:
                    print("\nError: the chosen song number does not exist within the playlist, returning to Main Menu.")
            else:
                print("\nError: input was not a valid integer, returning to Main Menu.")
        if (choice == "ex"):
            proList = [songList, lenList, currLen, numSong, addList, partition, fullLen]
            print("")
            print(proList)
        if (choice == "im"):
            print("Please input your infoList")
            print("")
            initList = input()
            if ((initList != '') and (initList[0] == '[') and (initList[-1] == ']') and (initList[1] == '[')):
                infoList = ast.literal_eval(initList)
            else: 
                print("\nError: the input was not a valid infoList, returning to Main Menu.")
                continue
            songList1 = infoList[0]
            lenList1 = infoList[1]
            currLen1 = infoList[2]
            numSong1 = infoList[3]
            addList1 = infoList[4]
            if (fullLen == infoList[6]) and (numSong == 0):
                partition = infoList[5]
                print("\nSuccesfully imported the infoList.")
            else:
                partition = 0
                print("\nWarning: Different cassette size detected, resetting partition.")
            songList.extend(songList1)
            lenList.extend(lenList1)
            currLen += currLen1
            numSong += numSong1
            addList.extend(addList1)
    return

def allocationManual():
    partition = input(f"\nPlease input the last song of Side A: ")
    return partition

def allocation(songList,lenList, currLen, numSong, addList, fullLen):
    addList = []
    addListSec = []
    i = 0
    add = 0
    addSec = 0
    sideLen = (fullLen/2)*60
    while (i < len(lenList)):
        add += int(lenList[i])
        addSec += time2sec(int(lenList[i]))
        addList.append(add)
        addListSec.append(addSec)
        i += 1
    partition = 0
    i = 0
    smallest = 100000000000
    while (i < len(addListSec)):
        if ((abs((addListSec[len(addListSec) - 1] - addListSec[i]) - addListSec[i]) < smallest) and ((addListSec[len(addListSec) - 1] - addListSec[i]) <= sideLen) and (addListSec[i] <= sideLen)):
            smallest = abs((addListSec[len(addListSec) - 1] - addListSec[i]) - addListSec[i])
            partition = i + 1
        i += 1
    if (partition == 0):
        print("Error: Track List cannot be allocated given the cassette size.")
    else: 
        print("Track List Successfully Allocated!")
    return partition
def addSong(songList,lenList,currLen,numSong, addList): 
    numNewSong = input(f"\nPlease input the amount of songs you would like to add: ")
    if (numNewSong.isnumeric() == False):
        return [songList, lenList, currLen, numSong, addList]
    numNewSong = int(numNewSong)
    onSong = 0
    while (onSong < numNewSong):
        print("\nSong " + str(numSong+1) + " | Total Length: " + time.strftime('%H:%M:%S', time.gmtime(currLen)))
        songList.append(input(f"Please input the song name: "))
    
        leng = input(f"Please input the song length (MMSS): ")
        if ((leng.isnumeric() == False) or (len(leng) > 4)):
            lenList.append(0)
        else:
            leng = int(leng)
            lenList.append(leng)
        currLen += int(time2sec(lenList[numSong]))
        addList.append(currLen)
        onSong += 1
        numSong += 1
    i = 0
    return [songList, lenList, currLen, numSong, addList]

def removeSong(songList,lenList,currLen,numSong, addList): 
    numDel = input(f"\nPlease enter the number of the song you would like to delete: ")
    if ((numDel.isnumeric() == True) and (int(numDel) <= numSong) and (int(numDel) > 0)):
        numDel = int(numDel)
    else:
        print("\nError: input was not a full number within 1 and " + str(numSong) + ".")
        return [songList, lenList, currLen, numSong, addList]
    currLen -= time2sec(lenList[numDel-1])
    numSong -= 1
    songList.pop(numDel-1)
    lenList.pop(numDel-1)
    addList.pop(numDel-1)
 
    return [songList, lenList, currLen, numSong, addList]
   
def removeAllSong(songList,lenList,currLen,numSong, addList): 
    choice = input(f"\nAre you sure you want to remove every song? [y/n]: ")
    if (choice == 'y'):
        songList = []
        lenList = []
        currLen = 0
        numSong = 0
        addList = []
        succ = 1
    else:
        succ = 0
    return [songList, lenList, currLen, numSong, addList,succ]
    
def renameTrack(songList,lenList, currLen, numSong, addList):
    numRen = input(f"\nPlease enter the number of the song you would like to rename: ")
    if ((numRen.isnumeric() == True) and (int(numRen) <= numSong) and (int(numRen) > 0)):
        numRen = int(numRen)
    else:
        print("\nError: input was not a full number within 1 and " + str(numSong) + ".")
        return songList
    newName = str(input(f"Please input the new name for track '{songList[numRen-1]}': "))
    if (newName != ""):
         songList[numRen-1] = newName
    return songList

def moveTrack(songList,lenList, numSong):
    numMove1 = input(f"\nPlease enter the number of the track you would like to move: ")
    numMove2 = input(f"Please enter the number of other the track you would like to move: ")
    if (((numMove1.isnumeric() == True) and (int(numMove1) <= numSong) and (int(numMove1) > 0)) and ((numMove2.isnumeric() == True) and (int(numMove2) <= numSong) and (int(numMove2) > 0))):
        numMove1 = int(numMove1)
        numMove2 = int(numMove2)
    else:
        print("\nError: one or more of the inputs was not a full number within 1 and " + str(numSong) + ".")
        return [songList, lenList]
    if ((numMove1 == "") or (numMove2 == "")) :
         return [songList, lenList]
    else:
        songList = swap(songList, (numMove1-1), (numMove2-1))
        lenList = swap(lenList, (numMove1-1), (numMove2-1))
    return [songList, lenList]

def relenTrack(songList,lenList, currLen, numSong, addList):
    numRen = input(f"\nPlease enter the number of the song you would like to change the length: ")
    if ((numRen.isnumeric() == True) and (int(numRen) <= numSong) and (int(numRen) > 0)):
        numRen = int(numRen)
    else:
        print("\nError: input was not a full number within 1 and " + str(numSong) + ".")
        return [songList,lenList, currLen, numSong, addList]
    oldLen = int(lenList[numRen-1])
    #print(oldLen)
    newLen = input(f"Please input the new length for track '{songList[numRen-1]}': ")
   
    if ((newLen.isnumeric() == False) or (len(newLen) > 4)):
        return [songList,lenList, currLen, numSong, addList]
    else:
        newLen = int(newLen)
        lenList[numRen-1] = newLen
        currLen -= (time2sec(oldLen) - time2sec(newLen))
        return [songList,lenList, currLen, numSong, addList]
  
def longestTrack(songList):
    i = 0
    longest = 0
    while (i < len(songList)):
        if (len(songList[i]) > longest):
            longest = len(songList[i])
        i += 1
    return longest

def time2sec(x):
    digit = [int(a) for a in str(x)]
    digit.reverse()
    total = 0
    i = 0
    multSec = 10
    multMin = 60
    while (i < len(digit)):
        if i == 0:
            total += digit[i]
        elif i == 1:
            total += (digit[i] * multSec)
        else:
            total += (digit[i] * multMin)
            multMin = multMin * 10
        i += 1
    return total

def swap(list, p1, p2):
    list[p1], list[p2] = list[p2], list[p1]
    return list

if __name__ == '__main__':
    initiate()
