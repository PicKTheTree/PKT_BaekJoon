// Problem title  :   CETVRTA(네번째 점)
// Problem Number :   3009
// Problem Tier   :   Bronze 3
// Date           :   2026/03/31, 10:54
// URL            :   https://www.acmicpc.net/problem/3009

// 문제
// 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

// 입력
// 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

// 출력
// 직사각형의 네 번째 점의 좌표를 출력한다.

// 예제 입력 1         예제 출력 1 
// 5 5                7 7
// 5 7
// 7 5

// 예제 입력 2         예제 출력 2 
// 30 20              30 10                
// 10 10
// 10 20

/// C++ Version
#include<iostream>
#include<vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    vector<int> x_list(3);
    vector<int> y_list(3);

    for (int i = 0; i < 3; i++) {cin >> x_list[i] >> y_list[i];}

    int x_answer = x_list[0] ^ x_list[1] ^ x_list[2];
    int y_answer = y_list[0] ^ y_list[1] ^ y_list[2];

    cout << x_answer << " " << y_answer;
    return 0;
}
    
