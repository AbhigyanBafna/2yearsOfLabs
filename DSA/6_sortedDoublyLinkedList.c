#include<stdio.h>
#include<stdlib.h>

struct node { //Here we go again -_-
int data;
struct node *next; 
struct node *prev; //The upgrade to DLL.
};

struct node *head = NULL; //Initializing ...

void display(){

    struct node *hpptr;
    hpptr = head; //Assigning head to helper pointer for traversal.

    if (hpptr == NULL){
        printf("Linked List is Empty");
        return;
    }
    while(hpptr != NULL){
        printf("%d \n",hpptr->data);
        hpptr=hpptr->next; //Printing data and moving on in life.
    }
    return;
}

void insert(int x){

    struct node *hpptr; //The helper.
    struct node *pnew; //The new node.

    pnew=(struct node*) malloc(sizeof(struct node)); //Initializing the new node...
    pnew->data=x; 
    pnew->next=NULL; 
    pnew->prev=NULL;

    if(head==NULL){ //Nothing present in LL
        head=pnew; //Making new node the head.
        return;
    }
    if(head->data > x){ //Checking if new data < head data
        pnew->next=head;
        head->prev=pnew; 
        head=pnew; //Head is bigger hence making new node the head to sort in Asc. Order
        return;
    }

    hpptr=head; //Initializing...

    while(hpptr->next!=NULL && hpptr->next->data<x){ //Finding the correct next node in asc. order for new node
        hpptr=hpptr->next; // Traversing ahead.
    }

    pnew->next=hpptr->next; //Assigning next node location to new node.

    if(hpptr->next!=NULL){
    hpptr->next->prev=pnew; //Giving the next node, the location to new node.
    }

    hpptr->next=pnew; //Assigning first node after head usually.
    pnew->prev=hpptr; //Giving new node the location to previous node.
    return;
}

void del(int x){ 
    struct node *hpptr; 
    struct node *temp; //The Target Node.

    if(head==NULL){
      printf("List is empty \n");  
      return;
    }

    if(head->data==x){ //If Value to delete is head...
        temp=head; 
        head=head->next; //Assigning new head.
        head->prev=NULL;
        free(temp); //Deleting head.
        return;
    }

    hpptr=head; 
    if(hpptr->next == NULL){
        printf("\nElement not found"); //End of LL Reached
        return;
    }

    while(hpptr->next->data != x){
    hpptr=hpptr->next; //Traversing until Target found.
    }
    
    temp=hpptr->next; //Target Acquired.
    
    hpptr->next=temp->next; //Giving location of Targets Next node to Targets previous Node. (Ensuring no strings attached)

    if(temp->next != NULL){ 
    temp->next->prev=hpptr; //Giving location of Targets previous node to Targets Next node.
    }

    free(temp); //Target goes BOOM.
    return;
}

int taker(){
    int x;
    printf("Enter Value: ");
    scanf("%d", &x);
    return x;
}

int main(){
    int n,x;
    while (n != 4){

        printf("\nEnter you choice\n1. Insert\n2. Delete\n3. Display\n4. Exit\n");
        scanf("%d", &n);
        switch (n){
        case 1:
            x = taker();
            insert(x);
            break;
        case 2:
            x = taker();
            del(x);
            break;
        case 3:
            display();
            break;
        case 4:
            printf("Thank you!");
            exit(0);
            break;
        default: //Optional
            printf("Bad input.\n");
        }

    }
    return 0;
}