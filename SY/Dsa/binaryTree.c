#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* left;
    struct node* right;
};

int val(){
    int data;
    printf("\nEnter value to insert : ");
    scanf("%d",&data);
    return data;
}

struct node* createNode(){
    int data = val();

    struct node *n = (struct node*) malloc(sizeof(struct node));
    n->data = data;
    n->left = NULL;
    n->right = NULL;

    return n;
}

int main(){
    struct node* root = createNode();
    struct node* n1 = createNode();
    struct node* n2 = createNode();

    //Linking the root to n1,n2
    root->left = n1;
    root->right = n2;

    return 0;
}