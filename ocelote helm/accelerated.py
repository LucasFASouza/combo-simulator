from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt


def simulate_turns(turns, multiplier):
    ocelots = 1
    cats = 0

    historic = [ocelots + cats]

    for _ in range(turns):
        ocelots += 1 * multiplier
        cats += (ocelots * multiplier) + (ocelots * multiplier) ** 2
        ocelots *= 2 * multiplier

        historic.append(ocelots + cats)

    return historic


def thousand_separator(x, pos):
    return f'{int(x):,}'.replace(',', '.')


# formatter = FuncFormatter(thousand_separator)


def plot_graphs(datasets, labels, colors):
    plt.figure(figsize=(14, 6))

    for data, label, color in zip(datasets, labels, colors):
        plt.plot(range(len(data)), data, label=label, color=color)

    plt.xlabel('Turnos', fontname='Calibri', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(range(len(datasets[0])), fontname='Calibri', fontsize=12)

    y_ticks = [float(10**i) for i in range(0, 91, 6)]
    y_labels = [f"10^{i}" for i in range(0, 91, 6)]
    plt.gca().set_yscale('log')
    plt.gca().set_yticks(y_ticks)
    plt.gca().get_yaxis().set_major_formatter(
        FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))
    plt.gca().set_yticklabels(y_labels, fontname='Calibri', fontsize=16)

    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig('ocelote helm/Multipliers_over_turns.png',
                dpi=200)
    plt.close()


if __name__ == "__main__":
    normal = simulate_turns(40, 1)
    dobro = simulate_turns(40, 2)
    triplo = simulate_turns(40, 3)
    seistuplo = simulate_turns(40, 6)

    print(seistuplo[-1])
    print(seistuplo[-2])

    plot_graphs([normal, dobro, triplo, seistuplo],
                ['Sem multiplicadores',
                 'Anointed Procession',
                'Ojer Taq, Deepest Foundation',
                 'Ambos'],
                ['red', 'blue', 'green', 'purple'])
