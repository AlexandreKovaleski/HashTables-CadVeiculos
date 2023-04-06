class HashTable:
    def __init__(self):
        self.size = 29
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.deleted = [False] * self.size

    def put(self,key,data):
        key = key.upper()
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
        key = key.upper()
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
        key = key.upper()
        indicehash = self.hashfunction(key,len(self.keys))

        if self.keys[indicehash] == key:
            self.keys[indicehash] = 'empty'
            self.values[indicehash] = 'empty'  #replace
            print("Placa " + key + ", removida com sucesso!\n")

        else: #aqui faz a sondagem linear
            nextslot = self.rehash(indicehash,len(self.keys))
            while self.keys[nextslot] != None and self.keys[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.keys))

            if self.keys[nextslot] == key:
                self.keys[nextslot] = 'empty'
                self.values[nextslot] = 'empty'
                print("Placa " + key + ", removida com sucesso!\n")
            else:
                print("Não foi possível encontrar a placa e removê-la!\n")
    

    def get(self, key):
        key = key.upper()
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

    def showAll(self):
        for item in self.keys:            
            if item != '':
                if item != None and item != 'empty':
                    print("[{}] = {}".format(item, self.get(item)))
                elif item == None:
                    print("[{}] = {}".format(item, item))