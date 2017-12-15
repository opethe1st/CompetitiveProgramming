'''CodeChef Long Challenge December, 2017'''

# pylint: disable=missing-docstring
from enum import Enum


NORMAL_PENALITIES = 5

class Penalty(Enum):
    GOAL = '1'
    MISS = '0'

class State(Enum):
    A_WIN = 'TEAM-A'
    B_WIN = 'TEAM-B '
    DRAW = 'TIE'
    A_TURN = 'aturn'
    B_TURN = 'bturn'
    A_SUDDEN_DEATH_TURN = 'asudden'
    B_SUDDEN_DEATH_TURN = 'bsudden'


def who_won(penalties):
    state = State.A_TURN
    a_turns = 0
    b_turns = 0
    a_score = 0
    b_score = 0
    for penalty in penalties+'00':
        # transition to sudden_death
        if (a_turns + b_turns) == 2 * NORMAL_PENALITIES:
            state = State.A_SUDDEN_DEATH_TURN
        # win in with normal penalties
        if state in [State.A_TURN, State.B_TURN]:
            if a_score > (NORMAL_PENALITIES - b_turns) + b_score:
                state = State.A_WIN
                break
            elif b_score > (NORMAL_PENALITIES - a_turns) + a_score:
                state = State.B_WIN
                break

        # win in sudden death
        if state in [State.A_SUDDEN_DEATH_TURN, State.B_SUDDEN_DEATH_TURN] and a_turns == b_turns:
            if a_score > b_score:
                state = State.A_WIN
                break
            elif b_score > a_score:
                state = State.B_WIN
                break
        # Sudden Death
        if state == State.A_SUDDEN_DEATH_TURN:
            a_turns += 1
            a_score += 1 if penalty == Penalty.GOAL else 0
            state = State.B_SUDDEN_DEATH_TURN
        elif state == State.B_SUDDEN_DEATH_TURN:
            b_turns += 1
            b_score += 1 if penalty == Penalty.GOAL else 0
            state = State.A_SUDDEN_DEATH_TURN

        elif state == State.A_TURN:
            a_turns += 1
            a_score += 1 if penalty == Penalty.GOAL else 0
            state = State.B_TURN
        elif state == State.B_TURN:
            b_turns += 1
            b_score += 1 if penalty == Penalty.GOAL else 0
            state = State.A_TURN
    else:
        return State.DRAW, ''
    return state, a_turns+b_turns


if __name__ == '__main__':
    while True:
        try:
            PENALITIES = input()
            winner, required_shots = who_won(penalties=PENALITIES)  # pylint: disable=invalid-name
            print('{winner} {required_shots}'.format(winner=winner, required_shots=required_shots))
        except EOFError:
            break
