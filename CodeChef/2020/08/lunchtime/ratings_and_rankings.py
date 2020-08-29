"""
chess tournament over M months
N players. ratings[i] rating of player i before the tournament
noted ratings changes at the end of the month
find the number of players, who peak ratings and peak ranking didnt occur in the same month.
For a particular player, there are multiple peak rating or peak ranking months. Chef wants to
consider the earliest of them.
for each player
    calculate their peak rating month
    calculate their peak ranking month

for the peak ranking month - this is max across all months so max(range(no_of_months), key=ratings[i][k])
for peak rating - need to sort every month - then figure out the rating considering that if there is a tie
all players with the same rating get the same ranking.
"""


def number_of_players_who_peak_ratings_not_same_as_peak_ranking(
    ratings, no_of_months, no_of_players
):
    max_rating = [
        max(range(no_of_months), key=lambda i: (ratings[player][i], -i))
        for player in range(no_of_players)
    ]
    # print(max_rating)
    max_ranking = compute_max_ranking(ratings, no_of_players, no_of_months)
    # print("best rating", max_rating, "best ranking", max_ranking)
    return sum(
        max_rating[player] != max_ranking[player] for player in range(no_of_players)
    )


def compute_max_ranking(ratings, no_of_players, no_of_months):
    ratings_by_month = list(zip(*ratings))
    rankings = []
    for month in range(no_of_months):
        rankings.append(
            rank_players(list(range(no_of_players)), ratings_by_month[month])
        )

    return list(
        min(range(no_of_months), key=lambda i: (rankings[i][player], i))
        for player in range(no_of_players)
    )


def rank_players(ids, scores):
    # print("ids, scores", ids, scores)
    ids = sorted(ids, key=lambda i: scores[i], reverse=True)
    ans = [0]*len(scores)
    previous = scores[ids[0]]
    latest_ranking = 0
    for i, player in enumerate(ids):
        if previous != scores[player]:
            ans[player] = i
            latest_ranking = i
        else:
            ans[player] = latest_ranking
        previous = scores[player]
    # print("ans", ans)
    return ans



T = int(input())
for _ in range(T):
    no_of_players, no_of_months = map(int, input().split())
    ratings = []  # the rows are player ratings
    initial_ratings = list(map(int, input().split()))
    for player in range(no_of_players):
        change_in_ratings = list(map(int, input().split()))
        current = initial_ratings[player]
        player_ratings = []
        for change in change_in_ratings:
            player_ratings.append(current + change)
            current += change
        ratings.append(player_ratings)
    print(
        number_of_players_who_peak_ratings_not_same_as_peak_ranking(
            ratings=ratings, no_of_months=no_of_months, no_of_players=no_of_players
        )
    )
