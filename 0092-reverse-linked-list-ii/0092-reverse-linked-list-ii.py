# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

	    #dummy 변수 만드는 이유 : left가 1일 경우에 head가 바뀔 수 있기 때문에 dummy 변수 필요
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # left 바로 전까지 이동
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        # reverse 수행
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next		#dummy.next를 이용하여 head부터 링크드 리스트 반환