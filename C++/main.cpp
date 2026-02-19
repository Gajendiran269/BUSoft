#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

// // // // // int main() {
// // // // //     string s = "gajendiran";
// // // // //     reverse(s.begin(), s.end());
// // // // //     cout << "Reversed String: " << s << endl;
// // // // //     return 0;
// // // // // }



// // // // int main() {
// // // //     int arr[] = {10, 25, 5, 40, 15};
// // // //     int n = sizeof(arr) / sizeof(arr[0]);

// // // //     int maxElement = *max_element(arr, arr + n);
// // // //     cout << "Maximum Element: " << maxElement << endl;
// // // //     return 0;
// // // // }



// // // bool isPalindrome(string s) {
// // //     int left = 0, right = s.length() - 1;
// // //     while (left < right) {
// // //         if (s[left] != s[right])
// // //             return false;
// // //         left++;
// // //         right--;
// // //     }
// // //     return true;
// // // }

// // // int main() {
// // //     string s = "madam";

// // //     if (isPalindrome(s))
// // //         cout << "Palindrome" << endl;
// // //     else
// // //         cout << "Not Palindrome" << endl;

// // //     return 0;
// // // }



// // void swapNumbers(int &a, int &b) {
// //     int temp = a;
// //     a = b;
// //     b = temp;
// // }

// // int main() {
// //     int x = 5, y = 10;
// //     swapNumbers(x, y);
// //     cout << "After Swap: x = " << x << " y = " << y << endl;
// //     return 0;
// // }


// using namespace std;

// int main() {
//     string s = "programming";
//     map<char, int> freq;

//     for (char c : s)
//         freq[c]++;

//     for (auto it : freq)
//         cout << it.first << " -> " << it.second << endl;

//     return 0;
// // }
// class Person {
// public:
//     string name;
//     int age;
    
//     Person(string n, int a) {
//         name = n;
//         age = a;
//     }
    
//     void display() {
//         cout << "Name: " << name << ", Age: " << age << endl;
//     }
// };

// int main() {
//     Person p1("John", 25);
//     Person p2("Alice", 30);
    
//     p1.display();
//     p2.display();
    
//     return 0;
// }
