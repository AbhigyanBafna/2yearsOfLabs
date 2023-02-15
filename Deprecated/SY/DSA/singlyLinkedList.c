#include<stdio.h>
#include<stdlib.h>

//Self Referencing Structure
struct node{
    int data;
    struct node *next; //Pointer to store address of next node
};

struct node *head;

void display(struct node *ptr){
    int i = 1;
    while(ptr !=NULL){
        printf("Element %d = %d\n",i++, ptr->data);
        ptr = ptr->next;
    }
}

int val(){
    int data;
    printf("\nEnter value to insert : ");
    scanf("%d",&data);
    return data;
}

struct node* insertF(struct node *head){
    int data;
    data = val(); //New Head Value
    struct node *ptr = (struct node *) malloc(sizeof(struct node)); //New Head
    
    ptr->next = head; //New Head Pointing to Old Head
    ptr->data = data;
    return ptr;
}

struct node* insertB(struct node *head){
    int data;
    data = val(); //New Head Value

    struct node *ptr = (struct node *)malloc(sizeof(struct node)); //New Node
    ptr->data = data;

    struct node *hp = head; //Helper pointer for traversal
    while(hp->next!=NULL){
        hp = hp->next; //Traversal to last node
    }

    hp->next = ptr; //Linking new node after last node
    ptr->next = NULL;
    return head;
}

/*
struct node* insertAfterVal(struct node *head){
    int target; //Value After which insertion is to be done.
    printf("Enter the number after which you would like to insert : ");
    scanf("%d",&target);
    
    struct node *ptr = (struct node *)malloc(sizeof(struct node)); //New Node
    int data;
    data = val(); //New Head Value
    ptr->data = data;

    struct node *hp;
    struct node *oldNode;
    hp = head;

    if (hp!= NULL){

        if(hp->data == target){
            head->next = ptr; //Inserting New Node after Head
            ptr->next = hp->next; //Linking New Node ka next to Head ka old next
            return head;
        }

        while (hp->next!=NULL){
    
            if (hp->next->data == target){
                oldNode = hp->next;
                oldNode->next = ptr;
                ptr->next = hp->next->next;
                return head;
            }
            hp = hp->next;
        }
    }
    return head;
}
*/

void del(struct node *head){
    int val;
    printf("\nEnter the value you want to delete : ");
    scanf("%d",&val);
    struct node *p = head;
    struct node *q = head->next;

    while(q->data!=val && q->next!=NULL){
        p=p->next;
        q=q->next;
    }

    p->next=q->next;
    free(q);
}

int main(){
    
    struct node *first;
    struct node *second;
    head = (struct node *)malloc(sizeof(struct node));
    first = (struct node *)malloc(sizeof(struct node));
    second = (struct node *)malloc(sizeof(struct node));

    head ->data = 7;
    head ->next = first;

    first ->data = 10;
    first ->next = second;

    second ->data = 131;
    second ->next = NULL;

    display(head);
    head = insertAfterVal(head);
    display(head);
    head = insertAfterVal(head);
    display(head);

    return 0;
}