from python.stack.Node import Node


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self) -> int:
        """
        Permite a contagem de quantos elementos há na lista apartir da função len()
        :return: O tamanho da lista
        """
        return self._size

    def __repr__(self):
        string = ''
        pointer = self._top
        while pointer:
            string += str(pointer.data) + '\n'
            pointer = pointer.previous
        return string

    def __str__(self):
        return self.__repr__()

    def push(self, elem):
        """
        Insere um elemento no topo da pilha
        Complexidade no pior caso: O(1)
        """
        node = Node(elem)
        node.previous = self._top
        self._top = node
        self._size += 1

    def pop(self):
        """
        Remove o último elemento inserido
        Complexidade no pior caso: O(1)
        :return: O elemento que foi removido
        """
        if self._size == 0:
            raise IndexError('pop from empty stack')
        value = self._top
        self._top = self._top.previous
        self._size -= 1
        return value.data

    def peek(self):
        """
        Recupera o último valor inserido na pilha
        Complexidade no pior caso: O(1)
        :return: O último valor inserido na pilha
        """
        if self._size == 0:
            raise IndexError('peek from empty stack')
        return self._top.data
    