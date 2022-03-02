class Hashlinear:
    def __init__(self,x):
        self.chave = x
        #print('O valor de x é: ',x)

    def funcaoHash(self):
        self.chaveHash = self.chave%4
        #print(self.chave)
        return self.chaveHash 
        
    def inserir(self):
        print('chave hash dentro do inserir',self.chaveHash)
        for cont in range(0,4): 
            #print('entrei aqui ')
            if matriz[self.chaveHash][cont] == -1: # se tiver elemento neste lugar
                matriz[self.chaveHash][cont] = self.chave
            #matriz[self.chaveHash][:]= self.chave 
                print('inserido na matriz',matriz[:][:])
                break
            else:
                #### continuar daki 
                print('não posso inserir')


        

matriz = [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]

condicao = "s"
while condicao == "s":

    aux = int(input('Digite a chave: '))
    objeto1 = Hashlinear(aux)  ## instanciei um objeto através do init
#objeto2 = Hashlinear(24)

    objeto1.funcaoHash()
#objeto2.funcaoHash()
    objeto1.inserir()
    condicao = input('Deseja inserir mais? ')
#objeto2.inserir()

#print('testeaqui',matriz[3][0])
#aux = int(input('digite a chave a ser buscada: '))
#print(Hashlinear.funcaoHash(aux))
