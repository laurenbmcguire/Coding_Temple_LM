class Card:
    def _init_(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def _str_(self):
            return f"Rank{self.rank} \Suite{self.suite}"


    c1 =Card (0,0)
    c2=Card (1,1)

    print (c1)
