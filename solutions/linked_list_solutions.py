from typing import Optional

class List_node:
    """
        list_node definition
    """
    def __init__(self, val: 0, next: None) -> None:
        self.val = val
        self.next = next


class linked_list_solutions:
    def reverse(self, head: Optional[List_node]) -> Optional[List_node]:
        """
            Description: reversing every node in the linked list
            head: reference to the first node
            return: reversed linked_list
        """
        
        temp = head
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev