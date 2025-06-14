from dwave.samplers import SimulatedAnnealingSampler

def solve_number_partitioning(number_set):
    """
    Solves the number partitioning problem for a given set of numbers
    using a classical simulated annealer.

    Args:
        number_set (list of int/float): The list of numbers to partition.

    Returns:
        A tuple containing the two partitioned sets and their sum difference.
    """
    print(f"--- Solving for set: {number_set} ---")

    # 1. Build the QUBO Formulation from our derived math
    Q = {}
    total_sum = sum(number_set)

    # Linear terms (h_i)
    for i in range(len(number_set)):
        s_i = number_set[i]
        # Key for linear term is (i, i)
        Q[(i, i)] = 4 * (s_i**2) - 4 * total_sum * s_i

    # Quadratic terms (J_ij)
    for i in range(len(number_set)):
        for j in range(i + 1, len(number_set)):
            s_i = number_set[i]
            s_j = number_set[j]
            # Key for quadratic term is (i, j)
            Q[(i, j)] = 8 * s_i * s_j

    # 2. Instantiate a local sampler
    sampler = SimulatedAnnealingSampler()

    # 3. Solve the QUBO
    # num_reads specifies how many times to run the annealing process
    sampleset = sampler.sample_qubo(Q, num_reads=100)

    # 4. Interpret and Display the Best Result
    best_solution = sampleset.first.sample
    energy = sampleset.first.energy
    
    print(f"Lowest energy found: {energy:.2f}")
    
    set_A = [number_set[i] for i, bit in best_solution.items() if bit == 0]
    set_B = [number_set[i] for i, bit in best_solution.items() if bit == 1]
    
    sum_A = sum(set_A)
    sum_B = sum(set_B)
    diff = abs(sum_A - sum_B)

    print(f"Set A: {set_A} (Sum: {sum_A})")
    print(f"Set B: {set_B} (Sum: {sum_B})")
    print(f"Difference: {diff}\n")

    return set_A, set_B, diff

if __name__ == "__main__":
    # --- Test Cases ---
    set1 = [10, 7, 6, 3] # Should find a perfect partition
    solve_number_partitioning(set1)

    set2 = [5, 3, 2, 6, 10, 8, 1] # A more complex case
    solve_number_partitioning(set2)

    set3 = [23, 54, 12, 88, 4, 32] # Even larger numbers
    solve_number_partitioning(set3)