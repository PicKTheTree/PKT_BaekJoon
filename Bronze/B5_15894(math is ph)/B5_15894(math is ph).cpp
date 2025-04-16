// Problem title  :   math is ph(수학은 체육과목 입니다)
// Problem Number :   15894
// Problem Tier   :   Bronze 3
// Date           :   2025/04/16, 22:05
// URL            :   https://www.acmicpc.net/problem/15894

// 문제
// "한 변의 길이가 1인 정사각형을 아래 그림과 같이 겹치지 않게 빈틈없이 계속 붙여 나간다. 가장 아랫부분의 정사각형이 n개가 되었을 때, 실선으로 이루어진 도형의 둘레의 길이를 구하시오."



// 입력
// 첫 번째 줄에 가장 아랫부분의 정사각형 개수 n이 주어진다. (1 ≤ n ≤ 109)

// 출력
// 첫 번째 줄에 형석이가 말해야 하는 답을 출력한다.

// 예제 입력         예제 출력 
// 1                4
// 3                12



/// C++ Version


#include<iostream>
using namespace std;

int main()
{   
    unsigned int input;
    cin >> input;
    cout << input * 4;
}