import Queue as queue
import copy
import numpy as np



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


    for i in range(col):
        for j in range(row):
            if puzzle[i][j] != goalState[i][j]:
                misplacedTiles += 1 #if the position in the puzzle does not match the one in
                                    #the goal puzzle, then increment the heurisitc/misplacedTiles
    return misplacedTiles



def aStarMTH(puzzle, goalState):
    #A* with the Misplaced Tile heuristic
    col = len(puzzle[0])
    row = len(puzzle)

    puzzleQ = queue.Queue()
    puzzleQ.put(puzzle)

    while not puzzleQ.empty():
        currentPuzzle = puzzleQ.get()
        numpPuzzle = np.array(currentPuzzle)
        findSpace = np.where(numpPuzzle==0)




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
    puzzle = [[1, 5, 2], [4, 0, 3], [7, 8, 6]]
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    x = 0
    y = 2
    print(MTHeuristic(puzzle, goalState))
    #uniformCostSearch(puzzle, goalState)





if __name__ == "__main__":
    main()
