def crosswordPuzzle(crossword, words):

    n= 10

    def check_vertial(colum_index, colum, word):
        word_length = len(word)
        for i in range(n - word_length + 1):
            if all([character == "-" or character == word[index] for index, character in
                    enumerate(colum[i:i + word_length])]):
                return (i, colum_index)

    def check_horizontal(row_index, row, word):
        word_length = len(word)
        for i in range(n - word_length + 1):
            if all([character == "-" or character == word[index] for index, character in
                    enumerate(row[i:i + word_length])]):
                return (row_index, i)

    def display_cross_board(board):
        for row in board:
            print("".join(row))

    def get_colum(crosswords, colum_index):
        return [crosswords[i][colum_index] for i in range(n)]

    def place_word(board, direction, position, word):
        print(f"========= placing word {word} at {position} ===========")
        display_cross_board(board)
        row, colum = position
        if direction == "horizontal":
            for i in range(len(word)):
                board[row][colum + i] = word[i]
        else:
            for i in range(len(word)):
                board[row + i][colum] = word[i]

        return board

    def delete_word(board, direction, position, word, ):
        print(f"========= deleting word {word} at {position} ===========")
        display_cross_board(board)
        row, colum = position
        if direction == "horizontal":
            for i in range(len(word)):
                board[row][colum + i] = "-"
        else:
            for i in range(len(word)):
                board[row + i][colum] = "-"
        return board

    def solve(crosswords):
        if not words:
            return crosswords
        horizontal_solutions = []
        vertical_solutions = []
        solutions = {}
        word = words.pop()
        for row_index, row in enumerate(crosswords):
            if check_horizontal(row_index, row, word):
                horizontal_solutions.append(check_horizontal(row_index, row, word))

        for colum_index in range(n):
            colum = get_colum(crosswords, colum_index)
            if check_vertial(colum_index, colum, word=word):
                vertical_solutions.append(check_vertial(colum_index, get_colum(crosswords, colum_index), word=word))
        solutions.setdefault('horizontal', []).extend(horizontal_solutions)
        solutions.setdefault('vertical', []).extend(vertical_solutions)
        for solution_type, sls in solutions.items():
            for sl in sls:
                crosswords = place_word(crosswords, solution_type, sl, word)
                import pdb;pdb.set_trace()
                if solve(crosswords):
                    return crosswords
                delete_word(crosswords, solution_type, sl, word)
        words.append(word)

    result = solve(crossword)
    return ["".join(line)  for line in result]
if __name__ == '__main__':

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()
    words = words.split(";")
    crossword = [list(row) for row in crossword]
    result = crosswordPuzzle(crossword, words)
    print(result)
