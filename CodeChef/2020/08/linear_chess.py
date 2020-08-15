"""
[][][][][][x][][]
           K
N other players numbered 1 to N. Chef can choose who to play against.
so player i is found at positions l*p[i] where l is an integer.
Does it jump over positions?
if player moves pawn to square with Chef's pawn chef's pawn is
captured and loses the game.

Idea
Find the shortest distance to chef from any position
- means it is reachable and the time it takes to reach that position - i.e K%p[i] and K > p[i] then K-p[i]/p[i] else inf
"""


def shortest_distance(chef_position, pawn_position):
    if chef_position % pawn_position != 0:
        return float('inf'), -1
    if chef_position < pawn_position:
        return float('inf'), -1
    return (chef_position - pawn_position)//pawn_position, pawn_position


def shortest_distance_to_chef_any_position(pawn_positions, chef_position):
    return min(
        (
            shortest_distance(chef_position, pawn_position)
            for pawn_position in pawn_positions
        ), key=lambda x:x[0]
    )[1]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        _, chef_position = map(int, input().split())
        pawn_positions = list(map(int, input().split()))
        print(
            shortest_distance_to_chef_any_position(
                pawn_positions,
                chef_position,
            )
        )
