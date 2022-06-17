class RangeError:
    pass

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
        #self.pn_huajian()

    def paixu(self):
        for i in range(len(self.oplist)):
            pass

    def pn_huajian(self):
        
        """
        DO NOT USE!!!! NOT FINISHED!!!
        If \sigma_n and \sigma_{-n} are next to each other, then cancel them.
        """
        for j in range(len(self.oplist)-1):
            if self.oplist[j] + self.oplist[j+1] == 0:
                self.oplist.pop(j)
                self.oplist.pop(j)
                return self.pn_huajian()

    def oto_huajian(self):
        """
        If 
        """
        pass
    
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

    def gamma(self, i):
        """
        Input i meanning \sigma_i^{-1}.
        This function does the \Delta^{-1}X\Delta function, the
        gamma automorphism.
        """
        return self.n - i

    def sigma_inv(self, i):
        """
        Input i means \sigma_i^{-1}.
        This function convert \sigma_i^{-1} into R_i\Delta^{-1} and returns R_i.
        """
        if i > self.n - 1:
            raise IndexError
        R_i = []
        for j in self.Delta:
            R_i.append(j)
        R_i.pop((2*self.n-i)*(i-1)//2)
        return R_i

    def neg_inv(self):
        """This function converts a word into form \Delta^iZ."""
        # change all negative operations into positive ones
        k = 0
        poslist = []
        while k<len(self.oplist):
            if self.oplist[k] < 0:
                ist = self.sigma_inv(self.oplist[k])
                self.oplist = self.oplist[:k] + ist + ['d'] + self.oplist[k+1:]
                k += len(ist)
                poslist.append(k+len(ist))
            else:
                k += 1
        # rearrange the word into the form \Delta^iZ
        self.inf = len(poslist)
        newlist = ["d" + str(self.inf)]
        if self.inf % 2:
            newlist += self.oplist[:poslist[0]]
            poslist.pop(0)
        for i in range(len(poslist)):
            newlist += 1
            pass
            
                
        
        
        
                
                
                
        
w3 = word(3)
p = w3.sigma_inv(1)
w3.oplist = p + w3.Delta_inv
w3.pn_huajian()

w11 = word(11)
p = w11.sigma_inv(3)
w11.oplist = p + w11.Delta_inv
w11.pn_huajian()
