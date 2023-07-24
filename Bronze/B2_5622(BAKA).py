#Problem Title  :   BAKA0(다이얼)
#Problem Number :   5622
#Problem Tier   :   Bronze 2
#Date           :   2023/07/24, 11:22
#URL            :   https://www.acmicpc.net/problem/5622


#Discription
# Mirko's grandma still uses an ancient pulse dial telephone with a rotary dial as shown in the following picture:
# For each digit that we want to dial, we need to turn the rotary dial clockwise until the chosen digit reaches the finger stop (metal fin). Then we let go of the dial and wait for it to return to its original position before we can dial another digit. In our modern, instant gratification world, the dial return often lasts much longer than our patience. More precisely, dialling the digit 1 takes a total of two seconds, while dialling any larger digit takes an additional second for each additional finger circle counting from 1 to the dialled digit (as shown in the picture).
# Mirko's grandma remembers phone numbers by memorizing a corresponding word which, when dialled, results in the correct number being dialled. When dialling a word, for each letter, we dial the digit which has that letter written next to it on the dial (for example, the digit 7 for the letter S). For example, the word UNUCIC corresponds to the number 868242. Your task is determining, for a given word, the total time required to dial that word.

# 입력
# The first and only line of input contains a single word consisting of between 2 and 15 (inclusive) uppercase English letters.

# 출력
# The first and only line of output must contain the required dialling time.

# Example input         Example Output
# WA                    13
# UNUCIC                36

result = 0 
number = {     2:['A', 'B', 'C'], 3:['D', 'E', 'F'], 4:['G', 'H', 'I'],
            5:['J', 'K', 'L'], 6:['M', 'N', 'O'], 7:['P', 'Q', 'R', 'S'],
            8:['T', 'U', 'V'], 9:['W', 'X','Y', 'Z']
        }

input_list = list(input())

for _ in input_list:
    for key, value in number.items(): 
        if _ in value: result += 1 + key

print(result)