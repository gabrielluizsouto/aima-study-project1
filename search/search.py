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
from game import Directions
from typing import List

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

def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    path_to_state = []
    problem_start = (problem.getStartState(), "", 0)
    visited_list = set()
    to_visit_list = util.Stack()

    to_visit_list.push((problem_start, path_to_state))
    # print("problem_start:", problem_start)
    # print("visited_list:", visited_list)
    # print("to_visit_list:", to_visit_list)
    # print("++++++++++")

    while to_visit_list.isEmpty() != True:
        current_state, path_to_state = to_visit_list.pop()
        current_node, action_to_node, action_cost = current_state
        # print("current_state, path_to_state", current_state, path_to_state)
        # print("current_node, action_to_node, cost_to_node", current_node, action_to_node, cost_to_node)

        visited_list.add(current_node)
        # print("visited_list", visited_list)

        if problem.isGoalState(current_node):
            # print("path_to_state", path_to_state)
            return path_to_state
        
        successors = problem.getSuccessors(current_node)
        # print("successors", successors)
        for successor in successors:
            if successor[0] not in visited_list:
                new_path_to_state = path_to_state + [successor[1]]
                to_visit_list.push((successor, new_path_to_state))

        # print("to_visit_list", to_visit_list)
        # input("--- Press Enter to continue...") # Or "Press any key to continue..."

    # print("path_to_state", path_to_state)
    return path_to_state

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    problem_start = (problem.getStartState(), "", 0)
    visited_list = set()
    to_visit_list = util.Queue()
    path_to_state = []

    to_visit_list.push((problem_start, path_to_state))
    visited_list.add(problem.getStartState())
    # print("problem_start : ", problem_start)
    # print("visited_list : ", visited_list)
    # print("to_visit_list : ", to_visit_list)
    # print("path_to_state : ", path_to_state)
    # print("+++++++++++")

    while to_visit_list.isEmpty() != True:
        current_state, path_to_state = to_visit_list.pop()
        current_node, action_to_node, action_cost = current_state

        # print("current_node : ", current_node)
        # print("path_to_state : ", path_to_state)
        # print("visited_list : ", visited_list)

        if problem.isGoalState(current_node) == True:
            return path_to_state

        successors = problem.getSuccessors(current_node)
        # print("successors : ", successors)
        for successor in successors:
            if successor[0] not in visited_list:
                new_path_to_state = path_to_state + [successor[1]]
                to_visit_list.push((successor, new_path_to_state))
                visited_list.add(successor[0])
    
        # print("to_visit_list : ", to_visit_list)
        # input("--- Press Enter to continue...") # Or "Press any key to continue..."
    return path_to_state

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    path_to_state = {}
    to_visit_list = util.PriorityQueue()
    visited_list = set()
    problem_start = problem.getStartState()

    path_to_state[problem_start] = []
    to_visit_list.push(problem_start, 0)
    # print("path_to_state:", path_to_state)
    # print("problem_start:", problem_start)
    # print("visited_list:", visited_list)
    # print("to_visit_list:", to_visit_list)

    while to_visit_list.isEmpty() != True:
        print("----------------")
        # current_node, instruction_to_reach_node, current_cost = to_visit_list.pop()
        current_node = to_visit_list.pop()
        # print("current_state:", current_node)

        visited_list.add(current_node)
        # print("visited_list:", visited_list)

        if problem.isGoalState(current_node):
            # print("path_to_state:", path_to_state[current_node])
            return path_to_state[current_node]
        
        successors = problem.getSuccessors(current_node)
        # print("successors:", successors)
        for successor in successors:
            successor_node, successor_instruction_to_reach, successor_cost_of_instruction = successor

            total_cost_to_reach_successor = successor_cost_of_instruction + problem.getCostOfActions(path_to_state[current_node])
            if successor_node not in visited_list:
                to_visit_list.update(successor_node, total_cost_to_reach_successor)
                if successor_node not in path_to_state or problem.getCostOfActions(path_to_state[successor_node]) > total_cost_to_reach_successor:
                    path_to_state[successor_node] = path_to_state[current_node] + [successor_instruction_to_reach]

        # print("to_visit_list:", to_visit_list)
        # print("path_to_state:", path_to_state)
        # input("--- Press Enter to continue...") # Or "Press any key to continue..."
    return False
    
def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Same code as uniformCostSearch, but with heuristic added to the cost."""
    path_to_state = {}
    to_visit_list = util.PriorityQueue()
    visited_list = set()
    problem_start = problem.getStartState()

    path_to_state[problem_start] = []
    to_visit_list.push(problem_start, 0)

    while to_visit_list.isEmpty() != True:
        current_node = to_visit_list.pop()

        visited_list.add(current_node)

        if problem.isGoalState(current_node):
            return path_to_state[current_node]
        
        successors = problem.getSuccessors(current_node)
        for successor in successors:
            successor_node, successor_instruction_to_reach, successor_cost_of_instruction = successor

            total_cost_to_reach_successor = successor_cost_of_instruction + problem.getCostOfActions(path_to_state[current_node]) + heuristic(successor_node, problem)
            if successor_node not in visited_list:
                to_visit_list.update(successor_node, total_cost_to_reach_successor)
                if successor_node not in path_to_state or problem.getCostOfActions(path_to_state[successor_node]) > total_cost_to_reach_successor:
                    path_to_state[successor_node] = path_to_state[current_node] + [successor_instruction_to_reach]
    return False
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
