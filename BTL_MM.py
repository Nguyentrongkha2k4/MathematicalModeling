"""From Bradley, Hax and Maganti, 'Applied Mathematical Programming', figure 8.1."""
import numpy as np

from ortools.graph.python import min_cost_flow


def main():
    """MinCostFlow simple interface example."""
    # Instantiate a SimpleMinCostFlow solver.
    smcf = min_cost_flow.SimpleMinCostFlow()

    # Define four parallel arrays: sources, destinations, capacities,
    # and unit costs between each pair. For instance, the arc from node 0
    # to node 1 has a capacity of 15.
    start_nodes = np.random.randint(0,0,0)
    for i in range(0, 99):
        if i+1 % 10 == 0:
            start_nodes = np.append(start_nodes, [i])
        elif i+1 < 90:
            start_nodes = np.append(start_nodes, [i, i])
        else:
            start_nodes = np.append(start_nodes, [i])
    print(start_nodes, len(start_nodes))
    end_nodes = np.random.randint(0,0,0)
    for i in range(0, 99):
        if i+1 < 90 and i+1 % 10 != 0:
            end_nodes = np.append(end_nodes, [i + 1, i + 10])
        elif i+1 % 10 == 0:
            end_nodes = np.append(end_nodes, [i + 10])
        else:
            end_nodes = np.append(end_nodes, [i + 1])
    print(end_nodes, len(end_nodes))
    capacities = np.random.randint( 100, 200, len(start_nodes))
    print(capacities, len(capacities))
    unit_costs = np.random.randint(1, 10, len(start_nodes))
    print(unit_costs, len(unit_costs))
    # Define an array of supplies at each node.
    supplies = [0]*100
    supplies[11] = 200
    supplies[25] = -200
    print(supplies)
    # Add arcs, capacities and costs in bulk using numpy.
    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs
    )

    # Add supply for each nodes.
    smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)

    # Find the min cost flow.
    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print("There was an issue with the min cost flow input.")
        print(f"Status: {status}")
        exit(1)
    print(f"Minimum cost: {smcf.optimal_cost()}")
    print("")
    print(" Arc    Flow / Capacity Cost")
    solution_flows = smcf.flows(all_arcs)
    costs = solution_flows * unit_costs
    for arc, flow, cost in zip(all_arcs, solution_flows, costs):
        if cost != 0:
            print(
                f"{smcf.tail(arc):1} -> {smcf.head(arc)}  {flow:3}  / {smcf.capacity(arc):3}       {cost}"
            )


if __name__ == "__main__":
    main()