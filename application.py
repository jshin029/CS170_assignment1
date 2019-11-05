import Queue as queue
import copy
import numpy as np
import heapq

def uniformCostSearch(puzzle, goalState):
    col = len(puzzle[0])
    row = len(puzzle)
    #obtain dimensions of puzzle

    depth = 0
    puzzleQ = queue.Queue()
    puzzleQ.put(puzzle)

    while not puzzleQ.empty():
        currentPuzzle = puzzleQ.get()
        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)

        index_row = findSpace[0][0]
        index_col = findSpace[1][0]

        #check if space can move up
        if (index_row - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row-1][index_col] = temp[index_row-1][index_col], temp[index_row][index_col]
            if temp == goalState:
                print depth + 1
                return
            puzzleQ.put(temp)

        #check if space can move down
        if (index_row + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row+1][index_col] = temp[index_row+1][index_col], temp[index_row][index_col]
            if temp == goalState:
                print depth
                return
            puzzleQ.put(temp)

        #check if space can move left
        if (index_col - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row][index_col-1] = temp[index_row][index_col-1], temp[index_row][index_col]
            if temp == goalState:
                print depth
                return
            puzzleQ.put(temp)

        #check if space can move right
        if (index_col + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row][index_col+1] = temp[index_row][index_col+1], temp[index_row][index_col]
            if temp == goalState:
                print depth
                return
            puzzleQ.put(temp)

def MTHeuristic(puzzle, goalState):
    misplacedTiles = 0
    col = len(puzzle[0])
    row = len(puzzle)
    #obtain dimensions of puzzle

    if puzzle == goalState: #heuristic should be 0 if already goalState
        return 0

    for i in range(col):
        for j in range(row):
            if puzzle[i][j] != goalState[i][j]:
                misplacedTiles += 1 #if the position in the puzzle does not match the one in
                                    #the goal puzzle, then increment the heuristic/misplacedTiles
    return misplacedTiles - 1 #subtract the misplacedTiles because the function above counts the empty tile as well

def MHDHeuristic(puzzle, goalState):
    totalMoves = 0
    col = len(puzzle[0])
    row = len(puzzle)
    #obtain dimensions of puzzle

    if puzzle == goalState: #heuristic should be 0 if already goalState
        return 0

    for i in range(col):
        for j in range(row):
            #if the number in given puzzle doesn't match the one in goalState then calculate moves
            if puzzle[i][j] != goalState[i][j] and puzzle[i][j] != 0:
                numpPuzzle = np.array(goalState)
                findSpace = np.where(numpPuzzle==puzzle[i][j]) #returns np array with the col and row index

                goal_row = findSpace[0][0] #finds the col index of correct position of number
                goal_col = findSpace[1][0] #finds the row index of correct position of number

                #calculates how many moves to get from initial position to the correct position
                totalMoves += abs(i - goal_row) + abs(j - goal_col)

    return totalMoves

def aStar(puzzle, goalState, heuristic):
    #A* with the Misplaced Tile heuristic
    col = len(puzzle[0])
    row = len(puzzle)
    numExpansions = 0
    #obtain dimensions of puzzle
    heap = []
    depth = 0
    F_N = heuristic(puzzle, goalState)
    heapq.heapify(heap)
    heapq.heappush(heap, (F_N, depth, puzzle))

    while len(heap) != 0:
        currentNode = heapq.heappop(heap)
        currentPuzzle = currentNode[2]
        if currentPuzzle == puzzle:
            currentDepth = 0 #if the node in the queue is the root node then depth should be 0
        else:
            currentDepth = currentNode[1]+1 #add 1 because we moved on to the child node so depth increases
        currentH_N = heuristic(currentPuzzle, goalState)

        print "The best state to expand with a: g(n) = ", currentDepth, " and h(n) = ", currentH_N, " is..."
        print currentPuzzle

        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)

        index_row = findSpace[0][0]
        index_col = findSpace[1][0]


        if currentPuzzle == goalState:
            print "number of expansions: ", numExpansions
            print "depth of goal state: ", currentDepth
            return currentPuzzle

        #enqueue the expanded child nodes
        #check if space can move up
        if (index_row - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row-1][index_col] = temp[index_row-1][index_col], temp[index_row][index_col]
            F_N = heuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        #check if space can move down
        if (index_row + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row+1][index_col] = temp[index_row+1][index_col], temp[index_row][index_col]
            F_N = heuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        #check if space can move left
        if (index_col - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row][index_col-1] = temp[index_row][index_col-1], temp[index_row][index_col]
            F_N = heuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        #check if space can move right
        if (index_col + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row][index_col+1] = temp[index_row][index_col+1], temp[index_row][index_col]
            F_N = heuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        numExpansions += 1

#def makePuzzle():
    # print("Enter your puzzle, use a zero to represent the blank")
    # row1 = input("Enter the first row, use space or tabs between numbers: ")
    # row2 = input("Enter the second row, use space or tabs between numbers: ")
    # row3 = input("Enter the third row, use space or tabs between numbers: ")

def main():
    puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    aStar(puzzle, goalState, MHDHeuristic)
    #uniformCostSearch(puzzle, goalState)


if __name__ == "__main__":
    main()
