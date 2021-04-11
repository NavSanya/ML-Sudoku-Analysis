#CSCI 191T Biology inspired ML 
#Project 1
#Sudoku solver
import numpy as np
#a=np.zeros((9,9),dtype=int)
#print(a)
#for index in a:
#    for row in range(9):
#        for colum in range(9):
#            a[row][colum]=colum+1
#print(a)
sudoku1 = [	[0,0,0,4,0,0,2,0,0],
			[7,0,8,5,2,6,0,9,0],
			[5,0,0,0,1,0,0,0,0],
			[2,3,5,0,0,0,0,0,1],
			[0,0,6,0,7,0,4,0,0],
			[4,0,0,0,0,0,6,3,9],
			[0,0,0,0,3,0,0,0,7],
			[0,6,0,1,5,2,9,0,4],
			[0,0,4,0,0,8,0,0,0]]
	
sudoku2 = [	[0,0,0,0,1,2,8,4,5],
			[0,1,0,7,0,0,0,3,0],
			[0,8,0,6,0,9,0,0,0],
			[2,0,0,0,0,7,4,0,0],
			[0,0,5,0,0,0,9,0,0],
			[0,0,8,9,0,0,0,0,2],
			[0,0,0,1,0,3,0,9,0],
			[0,3,0,0,0,4,0,8,0],
			[1,5,9,2,6,0,0,0,0]]

sudoku3 = [	[9,8,7,0,0,0,3,0,0],
			[1,6,0,0,8,0,0,9,0],
			[0,0,0,0,0,4,1,0,6],
			[0,2,0,0,0,6,0,0,8],
			[0,0,0,5,0,7,0,0,0],
			[3,0,0,9,0,0,0,6,0],
			[2,0,8,4,0,0,0,0,0],
			[0,7,0,0,1,0,0,5,9],
			[0,0,5,0,0,0,8,2,3]]

sudoku4 = [	[0,1,6,0,0,0,0,3,0],
			[8,0,0,9,0,0,2,0,6],
			[0,0,0,0,0,0,0,5,8],
			[0,7,2,4,0,6,0,0,0],
			[0,6,9,0,7,0,4,2,0],
			[0,0,0,3,0,5,9,6,0],
			[1,3,0,0,0,0,0,0,0],
			[6,0,4,0,0,1,0,0,5],
			[0,2,0,0,0,0,8,1,0]]
			
sudoku5 = [	[0,3,0,6,0,5,0,8,0],
			[7,0,0,3,0,0,0,0,0],
			[0,0,0,9,7,0,5,4,0],
			[0,6,7,0,0,0,3,0,8],
			[0,2,0,0,0,0,0,6,0],
			[4,0,9,0,0,0,7,5,0],
			[0,9,5,0,3,4,0,0,0],
			[0,0,0,0,0,7,0,0,2],
			[0,7,0,1,0,6,0,9,0]]

sudoku6 = [	[1,0,0,5,0,6,0,9,0],
			[0,3,0,0,8,0,4,0,0],
			[6,0,0,0,7,0,1,0,2],
			[0,0,0,0,0,7,0,2,4],
			[7,0,0,0,9,0,0,0,8],
			[9,2,0,6,0,0,0,0,0],
			[3,0,2,0,5,0,0,0,6],
			[0,0,1,0,6,0,0,5,0],
			[0,9,0,8,0,1,0,0,7]]

sudoku7 = [	[0,0,0,0,0,5,1,7,0],
			[5,0,9,6,0,1,0,8,0],
			[0,8,2,0,4,0,0,0,5],
			[0,0,3,0,0,0,0,0,0],
			[0,1,0,8,0,7,0,2,0],
			[0,0,0,0,0,0,5,0,0],
			[7,0,0,0,9,0,6,5,0],
			[0,5,0,4,0,6,7,0,8],
			[0,3,6,5,0,0,0,0,0]]
			
sudoku8 = [	[4,0,0,0,0,1,3,0,0],
			[0,2,0,0,3,0,0,7,6],
			[0,0,0,0,0,9,0,4,8],
			[0,6,0,0,0,7,2,5,0],
			[0,1,0,0,4,0,0,3,0],
			[0,5,7,3,0,0,0,9,0],
			[6,7,0,1,0,0,0,0,0],
			[1,9,0,0,5,0,0,6,0],
			[0,0,5,8,0,0,0,0,3]]

sudoku9 = [	[5,0,0,0,4,7,0,8,0],
			[0,7,0,5,0,0,0,0,0],
			[9,0,8,0,6,0,0,2,5],
			[0,2,0,0,0,3,0,0,0],
			[7,0,0,8,0,6,0,0,3],
			[0,0,0,9,0,0,0,4,0],
			[2,1,0,0,3,0,8,0,6],
			[0,0,0,0,0,9,0,5,0],
			[0,8,0,1,2,0,0,0,7]]

