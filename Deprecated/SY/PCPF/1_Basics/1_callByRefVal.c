 #include <stdio.h>  

//CALL BY VALUE
void Vswap (int a, int b)  
{  
    int temp;   
    temp = a;  
    a=b;  
    b=temp;  
    printf("CALL BY VALUE in function a = %d, b = %d\n",a,b); // a = 20, b = 10   
} 

//CALL BY REFERENCE
void Rswap (int *a, int *b)  
{  
    int temp;   
    temp = *a;  
    *a=*b;  
    *b=temp;  
    printf("CALL BY REF in function a = %d, b = %d\n",*a,*b); // a = 20, b = 10   
}  
 
int main() {  
    int a,b;
    a = 10;  b = 20;   
    Vswap(a,b);  
    printf("After CALL BY VALUE Swap a = %d, b = %d\n",a,b); // The value of actual parameters do not change. a = 10 b = 20
    a = 10;  b = 20; //Resetting values
    Rswap(&a,&b);  
    printf("After CALL BY REFERENCE Swap a = %d, b = %d\n",a,b); // The values of actual parameters do change. a = 20 b = 10
    return 0;
};
