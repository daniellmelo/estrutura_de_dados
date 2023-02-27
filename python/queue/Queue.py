from python.queue.Node import Node


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while pointer:
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return 'empty queue'

    def __str__(self):
        return self.__repr__()

    def push(self, elem):
        """
        Adiciona um elemento ao final da fila
        :param elem: elemento que será adicionado
        Comokexidade O(1)
        """
        node = Node(elem)
        if self._size == 0:
            self.last = node
            self.first = node
        else:
            self.last.next = node
            self.last = node
        self._size += 1

    def pop(self):
        """
        Remove e retorna o primeiro elemento da fila
        Complexidade O(1)
        """
        if self._size == 0:
            raise IndexError('empty queue')
        removed_first = self.first
        self.first = removed_first.next
        removed_first.next = None
        self._size -= 1
        return removed_first.data

    def peek(self):
        """
        Retorna o primeiro da fila
        Complexidade O(1)
        """
        if self._size == 0:
            raise IndexError('empty queue')
        return self.first.data
