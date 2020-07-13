class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.no_candidates = []

    def add_no_candidate(self, no_candidate):
        self.no_candidates.append(no_candidate)


