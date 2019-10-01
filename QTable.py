import pickle


class QTable:

    def __init__(self, initialize=True, content=0):

        if initialize:
            self.table = self.create_matrix(19683, 9, content)
        else:
            with open("QTable.txt", "rb") as read_file:
                self.table = pickle.load(read_file)

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

    def save_table(self):
        with open("QTable.txt", "wb") as write_file:
            pickle.dump(self.table, write_file)
