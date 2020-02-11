/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(1);
        ListNode tail=temp;

        // 片方が空になるまで
        while(l1!=null && l2!=null){
            // 値が小さい方の数値をtailにつなげる
            if(l1.val <= l2.val){
                tail.next = l1;
                l1 = l1.next;
            }else{
                tail.next = l2;
                l2 = l2.next;
            }
            
            // 末尾を更新
            tail=tail.next;
        }

        // 一方が空ならば空でないリストをそのままつなげる
        if(l1!=null){
            tail.next = l1;
        } else if(l2!=null){
            tail.next = l2;
        }

        return temp.next;
    }
}