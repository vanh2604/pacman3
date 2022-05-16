# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    # stack: ((x,y),[path]) #
    stack = Stack()

    visited = []
    path = []

    if problem.isGoalState(problem.getStartState()):
        return []
    stack.push((problem.getStartState(), []))

    while(True):

        # điểm dừng : không thể tìm thấy đường đi
        if stack.isEmpty():
            return []

        # Lấy thông tin của trạng thái hiện tại
        xy, path = stack.pop()

        # đến được điểm cần đến
        if problem.isGoalState(xy):
            return path
        if xy not in visited:
            visited.append(xy)
            succ = problem.getSuccessors(xy)
            if succ:
                for item in succ:
                    if item[0] not in visited:
                        newPath = path + [item[1]]
                        stack.push((item[0], newPath))
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    # queue: ((x,y),[path]) #
    queue = Queue()

    visited = []
    path = []

    # Check if initial state is goal state #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Start from the beginning and find a solution, path is empty list #
    queue.push((problem.getStartState(), []))

    while(True):
        # Terminate condition: can't find solution #
        if queue.isEmpty():
            return []
        # Get informations of current state #
        xy, path = queue.pop()  # Take position and path
        if problem.isGoalState(xy):
            return path

        if xy not in visited:
            visited.append(xy)
        # Get successors of current state #
            succ = problem.getSuccessors(xy)

        # Add new states in queue and fix their path #
            if succ:
                for item in succ:
                    if item[0] not in visited:

                        # Lectures code:
                        # All impementations run in autograder and in comments i write
                        # the proper code that i have been taught in lectures
                        # if problem.isGoalState(item[0]):
                        #   return path + [item[1]]

                        newPath = path + [item[1]]  # Calculate new path
                        queue.push((item[0], newPath))
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    _pQueue = PriorityQueue()
    _startNode = problem.getStartState()
    _visited = {}
    _cost = 0
    _action = []
    _pQueue.push((_startNode, _action, _cost), _cost)

    while not _pQueue.isEmpty():
        _current = _pQueue.pop()
        if problem.isGoalState(_current[0]):
            return _current[1]
        if _current[0] not in _visited:
            _visited[_current[0]] = True
            for next, act, co in problem.getSuccessors(_current[0]):
                if next and next not in _visited:
                    _pQueue.push(
                        (next, _current[1] + [act], _current[2] + co), _current[2] + co)
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "* YOUR CODE HERE *"
    from util import PriorityQueue
    _pQueue = PriorityQueue()
    _startNode = problem.getStartState()
    _visited = {}
    _cost = 0
    _action = []
    _pQueue.push((_startNode, _action, _cost), _cost)
    while not _pQueue.isEmpty():
        _current = _pQueue.pop()
        if(problem.isGoalState(_current[0])):
            return _current[1]
        if(_current[0] not in _visited):
            _visited[_current[0]] = True
            for next, act, co in problem.getSuccessors(_current[0]):
                if next and next not in _visited:
                    _pQueue.push(
                        (next, _current[1] + [act], _current[2] + co), _current[2] + heuristic(next, problem) + co)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
