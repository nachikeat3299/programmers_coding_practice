class Node:
    def __init__(self, item):
        self.next = None
        self.previous = None

        self.item = item


class Stack:
    def __init__(self, mode):
        if mode == "linked_list":
            self.mode = mode

        elif mode == "array":
            self.mode = mode
            self.stack = []

        self.item_count = 0
        self.top = None
        self.bottom = None

    def push(self, item):
        if self.mode == "linked_list":
            new_item = Node(item)

            if self.item_count == 0:
                self.top = new_item
                self.bottom = new_item
            else:
                self.top.next = new_item
                new_item.previous = self.top
                self.top = new_item

        elif self.mode == "array":
            self.stack.append(item)
            
            if self.item_count == 0:
                self.bottom = self.stack.index(item)

            self.top = self.stack.index(item)

        self.item_count += 1

    def pop(self):
        if self.item_count == 0:
            print("There is nothing in this stack")
            return

        if self.mode == "linked_list":
            if self.item_count == 1:
                _return = self.top.item
                del self.top.next
                self.top = None
                self.bottom = None

            else:
                _return = self.top.item
                self.top = self.top.previous
                del self.top.next
                self.top.next = None

        elif self.mode =="array":
            _return = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1

        self.item_count -= 1
        return _return

    def __str__(self):
        _return = ""

        if self.item_count == 0:
            _return = "There is nothing in this stack"

        if self.mode == "linked_list":
            current = self.bottom
            for i in range(self.item_count):
                if i < self.item_count - 1:
                    _return += "{0} -> ".format(current.item)
                elif i == self.item_count - 1:
                    _return += "{0}".format(current.item)

                if current.next != None:
                    current = current.next

                else:
                    break

        elif self.mode == "array":
            for i in range(self.bottom, self.top + 1):
                _return += "[{0}]".format(self.stack[i])
                
        return _return



