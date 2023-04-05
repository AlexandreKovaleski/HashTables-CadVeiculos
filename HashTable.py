class HashTable:
    def __init__(self):
        self.size = 29
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.deleted = [False] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def search(self, key):
        """
        Retorna o valor associado à chave fornecida, se existir
        """
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if not self.deleted[index] and self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        """
        Remove o par chave-valor associado à chave fornecida, se existir
        """
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if not self.deleted[index] and self.keys[index] == key:
                self.deleted[index] = True
                return
            index = (index + 1) % self.size

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,dado):
        self.put(key,dado)
"""
Nesta implementação, cada entrada na tabela hash contém uma chave, um valor e um indicador de exclusão, que é 
definido como False quando a entrada é criada e é definido como True quando a entrada é removida.

A função de hash utiliza o método de divisão para calcular o índice da chave. 
Se a posição correspondente estiver vazia, a chave e o valor são inseridos diretamente. 
Caso contrário, a tabela hash usa sondagem linear para encontrar a próxima posição vazia na tabela. 
Quando ocorre uma colisão, a nova entrada é adicionada na próxima posição disponível na tabela.

A função search usa sondagem linear para encontrar o valor associado à chave fornecida. 
A função delete define o indicador de exclusão como True quando a chave correspondente é encontrada. 
Com isso, a entrada não é realmente removida da tabela, mas é marcada como excluída. Isso é conhecido como lazy deletion.
Nesta implementação, foram adicionados os métodos set, get, e put, que são equivalentes para inserir e atualizar um par c
have-valor na tabela. A função get retorna o valor associado à chave fornecida, enquanto a função set e put inserem ou 
atualizam um par chave-valor na tabela. A função search é utilizada para buscar o valor associado à chave fornecida, 
e a função delete é utilizada para remover o par chave-valor associado à chave fornecida, utilizando lazy deletion, 
como na implementação anterior. Note que a função set na verdade redireciona para a função put, visto que é comum em 
algumas linguagens utilizar set para definir um valor em uma tabela hash. A função get é usada para recuperar um valor 
da tabela hash, e a função put é usada para inserir ou atualizar um valor na tabela hash. 
"""