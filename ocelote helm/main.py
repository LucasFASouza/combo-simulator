import math
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt


def apply_algorithm(ocelots, cats):
    ocelots += 1
    cats += ocelots + ocelots ** 2
    ocelots *= 2

    return ocelots, cats


def simulate_turns(turns):
    ocelots = 1
    cats = 0

    ocelots_list = [ocelots]
    cats_list = [cats]

    for _ in range(turns):
        ocelots, cats = apply_algorithm(ocelots, cats)
        ocelots_list.append(ocelots)
        cats_list.append(cats)

    return ocelots_list, cats_list


def thousand_separator(x, pos):
    return f'{int(x):,}'.replace(',', '.')


formatter = FuncFormatter(thousand_separator)


def plot_graphs(data, name, color):
    plt.figure(figsize=(6, 6))
    plt.plot(data, color=color)
    plt.xlabel('Turnos', fontname='Calibri', fontsize=14)
    plt.ylabel(name, fontname='Calibri', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(range(len(data)), fontname='Calibri', fontsize=12)
    plt.yscale('log')

    ticks = [
        1,
        1000,
        1000000,
        1000000000,
        1000000000000,
    ]
    ticks_labels = [
        '1',
        '1 Mil',
        '1 Milhão',
        '1 Bilhão',
        '1 Trilhão',
    ]

    max_value = max(data)
    while max_value < ticks[-1]:
        ticks.pop()
        ticks_labels.pop()

    hlines = [10**i for i in range(int(math.log10(max_value)) + 1)]

    plt.gca().set_yticks(ticks)
    plt.gca().set_yticklabels(ticks_labels, fontname='Calibri', fontsize=12)

    for y in hlines:
        plt.hlines(y, xmin=0, xmax=len(data)-1, colors='gray',
                   linestyles='dotted', linewidth=0.5)

    plt.tight_layout()
    plt.savefig(f'ocelote helm/{name}_over_turns.png',
                dpi=200, transparent=True)
    plt.close()


if __name__ == "__main__":
    ocelots_list, cats_list = simulate_turns(20)

    for i in range(len(ocelots_list)):
        print(f'Turno {i}: Ocelotes: {ocelots_list[i]}, Gatos: {cats_list[i]}')

    plot_graphs(ocelots_list, 'Ocelotes', 'green')
    plot_graphs(cats_list, 'Gatos', 'red')

# Se vc vender todos os ocelotes gerados até o turno 26 pelo preço médio da carta no card kingdom - 44,99 USD, te faltarão 5.300.000 USD para comprar a Wizard of the Coast
