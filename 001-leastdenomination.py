# This task is to find the least count of denomiation(s) for a given value
from collections import Counter

class DC(object):
    def __init__(self, denomination):
        self.denomination = denomination
        self.change = []

    def process_count(self, value_list):
        count = Counter(self.change)
        return (sum(dict(count).values()), dict(count))

    def process_change(self, value):
        possible_values = []
        for d in self.denomination:
            if d <= value:
                possible_values.append(d)
        #print("Possible Value", possible_values)
        max_value = max(possible_values)
        self.change.append(max_value)
        #print('Change', self.change)
        balance = value - max_value
        #print('Balacne', balance)
        if balance > 0:
            self.process_change(balance)
        else:
            #print('Final Change', self.change)
            return self.change

    def get_change(self, value):
        if value in self.denomination:
            #print('There in the denomination')
            self.change.append(value)
            return self.process_count(self.change)
        else:
            #print('Want to process')
            change = self.process_change(value)
            #print('Last Change', change)
            return self.process_count(change)


if __name__ == "__main__":
    dc = DC([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000])
    change = dc.get_change(7512)
    print(change)