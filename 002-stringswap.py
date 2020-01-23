'''
Input string: a!!!b.c.d,e'f,ghi
Output string: i!!!h.g.f,e'd,cba
'''
class StringSwap(object):
    def __init__(self, **kwargs):
        self.word = kwargs['word']
        self.forward_list = list(self.word)
        self.reverse_list = self.forward_list[::-1]
        self.forward_alpha_list = []
        self.forward_alpha_index = []
        self.reverse_alpha_list = []

    def forwardAlpha(self):
        for f in range(len(self.forward_list)):
            if self.forward_list[f].isalpha():
                self.forward_alpha_list.append(self.forward_list[f])
                self.forward_alpha_index.append(f)

    def reverseAlpha(self):
        for r in range(len(self.reverse_list)):
            if self.reverse_list[r].isalpha():
                self.reverse_alpha_list.append(self.reverse_list[r])

    def swap(self):
        self.forwardAlpha()
        self.reverseAlpha()
        forward_list = self.forward_list
        forward_index = self.forward_alpha_index
        reverse_alpha = self.reverse_alpha_list
        for fi, r in zip(forward_index, reverse_alpha):
            forward_list[fi] = r
        return ''.join(forward_list)
            

ss = StringSwap(word="a!!!b.c.d,e'f,ghi")
print(ss.swap())