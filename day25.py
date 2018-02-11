class LinkedList:
    class Node:
        def __init__(self):
            self.prev = None
            self.next = None
            self.data = 0

    def __init__(self):
        self.head = self.tail = self.current = self.Node()

    def append(self):
        self.tail.next = self.Node()
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def prepend(self):
        self.head.prev = self.Node()
        self.head.prev.next = self.head
        self.head = self.head.prev

    def move_right(self):
        if self.current.prev is None:
            self.prepend()
        self.current = self.current.prev
        return self.current

    def move_left(self):
        if self.current.next is None:
            self.append()
        self.current = self.current.next
        return self.current


def diagnose(tape):
    it = tape.head
    chksum = 0
    while it is not None:
        chksum = chksum + 1 if it.data == 1 else chksum
        it = it.next
    return chksum


if __name__ == '__main__':
    tape = LinkedList()
    blueprint = {
        'A': {
            0: (1, 'r', 'B'),
            1: (0, 'l', 'C')
        },
        'B': {
            0: (1, 'l', 'A'),
            1: (1, 'r', 'C')
        },
        'C': {
            0: (1, 'r', 'A'),
            1: (0, 'l', 'D')
        },
        'D': {
            0: (1, 'l', 'E'),
            1: (1, 'l', 'C')
        },
        'E': {
            0: (1, 'r', 'F'),
            1: (1, 'r', 'A')
        },
        'F': {
            0: (1, 'r', 'A'),
            1: (1, 'r', 'E')
        }
    }
    steps = 12134527
    state = 'A'

    for _ in range(steps):
        frame = tape.current
        rules = blueprint[state][frame.data]

        frame.data = rules[0]
        frame = tape.move_left() if rules[1] == 'l' else tape.move_right()
        state = rules[2]

    print(diagnose(tape))
