/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* ans=new ListNode();
        ListNode *result = ans;
        ListNode* temp1=l1;
        ListNode* temp2=l2;
        int carry=0;
        int digit;
        int value1;
        int value2;
        
        while(temp1!=NULL || temp2!=NULL || carry!=0){
            int sum=0;
            
            if(temp1!=NULL){
                sum+=temp1->val;
                temp1=temp1->next;
            }
            
            if(temp2!=NULL){
                sum+=temp2->val;
                temp2=temp2->next;
            }
            
            int value=sum + carry;
            carry=value/10;
            digit=value%10;

            ListNode* temp=new ListNode(digit);
            ans->val = temp->val;
            ans->next = temp;
            ans = ans->next;
            
        }
        ListNode* temp = result;
        ListNode* slast = NULL;
        while(temp->next)
        {
            slast = temp;
            temp = temp->next;
        }
        slast->next = NULL;
        delete temp;
        return result;
    }
};
