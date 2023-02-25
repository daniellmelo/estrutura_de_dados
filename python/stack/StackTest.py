from python.stack.Stack import Stack

# Adicionando dados na pilha:
stack = Stack()
stack.push(1)
stack.push(5)
stack.push(3)
stack.push(2)
stack.push(0)
stack.push(0)
stack.push('DADO')
stack.push(True)
stack.push(3)
stack.push(2)


# Representação da pilha
print(stack)


# Removendo 4 valores no topo da pilha e retornando o penúltimo valor removido
stack.pop()
stack.pop()
x = stack.pop()
stack.pop()
print(x)


# Print do valor que está no topo da pilha
print(stack.peek())