sudoku10 = [[3,2,0,0,8,0,0,0,1],
			[0,5,0,0,0,0,0,0,9],
			[8,9,1,0,7,0,3,0,0],
			[5,1,0,0,4,0,0,0,0],
			[0,0,0,7,0,3,0,0,0],
			[0,0,0,0,6,0,0,9,4],
			[0,0,8,0,3,0,9,4,6],
			[4,0,0,0,0,0,0,8,0],
			[9,0,0,0,1,0,0,5,3]]

sudoku11 = [[2,0,0,0,0,1,0,6,8],
			[1,8,4,0,0,0,0,0,0],
			[7,0,0,0,0,2,9,0,0],
			[0,4,1,0,2,0,0,7,0],
			[0,0,7,0,0,0,8,0,0],
			[0,6,0,0,3,0,1,5,0],
			[0,0,5,2,0,0,0,0,4],
			[0,0,0,0,0,0,2,8,7],
			[4,9,0,3,0,0,0,0,6]]

sudoku12 = [[6,1,0,0,0,9,0,0,2],
			[0,0,0,2,0,0,0,0,5],
			[0,0,5,1,6,4,8,0,0],
			[2,3,0,0,0,5,1,0,0],
			[0,0,0,0,0,0,0,0,0],
			[0,0,9,3,0,0,0,4,8],
			[0,0,6,9,1,8,5,0,0],
			[5,0,0,0,0,3,0,0,0],
			[8,0,0,7,0,0,0,9,6]]

sudoku13 = [[0,0,0,0,2,8,0,0,0],
			[0,7,0,9,4,0,0,1,6],
			[6,0,0,0,0,0,2,0,8],
			[0,3,0,0,6,2,0,0,0],
			[0,0,2,4,0,7,9,0,0],
			[0,0,0,3,9,0,0,7,0],
			[1,0,7,0,0,0,0,0,4],
			[5,2,0,0,3,4,0,8,0],
			[0,0,0,7,8,0,0,0,0]]

sudoku14 = [[0,0,4,9,0,0,0,2,0],
			[5,2,0,6,0,0,0,0,7],
			[0,3,0,0,0,0,0,4,6],
			[8,0,0,3,7,0,2,0,0],
			[0,0,5,0,6,0,4,0,0],
			[0,0,2,0,5,9,0,0,8],
			[4,1,0,0,0,0,0,8,0],
			[2,0,0,0,0,1,0,6,9],
			[0,6,0,0,0,3,7,0,0]]

sudoku15 = [[0,6,8,0,0,9,0,0,0],
			[0,1,0,0,6,0,0,5,0],
			[7,0,0,5,0,1,8,0,0],
			[6,0,2,0,4,0,0,7,5],
			[0,0,0,0,0,0,0,0,0],
			[3,5,0,0,1,0,2,0,9],
			[0,0,5,3,0,6,0,0,1],
			[0,9,0,0,2,0,0,3,0],
			[0,0,0,1,0,0,7,9,0]]

sudoku16 = [[0,0,0,4,0,2,8,1,6],
			[0,0,0,8,6,7,0,2,0],
			[0,0,6,0,0,0,0,0,0],
			[7,0,5,6,0,0,0,0,0],
			[9,0,0,3,0,5,0,0,1],
			[0,0,0,0,0,4,2,0,9],
			[0,0,0,0,0,0,4,0,0],
			[0,7,0,9,1,3,0,0,0],
			[6,5,2,7,0,8,0,0,0]]

sudoku17 = [[0,6,0,1,0,0,2,0,0],
			[0,3,0,0,2,4,6,0,7],
			[0,0,2,0,0,0,0,0,8],
			[0,0,0,0,0,0,5,0,4],
			[0,7,8,2,0,6,9,3,0],
			[3,0,1,0,0,0,0,0,0],
			[6,0,0,0,0,0,3,0,0],
			[2,0,3,9,7,0,0,1,0],
			[0,0,4,0,0,8,0,2,0]]

sudoku18 = [[0,4,0,9,0,6,0,0,0],
			[0,0,8,0,0,0,4,7,1],
			[0,7,3,0,1,0,0,6,2],
			[0,0,4,0,0,3,0,1,0],
			[0,0,0,0,0,0,0,0,0],
			[0,1,0,6,0,0,8,0,0],
			[1,9,0,0,3,0,2,4,0],
			[3,2,5,0,0,0,7,0,0],
			[0,0,0,5,0,2,0,9,0]]

