#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct ll_node {
    int data;
    struct ll_node*next;
};
struct ll_node *list;
struct ll_node*insert(struct ll_node *list)
{

    int value;

    struct ll_node *help_ptr = list;
    struct ll_node pnew = (struct ll_node) malloc(sizeof(struct ll_node));

   if(pnew!=NULL)
   {

      printf("Enter number to insert: ");
        scanf("%d",&value);

        pnew->data = value;
        pnew->next = NULL;

        if(list==NULL || list -> data > value)
        {
            pnew->next = list;
            list = pnew;
            return list;

        }
        while(help_ptr->next!=NULL && help_ptr -> next -> data < value )
        {

                help_ptr =help_ptr->next;
        }
        pnew->next=help_ptr->next;
        help_ptr->next=pnew;

        return list;
    }

    return list;

    }
struct ll_node * display()
{
    struct ll_node * help_ptr = list;
    if(list == NULL)
    {
        printf("Empty");
    }
    else
    {
        while(help_ptr !=NULL)
    {
        printf("\t %d", help_ptr-> data);
        help_ptr = help_ptr -> next;
    }
    }

};

struct ll_node *delete1(struct ll_node * list)
{
    int target;

    struct ll_node *help_ptr;
    struct ll_node *node2delete;
    help_ptr = list;

    printf("Enter number to delete: ");
    scanf("%d",&target);

    if (help_ptr!= NULL)
    {
        if(help_ptr->data == target)
        {
            list = help_ptr->next;
            free(help_ptr);
            return list;
        }
    while (help_ptr->next!=NULL)
    {
        if (help_ptr->next->data == target)
        {
            node2delete = help_ptr->next;
            help_ptr->next = help_ptr->next->next;
            free(node2delete);
            return list;
        }
        help_ptr = help_ptr->next;
    }
    }
    return list;
};

int main()
{

    int ch;
    list=NULL;
    do{
    printf("\n1.INSERT\n2.DELETE\n3.DISPLAY\n4.EXIT\n");
    printf("Enter your choice:");
    scanf("%d",&ch);
    switch(ch)
    {
    case 1:
        list=insert(list);
        break;
    case 2:
        //printf("delete");
    list=delete1(list);
    break;
   case 3:
       display( );
    break;
    case 4:
    exit(0);
    }
    } while(ch!= 4);

    return 0;
}