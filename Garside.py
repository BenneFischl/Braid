"""This is just the same code but cleaner. """

class word:
    """ A word. """

    def __init__(self, n):
        """
        n: number of strings, i.e. construct a word in B_n braid group.
        """
        
        self.n = n
        printstr = ''
        for i in range(self.n):
            printstr += '| '
        self.prtunit = printstr
        self.oplist = []
        self.Delta = []
        for i in range(n-1):
            for j in range(n-i-1):
                self.Delta.append(j+1)
        self.Delta_inv = []
        for i in range(len(self.Delta)):
            self.Delta_inv.append(-self.Delta[-i-1])

    def op(self, i):
        """
        i: swap ith and (i+1)th string with ith string under (i+1)th
        enter minus value to make inverse.
        """
        self.oplist.append(i)

    def __str__(self):
        prt = [self.prtunit]
        for i in self.oplist:
            if isinstance(i, int):
                ai = abs(i)
                line = ''
                for j in range(ai-1):
                    line += '| '
                line1 = line + '\ / '
                line3 = line + '/ \ '
                if i > 0:
                    line2 = line + ' /  '
                else:
                    line2 = line + ' \  '
                line = ''
                for j in range(self.n-ai-1):
                    line += '| '
                line1 += line
                line2 += line
                line3 += line
                prt.append(line1)
                prt.append(line2)
                prt.append(line3)
                prt.append(self.prtunit)
            else:
                prt.append('d')
        to_be_print = ''
        for k in prt:
            to_be_print += k
            to_be_print += "\n"
        return to_be_print

    def sigma_inv(self, i):
        """
        Input i means \sigma_{-i}^{-1}.
        This function convert \sigma_{-i}^{-1} into R_{-i}\Delta^{-1}
        and returns R_{-i}.
        """
        if -i > self.n - 1:
            raise IndexError
        R_i = []
        for j in self.Delta:
            R_i.append(j)
        R_i.pop((2*self.n+i)*(-i-1)//2)
        return R_i

    def neg_inv(self):
        """This function converts a word into form \Delta^iZ."""
        # change all negative operations into positive ones
        k = 0
        dcount = 0
        while k<len(self.oplist):
            if isinstance(self.oplist[k], int) and self.oplist[k] < 0:
                ist = self.sigma_inv(self.oplist[k])
                self.oplist = self.oplist[:k] + ist + ['d'] + self.oplist[k+1:]
                k += len(ist)
                dcount += 1
            k += 1
        # rearrange the word into the form \Delta^iZ
        self.inf = dcount
        revlist = self.oplist[::-1]
        newlist = []
        mult = 1
        for i in revlist:
            if isinstance(i, int):
                newlist.append(i*mult)
            else:
                mult *= -1
        for i in range(len(newlist)):
            if newlist[i]<0:
                newlist[i] += self.n
        newlist.append("d" + str(self.inf))
        rtlist = newlist[::-1]
        return rtlist