sudoku19 = [[0,2,8,0,0,0,0,0,9],
			[0,0,4,0,0,2,8,3,0],
			[0,9,0,8,0,6,0,0,0],
			[0,0,6,0,0,8,0,7,0],
			[0,3,0,4,0,7,0,2,0],
			[0,4,0,6,0,0,9,0,0],
			[0,0,0,2,0,1,0,8,0],
			[0,6,2,7,0,0,1,0,0],
			[3,0,0,0,0,0,2,4,0]]

sudoku20 = [[0,0,7,3,0,0,8,0,0],
			[8,0,3,1,5,0,0,9,0],
			[0,0,1,6,0,0,0,0,0],
			[7,9,0,0,0,0,2,1,6],
			[0,0,0,0,0,0,0,0,0],
			[1,8,2,0,0,0,0,3,4],
			[0,0,0,0,0,5,4,0,0],
			[0,5,0,0,2,8,1,0,3],
			[0,0,4,0,0,3,9,0,0]]

sudoku21 = [[1,3,4,5,0,6,0,9,0],
			[0,0,0,0,0,9,0,0,0],
			[6,9,0,0,7,1,0,0,0],
			[4,0,3,0,0,0,1,0,0],
			[0,1,0,0,0,0,0,7,0],
			[0,0,2,0,0,0,5,0,4],
			[0,0,0,1,9,0,0,4,6],
			[0,0,0,8,0,0,0,0,0],
			[0,5,0,7,0,3,9,8,1]]

sudoku22 = [[1,0,3,0,0,2,7,8,0],
			[0,0,0,0,0,3,2,0,0],
			[0,4,6,0,7,5,0,0,1],
			[0,0,1,0,0,0,8,0,4],
			[0,0,0,0,0,0,0,0,0],
			[7,0,8,0,0,0,5,0,0],
			[6,0,0,9,4,0,1,5,0],
			[0,0,9,3,0,0,0,0,0],
			[0,1,4,7,0,0,3,0,9]]

sudoku23 = [[0,0,7,0,5,0,0,2,9],
			[4,9,0,0,0,0,7,6,0],
			[0,0,0,0,1,0,0,0,0],
			[1,3,0,5,0,0,0,7,0],
			[0,7,4,0,0,0,8,3,0],
			[0,8,0,0,0,3,0,1,2],
			[0,0,0,0,4,0,0,0,0],
			[0,4,9,0,0,0,0,8,6],
			[7,5,0,0,9,0,1,0,0]]

sudoku24 = [[0,1,0,0,7,0,0,0,0],
			[0,7,6,9,0,0,8,5,3],
			[0,0,0,3,0,4,0,0,0],
			[0,6,7,0,5,0,2,0,9],
			[0,0,0,0,0,0,0,0,0],
			[1,0,8,0,9,0,7,4,0],
			[0,0,0,1,0,7,0,0,0],
			[2,8,1,0,0,9,4,6,0],
			[0,0,0,0,2,0,0,9,0]]

sudoku25 = [[0,5,0,0,0,2,0,0,9],
			[0,0,0,0,1,9,0,0,7],
			[0,0,8,3,4,0,0,0,0],
			[0,0,0,4,0,0,0,9,3],
			[7,0,3,9,2,8,4,0,5],
			[9,6,0,0,0,5,0,0,0],
			[0,0,0,0,9,3,8,0,0],
			[2,0,0,7,6,0,0,0,0],
			[3,0,0,8,0,0,0,1,0]]

sudoku26 = [[0,0,0,2,8,0,0,0,0],
			[4,9,0,0,0,5,0,2,0],
			[0,0,2,0,0,0,5,3,7],
			[9,0,0,0,0,8,0,7,0],
			[0,0,7,1,0,2,4,0,0],
			[0,8,0,3,0,0,0,0,6],
			[7,4,6,0,0,0,9,0,0],
			[0,1,0,5,0,0,0,6,3],
			[0,0,0,0,7,1,0,0,0]]

sudoku27 = [[0,0,7,0,0,0,0,0,0],
			[1,0,9,5,6,0,0,0,0],
			[0,5,0,0,0,8,0,0,2],
			[8,3,2,0,0,6,1,0,0],
			[7,4,0,0,0,0,0,9,6],
			[0,0,6,2,0,0,4,8,3],
			[2,0,0,9,0,0,0,5,0],
			[0,0,0,0,4,7,6,0,8],
			[0,0,0,0,0,0,3,0,0]]

