import copy
import random


class Play:

    def __init__(self, player1, player2, number_of_episodes, train, win_reward=1.0, lose_reward=-1.0, draw_reward=0.5):

        self.player_1 = player1
        self.player_2 = player2
        self.name_player_1 = "{}".format(self.player_1.name)
        self.name_player_2 = "{}".format(self.player_2.name)

        self.player_x_turn = None
        self.not_player_x_turn = None

        self.board = None
        self.board_next = None
        self.board_empty = [[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
                            [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
                            [0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]]

        self.move = None

        self.win_value = win_reward
        self.lose_value = lose_reward
        self.draw_value = draw_reward
        self.reward = None
        self.reward_opponent = None

        self.game_playing = True
        self.episodes = number_of_episodes
        self.training = train

        self.result = None
        self.statistics = None
        self.statistics_total = {self.name_player_1: 0, self.name_player_2: 0, "Draw": 0}
        self.statistic_empty = {self.name_player_1: 0, self.name_player_2: 0, "Draw": 0}

        self.play_tic_tac_toe()

    def set_up_game(self):

        self.board = copy.deepcopy(self.board_empty)
        self.reward = 0
        self.reward_opponent = 0

        if random.randint(0, 1) == 0:
            self.player_x_turn, self.not_player_x_turn = self.player_1, self.player_2
        else:
            self.player_x_turn, self.not_player_x_turn = self.player_2, self.player_1

        self.game_playing = True

        pass

    def end_of_turn(self):

        self.change_board()

        if self.player_x_turn == self.player_1:
            self.player_x_turn, self.not_player_x_turn = self.player_2, self.player_1
        else:
            self.player_x_turn, self.not_player_x_turn = self.player_1, self.player_2

        pass

    def update_board(self):

        self.board_next = copy.deepcopy(self.board)

        self.board_next[0][self.move] = 0.99
        self.board_next[2][self.move] = 0.01

        self.check_board()

        pass

    def change_board(self):

        self.board = copy.deepcopy(self.board_next)

        for i in range(len(self.board[0])):
            if self.board[0][i] == 0.01 and self.board[1][i] == 0.99:
                self.board[0][i] = 0.99
                self.board[1][i] = 0.01
            elif self.board[0][i] == 0.99 and self.board[1][i] == 0.01:
                self.board[0][i] = 0.01
                self.board[1][i] = 0.99

        pass

    def check_board(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for a, b, c in win_combinations:
            if self.board_next[0][a] == self.board_next[0][b] == self.board_next[0][c] == 0.99:

                self.reward = self.win_value
                self.reward_opponent = self.lose_value

                self.game_playing = False

                self.result = self.player_x_turn
                #print(self.result)

                return

            elif self.board_next[2].count(0.99) == 0:

                self.reward = self.draw_value
                self.reward_opponent = self.draw_value

                self.game_playing = False

                self.result = True

                return

    def update_statistics(self, episode):

        if self.result == self.player_1:
            self.statistics[self.name_player_1] += 1
            self.statistics_total[self.name_player_1] += 1
        elif self.result == self.player_2:
            self.statistics[self.name_player_2] += 1
            self.statistics_total[self.name_player_2] += 1
        elif self.result:
            self.statistics["Draw"] += 1
            self.statistics_total["Draw"] += 1

        if (episode + 1) % 10000 == 0:

            print("After episode", episode + 1, ": ", self.statistics)

            self.statistics = copy.deepcopy(self.statistic_empty)

        pass

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

    def play_tic_tac_toe(self):

        self.statistics = copy.deepcopy(self.statistic_empty)

        for episode in range(self.episodes):

            self.set_up_game()

            while self.game_playing:
                self.move = self.player_x_turn.make_move(self.board, episode, self.training)
                #print(self.prepare_board(self.board))
                self.update_board()

                self.player_x_turn.buffer_experience(self.board, self.move, self.reward, self.board_next, True)
                self.not_player_x_turn.buffer_experience(self.board, self.move, self.reward_opponent, self.board_next,
                                                         False)
                self.end_of_turn()

            self.update_statistics(episode)
            if self.training:
                self.player_1.evolve()
                self.player_2.evolve()

        print("\n Final statistics: ", self.statistics_total, "\n")
