import matplotlib.pyplot as plt

def calculate_probability(num_dice):
    # Probabilidade de um único dado ter um resultado de 15 ou mais
    single_dice_probability = 6 / 20
    
    # Probabilidade de nenhum dos dados ter um resultado de 15 ou mais
    no_fifteen_or_more = (1 - single_dice_probability) ** num_dice
    
    # Probabilidade de pelo menos um dado ter um resultado de 15 ou mais
    at_least_one = 1 - no_fifteen_or_more
    
    return at_least_one * 100

def main():
    num_dice_range = range(1, 21)
    probabilities = [calculate_probability(num_dice) for num_dice in num_dice_range]

    plt.figure(figsize=(12, 8))
    plt.plot(num_dice_range, probabilities, marker='o', markersize=4, color='red')  # Definindo o tamanho das bolinhas

    plt.xlabel('Dados lançados', fontname='Calibri', fontsize=14)  # Definindo a fonte e tamanho do rótulo do eixo x
    plt.ylabel('Probabilidade de repetir o processo (%)', fontname='Arial', fontsize=14)  # Definindo a fonte e tamanho do rótulo do eixo y
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(num_dice_range, fontname='Calibri', fontsize=10)  # Definindo a fonte e tamanho dos rótulos do eixo x
    plt.yticks(range(0, 101, 5), fontname='Calibri', fontsize=10)  # Definindo a fonte e tamanho dos rótulos do eixo y

    plt.tight_layout()
    
    # Adicionando linhas horizontais intermediárias a cada 5%
    for i in range(5, 100, 5):
        plt.axhline(y=i, color='lightgray', linestyle='--', linewidth=0.5)
    
    plt.savefig('probabilidade_dados.png', dpi=200, transparent=True)  # Salvar com fundo transparente
    plt.show()

if __name__ == "__main__":
    print(calculate_probability(40))
    main()
