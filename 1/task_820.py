class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        for num in a:
            self.lst.append(num)
            if len(self.lst) == 5:
                print(sum(self.lst))
                self.lst = []

    def get_current_part(self):
        return self.lst
