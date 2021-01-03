"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    
    nome1 = input('Digite o primeiro nome:\n') 
    nome2 = input('Digite o segundo nome:\n')
    nome3 = input('Digite o terceiro nome:\n')

    ordem = [nome1, nome2, nome3]
    for i in range(len(ordem)):
        for a in range(len(ordem) - 1):
            if ordem[a] < ordem[a+1]:
                ordem[a], ordem[a+1] = ordem[a+1], ordem[a]

    print (ordem[0])
    print (ordem[1])
    print (ordem[2])            

if __name__ == '__main__':
    main()
