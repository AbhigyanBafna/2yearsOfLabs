#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], int n){
    printf("\n");
    for (int i = 0; i < n; i++){
            printf("%d ", arr[i]);
        }
    printf("\n");
}

void insertionSort(int arr[], int n){
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        printArray(arr,n);

        while (j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void selectionSort(int arr[], int n) {

  for (int step = 0; step < n - 1; step++) {

    printArray(arr,n);

    int min = step;

        for (int i = step + 1; i < n; i++) {
          if (arr[i] < arr[min])
            min = i;
        }

        swap(&arr[min], &arr[step]);
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
    printf("\n1.Insertion sort \n2.Selection sort \n3.Exit\n");
    printf("Please enter your choice : ");
    scanf("%d",&sort);
        switch(sort){
            case 1 :
                insertionSort(arr, n);
                printArray(arr, n);
                break;
            case 2 :
                selectionSort(arr, n);
                printArray(arr,n);
                break;
            case 3 :
                exit(0);
        }
    }
    return 0;
}
