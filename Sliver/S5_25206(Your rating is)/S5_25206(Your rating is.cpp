// Problem title  :   Your rating is(너의 평점은)
// Problem Number :   25206
// Problem Tier   :   Sliver 5
// Date           :   2025/04/03, 14:53
// URL            :   https://www.acmicpc.net/problem/25206


// 문제
// 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!

// 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

// 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

// 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

// A+	4.5
// A0	4.0
// B+	3.5
// B0	3.0
// C+	2.5
// C0	2.0
// D+	1.5
// D0	1.0
// F	0.0
// P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.

// 과연 치훈이는 무사히 졸업할 수 있을까?

// 입력
// 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

// 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

// 출력
// 치훈이의 전공평점을 출력한다.

// 정답과의 절대오차 또는 상대오차가 
// \(10^{-4}\) 이하이면 정답으로 인정한다.

// 예제 입력 1                                  예제 출력 1 
// ObjectOrientedProgramming1 3.0 A+            3.284483
// IntroductiontoComputerEngineering 3.0 A+
// ObjectOrientedProgramming2 3.0 A0
// CreativeComputerEngineeringDesign 3.0 A+
// AssemblyLanguage 3.0 A+
// InternetProgramming 3.0 B0
// ApplicationProgramminginJava 3.0 A0
// SystemProgramming 3.0 B0
// OperatingSystem 3.0 B0
// WirelessCommunicationsandNetworking 3.0 C+
// LogicCircuits 3.0 B0
// DataStructure 4.0 A+
// MicroprocessorApplication 3.0 B+
// EmbeddedSoftware 3.0 C0
// ComputerSecurity 3.0 D+
// Database 3.0 C+
// Algorithm 3.0 B0
// CapstoneDesigninCSE 3.0 B+
// CompilerDesign 3.0 D0
// ProblemSolving 4.0 P



///// C++ Version
#include<iostream>
using namespace std;

int main() 
{
    string lecture_name; double avg_score = 0; float sum_grade = 0;
    double score[20]; float grade[20]; string input_score; 

    for(int i = 0; i < 20; i++)
    {
        cin >> lecture_name >> grade[i] >> input_score;

        if (input_score[0] == 'P') continue;
        else if(input_score[0] == 'A') score[i] = 4.0;
        else if (input_score[0] == 'B') score[i] = 3.0;
        else if (input_score[0] == 'C') score[i] = 2.0;
        else if (input_score[0] == 'D') score[i] = 1.0;
        else if (input_score[0] == 'F') score[i] = 0.0;
        else cout << "error";

        if(input_score[1] == '+') score[i] += 0.5;
        
        sum_grade += grade[i];
        avg_score += grade[i] * score[i];
    }

    cout << avg_score / sum_grade;
    return 0;
}
