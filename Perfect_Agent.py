# Newell and Simon's 1972


class PerfectAgent:

    def __init__(self, name):

        self.name = name

        pass

    @staticmethod
    def make_move(board, episode, training):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        # 1. Win
        for a, b, c in win_combinations:
            if board[0][a] == board[0][b] == 0.99 and board[2][c] == 0.99:
                return c
            elif board[0][a] == board[0][c] == 0.99 and board[2][b] == 0.99:
                return b
            elif board[0][b] == board[0][c] == 0.99 and board[2][a] == 0.99:
                return a

        # 2. Block
        for a, b, c in win_combinations:
            if board[1][a] == board[1][b] == 0.99 and board[2][c] == 0.99:
                return c
            elif board[1][a] == board[1][c] == 0.99 and board[2][b] == 0.99:
                return b
            elif board[1][b] == board[1][c] == 0.99 and board[2][a] == 0.99:
                return a

        # 3. Fork
        for a, b, c in win_combinations:
            for d, e, f in win_combinations:
                if a == (d or e or f) or b == (d or e or f) or c == (d or e or f):
                    if board[2][a] == board[2][b] == 0.99 and board[0][c] == 0.99:
                        if a == (d or e or f):
                            return a
                        elif b == (d or e or f):
                            return b
                    elif board[2][a] == board[2][c] == 0.99 and board[0][b] == 0.99:
                        if a == (d or e or f):
                            return a
                        elif c == (d or e or f):
                            return c
                    elif board[2][b] == board[2][c] == 0.99 and board[0][a] == 0.99:
                        if b == (d or e or f):
                            return b
                        elif c == (d or e or f):
                            return c

        # 4. Block Fork
        for a, b, c in win_combinations:
            for d, e, f in win_combinations:
                if a == (d or e or f) or b == (d or e or f) or c == (d or e or f):
                    if board[2][a] == board[2][b] == 0.99 and board[1][c] == 0.99:
                        if a == (d or e or f):
                            for g, h, i in win_combinations:
                                if board[2][g] == board[2][h] == 0.99 and board[0][i] == 0.99:
                                    if g == a:
                                        return g
                                    elif h == a:
                                        return h
                                    else:
                                        return g
                            return a
                        elif b == (d or e or f):
                            for g, h, i in win_combinations:
                                if board[2][g] == board[2][h] == 0.99 and board[0][i] == 0.99:
                                    if g == b:
                                        return g
                                    elif h == b:
                                        return h
                                    else:
                                        return g
                            return b
                    elif board[2][a] == board[2][c] == 0.99 and board[1][b] == 0.99:
                        if a == (d or e or f):
                            for g, h, i in win_combinations:
                                if board[2][g] == board[2][h] == 0.99 and board[0][i] == 0.99:
                                    if g == a:
                                        return g
                                    elif h == a:
                                        return h
                                    else:
                                        return g
                            return a
                        elif c == (d or e or f):
                            for g, h, i in win_combinations:
                                if board[2][g] == board[2][h] == 0.99 and board[0][i] == 0.99:
                                    if g == c:
                                        return g
                                    elif h == c:
                                        return h
                                    else:
                                        return g
                            return c
                    elif board[2][b] == board[2][c] == 0.99 and board[1][a] == 0.99:
                        if b == (d or e or f):
                            for g, h, i in win_combinations:
                                if board[2][g] == board[2][h] == 0.99 and board[0][i] == 0.99:
                                    if g == b:
                                        return g
                                    elif h == b:
                                        return h
                                    else:
                                        return g
                            return b
                        elif c == (d or e or f):
                            for g, h, i in win_combinations:
                                if board[2][g] == board[2][h] == 0.99 and board[0][i] == 0.99:
                                    if g == c:
                                        return g
                                    elif h == c:
                                        return h
                                    else:
                                        return g
                            return c

        # 5. Play Center
        if board[2][4] == 0.99:
            return 4

        # 6. Play Opposite Corner
        if board[1][0] == 0.99:
            if board[2][8] == 0.99:
                return 8
        elif board[1][2] == 0.99:
            if board[2][6] == 0.99:
                return 6
        elif board[1][6] == 0.99:
            if board[2][2] == 0.99:
                return 2
        elif board[1][8] == 0.99:
            if board[2][0] == 0.99:
                return 0

        # 7. Play Empty Corner
        if board[2][0] == 0.99:
            return 0
        elif board[2][2] == 0.99:
            return 2
        elif board[2][6] == 0.99:
            return 6
        elif board[2][8] == 0.99:
            return 8

        # 8. Play Empty Side
        if board[2][1] == 0.99:
            return 1
        elif board[2][3] == 0.99:
            return 3
        elif board[2][5] == 0.99:
            return 5
        elif board[2][7] == 0.99:
            return 7

    @staticmethod
    def buffer_experience(a, b, c, d, e):

        pass

    @staticmethod
    def evolve():

        pass

    @staticmethod
    def learn(a, b, c, d):

        pass
