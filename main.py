import simpy
from environment import Product
from simulation import run_shop, profits_in_time
from fuzzy_logic import set_up_fuzzy_tip
from tabu_search import TabuSearch


def main():
    shop_size = 100
    num_cashiers = 20
    list_product = [Product('Pizza', 10), Product('Pan', 5), Product('Tomate', 3), Product('Lechuga', 1), Product('Juguete', 20), Product('Cerveza', 3), Product('Chocolate', 2)]
    products = {item.name : item for item in list_product}
    simulation_time = 60 * 60
    shelves_count= 10

    # shelves_distribution = [1, 0, 1, 2, 3, 4, 5, 6, 1, 2]
    
    # Run the simulation
    # env = simpy.Environment()
    # tipping = set_up_fuzzy_tip(len(shelves_distribution))
    # env.process(run_shop(env, num_cashiers, shop_size, products, shelves_distribution, tipping))
    # env.run(until=simulation_time)

    ts= TabuSearch(shelves_count, list_product,shop_size, num_cashiers, simulation_time, 5)



if __name__ == "__main__":
    main()
    print(profits_in_time[-1])



