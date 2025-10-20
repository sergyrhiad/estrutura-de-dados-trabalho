#Exigencia 1/7
#Classe do nó da lista: Representa um paciente com cartão

class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero                              #Número do cartão
        self.cor = cor                                    #Cor do cartão
        self.proximo = None                               #Ponteiro para o próximo

#Lista Encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        #contadores para numeração automática
        self.proximoNumeroV = 1                        #V: 1, 2, 3, ...
        self.proximoNumeroA = 201                      #A: 201, 202, 203, ...

#Checa se a lista está vazia
    def estaVazia(self) -> bool:
        return self.inicio is None
    
#Mostrar a lista
    def exibir(self):
        atual = self.inicio
        itens = []
        while atual is not None:                               #Vai percorre até achar None
            itens.append(f"{atual.cor}-{atual.numero}")
            atual = atual.proximo
        print(" >> ".join(itens) if itens else "(lista vazia)")

#Exigencia 2/7: adicionar no final, sem a prioridade
    def inserirSemPrioridade(self, nodo):
            
            #situação 1: lista vazia o nó vira head
            if self.inicio is None:
                self.inicio = nodo
                return
            
            #situação 2: Percorre até o fim
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            
            #encaixa no final
            atual.proximo = nodo

    #Insere um novo nó no fim da lista
    def inserirNoFinal(self, numero, cor):
        novo = Nodo(numero, cor)                                #Criando novo nó
        if self.inicio is None:
            self.inicio = novo
            return
        
    #Anda até o ultimo
        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

#Ornaganiza a quem vem antes

    def vemAntes(self, cor1, num1, cor2, num2) -> bool:
        if cor1 == "A" and cor2 == "V":                    #Amarelo sempre vem antes de verde
            return True
        if cor1 == "V" and cor2 == "A":
            return False
        return num1 < num2                                 #Mesma cor o menor número vem antes
    
#Insere um novo nó ja na ordem correta
    def inserirOrdenado(self, numero, cor):
        novo = Nodo(numero, cor)

        #situação 1
        if self.inicio is None or self.vemAntes(cor,numero, self.inicio.cor, self.inicio.numero):
            novo.proximo = self.inicio
            self.inicio = novo
            return
        
        #situacao2
        anterior = self.inicio
        atual = self.inicio.proximo

        while (atual is not None and not self.vemAntes(cor, numero,atual.cor, atual.numero)):
            anterior = atual
            atual = atual.proximo

        #encaixe
        novo.proximo = atual
        anterior.proximo = novo

#Exigencia 3/7 - Adicionar com prioridade de cor
    def inserirComPrioridade(self, nodo):

        #situação 1: Lista vazia, novo vira head
        if self.inicio is None:
            self.inicio = nodo
            return
        
        #situação 2: encontrar o limite entre os blocos A e o V
        anterior = None
        atual = self.inicio

    #Avança quando estiver no bloco A
        while atual is not None and atual.cor == "A":
            anterior = atual
            atual = atual.proximo

    #Iserir no limite, entre o anterior e o atual
        if anterior is None:
            #entra como head
            nodo.proximo = self.inicio
            self.inicio = nodo
        else:
            #se tiver pelo menos um A, o novo vai após o ultimo A
            nodo.proximo = atual
            anterior.proximo = nodo
    #Exigencia 4/7: inserir()
    def inserir(self):
        #pergunta a cor
        while True:
            cor = input("Informe a cor do cartão (A = Amarelo | V = Verde): ").strip().upper()
            if cor in ("A", "V"):
                break
            print("Entrada inválida. Digite 'A' ou 'V'.")

        #Adiciona número automático de acordo com a cor
        if cor == "V":
            numero = self.proximoNumeroV
            self.proximoNumeroV += 1
        else:                                 # se a cor for == A
            numero = self.proximoNumeroA
            self.proximoNumeroA += 1
        
        #Cria o Nodo com cor/numero
        novo = Nodo(numero, cor)

        #Insere como exigencia
        if self.estaVazia():
            self.inicio = novo
        else:
            if cor == "V":
                self.inserirSemPrioridade(novo)
            else:
                self.inserirComPrioridade(novo)
        print(f"Paciente inserido")

    #Mostra os pacientes na fila, ela chama a função feita anteriormente 'exibir()'
    def imprimirListaEspera(self):
        print("Lista de espera atual: ")
        self.exibir()

    #Se a lista estiver vazia, apenas avisa que não há pacientes
    def atenderPaciente(self):
        if self.inicio is None:
            print("Nenhum paciente na fila para atendimento.")
            return
        
    #Essa função remove o primeiro paciente da fila e imprime a mensagem
        paciente = self.inicio
        self.inicio = self.inicio.proximo

    #Mensagem de chamada do paciente
        print(f"Chamando paciente com cartao {paciente.cor}-{paciente.numero} para atendimento.")

#Teste Simples
if __name__ == "__main__":
    fila = ListaEncadeada()

    #Menu principal da triagem
    while True:
        print("-------------------------------------------")
        print("| =========== MENU PRINCIPAL ============= |")
        print("|  --------------------------------------  |")
        print("| 1-  Adicionar pacientes a fila           |")
        print("| 2-  Mostrar pacientes na fila            |")
        print("| 3-  Chamar pacientes                     |")
        print("| 4-  Sair                                 |")
        print("-------------------------------------------")

        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "1":
            #Chama a função inserir(), que ja cuida da cor e numeração
            fila.inserir()
        elif opcao == "2":
            #Mostra a lista de espera
            fila.imprimirListaEspera()
        elif opcao == "3":
            #Atende o primeiro paciente da fila
            fila.atenderPaciente()
        elif opcao == "4":
            print("Fechando Programa ....")
        else:
            print("Opcao invalida. tente novamente.")