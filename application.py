import Queue as queue
import copy
import numpy as np
import heapq

def uniformCostSearch(puzzle, goalState):
    col = len(puzzle[0])
    row = len(puzzle)
    #obtain dimensions of puzzle

    depth = 0
    maxQ = 0
    expanded = 0
    puzzleQ = queue.Queue()
    puzzleQ.put(puzzle)

    print "\n"
    print "Expanding state "
    print puzzle[0]
    print puzzle[1]
    print puzzle[2]
    print "\n"

    while not puzzleQ.empty():
        if maxQ < puzzleQ.qsize():
            maxQ = puzzleQ.qsize()

        currentPuzzle = puzzleQ.get()
        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)

        if currentPuzzle == puzzle:
            depth = 0 #if currentPuzzle is the given puzzle then the depth should be 0
        else:
            depth += 1

        index_row = findSpace[0][0]
        index_col = findSpace[1][0]

        if currentPuzzle == goalState:
            print "maximum queue size: ", maxQ
            print "number of nodes expanded: ", expanded
            return

        print "The best state to expand with a g(n) = ", depth, " is..."
        print currentPuzzle[0]
        print currentPuzzle[1]
        print currentPuzzle[2], "Expanding this node..."
        expanded += 1

        #check if space can move left
        if (index_col - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row][index_col-1] = temp[index_row][index_col-1], temp[index_row][index_col]
            puzzleQ.put(temp)

        #check if space can move right
        if (index_col + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row][index_col+1] = temp[index_row][index_col+1], temp[index_row][index_col]
            puzzleQ.put(temp)

        #check if space can move up
        if (index_row - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row-1][index_col] = temp[index_row-1][index_col], temp[index_row][index_col]
            puzzleQ.put(temp)

        #check if space can move down
        if (index_row + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[index_row][index_col], temp[index_row+1][index_col] = temp[index_row+1][index_col], temp[index_row][index_col]
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
    maxQ = 0
    heapq.heapify(heap)
    F_N = heuristic(puzzle, goalState)
    heapq.heappush(heap, (F_N, depth, puzzle))

    print "\n"
    print "Expanding state "
    print puzzle[0]
    print puzzle[1]
    print puzzle[2]
    print "\n"

    while len(heap) != 0:
        if maxQ < len(heap):
            maxQ = len(heap)

        currentNode = heapq.heappop(heap)
        currentPuzzle = currentNode[2]
        if currentPuzzle == puzzle:
            currentDepth = 0 #if the node in the queue is the root node then depth should be 0
        else:
            currentDepth = currentNode[1]+1 #add 1 because we moved on to the child node so depth increases
        currentH_N = heuristic(currentPuzzle, goalState)

        print "The best state to expand with a: g(n) = ", currentDepth, " and h(n) = ", currentH_N, " is..."
        print currentPuzzle[0]
        print currentPuzzle[1]
        print currentPuzzle[2], "Expanding this node..."
        print "\n"

        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)

        index_row = findSpace[0][0]
        index_col = findSpace[1][0]

        if currentPuzzle == goalState:
            print "Goal!!"
            print "\n"
            print "To solve this problem the search algorithm expanded a total of", numExpansions, " nodes"
            print "The maximum number of nodes in the queue at any one time was ", maxQ,
            print "The depth of the goal node was ", currentDepth
            return currentPuzzle

        #enqueue the expanded child nodes

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

        numExpansions += 1

def main():
    choice = input("Welcome to my (John Shin's) 170 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own. \n")

    if choice == 1:
        diff_level = input("Please enter a difficulty level for your default puzzle from (1-5): ")
        if diff_level == 1:
            print "You chose the trivial level"
            puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif diff_level == 2:
            print "You chose the very easy level"
            puzzle = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        elif diff_level == 3:
            print "You chose the easy level"
            puzzle = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
        elif diff_level == 4:
            print "You chose the doable level"
            puzzle = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
        elif diff_level == 5:
            print "You chose the oh boy level"
            puzzle = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]

    if choice == 2:
        print "Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle delimiting the numbers with a space. RET only when finished. \n"
        first_row, second_row, third_row, puzzle = [], [], [], []
        print "Enter the first row: "
        index0,index1,index2=map(int,raw_input().split())
        first_row.append(index0)
        first_row.append(index1)
        first_row.append(index2)

        print "Enter the second row: "
        index0,index1,index2=map(int,raw_input().split())
        second_row.append(index0)
        second_row.append(index1)
        second_row.append(index2)

        print "Enter the third row: "
        index0,index1,index2=map(int,raw_input().split())
        third_row.append(index0)
        third_row.append(index1)
        third_row.append(index2)

        puzzle.append(first_row)
        puzzle.append(second_row)
        puzzle.append(third_row)

    algorithm_choice = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) the Manhattan Distance Heuristic. ")
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    if algorithm_choice == 1:
        #uniform cost search
        uniformCostSearch(puzzle, goalState)
    elif algorithm_choice == 2:
        #A* using missing tile heuristic
        aStar(puzzle, goalState, MTHeuristic)
    elif algorithm_choice == 3:
        #A* using manhattan distance heuristic
        aStar(puzzle, goalState, MHDHeuristic)


    #Sample puzzles generated
    #puzzle = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
    #puzzle = [[4, 1, 3], [2, 8, 5], [7, 0, 6]]
    #puzzle = [[0, 2, 3], [1, 5, 6], [4, 7, 8]]
    #puzzle = [[1, 3, 0], [4, 2, 5], [7, 8, 6]]
    #puzzle = [[1, 2, 3], [7, 4, 5], [0, 8, 6]]

if __name__ == "__main__":
    main()
