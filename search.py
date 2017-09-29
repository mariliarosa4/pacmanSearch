"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
 
  print problem #recebido do arquivo searchAgents funcao registerInitialState
  node = {}
  node["proximo"] = None
  node["acao"] = None
  abertos = {}
  caminho = []
  lista = util.Stack()#pilha
  state = problem.getStartState()
  node["state"] = state
  lista.push(node)
 
  while not lista.isEmpty():
    node = lista.pop()
    state = node["state"]
   
    abertos[hash(state)] = True

    if problem.isGoalState(state) == True:
      break

    for child in problem.getSuccessors(state):
      if not abertos.has_key(hash(child[0])):
        sub_node = {}
        sub_node["proximo"] = node
        sub_node["acao"] = child[1]
        sub_node["state"] = child[0]
        lista.push(sub_node)
  while node["acao"] != None:
    caminho.insert(0, node["acao"])#insere no inicio do array
    node = node["proximo"]

  return caminho
  

def breadthFirstSearch(problem):

  node = {}
  node["proximo"] = None
  node["acao"] = None
  abertos = {}
  caminho = []
  
  fila = util.Queue()#fila fifo
  state = problem.getStartState()

  node["state"] = state
  fila.push(node)

  while not fila.isEmpty():
    node = fila.pop()
    state = node["state"]
    
    abertos[state] = True
    if problem.isGoalState(state) == True:
      break

    for child in problem.getSuccessors(state):
      if child[0] not in abertos:
        sub_node = {}
        sub_node["proximo"] = node
        sub_node["acao"] = child[1]
        sub_node["state"] = child[0]
        fila.push(sub_node)

  while node["acao"] != None:
    caminho.insert(0, node["acao"])
    node = node["proximo"]

  return caminho
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  print problem

  frontier = util.FasterPriorityQueue()
  visited = {}

  state = problem.getStartState()
  node = {}
  node["parent"] = None
  node["action"] = None
  node["state"] = state
  node["cost"] = 0
  node["eval"] = heuristic(state, problem)
  # A* use f(n) = g(n) + h(n)
  frontier.push(node, node["cost"] + node["eval"])

  while not frontier.isEmpty():
    node = frontier.pop()
    state = node["state"]
    cost = node["cost"]
    v = node["eval"]
    #print state

    if visited.has_key(state):
      continue

    visited[state] = True
    if problem.isGoalState(state) == True:
      break

    for child in problem.getSuccessors(state):
      if not visited.has_key(child[0]):
        sub_node = {}
        sub_node["parent"] = node
        sub_node["state"] = child[0]
        sub_node["action"] = child[1]
        sub_node["cost"] = child[2] + cost
        sub_node["eval"] = heuristic(sub_node["state"], problem)
        frontier.push(sub_node, sub_node["cost"] + node["eval"])

  actions = []
  while node["action"] != None:
    actions.insert(0, node["action"])
    node = node["parent"]

  return actions
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


