class Distribution():

    def __init__(self):
        self.dic = {}

    def add_single(self, k, v = 1):
        if k in self.dic.keys():
            self.dic[k] += v
        else:
            self.dic[k] = v

    def __add__(self, dist2):
        new_dist = Distribution() # !!!
        new_dist.dic = self.dic
        for key2 in dist2.dic.keys():
            if key2 in new_dist.dic.keys():
                new_dist.dic[key2] += dist2.dic[key2]
            else:
                new_dist.dic[key2] = dist2.dic[key2]
        return new_dist # !!!

    def __str__(self): # !!!
        string = ''
        for k in self.dic.keys():
            string += '{} {}\n'.format(k, self.dic[k])
        return string


d1 = Distribution()
for cc in 'cgcccg':
    d1.add_single(cc)
d2 = Distribution()
for cc in 'atttta':
    d2.add_single(cc)
print('{}'.format(d1+d2))
