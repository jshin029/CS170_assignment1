import Queue as queue
import copy
import numpy as np
import heapq


def uniformCostSearch(puzzle, goalState):
    col = len(puzzle[0])
    row = len(puzzle)

    puzzleQ = queue.Queue()
    puzzleQ.put(puzzle)

    while not puzzleQ.empty():
        currentPuzzle = puzzleQ.get()
        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)

        x = findSpace[0][0]
        y = findSpace[1][0]

        #check if space can move up
        if (x - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x-1][y] = temp[x-1][y], temp[x][y]
            if temp == goalState:
                print("we made it")
                break
            puzzleQ.put(temp)

        #check if space can move down
        if (x + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
            if temp == goalState:
                print("we made it")
                break
            puzzleQ.put(temp)

        #check if space can move left
        if (y - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
            if temp == goalState:
                print("we made it")
                break
            puzzleQ.put(temp)

        #check if space can move right
        if (y + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
            if temp == goalState:
                print("we made it")
                break
            puzzleQ.put(temp)

def MTHeuristic(puzzle, goalState):
    misplacedTiles = 0
    col = len(puzzle[0])
    row = len(puzzle)

    if puzzle == goalState:
        return 0

    for i in range(col):
        for j in range(row):
            if puzzle[i][j] != goalState[i][j]:
                misplacedTiles += 1 #if the position in the puzzle does not match the one in
                                    #the goal puzzle, then increment the heurisitc/misplacedTiles
    return misplacedTiles - 1 #subtract the misplacedTiles because the function above counts the empty tile as well


def aStarMTH(puzzle, goalState):
    #A* with the Misplaced Tile heuristic
    col = len(puzzle[0])
    row = len(puzzle)
    numExpansions = 0

    heap = []
    depth = 0
    F_N = MTHeuristic(puzzle, goalState)
    heapq.heapify(heap)
    heapq.heappush(heap, (F_N, depth, puzzle))

    while len(heap) != 0:
        currentNode = heapq.heappop(heap)
        currentPuzzle = currentNode[2]
        if currentPuzzle == puzzle:
            currentDepth = currentNode[1] #if the node in the queue is the root node then depth should be 0
        else:
            currentDepth = currentNode[1] + 1 #add 1 because we moved on to the child node so depth increases
        currentH_N = MTHeuristic(currentPuzzle, goalState)

        print "The best state to expand with a: g(n) = ", currentDepth, " and h(n) = ", currentH_N, " is..."
        print currentPuzzle

        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)

        x = findSpace[0][0]
        y = findSpace[1][0]


        if currentPuzzle == goalState:
            print "number of expansions: ", numExpansions
            print "depth of goal state: ", currentDepth
            return currentPuzzle

        #enqueue the expanded child nodes
        #check if space can move up
        if (x - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x-1][y] = temp[x-1][y], temp[x][y]
            F_N = MTHeuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))


        #check if space can move down
        if (x + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
            F_N = MTHeuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        #check if space can move left
        if (y - 1) >= 0:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
            F_N = MTHeuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        #check if space can move right
        if (y + 1) < row:
            temp = copy.deepcopy(currentPuzzle)
            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
            F_N = MTHeuristic(temp, goalState)
            newF_N = F_N + currentDepth
            heapq.heappush(heap, (newF_N, currentDepth, temp))

        numExpansions += 1



    # while not puzzleQ.empty():
    #     currentPuzzle = puzzleQ.get()
    #     numpPuzzle = np.array(currentPuzzle)
    #     findSpace = np.where(numpPuzzle==0)



# function general-search(problem, QUEUEING-FUNCTION)
# nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
# loop do
#  if EMPTY(nodes) then return "failure"
#    node = REMOVE-FRONT(nodes)
#  if problem.GOAL-TEST(node.STATE) succeeds then return node
#     nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
#  end

def makePuzzle():
    print("hello")
    # print("Enter your puzzle, use a zero to represent the blank")
    # row1 = input("Enter the first row, use space or tabs between numbers: ")
    # row2 = input("Enter the second row, use space or tabs between numbers: ")
    # row3 = input("Enter the third row, use space or tabs between numbers: ")

def main():
    puzzle = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    x = 0
    y = 2
    aStarMTH(puzzle, goalState)
    #uniformCostSearch(puzzle, goalState)
    # heap = []
    # heapq.heapify(heap)
    # heapq.heappush(heap, (1, 2, [1, 2, 3, 4]))
    # heapq.heappush(heap, (3, 2, [2, 4, 1, 2]))
    # heapq.heappush(heap, (2, 2, [1, 4, 1, 2]))
    # heapq.heappush(heap, (1, 2, [1, 4, 1, 2]))
    #
    #
    # print(heapq.heappop(heap))
    # print(heapq.heappop(heap))
    # print(heapq.heappop(heap))
    # print(heapq.heappop(heap))







if __name__ == "__main__":
    main()
