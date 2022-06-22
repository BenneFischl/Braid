
class word:
    
    def __init__(self, n):
        self.n = n
        self.oplist = []
        self.Delta = []
        for i in range(n-1):
            for j in range(n-i-1):
                self.Delta.append(j+1)
        self.Delta_inv = []
        for i in range(len(self.Delta)):
            self.Delta_inv.append(-self.Delta[-i-1])

    def sigma_inv(self, i):
        if -i > self.n - 1:
            raise IndexError
        R_i = []
        for j in self.Delta:
            R_i.append(j)
        R_i.pop((2*self.n+i)*(-i-1)//2)
        return R_i

    def neg_inv(self):
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

    def SnF(self):
        plist = self.neg_inv()
        strand_list = [i+1 for i in range(self.n)]
        past_op_list = []
        A_list = []
        Ai_list = []
        SAi_list = []
        FAi_list = []
        permutation = []
        for i in range(1, len(plist)):
            p = plist[i]
            si, si1 = strand_list[p-1], strand_list[p]
            if si < si1:
                optp = (si, si1)
            else:
                optp = (si1, si)
            if optp not in past_op_list:
                past_op_list.append(optp)
                A_list.append(p)
            else:
                Ai_list.append(A_list)
                SAi_list.append(past_op_list)
                f = []
                for j in past_op_list:
                    fi = strand_list.index(j[0]) + 1
                    fi1 = strand_list.index(j[1]) + 1
                    if fi < fi1:
                        f.append((fi, fi1))
                    else:
                        f.append((fi1, fi))
                FAi_list.append(f)
                permutation.append(strand_list)
                strand_list = [i+1 for i in range(self.n)]
                A_list = [p]
                past_op_list = [optp]
            strand_list[p-1], strand_list[p] = si1, si
        Ai_list.append(A_list)
        SAi_list.append(past_op_list)
        f = []
        for j in past_op_list:
            fi = strand_list.index(j[0]) + 1
            fi1 = strand_list.index(j[1]) + 1
            if fi < fi1:
                f.append((fi, fi1))
            else:
                f.append((fi1, fi))
        FAi_list.append(f)
        return Ai_list, SAi_list, FAi_list, permutation

    def SinFcheck(self, Slist, Flist):
        for i in range(len(Slist)-1):
            for j in Slist[i+1]:
                if j not in Flist[i]:
                    return i, j
        return False

    def nmlise(self):
        A, S, F, P = self.SnF()
        for i in range(len(A)-1):
            sf = self.SinFcheck(S, F)
            if sf:
                self.inf += 1
                A[sf[0]].append(sf[1])
                P[sf[0]][sf[1]-1], P[sf[0]][sf[1]] = P[sf[0]][sf[1]], \
                                                     P[sf[0]][sf[1]-1]
                for j in range(:sf[0]+1):
                    A[j] = [self.n-k for k in A[j]]
                    P[j] = [self.n-m for m in P[j][::-1]]
                A[sf[0]+1] = [self.n-k for k in [self.sigma_inv(-sf[1])]] \
                             + A[sf[0]+1]
                
                return self.nmlise()
        
        return 
            
                    
                
                
            

w3 = word(3)
#p = w3.sigma_inv(-1)
w3.oplist = [-1]
print(w3.neg_inv())
print(w3.SnF())


w11 = word(11)
#p = w11.sigma_inv(-3)
w11.oplist = [-3]
print(w11.neg_inv())
print(w11.SnF())

w9 = word(9)
w9.oplist = [1, 2, 3, 4, 5, -1, -3]
print(w9.neg_inv())
print(w9.SnF())
