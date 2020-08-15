

def jedi_wins(darth_health, attack_power):
    # print(darth_health, attack_power)
    while attack_power:
        darth_health -= attack_power
        attack_power //= 2
        # print(darth_health, attack_power)
    return darth_health <= 0


T = int(input())
for _ in range(T):
    darth_health, attack_power = map(int, input().split())
    print(int(jedi_wins(darth_health, attack_power)))
