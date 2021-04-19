class Address:
    def __init__(self, address, prefix):
        self.separator = ":"
        self.separator_double = "::"
        self.zero = "0"
        self.four_zero = "0000"
        self.address = address
        self.group = self.address.split(self.separator)
        try:
       	    self.prefix = int(prefix)
        except Exception as e:
            self.prefix = 0

    def handle_separator(self):
        split = self.address.split(self.separator_double)
        if len(split) != 2:
            return self.address
        avant = len(split[0].split(self.separator))
        apres = len(split[1].split(self.separator))
        init = 8
        if len(split[0]) == 0 or len(split[1]) == 0:
            init = 9
        zero = ""
        if len(split[0].split(self.separator)[0]) != 0:
            zero += self.separator
        for x in range(init - (avant + apres)):
            zero += self.four_zero
            if x != init -1 - (avant + apres):
                zero += self.separator
        if len(split[1].split(self.separator)[0]) != 0:
            zero += self.separator
        return self.address.replace(self.separator_double, zero)

    def reseau(self):
        adresse =  self.expand_address()
        liste = adresse.split(self.separator)
        intClasse = int(self.prefix/16)
        if intClasse > 128 or intClasse < 0:
            raise Exception("invalid class prefix")
        ret = ""
        x = 0
        while x < intClasse:
            if self.minimize_group(liste[x]) == self.zero:
                indice = self.minimize_handle_separator(x, liste)
                if indice >= intClasse - 1:
                    break
                else :
                    ret += self.minimize_group(liste[x]) + self.separator
            else :
                ret += self.minimize_group(liste[x]) + self.separator
            x += 1
        if self.prefix % 16 != 0:
            if(self.minimize_group(liste[x]) == self.zero):
                return ret + self.separator
            reste = (self.prefix % 16) / 4
            j = 0
            while j < reste:
                ret += liste[x][j]
                j += 1
            while j < 4:
                ret += self.zero
                j += 1
            ret += self.separator
        print(self.prefix)
        return ret + self.separator

    def complete_group(self, abr):
        if(abr == self.zero):
            return self.four_zero
        if len(abr) == 4:
            return abr
        before = ""
        for x in range(4-len(abr)):
            before += self.zero
        return before + abr

    def minimize_handle_separator(self, indice, liste):
        if self.minimize_group(liste[indice + 1]) != self.zero:
            return indice
        for j in range(indice + 2, len(self.group)):
            if self.minimize_group(liste[j]) != self.zero:
                return j - 1
        return len(self.group) - 1

    def minimize_group(self, ip):
        indice = 4
        for i in range(0, 4):
            if ip[i] != self.zero:
                indice = i
                break
        if indice == 4:
            return self.zero
        ret = ""
        for i in range(indice, 4):
            ret += ip[i]
        return ret

    def expand_address(self):
        adresse = self.handle_separator()
        liste = adresse.split(self.separator)
        ret = ""
        for x in range(len(liste) - 1):
            ret += self.complete_group(liste[x]) + self.separator
        ret += self.complete_group(liste[len(liste) - 1])
        return ret