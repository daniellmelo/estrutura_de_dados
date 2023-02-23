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

    def __getitem__(self, index: int):
        """
        Permite obter um elemento apartir do seu index
        :param index: index do elemento que desejamos
        :return: Pode retornar um IndexError caso tentemos acessar um index inexistente
        """
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError('lista index out of range')

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
            raise IndexError('lista index out of range')

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
                raise IndexError('lista index out of range')
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

    def remove(self, index):
        pointer = self.head
        for i in range(index -1):
            pointer = pointer.next


if __name__ == '__main__':
    lista = LinkedList()
    lista.append(33)
    lista.append(66)
    lista.append(99)
    lista.append(88)
    lista.append(22)
    lista.insert(6, 1000)

    for i in lista:
        print(i)
