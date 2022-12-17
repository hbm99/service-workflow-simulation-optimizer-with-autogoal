from walking_problem.heuristic_problem_utils import astar_search, path_actions, path_states
from walking_problem.walking_problem_utils import WalkingProblem
from environment import ShopEnviroment, Cell

shop_environment = ShopEnviroment(8, ["A"], 1)

start = (0, 0)
for item_to_buy in [(5, 5), (2, 3)]:
    p = WalkingProblem(start, [item_to_buy], shop_map = shop_environment.map)

    sol = astar_search(p)
    print(path_actions(sol))
    print(path_states(sol))
    
    start = item_to_buy