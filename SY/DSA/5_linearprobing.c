#include <stdio.h>
#include<stdlib.h>

int h[100];

void insert(int tsize)
{
int TABLE_SIZE = tsize;
 int key,index,i,flag=0,hkey;
 printf("\nenter a value to insert into hash table\n");
 scanf("%d",&key);
 hkey=key%TABLE_SIZE;
 for(i=0;i<TABLE_SIZE;i++)
    {

     index=(hkey+i)%TABLE_SIZE;

     if(h[index] == -1)
     {
        h[index]=key;
         break;
     }

    }

    if(i == TABLE_SIZE)

     printf("\nelement cannot be inserted\n");
}
void search(int tsize)
{
    int TABLE_SIZE = tsize;
 int key,index,i,flag=0,hkey;
 printf("\nenter search element\n");
 scanf("%d",&key);
 hkey=key%TABLE_SIZE;
 for(i=0;i<TABLE_SIZE; i++)
 {
    index=(hkey+i)%TABLE_SIZE;
    if(h[index]==key)
    {
      printf("value is found at index %d\n",index);
      break;
    }
  }
  if(i == TABLE_SIZE)
    printf("\n value is not found\n");
}
void display(int tsize)
{
  int TABLE_SIZE = tsize;
  int i;
  printf("Index\t");
  for(i=0;i< TABLE_SIZE; i++){
  printf("%d \t",i);
     
  }
  printf("\n");
  printf("Values\t");
  for(i=0;i< TABLE_SIZE; i++){
  printf("%d \t ",h[i]);    
  }
  printf("\n");
 
}
int main()
{
    int tsize;
    printf("Enter size of array: ")
    scanf("%d",&tsize);
    int opt,i;
    for( i =0;i<tsize;i++)
    {
        h[i]=-1;    
    }
    do
    {   
        printf("\n1)Insert \n2)Display \n3)Search \n4)Exit \n");
        printf("Enter yor choice:");
        scanf("%d",&opt);
        switch(opt)
        {
            case 1:
                insert(tsize);
                break;
            case 2:
                display(tsize);
                break;
            case 3:
                search(tsize);
                break;
            case 4:
                exit(0);
        }
    }
    while(opt!=4);
    return 0;
}
