/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return head;
        Node curr=head;
        while(curr!=null){
            Node copy=new Node(curr.val);
            copy.next=curr.next;
            curr.next=copy;
            curr=curr.next.next;
        }
        curr=head;
        while(curr!=null && curr.next!=null){
            if(curr.random!=null){
                curr.next.random=curr.random.next;
            }
            curr=curr.next.next;
        }
        curr=head;
        Node nhead=head.next;
        while(curr!=null){
            Node copy=curr.next;
            curr.next=copy.next;
            if(copy.next!=null){
            copy.next=copy.next.next;
            }
            curr=curr.next;
        }
        return nhead;
    }
}