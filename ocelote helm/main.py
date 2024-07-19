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


# formatter = FuncFormatter(thousand_separator)


def plot_graphs(datasets, labels, colors):
    plt.figure(figsize=(14, 6))

    for data, label, color in zip(datasets, labels, colors):
        plt.plot(range(len(data)), data, label=label, color=color)

    plt.xlabel('Turnos', fontname='Calibri', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(range(len(datasets[0])), fontname='Calibri', fontsize=12)

    y_ticks = [float(10**i) for i in range(0, 25, 3)]
    y_labels = ['1', '1 Mil', '1 Milhão', '1 Bilhão',
                '1 Trilhão', '1 Quadrilhão', '1 Quintilhão', '1 Sextilhão', '1 Septilhão']
    plt.gca().set_yscale('log')
    plt.gca().set_yticks(y_ticks)
    plt.gca().get_yaxis().set_major_formatter(
        FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))
    plt.gca().set_yticklabels(y_labels, fontname='Calibri', fontsize=16)

    plt.legend(loc='upper left')

    powers_of_ten = [10**i for i in range(1, 26)]
    for y in powers_of_ten:
        plt.hlines(y, xmin=0, xmax=len(data)-1, colors='gray',
                   linestyles='dotted', linewidth=0.5)

    plt.tight_layout()
    plt.savefig('ocelote helm/Combined_over_turns.png',
                dpi=200, transparent=True)
    plt.close()


if __name__ == "__main__":
    ocelots_list, cats_list = simulate_turns(40)

    for i in range(len(ocelots_list)):
        if i in [20,21,29,30,31,39,40]:
            # print as 000,000,000
            print(f'{cats_list[i]:,}'.replace(',', '.'))

    cats_list[0] = None

    plot_graphs([cats_list, ocelots_list], [
                'Gatos', 'Ocelotes'], ['red', 'green'])
