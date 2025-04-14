// Problem title  :   Factors And Multiples(배수와 약수)
// Problem Number :   5086
// Problem Tier   :   Bronze 3
// Date           :   2025/04/14, 17:32
// URL            :   https://www.acmicpc.net/problem/5086

// 문제
// 4 × 3 = 12이다.

// 이 식을 통해 다음과 같은 사실을 알 수 있다.

// 3은 12의 약수이고, 12는 3의 배수이다.

// 4도 12의 약수이고, 12는 4의 배수이다.

// 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

// 첫 번째 숫자가 두 번째 숫자의 약수이다.
// 첫 번째 숫자가 두 번째 숫자의 배수이다.
// 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
// 입력
// 입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

// 출력
// 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

// 예제 입력         예제 출력 
// 8 16              factor
// 32 4             multiple
// 17 5             neither
// 0 0



/// C++ Version


#include<iostream>
using namespace std;

int main()
{   
    int num_1, num_2;

    while(1)
    {
        cin >> num_1 >> num_2;

        if(num_1 == 0 && num_2 == 0) break;
        if(num_1 >= num_2)
        {
            if(num_1 % num_2 == 0) cout << "multiple\n";
            else cout << "neither\n";
        }

        else
        {
            if(num_2 % num_1 == 0) cout << "factor\n";
            else cout << "neither\n";
        }

    }
}