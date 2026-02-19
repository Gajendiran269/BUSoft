#include <stdio.h>
#include <string.h>


 // int isPrime(int n) {
 //     if (n <= 1) return 0;
 //     if (n <= 3) return 1;
 //     if (n % 2 == 0 || n % 3 == 0) return 0;
    
 //     for (int i = 5; i * i <= n; i++) {
 //         if (n % i == 0)
 //             return//     return 1;
 // }

 // int main() {
 //     int num;
 //     printf("Enter a number: ");
 //     scanf("%d", &num);
    
 //     if (isPrime(num))
//         printf("%d is prime\n", num);
 //     else
 //         printf("%d is not prime\n", num);
    
 //     return 0;
  // }

 // int isPalindrome(char str[]) {
//     int left = 0, right = strlen(str) - 1;
//     while (left < right) {
 //         if (str[left] != str[right])
 //             return 0;
 //         left++;
 //         right--;
 //     }
 //     return 1;
 // }

 // int main() {
 //     char str[100];
 //     printf("Enter a string: ");
 //     scanf("%s", //     if (isPalindrom //         printf("%s is a palindrome\n" //   //         printf("%s is not a palindrome\n", str);
    
//     return 0;
// }
// int main() {
//     char str[100];
//     printf("Enter a string: ");
 //     scanf("%s", str);
    
//     int len = strlen(str)
//     for (int i = len - 1; i >= 0; i--) {
//         printf("%c", str[i]);
 //     }
//     printf("\n");
    
//     return 0;
 // }

 // int factorial(int n) {
 //     if (n <= 1)
 //         return 1;
//     return n * factorial(n - 1);
 // }

 // int main() {
 //     int num;
 //     printf("Enter a number: ");
 //     scanf("%d", &num);
 //     printf("Factorial of %d is %d\n", num, factorial(num));
    
//     return 0;
// }

// int main() {
//     int a, b, c, largest;
//     printf("Enter three numbers: ");
//     scanf("%d %d %d", &a, &b, &c);
    
//     largest = (a > b) ? (a > c ? a : c) : (b > c ? b : c);
    
//     printf("Largest number is %d\n", largest);
    
//     return 0;
// }

// int main() {
//     int arr[100], n;
//     printf("Enter array size: ");
//     scanf("%d", &n);
    
//     printf("Enter %d elements: ", n);
//     for (int i = 0; i < n; i++)
//         scanf("%d", &arr[i]);
    
//     printf("Duplicate elements: ");
//     for (int i = 0; i < n; i++) {
//         for (int j = i + 1; j < n; j++) {
//             if (arr[i] == arr[j]) {
//                 printf("%d ", arr[i]);
//                 break;
//             }
//         }
//     }
//     printf("\n");
    
//     return 0;
// }

// void swap(int *a, int *b) {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

// int main() {
//     int x, y;
//     printf("Enter two numbers: ");
//     scanf("%d %d", &x, &y);
    
//     printf("Before swap: x = %d, y = %d\n", x, y);
//     swap(&x, &y);
//     printf("After swap: x = %d, y = %d\n", x, y);
    
//     return 0;

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter array size: ");
    scanf("%d", &n);
    
    int *arr = (int *)malloc(n * sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    printf("Enter %d elements: ", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    
    printf("Array elements: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    
    free(arr);

    return 0;
}
