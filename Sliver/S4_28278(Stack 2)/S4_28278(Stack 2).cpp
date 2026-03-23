// Problem title  :   Stack2
// Problem Number :   28278
// Problem Tier   :   Sliver 4
// Date           :   2026/03/23, 13:41
// URL            :   https://www.acmicpc.net/problem/28278


// 문제
// 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

// 명령은 총 다섯 가지이다.

// 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
// 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
// 3: 스택에 들어있는 정수의 개수를 출력한다.
// 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
// 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

// 입력
// 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

// 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

// 출력을 요구하는 명령은 하나 이상 주어진다.

// 출력
// 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

// 예제 입력 1    
// 9
// 4
// 1 3
// 1 5
// 3
// 2
// 5
// 2
// 2
// 5

// 예제 출력 1
// 1
// 2
// 5
// 3
// 3
// -1
// -1




///// C++ Version
#include<iostream>
#include<stack>
using namespace std;


stack<int> stack_1;

int stack_remote(int num)
{
    switch (num)
    {
        case 1:
        {
            int element = 0;
            cin >> element;
            stack_1.push(element);
            break;
        }
        case 2:
            
            if (!stack_1.empty()) {cout << stack_1.top() << "\n"; stack_1.pop();}
            else {cout << -1 << "\n";} 
            break;

        case 3:

            cout << stack_1.size() << "\n";
            break;

        case 4:

            if (!stack_1.empty()) {cout << 0 << "\n";}
            else {cout << 1 << "\n";} 
            break;

        case 5:
            
            if (!stack_1.empty()) {cout << stack_1.top() << "\n";}
            else {cout << -1 << "\n";} 
            break;

        default:
            cout << "Unknown\n";
            break;
    }
    return 0;
}

int main()
{
    
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);

    int N, remote_num = 0;
    cin >> N;

    while (N--)
    {
        cin >> remote_num;
        stack_remote(remote_num);
    }
    
    return 0;
}
