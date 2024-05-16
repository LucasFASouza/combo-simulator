import random

def roll_dice(dices):
    rolls = []

    for _ in range(dices):
        result = random.randrange(1, 20)
        rolls.append(result)

    return max(rolls)

def simulate(infinite, initial_doublers, mode):
    loop = True
    copies = 0
    dice_rolled = 0

    while loop and copies < infinite:
        doublers = initial_doublers + copies

        die = roll_dice(doublers)

        copies += 1
        dice_rolled += 1

        if mode == 2:
            print(f"\nRolagem {dice_rolled}. Você rolou um {die}")
            print(f"Cópias geradas até agora: {copies}")
            input("Pressione Enter para continuar.")

        if die < 15:
            loop = False

    if copies != infinite:            
        print(f"\nForam criadas {copies} cópias. Dados foram rolados {dice_rolled} vezes.")
        print("Se você está copiando um Wyll, ele ganhará marcadores +1/+1 para cada rolagem.")
        print(f"Assim, você terá uma cópia com +{dice_rolled}/+{dice_rolled}. Uma com +{dice_rolled - 1}/+{dice_rolled - 1}. E assim por diante.")

    else:
        print("\nVocê conseguiu criar mais de 50 cópias. O combo é infinito.")
        print("Escolha um número arbitrário de cópias e marcadores e seja feliz!")

    return copies, dice_rolled


def main():
    infinite = input("Quantas cópias serão consideradas infinito? (Enter para 50): ") or 50
    initial_doublers = input("Quantos efeitos iniciais de vantagem você tem? (Enter para 1): ") or 1

    print("\nQual modo de simulção você deseja?")
    print("1 - Simples: Você receberá o número de cópias e o número de dados rolados.")
    print("2 - Detalhado: O programa irá pausar a cada rolagem para você aplicar suas habilidades desencadeadas.")

    mode = input("Qual modo? (Enter para 1): ") or 1

    simulate(int(infinite), int(initial_doublers), int(mode))

if __name__ == "__main__":
    main()