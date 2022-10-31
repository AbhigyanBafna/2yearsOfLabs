#include <stdio.h>
#include <stdlib.h>
#define SIZE 10

struct queue{   //Cause structs are superior to arrays -_-

    int items[SIZE]; //If you don't know what this is go back to first year.
    int front; //Points to front of queue.
    int rear; //Points to end of queue.

}s1;

//Adds Elements to Queue
void enqueue(){
    int x;
    if (s1.rear == SIZE - 1){  //Rear reached end of Array hence no more space.
        printf("Error : Queue Full\n");
        return;
    }

    if (s1.front == -1){ //Initializing front of queue while inserting first element.
            s1.front = 0;
    }

    printf("Enter number : "); //Insertion of element.
    scanf("%d", &x);
    s1.items[s1.rear] = x;
    s1.rear++; //Mapping rear to end of queue.
    return;
}

// Removes Elements from Queue
void dequeue(){

    if (s1.front == -1){ //No elements present in Queue to delete
        printf("Error : Queue Empty\n");
        return;
    }
    printf("Dequeued item: %d\n", s1.items[s1.front]);
    s1.front++;

    if (s1.front > s1.rear){ //If front exceeds back that means queue is empty
        s1.front = -1; //So we reset the queue by this.
        s1.rear = -1;
    }
    return;
}

//Probably know what this does.
void display(){

    if (s1.rear == -1){
        printf("Queue is Empty.\n");
        return;
    }
    for (int i = s1.front; i <= s1.rear; i++){
        printf("%d ", s1.items[i]); //Printing each element from front to back.
    }
    return;
}

void main(){

    s1.front = -1;
    s1.rear = -1; //Initializing front and back variables
    int n; //Choice for Switch Case.

    while (n != 4){ //While loop to run Menu until Exit.

        printf("\nEnter you choice\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n");
        scanf("%d", &n);
        switch (n){
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
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
}

/*

Stack is a linear DS following FIFO. 
They are like real world Queue's.
Using array/struct makes the queue static.
To make it dynamic we can use LL.

Time Complexites :

enqueue() : O(1)
dequeue() : O(1)
display() : O(n)

*/