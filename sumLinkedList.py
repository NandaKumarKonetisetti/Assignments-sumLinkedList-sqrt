print("Enter the first linked list values:")
l1 = list(map(int, input().split()))
print("Enter the second linked list values:")
l2 = list(map(int, input().split()))


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def create_linked_list(li):
    head = Node(li[0])
    current = head
    for data in li[1:]:
        new_node = Node(data)
        current.next = new_node
        current = new_node
    return head


def reverse_linked_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def sum_lists(node1, node2):
    head = None
    prev = None
    current1 = node1
    current2 = node2
    carry = 0
    while current1 or current2:
        data1 = current1.data if current1 else 0
        data2 = current2.data if current2 else 0
        total = data1 + data2 + carry
        carry = total // 10
        digit = total % 10

        node = Node(digit)
        if head is None:
            head = node
        else:
            prev.next = node
        prev = node

        if current1:
            current1 = current1.next
        if current2:
            current2 = current2.next

    if carry > 0:
        node = Node(carry)
        prev.next = node

    return head


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()


linked_list1 = create_linked_list(l1)
linked_list2 = create_linked_list(l2)
reverse_linked_list1 = reverse_linked_list(linked_list1)
reverse_linked_list2 = reverse_linked_list(linked_list2)

print("Sum of the two linked lists:")
result = sum_lists(reverse_linked_list1, reverse_linked_list2)
print_linked_list(result)


