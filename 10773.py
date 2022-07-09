t = input()
stack = []
for i in range(int(t)):
    b = int(input())
    stack.append(b) if b != 0 else stack.pop()
print(sum(stack))