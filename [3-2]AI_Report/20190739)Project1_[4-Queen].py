# 20190739 박경태 인공지능 과제1

# 설명 :
# 본 코드는 유전자 알고리즘을 활용하여 4-queen 문제를 해결하기 위한 코드이다.
# 최대한 각 기능들을 함수로 구현하는 것을 목표로 하였다.
# 또한, matplotlib를 활용하여, 퀸의 위치를 GUI로 출력하는 기능을 구현하였다.
# 참조 : https://untitledtblog.tistory.com/110

import random
import matplotlib.pyplot as plt

# 유전자 클래스
# x축 기준으로 가장 왼쪽의 Queen1부터 시작하여,
# Queen4까지의 y축 위치를 저장한 염색체를 생성한다.
# 이때 초기 염색체의 유전자는 무작위로 생성한다. ex)[2,0,3,1]
class Chromosome:
    def __init__(self, genes):
        self.genes = genes.copy()  # 유전자는 리스트로 구현된다. ex)[0,2,1,3]
        self.hits = 0  # 퀸이 서로 공격 당할 수 있는 경우의 수

    # self.hits 을 계산하는 함수
    def hits_check(self):
        queen_hits = 0
        for i in range(len(self.genes)):

            for j in range(i + 1, len(self.genes)):

                # 퀸i와 퀸j가 서로 같은 y축에 있거나, 대각선에 있는 경우
                if (self.genes[i] == self.genes[j]
                    or abs(i - j) == abs(self.genes[i] - self.genes[j])):
                    queen_hits += 1
        self.hits = queen_hits

# 현 새대의 염색체를 생성하는 함수이다.
# population_size만큼 염색체를 생성한다.
# 4-queen 이므로 유전자 갯수는 4개로 고정이다.
def create_population(population_size, size):
    population = []
    for _ in range(population_size):
        genes = [random.randint(0, size - 1) for _ in range(size)]
        chromosome = Chromosome(genes)
        population.append(chromosome)
    return population

# 다음 세대의 염색체를 생성하기 위한 부모 염색체를 선택하는 함수이다.
# self.hits의 수가 적을 수록 부모로 선택될 확률이 높아진다. >> 룰렛 휠 사용
def selection(population, scores):
    selected_parents = []
    for _ in range(2):
        selected = random.choices(population, weights=[1 / (s.hits + 1) for s in population])
        selected_parents.append(selected[0])
    return selected_parents

# 부모로 선택된 두 개의 염색체를 기반으로 새로운 자식을 생성한다.
# 이때, 사용될 인덱스는 랜덤이다.
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.genes) - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Chromosome(child_genes)

# 돌연변이를 발생하여, 새로운 염색체를 생성한다.
def mutate(chromosome, size):
    mutate_index = random.randint(0, len(chromosome.genes) - 1)
    chromosome.genes[mutate_index] = random.randint(0, size - 1)

# consloe에 Queen의 위치를 표시한다.
def print_queen_positions(board):
    for i in range(len(board)):
        print(f"[{i+1}, {board[3-i]+1}]")


# matplotlib를 활용하여, 체스판 형태를 table의 형태로 나태낸다.
# 그 후, 최적의 해(hits=0)을 찾으면, 각 Queen의 위치를 표시한다.
def print_board(board):
    board_size = len(board)

    plt.figure(figsize=(8, 8))

    data = [['' for _ in range(board_size)] for _ in range(board_size)]
    for i, row in enumerate(board):
        data[row][i] = '♛'

    table = plt.table(cellText=data, loc='center', cellLoc='center', edges='closed')

    # table의 셀의 크기를 정사각형으로 만들기 위한 반복문
    # 또한 체스판 처럼 색칠을 칠하였다.
    # 참조 : https://omgchess.blogspot.com/2015/09/chess-board-color-schemes.html
    cell_size = 1.0 / board_size
    for i in range(board_size):
        for j in range(board_size):
            cell = table[i, j]
            cell.set_height(cell_size)
            cell.set_width(cell_size)
            text = cell.get_text()
            text.set_fontsize(60)

            if (i + j) % 2 == 0:
                cell.set_facecolor((184/255, 139/255, 74/255))
            else:
                cell.set_facecolor((227/255, 193/255, 111/255))

    # Queen의 위치를 나타내는 x, y축을 추가하였다.
    # 하지만, 현재의 plot은 table이므로, x,y 값은 존재하지 않는다.
    # 따라서, 강제로 x, y의 label을 추가하여 값을 표시하도록 하였다.
    x_tick_labels = [str(i+1) for i in range(board_size)] # 1 ~ 4
    y_tick_labels = [str(i+1) for i in range(board_size)] # 1 ~ 4
    plt.xticks([0.125 + i * 0.25 for i in range(board_size)], x_tick_labels)
    plt.yticks([0.125 + i * 0.25 for i in range(board_size)], y_tick_labels)

    plt.title('20190739 Park Kyeong Tae')
    plt.show()
def genetic_algorithm(population_size, size, generations):

    population = create_population(population_size, size)

    for gen in range(generations):

        #
        for chrom in population:    chrom.hits_check()
        best_chrom = min(population, key=lambda x: x.hits)

        if best_chrom.hits == 0:
            return best_chrom.genes

        parents = []
        for _ in range(population_size):
            parent_selection = selection(population, [chrom.hits for chrom in population])
            parents.append(parent_selection)

        children = []
        for i in range(population_size):
            child = crossover(parents[i][0], parents[i][1])
            children.append(child)

        # 10% 확률로 돌연변이가 발생하여, 자식 유전자를 변경한다.
        for child in children:
            if random.random() < 0.1:  mutate(child, size)

        population = children

    return None  # 적합도가 0인 해를 찾지 못하면, None을 반환한다.

solution = genetic_algorithm(100, 4, 1000)
if solution:
    print("Solution found:"
          "\nx, y")
    print_queen_positions(solution) # 적합한 해가 발견되면 consloe에 퀸의 위치 표시
    print_board(solution)  # 적합한 해가 발견되면 체스판에 퀸의 위치 표시

else:
    print("No solution found within generations.")