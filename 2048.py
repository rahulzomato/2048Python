import random, sys
class Helpers(object):

    @staticmethod
    def merge(line):
        merged = False
        non_zeroes = [i for i in line if i != 0]
        while len(non_zeroes) != len(line):
            non_zeroes.append(0)

        result = []
        for number in range(0, len(non_zeroes) - 1):
            if non_zeroes[number] == non_zeroes[number + 1] and not merged:
                result.append(non_zeroes[number] * 2)
                if (non_zeroes[number] * 2 == 2048):
                    print ('You won')
                    sys.exit(0)
                merged = True
            elif non_zeroes[number] != non_zeroes[number + 1] and not merged:
                result.append(non_zeroes[number])
            elif merged:
                merged = False

        if non_zeroes[-1] != 0 and not merged:
            result.append(non_zeroes[-1])

        while len(result) != len(non_zeroes):
            result.append(0)

        return result

class Game(object):

    def __init__(self, size):
        self.game = True
        self.matrix = []
        for i in range(0, size):
            self.matrix.append([0]*size)

    def place_random_2_4(self):
        print ('placing a random number (2/4)')
        positions_available = []
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if not self.matrix[i][j]:
                    positions_available.append([i,j])

        if not positions_available:
            print('Game over')
            self.game = False

        random_pos = random.choice(positions_available)
 
        weighted_choices = [(2, 9), (4, 1)]
        population = [val for val, cnt in weighted_choices for i in range(cnt)]
        weighted_random_val = random.choice(population)

        self.matrix[random_pos[0]][random_pos[1]] = weighted_random_val


    def print(self):
        for row in self.matrix:
            print(row)

    def move(self, direction):
        # left
        if direction == 0:
            print('move left')
            new_matrix = [Helpers.merge(row) for row in self.matrix]
            self.matrix = new_matrix

        # right
        elif direction == 1:
            print('move right')
            temp_matrix = [list(reversed(row)) for row in self.matrix]
            new_matrix = [Helpers.merge(row) for row in temp_matrix]
            new_matrix = [list(reversed(row)) for row in new_matrix]
            self.matrix = new_matrix

        # up
        elif direction == 2:
            print ('move up')
            transposed = zip(*self.matrix)
            new_matrix = [Helpers.merge(row) for row in transposed]
            transposed = map(list, zip(*new_matrix))

        # down
        else:
            print ('move down')
            transposed = zip(*self.matrix)
            temp_matrix = [list(reversed(row)) for row in transposed]
            new_matrix = [Helpers.merge(row) for row in temp_matrix]
            new_matrix = [list(reversed(row)) for row in new_matrix]
            transposed = map(list, zip(*new_matrix))



if __name__=='__main__':
    game = Game(3)
    # game.print()
    game.matrix= [
        [2,2,4,8],
        [0,4,4,0],
        [0,0,2,16],
        [0,0,0,0]
    ]

    game.print()
    game.place_random_2_4()
    # game.move(1)
    game.print()
