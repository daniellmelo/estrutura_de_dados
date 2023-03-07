from python.tree.Node import Node


class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        """
        O percurso em ordem simétrica é muito utilizado para árvores binárias de busca, um dos assuntos do próximo
    capítulo. Os passos que o compõem são os seguintes, para cada uma das suas subárvores:
    1. percorrer a sua subárvore esquerda, em ordem simétrica;
    2. visitar a raiz;
    3. percorrer a sua subárvore direita, em ordem simétrica.
    Complexidade: O(n)
        :parameter node: indica qual subárvore percorreremos.
        :return:
        """
        if node is None:
            node = self.root
        if node.left:  # percorrer a sua subárvore esquerda, em ordem simétrica
            print('(', end='')
            self.inorder_traversal(node.left)

        print(node, end='')  # visitar a raiz

        if node.right:  # percorrer a sua subárvore direita, em ordem simétrica
            self.inorder_traversal(node.right)
            print(')', end='')



