def commission_decorator(func):
    def wrapper(balance, amount):
        commission = 1
        total_amount = amount + commission

        if balance < total_amount:
            return "შეცდომა: ანგარიშზე საკმარისი თანხა არ არის"

        return func(balance, total_amount)

    return wrapper


@commission_decorator
def transaction(balance, amount):
    return balance - amount


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def search(self, data):
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True

            current = current.next

        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


print(transaction(20, 5))
print(transaction(5, 5))

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display()
linked_list.search(20)
linked_list.display()
