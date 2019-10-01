import TicTacToe, Random_Agent, TabularQLearning_Agent, QTable, Human_Agent

QTable = QTable.QTable(initialize=True)

Player1 = TabularQLearning_Agent.Agent("Tabular-Q-Learning-Agent 1", QTable)
Player2 = TabularQLearning_Agent.Agent("Tabular-Q-Learning-Agent 2", QTable)
Player3 = Random_Agent.RandomPlayerTicTacToe("Random")
Player4 = Human_Agent.HumanPlayerTicTacToe("Human", "X")

#Humann = TicTacToe.Play(Player1, Player4, number_of_episodes=100, train=True)

Test1 = TicTacToe.Play(Player1, Player3, number_of_episodes=10000, train=False)
Training = TicTacToe.Play(Player1, Player3, number_of_episodes=100000, train=True)
Test2 = TicTacToe.Play(Player1, Player3, number_of_episodes=10000, train=False)

QTable.save_table()

#Test3 = TicTacToe.Play(Player1, Player3, number_of_episodes=10000, train=True)
