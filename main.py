import random
import simpy
from environment import Product
from simulation import run_shop



def main():
    random.seed(42)
    shop_size = 8
    num_cashiers = 1
    list_product = [Product('Pizza', 10), Product('Pan', 5)]
    products = {item.name : item for item in list_product}
    simulation_time = 4
    shelves_distribution = [1, 0, 1]
    
    # Run the simulation
    env = simpy.Environment()
    env.process(run_shop(env, num_cashiers, shop_size, products, shelves_distribution))
    env.run(until=simulation_time)
    
    
    


if __name__ == "__main__":
    main()



