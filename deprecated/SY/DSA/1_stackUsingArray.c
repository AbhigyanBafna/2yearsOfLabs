#include <stdio.h>
#include <stdlib.h>
#define Size 5 //Size of Stack

void push();
void pop();
void display();

struct stack{ //Struct is sUpErIOr
    int top;
    int item[Size];
}s1;

int main()
{
    s1.top = -1; //Initializing ... 
    int choice;
    printf("Stack Menu\n 1. Push\n 2. Pop\n 3. Display\n 4. Exit\n");
    do{
    printf("Enter Operation Num: ");
    scanf("%d",&choice);
        switch(choice){
            case 1 : push();
            printf("\n"); //Optional Spacing
            break;
            case 2 : pop();
            printf("\n");
            break;
            case 3 : display();
            printf("\n");
            break;
            case 4 : printf("Goodbye");
            exit(0);
            default : printf("Bad input.\n");
        }
    }while(choice != 4);
    return 0;
}

void push(){
    int X;
    if(s1.top == Size-1){
        printf("Error Stack is Full \n");
        return;
    }
    printf("Please enter number to push into Stack\n");
    scanf("%d",&X);
    printf("\n");
    s1.top++;
    s1.item[s1.top]=X;
    printf("Number has been successfully Pushed\n \n");
    printf("Displaying Stack :\n");
    display();
}

void pop(){
    if(s1.top == -1){
        printf("Error Stack is Empty\n");
        return;
    }
    printf("Item %d: %d has been poped!\n",s1.top+1,s1.item[s1.top]);
    s1.top--;
    printf("Displaying Stack :\n");
    display();
}

void display(){
    int count = 1;

    for(int i = s1.top; i>=0; i--){
        printf("Item %d : %d \n",count,s1.item[i]);
        count++;
    }
}

/*

Stack is a linear DS following LIFO. 
Data in the middle or bottom cannot be modified 
all operations are performed at top.
Using array/struct makes the stack static.
To make it dynamic we can use LL.

Time Complexites :

push() : O(1)
pop() : O(1)
display() : O(n)

*/