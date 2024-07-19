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
    plt.title(name, fontname='Calibri', fontsize=16)
    plt.xlabel('Turnos', fontname='Calibri', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(range(len(data)), fontname='Calibri', fontsize=14)
    plt.yticks(fontname='Calibri', fontsize=16)
    plt.gca().yaxis.set_major_formatter(formatter)
    # plt.yscale('log')
    plt.tight_layout()
    plt.savefig(f'ocelote helm/{name}_over_turns.png',
                dpi=200, transparent=True)
    plt.close()

if __name__ == "__main__":
    ocelots_list, cats_list = simulate_turns(10)

    for i in range(len(ocelots_list)):
        print(f'Turno {i}: Ocelotes: {ocelots_list[i]}, Gatos: {cats_list[i]}')

    plot_graphs(ocelots_list, 'Ocelotes', 'green')
    plot_graphs(cats_list, 'Gatos', 'red')
