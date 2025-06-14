# Solving Number Partitioning with a QUBO Formulation

This project demonstrates how to solve a classic NP-hard problem, **Number Partitioning**, by formulating it as a Quadratic Unconstrained Binary Optimization (QUBO) problem and solving it using the D-Wave Ocean SDK.

The entire solution runs locally using the SDK's `SimulatedAnnealingSampler`, showcasing the ability to develop and validate complex optimization models without requiring access to quantum hardware.

## The Number Partitioning Problem

Given a set of numbers `S`, the goal is to partition it into two disjoint subsets, `A` and `B`, such that the absolute difference between the sum of their elements is minimized.

## My QUBO Formulation Approach

To map this problem to a format solvable by an annealer, I derived the following QUBO:

1.  **Binary Variables:** I assigned a binary variable `qᵢ ∈ {0, 1}` to each number `sᵢ` in the set `S`. The assignment rule is:

    - If `qᵢ = 0`, `sᵢ` belongs to Set A.
    - If `qᵢ = 1`, `sᵢ` belongs to Set B.

2.  **Objective Function:** The goal is to minimize the squared difference between the sums of the two sets:
    `H = (Sum(A) - Sum(B))²`

3.  **Mathematical Derivation:** By substituting the binary variables, the objective function becomes:
    `H = (∑ sᵢ(1 - qᵢ) - ∑ sᵢqᵢ)² = (K - 2∑ sᵢqᵢ)²`
    where `K` is the total sum of all numbers in `S`.

    Expanding this expression and simplifying (using the property that `qᵢ² = qᵢ`) yields the final QUBO form with linear (`hᵢ`) and quadratic (`Jᵢⱼ`) coefficients:

    - `hᵢ = 4sᵢ² - 4Ksᵢ`
    - `Jᵢⱼ = 8sᵢsⱼ`

This formulation is implemented in `number_partition_solver.py`.

## How to Run This Project

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Set up the environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Run the solver:**
    ```bash
    python number_partition_solver.py
    ```

## Example Output

```
--- Solving for set: [10, 7, 6, 3] ---
Lowest energy found: -676.00
Set A: [10, 3] (Sum: 13)
Set B: [7, 6] (Sum: 13)
Difference: 0
```
