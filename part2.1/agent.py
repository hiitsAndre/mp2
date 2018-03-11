from board import Board

class Agent:
    def _init_(self, color):
        self.color = color
        self.char1 = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
        self.char2 = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
        if color == 1:
            self.char = self.char1
            self.this = 1
            self.other = 2
        else:
            self.char = self.char2
            self.this = 2
            self.other = 1
    def move(self,board,x,y):
		board.config[x][y]=self.color
		print(board.toString())
    def strategy1(self,board):
        for i in range(7):
            for j in range(7):
                if board.config[i][j] == self.color:
                    if self.ready(board,i,j,this) == True:
                        if self.check_legal(board,i-1,j) and self.win(board):
                            self.move(board,i-1,j)
                            return True
                        elif self.check_legal(board,i,j+1) and self.win(board):
                            self.move(board,i,j+1)
                            return True
                        elif self.check_legal(board,i+1,j) and self.win(board):
                            self.move(board,i+1,j)
                            return True
                        elif self.check_legal(board,i,j-1) and self.win(board):
                            self.move(board,i,j-1)
                            return True
        return False
    def strategy2(self,board):
        for i in range(7):
            for j in range(7):
                if board.config[i][j] == self.color:
                    if self.ready(board,i+1,j,other):
                        if self.check_legal(board,i+5,j) and self.win(board):
                            self.move(board,i+5,j)
                            return True
                    elif self.ready(board,i,j+1,other):
                        if self.check_legal(board,i,j+5) and self.win(board):
                            self.move(board,i,j+5)
                            return True
                    elif self.ready(board,i-1,j,other):
                        if self.check_legal(board,i-5,j) and self.win(board):
                            self.move(board,i-5,j)
                            return True
                    elif self.ready(board,i,j-1,other):
                        if self.check_legal(board,i,j-5) and self.win(board):
                            self.move(board,i,j-5)
                            return True
                    elif self.ready(board,i-1,j-1,other):
                        if self.check_legal(board,i-5,j-5) and self.win(board):
                            self.move(board,i-5,j-5)
                            return True
                    elif self.ready(board,i-1,j+1,other):
                        if self.check_legal(board,i-5,j+5) and self.win(board):
                            self.move(board,i-5,j+5)
                            return True
                    elif self.ready(board,i+1,j-1,other):
                        if self.check_legal(board,i+5,j-5) and self.win(board):
                            self.move(board,i+5,j-5)
                            return True
                    elif self.ready(board,i+1,j+1,other):
                        if self.check_legal(board,i+5,j+5) and self.win(board):
                            self.move(board,i+5,j+5)
                            return True
        return False
    def strategy3(self,board):
        for i in range(7):
            for j in range(7):
                if board.config[i][j] !=0 and board.config[i][j] != self.color:
                    if self.three(board,i,j,other) == True:
                        if self.check_legal(board,i-1,j) and self.win(board):
                            self.move(board,i-1,j)
                            return True
                        elif self.check_legal(board,i+3,j) and self.win(board):
                            self.move(board,i+3,j)
                            return True
                        elif self.check_legal(board,i,j+1) and self.win(board):
                            self.move(board,i,j+1)
                            return True
                        elif self.check_legal(board,i,j-3) and self.win(board):
                            self.move(board,i,j-3)
                            return True
                        elif self.check_legal(board,i+1,j) and self.win(board):
                            self.move(board,i+1,j)
                            return True
                        elif self.check_legal(board,i-3,j) and self.win(board):
                            self.move(board,i-3,j)
                            return True
                        elif self.check_legal(board,i,j-1) and self.win(board):
                            self.move(board,i,j-1)
                            return True
                        elif self.check_legal(board,i,j+3) and self.win(board):
                            self.move(board,i,j+3)
                            return True
        return False
    def strategy4(self,board):
	def check_legal(self,board,x,y):
		if x>7 or x<0:
			return False
		if y>7 or y<0:
			return False
		if board.config[x][y] !=0:
			return False
		return True
    def three(self,board,x,y,color):
        if self.ready_horiz(board,x,y,color) or self.ready_vert(board,x,y,color) or self.ready_diag1(board,x,y,color) or self.ready_diag2(board,x,y,color):
            return True
    def three_horiz(self,board,x,y,color):
		if (x+2)<7:
			if (board.config[x][y] == color) and (board.config[x+1][y] == color) and (board.config[x+2][y] == color):
				return True
	def three_vert(self,board,x,y,color):
		if (y+2)<7:
			if (board.config[x][y] == color) and (board.config[x][y+1] == color) and (board.config[x][y+2] == color):
                return True
	def three_diag1(self,board,x,y,color):
		if (x+2<7 and y+2<7):
			if (board.config[x][y] == color) and (board.config[x+1][x+1] == color) and (board.config[x+2][y+2] == color):
                return True
    def three_diag2(self,board,x,y,color):
    	if (x-2>=0 and y+2<7):
    		if (board.config[x][y] == color) and (board.config[x-1][y+1] == color) and (board.config[x-2][y+2] == color):
    			return True

    def ready(self,board,x,y,color):
        if self.ready_horiz(board,x,y,color) or self.ready_vert(board,x,y,color) or self.ready_diag1(board,x,y,color) or self.ready_diag2(board,x,y,color):
            return True
    def ready_horiz(self,board,x,y,color):
		if (x+3)<7:
			if (board.config[x][y] == color) and (board.config[x+1][y] == color) and (board.config[x+2][y] == color) and (board.config[x+3][y] == color):
				return True
	def ready_vert(self,board,x,y,color):
		if (y+3)<7:
			if (board.config[x][y] == color) and (board.config[x][y+1] == color) and (board.config[x][y+2] == color) and (board.config[x][y+3] == color):
                return True
	def ready_diag1(self,board,x,y,color):
		if (x+3<7 and y+3<7):
			if (board.config[x][y] == color) and (board.config[x+1][x+1] == color) and (board.config[x+2][y+2] == color) and (board.config[x+3][y+3] == color):
                return True
    def ready_diag2(self,board,x,y,color):
    	if (x-3>=0 and y+3<7):
    		if (board.config[x][y] == color) and (board.config[x-1][y+1] == color) and (board.config[x-2][y+2] == color) and (board.config[x-3][y+3] == color):
    			return True

    def win(self,board):
        for i in range(7):
            for j in range(7):
                if self.check_horiz(board,i,j,self.color) or self.check_vert(board,i,j,self.color) or self.check_diag1(board,i,j,self.color) or self.check_diag2(board,i,j,self.color):
                    return True
    def check_horiz(self,board,x,y,color):
        if (x+4)<7:
            if (board.config[x][y] == color) and (board.config[x+1][y] == color) and (board.config[x+2][y] == color) and (board.config[x+3][y] == color) and (board.config[x+4][y] == color):
				return True
	def check_vert(self,board,x,y,color):
		if (y+4)<7:
			if (board.config[x][y] == color) and (board.config[x][y+1] == color) and (board.config[x][y+2] == color) and (board.config[x][y+3] == color) and (board.config[x][y+4] == color):
				return True
	def check_diag1(self,board,x,y,color):
		if (x+4<7 and y+4<7):
			if (board.config[x][y] == color) and (board.config[x+1][y+1] == color) and (board.config[x+2][y+2] == color) and (board.config[x+3][y+3] == color) and (board.config[x+4][y+4] == color):
				return True
	def check_diag2(self,board,x,y,color):
		if (x-4>=0 and y+4<7):
			if (board.config[x][y] == color) and (board.config[x-1][y+1] == color) and (board.config[x-2][y+2] == color) and (board.config[x-3][y+3] == color) and (board.config[x-4][y+4] == color):
				return True
