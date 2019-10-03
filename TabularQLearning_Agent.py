import random
import copy


class Agent:

    def __init__(self, name, q_table, lr_start=0.1, lr_end=0.01, lr_decay=0.9999, reward_discount=0.9, eps_start=0.0,
                 eps_end=0.0, eps_decay=0.95):
        # alpha decay hat keinen aunfluss
        # epsilon decay braucht es nur länger

        self.name = name

        self.q = q_table

        self.epsilon = 0.0
        self.epsilon_start = eps_start
        self.epsilon_end = eps_end
        self.epsilon_decay = eps_decay

        self.alpha = 0.1
        self.lr_start = lr_start
        self.lr_end = lr_end
        self.lr_decay = lr_decay

        self.episode = None

        self.gamma = reward_discount

        self.experience = []

    @staticmethod
    def create_matrix(rows, columns, content):
        result_matrix = []
        for i in range(rows):
            empty_matrix = []
            for j in range(columns):
                empty_matrix += [content]
            result_matrix += [empty_matrix]
            del empty_matrix

        return result_matrix

    @staticmethod
    def prepare_board(board):
        board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(board_state)):
            if board[0][i] == 0.99:
                board_state[i] = 2
        for j in range(len(board_state)):
            if board[1][j] == 0.99:
                board_state[j] = 1
        return board_state

    @staticmethod
    def board_to_number(board):
        number = 0
        for i in range(9):
            number += board[i] * 3 ** (8 - i)

        return number

    def make_move(self, board, episode, training):

        if training:
            if self.epsilon == 0.0:
                self.epsilon = copy.deepcopy(self.epsilon_start)
                self.alpha = copy.deepcopy(self.lr_start)

            if self.episode != episode:
                self.episode = episode
                self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
                self.alpha = max(self.lr_end, self.alpha * self.lr_decay)
        else:
            self.epsilon = 0.0

        q_values = self.q.table[self.board_to_number(self.prepare_board(board))]
        for i in range(len(q_values)):
            if board[2][i] == 0.01:
                q_values[i] = -10

        if random.random() > self.epsilon:

            return q_values.index(max(q_values))

        else:
            while True:
                random_number = random.randint(0, 8)
                if q_values[random_number] != -10:

                    return random_number

    def buffer_experience(self, board, move, reward, board_next, turn):

        self.experience.append([self.prepare_board(board), move, reward, self.prepare_board(board_next), turn])

        pass

    def evolve(self):

        for i in reversed(range(len(self.experience))):
            if i < len(self.experience) - 2 and self.experience[i][4]:
                board = self.board_to_number(self.experience[i][0])
                board_next = self.board_to_number(self.experience[i + 2][0])
                #print(board_next)
                #print(self.q.table[board][self.experience[i][1]], "3")
                self.q.table[board][self.experience[i][1]] = (1.0 - self.alpha) * self.q.table[board][
                    self.experience[i][1]] + self.alpha * self.gamma * max(
                        self.q.table[board_next])
                #print(self.q.table[board][self.experience[i][1]])

            elif i == len(self.experience) - 2 and self.experience[i][4]:
                board = self.board_to_number(self.experience[i][0])
                #print(self.q.table[board][self.experience[i][1]], "2")
                self.q.table[board][self.experience[i][1]] = (1.0 - self.alpha) * self.q.table[board][
                    self.experience[i][1]] + self.alpha * self.experience[i + 1][2]
                #print(self.q.table[board][self.experience[i][1]])

            elif i == len(self.experience) - 1 and self.experience[i][4]:
                board = self.board_to_number(self.experience[i][0])
                #print(self.q.table[board][self.experience[i][1]], "1")
                self.q.table[board][self.experience[i][1]] = (1.0 - self.alpha) * self.q.table[board][
                    self.experience[i][1]] + self.alpha * self.experience[i][2]
                #print(self.q.table[board][self.experience[i][1]])

        self.experience = []

        pass

    def learn(self, board, move, reward, board_next):
        board = self.board_to_number(self.prepare_board(board))
        board_next = self.board_to_number(self.prepare_board(board_next))
        self.q.table[board][move] = (1.0 - self.alpha) * self.q.table[board][move] + self.alpha * (
                    reward + self.gamma * max(self.q.table[board_next]))