sudoku28 = [[8,0,0,4,5,0,7,0,0],
			[0,0,0,0,2,0,3,0,0],
			[9,0,7,3,0,8,0,0,2],
			[0,6,0,0,0,0,0,0,3],
			[0,8,4,0,9,0,2,7,0],
			[7,0,0,0,0,0,0,5,0],
			[2,0,0,6,0,7,5,0,4],
			[0,0,8,0,4,0,0,0,0],
			[0,0,5,0,1,3,0,0,9]]

sudoku29 = [[0,5,0,0,8,0,6,4,0],
			[0,0,7,0,0,1,9,0,0],
			[3,0,0,0,2,9,0,0,1],
			[0,0,8,0,0,2,0,7,3],
			[0,0,0,0,5,0,0,0,0],
			[2,9,0,8,0,0,1,0,0],
			[6,0,0,9,1,0,0,0,7],
			[0,0,2,3,0,0,4,0,0],
			[0,3,1,0,7,0,0,5,0]]

sudoku30 = [[1,0,0,8,5,0,3,0,6],
			[0,0,0,0,6,0,0,8,0],
			[5,0,8,0,0,4,0,0,9],
			[0,0,0,3,0,0,0,0,1],
			[0,9,1,0,0,0,2,7,0],
			[3,0,0,0,0,2,0,0,0],
			[9,0,0,6,0,0,1,0,7],
			[0,5,0,0,9,0,0,0,0],
			[8,0,7,0,4,3,0,0,2]]

    
sudoList_Non_NP = [sudoku1, sudoku2,sudoku3,sudoku4,sudoku5,sudoku6,sudoku7,
					sudoku8,sudoku9,sudoku10,sudoku11,sudoku12,sudoku13,sudoku14,
					sudoku15,sudoku16,sudoku17,sudoku18,sudoku19,sudoku20,
					sudoku21,sudoku22,sudoku23,sudoku24,sudoku25,sudoku26,
					sudoku27,sudoku28,sudoku29,sudoku30]

#create deepcopy of sudoku puzzles that can be modified and reset 
copy_sudoku_lists = []
for i in sudoList_Non_NP:
    copy_sudoku_lists.append(copy.deepcopy(i))

s1=np.reshape(sudoku1,(9,9))
s2=np.reshape(sudoku2,(9,9))
s3=np.reshape(sudoku3,(9,9))
s4=np.reshape(sudoku4,(9,9))
s5=np.reshape(sudoku5,(9,9))
s6=np.reshape(sudoku6,(9,9))
s7=np.reshape(sudoku7,(9,9))
s8=np.reshape(sudoku8,(9,9))
s9=np.reshape(sudoku9,(9,9))
s10=np.reshape(sudoku10,(9,9))
s11=np.reshape(sudoku11,(9,9))
s12=np.reshape(sudoku12,(9,9))
s13=np.reshape(sudoku13,(9,9))
s14=np.reshape(sudoku14,(9,9))
s15=np.reshape(sudoku15,(9,9))
s16=np.reshape(sudoku16,(9,9))
s17=np.reshape(sudoku17,(9,9))
s18=np.reshape(sudoku18,(9,9))
s19=np.reshape(sudoku19,(9,9))
s20=np.reshape(sudoku20,(9,9))
s21=np.reshape(sudoku21,(9,9))
s22=np.reshape(sudoku22,(9,9))
s23=np.reshape(sudoku23,(9,9))
s24=np.reshape(sudoku24,(9,9))
s25=np.reshape(sudoku25,(9,9))
s26=np.reshape(sudoku26,(9,9))
s27=np.reshape(sudoku27,(9,9))
s28=np.reshape(sudoku28,(9,9))
s29=np.reshape(sudoku29,(9,9))
s30=np.reshape(sudoku30,(9,9))

#print(1,"\n",s1)
# print(2,"\n",s2)
# print(3,"\n",s3)
# print(4,"\n",s4)
# print(5,"\n",s5)
# print(6,"\n",s6)
# print(7,"\n",s7)
# print(8,"\n",s8)
# print(9,"\n",s9)
# print(10,"\n",s10)
# print(11,"\n",s11)
# print(12,"\n",s12)
# print(13,"\n",s13)
# print(14,"\n",s14)
# print(15,"\n",s15)
# print(16,"\n",s16)
# print(17,"\n",s17)
# print(18,"\n",s18)
# print(19,"\n",s19)
# print(20,"\n",s20)
# print(21,"\n",s21)
# print(22,"\n",s22)
# print(23,"\n",s23)
# print(24,"\n",s24)
# print(25,"\n",s25)
# print(26,"\n",s26)
# print(27,"\n",s27)
# print(28,"\n",s28)
# print(29,"\n",s29)
# print(30,"\n",s30)

sudoLst=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,
		s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,
		s21,s22,s23,s24,s25,s26,s27,s28,s29,s30]
#print(sudoLst)