class Hashlinear:
    def __init__(self,x):
        self.chave = x


    def funcaoHash(self):
        self.chaveHash = self.chave%4
        return self.chaveHash 


    def inserir(self):
        aux2 = 0
        contAux = 0
        print('chave hash dentro do inserir',self.chaveHash)
        for cont in range(0,4): 
            if matriz[self.chaveHash][cont] == -1: # se tiver elemento neste lugar
                matriz[self.chaveHash][cont] = self.chave
                print('inserido na matriz',matriz[:][:])
                break
            else:
                #### continuar daki 
                aux2 = aux2 + 1 ###incremento
                if aux2 == 4:   ## se o bucket encheu 
                    contAux = contAux+1
                    print('o conta ta valendo:',cont)
                    
                    listAux = [-1,-1,-1,-1]
                    matriz.append(listAux[:])
                    matriz[4][contAux] = self.chave


                    print('teste da nova incerção',matriz[:][:])
                    """
                    listaAux = []
                    #listaAux.append(matriz[self.chaveHash][:])
                    #print("lista",listaAux[:])
                    listaAux.append(matriz[self.chaveHash][:])
                    print('essa é a pilha',listaAux[:]) 

                    print('encheu!!')
"""
                #print('não posso inserir')


        

matriz = [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]

condicao = "s"
while condicao == "s":

    aux = int(input('Digite a chave: '))
    objeto1 = Hashlinear(aux)  ## instanciei um objeto através do init

    objeto1.funcaoHash()

    objeto1.inserir()
    condicao = input('Deseja inserir mais? ')

