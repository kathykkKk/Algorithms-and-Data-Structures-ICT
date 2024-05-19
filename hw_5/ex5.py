class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack_pointers = [None, None, None]
        self.free_pointer = None
        self.free_list = None

        for i in range(stack_size * 3):
            node = Node(None)
            node.next = self.free_list
            self.free_list = node

        self.free_pointer = self.free_list

    def push(self, stack_num, data):
        if self.is_full():
            print("Stack is full")
            return None

        new_node = self.free_pointer
        self.free_pointer = self.free_pointer.next
        new_node.data = data

        new_node.next = self.stack_pointers[stack_num]
        self.stack_pointers[stack_num] = new_node

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            print("Stack is empty")
            return None

        popped_node = self.stack_pointers[stack_num]
        self.stack_pointers[stack_num] = popped_node.next

        popped_data = popped_node.data
        popped_node.data = None
        popped_node.next = self.free_pointer
        self.free_pointer = popped_node

        return popped_data

    def is_full(self):
        return self.free_pointer is None

    def is_empty(self, stack_num):
        return self.stack_pointers[stack_num] is None


# Пример использования
three_stacks = ThreeStacks(2)

three_stacks.push(0, 1)
three_stacks.push(0, 2)
three_stacks.push(0, 3)
three_stacks.push(0, 4)
three_stacks.push(1, 3)
three_stacks.push(2, 4)
three_stacks.push(0, 4) # произошло переполнение, элемент не добавлен

print(three_stacks.pop(0))
print(three_stacks.pop(0))
print(three_stacks.pop(0))
print(three_stacks.pop(1))
print(three_stacks.pop(2))
print(three_stacks.pop(2))

