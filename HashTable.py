class HashTable:
    def __init__(self):
        self.size = 29
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.deleted = [False] * self.size

    def put(self,key,data):
        key = key.lower()
        hashvalue = self.hashfunction(key,len(self.keys))

        if self.keys[hashvalue] == None:
            self.keys[hashvalue] = key
            self.values[hashvalue] = data
        else:
            if self.keys[hashvalue] == key:
                self.values[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.keys))
                while self.keys[nextslot] != None and \
                                self.keys[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.keys))

            if self.keys[nextslot] == None:
                self.keys[nextslot]=key
                self.values[nextslot]=data
            else:
                self.values[nextslot] = data #replace

    def hashfunction(self,key,size):
        return ord(key.lower()[0]) % size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def search(self, key):
        key = key.lower()
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
        key = key.lower()
        """
        Remove o par chave-valor associado à chave fornecida, se existir
        """
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if not self.deleted[index] and self.keys[index] == key:
                self.deleted[index] = True
                return
            index = (index + 1) % self.size

    def get(self, key):
        key = key.lower()
        startslot = self.hashfunction(key,len(self.keys))

        data = None
        stop = False
        found = False
        position = startslot
        while self.keys[position] != None and  \
                            not found and not stop:
            if self.keys[position] == key:
                found = True
                data = self.values[position]
            else: #se elemento não estiver na posicao ele faz o rehash para encontra-lo, assim como fez para posiciona-lo
                position=self.rehash(position,len(self.keys))
                if position == startslot: #se voltou a posicao inicial do hash ele vai parar
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
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
Nesta implementação, foram adicionados os métodos set, get, e put, que são equivalentes para inserir e atualizar um par 
chave-valor na tabela. A função get retorna o valor associado à chave fornecida, enquanto a função set e put inserem ou 
atualizam um par chave-valor na tabela. A função search é utilizada para buscar o valor associado à chave fornecida, 
e a função delete é utilizada para remover o par chave-valor associado à chave fornecida, utilizando lazy deletion, 
como na implementação anterior. Note que a função set na verdade redireciona para a função put, visto que é comum em 
algumas linguagens utilizar set para definir um valor em uma tabela hash. A função get é usada para recuperar um valor 
da tabela hash, e a função put é usada para inserir ou atualizar um valor na tabela hash. 
"""