// Problem title  :   Turet(터렛)
// Problem Number :   1002
// Problem Tier   :   Sliver 3
// Date           :   2026/03/19, 08:57
// URL            :   https://www.acmicpc.net/problem/1002

// 문제
// 조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.



// 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

// 조규현의 좌표 
// (x1, y1)와 백승환의 좌표 
// (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 
// r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.1

// 입력
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

// 한 줄에 공백으로 구분 된 여섯 정수 
// x1, y1, r1, x2, y2, r2 가 주어진다.

// 출력
// 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1 출력한다.

// 예제 입력             예제 출력
// 3
// 0 0 13 40 0 37       2   
// 0 0 3 0 7 4          1 
// 1 1 1 1 1 5          0 


///// C++ Version

#include<iostream>
#include<cmath>
using namespace std;

int main() 
{
    //Clear_buffer_code
    ios::sync_with_stdio(false); 
    cin.tie(0); 
    cout.tie(0);   
    
    int num;
    cin >> num;
    for (int i=0; i<num; i++)
    {
        int x1, y1, r1, x2, y2, r2, sum_r1r2, difference_r1r2;
        double distance;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

        sum_r1r2 = r1 + r2;
        difference_r1r2 = abs(r1 -r2);
        distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)); 
    
        //두 터렛이 같은 위치에 있을 때 
        if (distance == 0) 
        {
            if (r1 == r2) {cout << -1 << "\n";}
            else {cout << 0 << "\n";}
        }

        //두 터렛이 내접하거나 외접할 때                                     
        else if (distance == difference_r1r2 || distance == sum_r1r2) {cout << 1 << "\n";}   
        
        //두 터렛이 두 점에서 만날 때
        else if (distance > difference_r1r2 && distance < sum_r1r2) {cout << 2 << "\n";}
        
        //두 터렛이 만나지 않을 때
        else {cout << 0 << "\n";}                                                               
    }
}
