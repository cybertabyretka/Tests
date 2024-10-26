from LinkedList import LinkedList


class Stack:
    def __init__(self, *elements: any) -> None:
        self.linked_list: LinkedList = LinkedList(*reversed(elements))

    def __str__(self) -> str:
        """
        :return: stack representation
        """
        return self.linked_list.__str__()

    def push(self, element: any) -> None:
        """
        :param element: element to push
        :return: None
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.peek()
        2
        """
        self.linked_list.append_to_start(element)

    def pop(self) -> any:
        """
        :return: deleted from stack element
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.pop()
        1
        """
        return self.linked_list.remove_first()

    def peek(self) -> any:
        """
        :return: first element in stack
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.peek()
        2
        """
        return self.linked_list[0]

    def size(self) -> int:
        """
        :return: stack len
        >>> stack = Stack(1, 2, 3, 4, 5)
        >>> stack.size()
        5
        """
        return len(self.linked_list)

    def clear(self):
        """
        :return: None
        >>> stack = Stack(1, 2, 3, 4, 5)
        >>> stack.clear()
        >>> stack.size()
        0
        """
        self.linked_list.clear()

    def is_empty(self):
        """
        :return: flag is stack empty
        >>> stack = Stack(1, 2, 3, 4, 5)
        >>> stack.is_empty()
        False
        >>> stack.clear()
        >>> stack.is_empty()
        True
        """
        return self.linked_list.is_empty()
