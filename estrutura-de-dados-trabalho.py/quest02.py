#Exigência 1/7
#Cria tabela com 10 posições, todoas iniciadas em None
class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10         #Exigência 1/7

    #Exigência 5/7
    #Calcular a posição da sigla na tabela hash
    def hashFuncao(self, sigla):
        if sigla == "DF":
            return 7
        return (ord(sigla[0])+ord(sigla[1])) % 10

    #Exigência 3/7
    #Insere um novo estado no início da lista encadeada
    def inserirEstado(self, sigla, nomeEstado):
        novo = Estado(sigla, nomeEstado)             #Cria um novo nodo
        posicao = self.hashFuncao(sigla)             #Calcula posição da tabela
        novo.proximo = self.tabela[posicao]          #Aponta para o atual head
        self.tabela[posicao] = novo                  #'novo' vira head

#Exigência 4/7
#Imprimi a tabela hash com os estados por posição
    def imprimirTabela(self):
        for i in range(10):
            print(f"Posicao {i}:", end=" ")
            atual = self.tabela[i]
            if atual is None:
                print("Vazio")
            else:
                while atual:
                    print(f"{atual.sigla}", end=" >> ")
                    atual = atual.proximo
                print("Vazio")                               #Fim da lista

#Exigência 2/7
#Classe do nó lista que representa um estado
class Estado:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla                            #Sigla do Estado
        self.nomeEstado = nomeEstado                  #Nome do Estado
        self.proximo = None

#Teste EC04
if __name__ == "__main__":
    tabela = TabelaHash()

    #Saida 1/3 - Antes de adicionar informações
    print("(1/3) - Impressao da tabela hash antes de inserir qualquer informacao:")
    tabela.imprimirTabela()

    #Exigência 6/7 - Adicionando os 27 Estados
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    for sigla, nome in estados:
        tabela.inserirEstado(sigla, nome)

    #Saida 2/3 - Após inserir os Estados
    print("\n(2/3) - Tabel hash apos inserir os 26 estados + DF:")
    tabela.imprimirTabela()

    #Exigência 7/7 - Adicionar estado fictício
    tabela.inserirEstado("IC", "Estado Maanain")

    #Saida 3/3 - Após adicionar o estado fictício
    print("\nTabel hash apos inserir os 26 estados + DF: e estado ficticio:")
    tabela.imprimirTabela()
