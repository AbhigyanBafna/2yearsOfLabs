#include <stdio.h> 
#include <stdlib.h>

void printArr(int a[], int n) {  
    printf("Sorted Array : \n");
    
    for(int i=0;i<n;i++){
        printf("%d\t",a[i]);
    }
    printf("\n"); 
}

// QUICK SORT

int partition (int a[], int start, int end)  {  
    int pivot = a[end]; // pivot element  
    int i = (start - 1);  
  
    for (int j = start; j <= end - 1; j++){    //Starting fron first element to second last as last element is pivot.
    
        if (a[j] < pivot){ //Taking all elements smaller to pivot on left side. (Virtual Array)
            i++; 
            int t = a[i];  
            a[i] = a[j];  
            a[j] = t;  
        }  
    }  
    int t = a[i+1];  
    a[i+1] = a[end]; //Assigning pivot to its right place.
    a[end] = t;  
    return (i + 1); //Returning pivot element's index.
}  
  
/* function to implement quick sort */  
void quickSort(int a[], int start, int end) { /* a[] = array to be sorted, start = Starting index, end = Ending index */  

    if (start < end) { 
        int p = partition(a, start, end); //p is the partitioning index  
        quickSort(a, start, p - 1); //Sorting left virtual array.
        quickSort(a, p + 1, end); //Sorting Right virtual array.
    }  

}   

//RADIX SORT

int largest(int a[], int n){
    int larger=a[0];

    for(int i=1;i<n;i++){ //Finds out the largest element in the array.
        if(a[i]>larger){
            larger=a[i]; 
        }
    }
    return larger;
}

void radixSort(int a[],int n){
    int bucket[10][10]; //Sorted elements are placed in here.
    int bucketC[10]; //Counts the number of elements in bucket. 
    int i,j,k,rem,NOP=0,divisor=1,maxE,pass;
    
    maxE=largest(a,n); //Largest Element in Array

    while(maxE>0){
        NOP++; //Finding total number of passes based on Digits in maxE
        maxE/=10;
    }

    for(pass=0 ; pass<NOP ; pass++){ 

        for(i=0;i<10;i++){
            bucketC[i]=0; //Initializing bucketC before sorting.
        }

        for(i=0;i<n;i++){
            rem=(a[i]/divisor)%10; //Finding DIGIT (Units, Tens, Hundreds...)
            bucket[rem][bucketC[rem]] = a[i]; //Assigning bucket to element based on DIGIT
            bucketC[rem] += 1;
        }

        i=0;
        for(k=0;k<10;k++){
            for(j=0;j<bucketC[k];j++){ 
                a[i]=bucket[k][j]; //Ordering Array based on DIGIT Sorting.
                i++;
            }
        }
        divisor *=10; //Changing Divisor for increment in DIGIT in next pass.
    }
}

int main(){
    int sort, n;
    int i;

    while(sort != 4){

    printf("Please enter number of elements : ");
    scanf("%d",&n);
    int arr[n];

    printf("\n");

    for(i = 0; i<n ; i++){
        printf("Element %d : ", i+1);
        scanf("%d",&arr[i]);
    }

    printf("\n1.Quick Sort \n2.Radix Sort \n3.Exit\n");

    printf("Please enter your choice : ");
    scanf("%d",&sort);
        switch(sort){
            case 1 :
                quickSort(arr,0,n);
                printArr(arr,n);
                break;
            case 2 :
                radixSort(arr, n);
                printArr(arr,n);
                break;
            case 3 :
                exit(0);
        }
    }
    return 0;
}