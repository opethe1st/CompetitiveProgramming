"""
cells - array of length N. 1 indexed. with values 0/1
players take turns. initially both outside the strip.
each turn, current player picks a free call and move there. then this cell becomes blocked.
nayeon players first.
can only move to left orgiht adjacent cell from cell c if it is free. if a player is unable to move, to a free
cell, the player has lost.
They both play optimally, find out who wins
Idea.
Nayoen needs to pick a portion with an odd number of ones together?
space is a sequence of free slots
if it is a space with two and nayoeon picks that then nayeon loses
if it is a space with three and nayeon picks the middle then nayeon wins
if it is a space with four and nayeon
One of the properties of this is that, nayeon moves right or left as the game progress,
the challenge is whether nayeon would hit a blocked cell before tzuyu.
the length of the space is odd, what is the optimal first move? move to the middle the regardless of
where tzuyu starts moving, tzuyu will run out of moves first
if the length of the space is even, move to the middle but tzuyu can match every move. don't move to the middle,
then tzuyu will make sure to box nayeon ni by moving next
So it seems nayoen only wins if there a space of odd length that is not one
if instead all the spaces are of even length that nayeon wins
if there is more than one space of length 1. nayeon loses
if there is only one space of length 1, nayeon wins
Oh it is more complicated. that it is more complicated! Tzuyu might decide to pick a space
that is different from nayeon's space. So if nayeon pick the largest odd space greater than 1
then if there is a space that is more than half of the current, tzuyu will pick that space
if not
"""


def nayeon_wins(A):
    sizes = []
    prev = 1
    count = 1
    for cell in A+[1]:
        if prev == 0:
            if prev == cell:
                count += 1
            else:
                sizes.append(count)
                count = 1
        prev = cell

    if not sizes:
        return "No"
    # print(sizes)
    sizes.sort(reverse=True)
    largest, next_largest = sizes[0], sizes[1] if len(sizes)>1 else 0
    if next_largest*2 < largest and largest % 2 == 1:
        return "Yes"
    else:
        return "No"


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(nayeon_wins(A))
