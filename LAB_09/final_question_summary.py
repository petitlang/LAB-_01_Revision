def print_classification():
    """
    Print the complexity classification of each exercise.
    """

    print("===== 1. Classification =====")

    classifications = [
        {
            "exercise": "EX1",
            "problem": "Minimum Dominating Set",
            "decision": "NP-Complete",
            "optimization": "NP-Hard"
        },
        {
            "exercise": "EX2",
            "problem": "Graph Coloring",
            "decision": "NP-Complete",
            "optimization": "NP-Hard"
        },
        {
            "exercise": "EX3",
            "problem": "0/1 Knapsack",
            "decision": "NP-Complete",
            "optimization": "NP-Hard"
        }
    ]

    for item in classifications:
        print(item["exercise"], "-", item["problem"])
        print("Decision Version:", item["decision"])
        print("Optimization Version:", item["optimization"])
        print()

    print("Note:")
    print("Verification is polynomial time.")
    print("Optimization is hard in general.")
    print("For EX3, DP is pseudo-polynomial: O(N * budget).")
    print("It depends on the numeric value of the budget.")
    print("-" * 60)


def print_decision_vs_optimization():
    """
    Print decision version and optimization version for each exercise.
    """

    print("\n===== 2. Decision vs Optimization =====")

    print("\nEX1 - Influencer Coverage")
    print("Optimization version:")
    print("Find the smallest selected user set that covers all users.")
    print("Decision version:")
    print("Given graph G and integer k,")
    print("does there exist a selected user set of size <= k")
    print("such that every user is selected or adjacent to a selected user?")

    print("\nEX2 - Conflict-Free Labeling")
    print("Optimization version:")
    print("Find the minimum number of labels needed.")
    print("Decision version:")
    print("Given graph G and integer k,")
    print("can we assign at most k labels")
    print("so that connected users have different labels?")

    print("\nEX3 - Budget vs Reach")
    print("Optimization version:")
    print("Maximize total influence under the budget.")
    print("Decision version:")
    print("Given budget B and target influence T,")
    print("does there exist a subset of users")
    print("with total cost <= B and total influence >= T?")

    print("\nWhy it matters:")
    print("Decision problems return YES / NO.")
    print("They are useful for complexity classification.")
    print("-" * 60)


def print_scalability():
    """
    Print scalability analysis for N = 1000 and N = 1000000.
    """

    print("\n===== 3. Scalability =====")

    user_sizes = [1000, 1000000]

    for n in user_sizes:
        print(f"\nWhen users = {n}")

        print("EX1:")
        print(f"Exact brute force: O(2^{n})")
        print("Result: impossible for exact brute force.")

        print("EX2:")
        print(f"Exact coloring: O(k^{n})")
        print("Result: impossible for exact backtracking.")

        print("EX3:")
        print("DP: O(N * budget)")
        print("Result: possible only if budget is small.")
        print("If both N and budget are large, DP is too slow.")

    print("\nProblems that fail first:")
    print("EX1 and EX2")
    print("Reason: exact methods are exponential in N.")

    print("\nEX3 note:")
    print("EX3 may work for medium cases because DP is pseudo-polynomial.")
    print("But it fails when both N and budget are very large.")
    print("-" * 60)


def print_engineering_perspective():
    """
    Print practical engineering choices.
    """

    print("\n===== 4. Engineering Perspective =====")

    print("Approximation is acceptable when:")
    print("- N is very large")
    print("- exact solution is too slow")
    print("- the system needs a fast answer")
    print("- a good solution is enough")
    print("- perfect optimality is not required")

    print("\nReal platforms may use:")
    print("- greedy algorithms")
    print("- heuristics")
    print("- approximation algorithms")
    print("- local search")
    print("- priority queues")
    print("- distributed computation")
    print("- machine learning ranking")

    print("\nExamples:")
    print("EX1: pick users that cover many uncovered users.")
    print("EX2: use greedy coloring instead of exact chromatic number.")
    print("EX3: use greedy ratio, heuristics, or optimized DP.")

    print("\nMain trade-off:")
    print("less optimality  =>  more speed and scalability")
    print("-" * 60)


def print_reflection():
    """
    Print reflection about NP-Complete and NP-Hard problems.
    """

    print("\n===== 5. Reflection =====")

    print("Some problems resist efficient solutions because")
    print("they require searching many combinations.")

    print("\nCommon structure of NP-Complete problems:")
    print("- many possible choices")
    print("- strong constraints")
    print("- easy to verify one solution")
    print("- hard to find the best solution")
    print("- combinatorial explosion")

    print("\nExamples:")
    print("EX1: choose subset of users => 2^N subsets")
    print("EX2: choose label for each user => k^N assignments")
    print("EX3: choose subset of users under budget => 2^N subsets")

    print("\nIf P = NP:")
    print("These hard decision problems could be solved in polynomial time.")
    print("EX1: optimal influencer coverage could be found efficiently.")
    print("EX2: minimum labels could be found efficiently.")
    print("EX3: optimal budget selection could be found efficiently.")

    print("\nMeaning for AI systems:")
    print("AI systems cannot always find perfect optimal solutions quickly.")
    print("For scheduling, routing, recommendation and resource allocation,")
    print("they usually search for a good solution, not always the perfect one.")
    print("-" * 60)


def print_edge_cases():
    """
    Print edge cases for the three exercises.
    """

    print("\n===== 6. Edge Cases =====")

    print("\nEmpty graph")
    print("EX1: no users => minimum coverage = 0")
    print("EX2: no users => minimum labels = 0")
    print("EX3: no users => maximum influence = 0")

    print("\nFully connected graph")
    print("EX1: one selected user can cover all users => minimum coverage = 1")
    print("EX2: every pair is connected => minimum labels = N")
    print("EX3: graph structure does not matter directly")

    print("\nBudget = 0")
    print("EX3: if all costs > 0, no user can be selected")
    print("maximum influence = 0")
    print("selected_users = []")
    print("If some users have cost 0, they can be selected.")

    print("\nVery sparse graph")
    print("EX1: more selected users may be needed")
    print("EX2: fewer edges => fewer conflicts => coloring is easier")

    print("\nVery dense graph")
    print("EX1: fewer selected users may cover many users")
    print("EX2: more edges => more constraints => coloring is harder")
    print("-" * 60)


def print_final_conclusion():
    """
    Print final conclusion.
    """

    print("\n===== Final Conclusion =====")

    print("The three exercises show the difference between")
    print("easy verification and hard optimization.")

    print("\nEX1:")
    print("Verify coverage quickly, but finding minimum coverage is hard.")

    print("\nEX2:")
    print("Verify labeling quickly, but finding minimum labels is hard.")

    print("\nEX3:")
    print("Verify budget quickly, but finding maximum influence can be hard.")

    print("\nFor small inputs, exact algorithms are useful.")
    print("For large real-world platforms, exact algorithms are usually too slow.")

    print("\nPractical systems use:")
    print("- greedy methods")
    print("- heuristics")
    print("- approximations")

    print("\nGoal:")
    print("good solution + fast runtime")
    print("-" * 60)


def run_final_question_summary():
    """
    Run all final question parts.
    """

    print_classification()
    print_decision_vs_optimization()
    print_scalability()
    print_engineering_perspective()
    print_reflection()
    print_edge_cases()
    print_final_conclusion()


if __name__ == "__main__":
    run_final_question_summary()