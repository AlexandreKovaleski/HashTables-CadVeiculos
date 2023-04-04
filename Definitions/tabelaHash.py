class HashTable:
    def __init__(self):
        self.size = 29
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.deleted = [False] * self.size

    def hash_function(self, key):
        """
        Função hash que retorna o índice da chave
        """
        return key % self.size

    def insert(self, key, value):
        """
        Insere um par chave-valor na tabela hash
        """
        index = self.hash_function(key)
        if self.keys[index] is None or self.keys[index] == key or self.deleted[index]:
            self.keys[index] = key
            self.values[index] = value
            self.deleted[index] = False
        else:
            while True:
                index = (index + 1) % self.size
                if self.keys[index] is None or self.keys[index] == key or self.deleted[index]:
                    self.keys[index] = key
                    self.values[index] = value
                    self.deleted[index] = False
                    break

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
"""