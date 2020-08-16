"""
Clarify
N guests - 1 to N.
guest belongs to a family - F[i] is the family i belongs to
Need to find an optimal seating arrangement
People seating at a table need to have consecutive numbers
two guests i and j are likely to get into an argument if F[i] == F[j]
Each table cost K rupees. if it costs 0 then would have just sat everyone in their own table
Inefficiency of a seating arrangment -> total cost of tables plus number of guest likely to
get into an argument.
Find the minimum possible inefficiency which we can achieve
Constraints
1<=T<=100
1<=N<=1000
1<=K<=1000
1<=F[i]<=100
sum of N across test cases is 5000
Constraints suggest that a quadratic solution is acceptable.
Extrema - everyone in one table - then inefficiency is number of guests
that have more than one family member + K
everyone on their own table - N*K
so this is dynamic programming
smallest[i][j] = min(smallest[i][k] + smallest[k][j], K+number_of_guests_with_more_than_one_family_member)

How to optimise
so is there a way not to have the two loops? is there a better recurrence relation? or way to terminate early?
Can we count the number of duplicate families in a range fast?
Can I invert it to find the number of people in a range with just a family.
one way is to keep track of for each family in order where each member is
then to count in a range binary search either range
can also do keep track of the families that appear just once in each half
then when merging if a family appears on both sides, remove it
only_family_member[i][j] = (
    (only_family_member[i][(i+j)//2] | only_family_member[(i+j)//2][j])
    - (only_family_member[i][(i+j)//2] & only_family_member[(i+j)//2][j])
)
other idea - build a prefix_unique array?
"""
import heapq


def min_efficiency(no_of_people, cost_of_table, families):
    table_costs = [[None for _ in range(no_of_people)] for _ in range(no_of_people)]
    for i in range(no_of_people):
        table_costs[i][i] = cost_of_table

    for i in range(no_of_people):
        # print(i)
        seen_once = set([families[i]])
        seen_more_than_once = set()
        cost = table_costs[i][i]
        for j in range(i + 1, no_of_people):
            if families[j] in seen_once:
                cost += 2
            if families[j] in seen_more_than_once:
                cost += 1
            if families[j] in seen_once:
                seen_once.remove(families[j])
                seen_more_than_once.add(families[j])
            elif families[j] not in seen_more_than_once:
                seen_once.add(families[j])
            # print(seen_once, seen_more_than_once)
            table_costs[i][j] = cost
        # print()
    # print(table_costs)
    heap = [(table_costs[0][j], -j) for j in range(no_of_people)]
    heapq.heapify(heap)
    # print(heap)
    seen_costs = set()
    while heap:
        # print(heap)
        cost, person = heapq.heappop(heap)
        person = -person
        while heap and heap[0][0] == cost:
            heapq.heappop(heap)

        # print(cost, person)
        seen_costs.add(cost)
        if person == (no_of_people - 1):
            return cost
        for next_person in range(person + 1, no_of_people):
            if (cost + table_costs[person+1][next_person]) not in seen_costs:
                heapq.heappush(
                    heap,
                    (cost + table_costs[person+1][next_person], -next_person)
                )


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        no_of_people, cost_of_table = map(int, input().split())
        families = list(map(int, input().split()))
        print(
            min_efficiency(
                no_of_people=no_of_people,
                cost_of_table=cost_of_table,
                families=families,
            )
        )
