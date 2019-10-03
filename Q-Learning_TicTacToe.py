import TicTacToe, Random_Agent, TabularQLearning_Agent, QTable, Human_Agent, Perfect_Agent

QTable = QTable.QTable(initialize=True, content=0.6)

Player1 = TabularQLearning_Agent.Agent("Tabular-Q-Learning-Agent 1", QTable)
Player2 = TabularQLearning_Agent.Agent("Tabular-Q-Learning-Agent 2", QTable)
Player3 = Random_Agent.RandomPlayerTicTacToe("Random")
Player4 = Human_Agent.HumanPlayerTicTacToe("Human", "X")
Player5 = Perfect_Agent.PerfectAgent("Perfect")

TicTacToe_Q_vs_Q = TicTacToe.TicTacToe(Player1, Player2)
TicTacToe_Q_vs_P = TicTacToe.TicTacToe(Player1, Player5)

TicTacToe_Q_vs_Q.Play(episodes=100000, training=True)
TicTacToe_Q_vs_P.Play(episodes=10000, training=False)

QTable.save_table()
