class Abbreviation:
    
    def __init__(self, address):
        self.zero = "0"
        self.double_point = ":"
        self.address = address
        self.liste = self.address.split(self.double_point)

    def handle_double_point(self, i):
        first = 2   
        last = 1
        if self.short_list(self.liste[i+last]) != self.zero:
            return i
        for j in range(i+first, len(self.liste)):
            if self.short_list(self.liste[j]) != self.zero:
                return j-last
        return len(self.liste)-last

    def short_list(self, list_item):
        base_ind = 4
        ind = base_ind
        for i in range(0, base_ind):
            if list_item[i] != self.zero:
                ind = i
                break
        if ind == base_ind:
            return self.zero
        ret = ""
        for i in range(ind, base_ind):
            ret += list_item[i]
        return ret

    def abbreviation(self):
        ret = ""
        base_ind = 0
        last = 1
        ind_for_list = 7
        ind = i = base_ind
        verify = True
        
        while i < len(self.liste) - last:
            abr = self.short_list(self.liste[i])
            if(abr != self.zero):
                ret += abr + self.double_point
            else:
                if verify == True:
                    ind = self.handle_double_point(i)
                    if ind != i:
                        ret += self.double_point
                        verify = False
                        i = ind
                    else:
                        ret += abr + self.double_point
                else:
                    ret += abr + self.double_point
            i = i + last
        
        if ind != ind_for_list:
            ret += self.short_list(self.liste[ind_for_list])
        
        return ret