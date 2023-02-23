from python.lists.Node import Node


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def __len__(self) -> int:
        """
        Permite a contagem de quantos elementos há na lista apartir da função len()
        :return: O tamanho da lista
        """
        return self._size

    def __repr__(self):
        string = ''
        pointer = self.head
        while pointer:
            string += str(pointer.data) + '->'
            pointer = pointer.next
        return string

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, index: int):
        """
        Permite obter um elemento apartir do seu index
        :param index: index do elemento que desejamos
        :return: Pode retornar um IndexError caso tentemos acessar um index inexistente
        """
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError('list index out of range')

    def __setitem__(self, index: int, value):
        """
        Permite a substituição de um elemento na lista apartir do seu index
        :param index: Index do elemento que desejamos substituir
        :param value: novo valor do elemento
        :return: Pode retornar IndexError caso tentemos substituir um elemento com index inexistente
        """
        pointer = self._getnode(index)
        if pointer:
            pointer.data = value
        else:
            raise IndexError('list index out of range')

    def _getnode(self, index):
        """
        Retorna, com base no index, o nó desejado
        :param index: posição do nó
        :return: O nó
        """
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        return pointer

    def append(self, elem):
        """
        Insere um elemento ao fim da lista
        :param elem: elemento que desejamos inserir
        """
        if self.head:  # há um elemento (mesma coisa que if True)
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
            self._size += 1
        else:  # Primeira inserção: → não há elemento na lista (mesma coisa que if False (None é False))
            self.head = Node(elem)
            self._size += 1

    def index(self, elem):
        """
        Procura um elemento na lista e retorna em qual index ele se encontra
        :param elem: Elemento que estamos procurando
        :return: Index do elemento ou ValueError caso o elemento não esteja na lista
        """
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')

    def insert(self, index, elem):
        """
        Insere um elemento em qualquer posição da lista
        :param index: Posição da lista em que queremos inserir um elemento
        :param elem: elemento que será inserido
        """
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        """
        Remove a primeira ocorrência de um elemento apartir do seu valor
        :param elem: Elemento que desejamos
        :return: True caso o elemento tenha sido removido
        """
        if not self.head:
            raise ValueError(f"{elem} is not in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            pointer = self.head.next
            previous = self.head
            while pointer:
                if pointer.data == elem:
                    previous.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                previous = pointer
                pointer = pointer.next

        raise ValueError(f"{elem} is not in list")

    def delete(self, index):

        """
        Remove um elemento pelo index
        :param index: Index do elemento que desejamos remover
        :return: Retorna IndexError caso não haja um elemento no index dado
        """
        if index == 0:
            self.head = self.head.next
        else:
            previous_pointer = self._getnode(index-1)
            pointer = self._getnode(index+1)
            previous_pointer.next = pointer
        self._size -= 1

    def clear(self):
        """Esvazia a lista"""
        pointer = self._getnode(self._size-1)
        self.head = pointer.next
        self._size = 0
