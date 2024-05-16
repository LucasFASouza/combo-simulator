import random
import matplotlib.pyplot as plt

INFINITE = 30
REPS = 50000

def roll_dice(dices):
    rolls = []

    for _ in range(dices):
        result = random.randrange(1, 20)
        rolls.append(result)

    return max(rolls)

results = {}

initial_doublers_list = []
infinites_percentage_list = []

for initial_doublers in range(1, 21):
    print(f"\nSimulating {initial_doublers} starting advantage")

    i = 0
    infinites = 0

    while i < REPS:        
        loop = True
        copies = 0

        while loop and copies < INFINITE:
            doublers = initial_doublers + copies

            die = roll_dice(doublers)

            copies += 1

            if die < 15:
                loop = False

        if copies == INFINITE:
            infinites += 1

        i += 1

    initial_doublers_list.append(initial_doublers)
    infinites_percentage_list.append(infinites / REPS * 100)

    print(f"Chances of infinite combo: {infinites / REPS * 100:.2f}%")

plt.figure(figsize=(16, 7))
plt.plot(initial_doublers_list, infinites_percentage_list, marker='o', markersize=4, color='red')  # Definindo o tamanho das bolinhas

plt.xlabel('Efeitos de vantagem', fontname='Calibri', fontsize=14)  # Definindo a fonte e tamanho do rótulo do eixo x
plt.ylabel('Chances de combar infinitamente', fontname='Arial', fontsize=14)  # Definindo a fonte e tamanho do rótulo do eixo y
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(initial_doublers_list, fontname='Calibri', fontsize=10)  # Definindo a fonte e tamanho dos rótulos do eixo x
plt.yticks(range(0, 101, 5), fontname='Calibri', fontsize=10)  # Definindo a fonte e tamanho dos rótulos do eixo y

plt.tight_layout()

# Adicionando linhas horizontais intermediárias a cada 5%
for i in range(5, 100, 5):
    plt.axhline(y=i, color='lightgray', linestyle='--', linewidth=0.5)

plt.savefig('inifinite_by_advantage.png', dpi=200, transparent=True)  # Salvar com fundo transparente

print(initial_doublers_list)
print(infinites_percentage_list)