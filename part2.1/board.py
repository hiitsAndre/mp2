class Board:
    def _init_(self):
        self.config = [[0 for x in xrange(7)] for x in xrange(7)]
    def toString(self):
        rtn="-------------------------------"
        for j in range(7):
			rtn+="\n"+"|"
			for i in range(7):
				pos = self.config[i][j]
				if pos==0:
					pos=" "

				rtn+=str(pos)+"|"
		rtn+="\n-------------------------------"
		return rtn
