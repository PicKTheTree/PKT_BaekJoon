// Problem title  :   escape from square
// Problem Number :   1085
// Problem Tier   :   Bronze 3
// Date           :   2026/03/30, 11:04
// URL            :   https://www.acmicpc.net/problem/1085

// 문제
// 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 
// 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 x, y, w, h가 주어진다.

// 출력
// 첫째 줄에 문제의 정답을 출력한다.

// 제한
// 1 ≤ w, h ≤ 1,000
// 1 ≤ x ≤ w-1
// 1 ≤ y ≤ h-1
// x, y, w, h는 

// 예제 입력            예제 출력 
// 6 2 10 3             1
// 1 1 5 5              1
// 653 375 1000 1000    347



/// C++ Version


#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
        int x, y, w, h;
        cin >> x >> y >> w >> h;

        cout << min({x, y, w - x, h - y});

        return 0;
}
    
