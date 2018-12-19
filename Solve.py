#SolveDoku - Sudoku made easy
#Copyright (C) 2018  Matt Patterson
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see https://www.gnu.org/licenses/.
#
#If you have questions please send an email to leeland230.fun@gmail.com
#or post an issue at https://github.com/End3rYT/Solvedoku/issues
#from Sudoku import *
from tkinter import *
from time import *
window = Tk()

puzzlenums = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

solveBtn = Button(window, width = 5)
e11 = Entry(window,relief='groove',width=2)
e12 = Entry(window, relief='groove',width=2)
e13 = Entry(window, relief='groove',width=2)
e14 = Entry(window, relief='groove',width=2)
e15 = Entry(window, relief='groove',width=2)
e16 = Entry(window, relief='groove',width=2)
e17 = Entry(window, relief='groove',width=2)
e18 = Entry(window, relief='groove',width=2)
e19 = Entry(window, relief='groove',width=2)
e21 = Entry(window, relief='groove',width=2)
e22 = Entry(window, relief='groove',width=2)
e23 = Entry(window, relief='groove',width=2)
e24 = Entry(window, relief='groove',width=2)
e25 = Entry(window, relief='groove',width=2)
e26 = Entry(window, relief='groove',width=2)
e27 = Entry(window, relief='groove',width=2)
e28 = Entry(window, relief='groove',width=2)
e29 = Entry(window, relief='groove',width=2)
e31 = Entry(window, relief='groove',width=2)
e32 = Entry(window, relief='groove',width=2)
e33 = Entry(window, relief='groove',width=2)
e34 = Entry(window, relief='groove',width=2)
e35 = Entry(window, relief='groove',width=2)
e36 = Entry(window, relief='groove',width=2)
e37 = Entry(window, relief='groove',width=2)
e38 = Entry(window, relief='groove',width=2)
e39 = Entry(window, relief='groove',width=2)
e41 = Entry(window, relief='groove',width=2)
e42 = Entry(window, relief='groove',width=2)
e43 = Entry(window, relief='groove',width=2)
e44 = Entry(window, relief='groove',width=2)
e45 = Entry(window, relief='groove',width=2)
e46 = Entry(window, relief='groove',width=2)
e47 = Entry(window, relief='groove',width=2)
e48 = Entry(window, relief='groove',width=2)
e49 = Entry(window, relief='groove',width=2)
e51 = Entry(window, relief='groove',width=2)
e52 = Entry(window, relief='groove',width=2)
e53 = Entry(window, relief='groove',width=2)
e54 = Entry(window, relief='groove',width=2)
e55 = Entry(window, relief='groove',width=2)
e56 = Entry(window, relief='groove',width=2)
e57 = Entry(window, relief='groove',width=2)
e58 = Entry(window, relief='groove',width=2)
e59 = Entry(window, relief='groove',width=2)
e61 = Entry(window, relief='groove',width=2)
e62 = Entry(window, relief='groove',width=2)
e63 = Entry(window, relief='groove',width=2)
e64 = Entry(window, relief='groove',width=2) 
e65 = Entry(window, relief='groove',width=2)
e66 = Entry(window, relief='groove',width=2)
e67 = Entry(window, relief='groove',width=2)
e68 = Entry(window, relief='groove',width=2)
e69 = Entry(window, relief='groove',width=2)
e71 = Entry(window, relief='groove',width=2)
e72 = Entry(window, relief='groove',width=2)
e73 = Entry(window, relief='groove',width=2)
e74 = Entry(window, relief='groove',width=2)
e75 = Entry(window, relief='groove',width=2)
e76 = Entry(window, relief='groove',width=2)
e77 = Entry(window, relief='groove',width=2)
e78 = Entry(window, relief='groove',width=2)
e79 = Entry(window, relief='groove',width=2)
e81 = Entry(window, relief='groove',width=2)
e82 = Entry(window, relief='groove',width=2)
e83 = Entry(window, relief='groove',width=2)
e84 = Entry(window, relief='groove',width=2)
e85 = Entry(window, relief='groove',width=2)
e86 = Entry(window, relief='groove',width=2)
e87 = Entry(window, relief='groove',width=2)
e88 = Entry(window, relief='groove',width=2)
e89 = Entry(window, relief='groove',width=2)
e91 = Entry(window, relief='groove',width=2)
e92 = Entry(window, relief='groove',width=2)
e93 = Entry(window, relief='groove',width=2)
e94 = Entry(window, relief='groove',width=2)
e95 = Entry(window, relief='groove',width=2)
e96 = Entry(window, relief='groove',width=2)
e97 = Entry(window, relief='groove',width=2)
e98 = Entry(window, relief='groove',width=2)
e99 = Entry(window, relief='groove',width=2)
# Output
o11 = Label(window,relief='groove',width=2)
o12 = Label(window,relief='groove',width=2)
o13 = Label(window,relief='groove',width=2)
o14 = Label(window,relief='groove',width=2)
o15 = Label(window,relief='groove',width=2)
o16 = Label(window,relief='groove',width=2)
o17 = Label(window,relief='groove',width=2)
o18 = Label(window,relief='groove',width=2)
o19 = Label(window,relief='groove',width=2)
o21 = Label(window,relief='groove',width=2)
o22 = Label(window,relief='groove',width=2)
o23 = Label(window,relief='groove',width=2)
o24 = Label(window,relief='groove',width=2)
o25 = Label(window,relief='groove',width=2)
o26 = Label(window,relief='groove',width=2)
o27 = Label(window,relief='groove',width=2)
o28 = Label(window,relief='groove',width=2)
o29 = Label(window,relief='groove',width=2)
o31 = Label(window,relief='groove',width=2)
o32 = Label(window,relief='groove',width=2)
o33 = Label(window,relief='groove',width=2)
o34 = Label(window,relief='groove',width=2)
o35 = Label(window,relief='groove',width=2)
o36 = Label(window,relief='groove',width=2)
o37 = Label(window,relief='groove',width=2)
o38 = Label(window,relief='groove',width=2)
o39 = Label(window,relief='groove',width=2)
o41 = Label(window,relief='groove',width=2)
o42 = Label(window,relief='groove',width=2)
o43 = Label(window,relief='groove',width=2)
o44 = Label(window,relief='groove',width=2)
o45 = Label(window,relief='groove',width=2)
o46 = Label(window,relief='groove',width=2)
o47 = Label(window,relief='groove',width=2)
o48 = Label(window,relief='groove',width=2)
o49 = Label(window,relief='groove',width=2)
o51 = Label(window,relief='groove',width=2)
o52 = Label(window,relief='groove',width=2)
o53 = Label(window,relief='groove',width=2)
o54 = Label(window,relief='groove',width=2)
o55 = Label(window,relief='groove',width=2)
o56 = Label(window,relief='groove',width=2)
o57 = Label(window,relief='groove',width=2)
o58 = Label(window,relief='groove',width=2)
o59 = Label(window,relief='groove',width=2)
o61 = Label(window,relief='groove',width=2)
o62 = Label(window,relief='groove',width=2)
o63 = Label(window,relief='groove',width=2)
o64 = Label(window,relief='groove',width=2)
o65 = Label(window,relief='groove',width=2)
o66 = Label(window,relief='groove',width=2)
o67 = Label(window,relief='groove',width=2)
o68 = Label(window,relief='groove',width=2)
o69 = Label(window,relief='groove',width=2)
o71 = Label(window,relief='groove',width=2)
o72 = Label(window,relief='groove',width=2)
o73 = Label(window,relief='groove',width=2)
o74 = Label(window,relief='groove',width=2)
o75 = Label(window,relief='groove',width=2)
o76 = Label(window,relief='groove',width=2)
o77 = Label(window,relief='groove',width=2)
o78 = Label(window,relief='groove',width=2)
o79 = Label(window,relief='groove',width=2)
o81 = Label(window,relief='groove',width=2)
o82 = Label(window,relief='groove',width=2)
o83 = Label(window,relief='groove',width=2)
o84 = Label(window,relief='groove',width=2)
o85 = Label(window,relief='groove',width=2)
o86 = Label(window,relief='groove',width=2)
o87 = Label(window,relief='groove',width=2)
o88 = Label(window,relief='groove',width=2)
o89 = Label(window,relief='groove',width=2)
o91 = Label(window,relief='groove',width=2)
o92 = Label(window,relief='groove',width=2)
o93 = Label(window,relief='groove',width=2)
o94 = Label(window,relief='groove',width=2)
o95 = Label(window,relief='groove',width=2)
o96 = Label(window,relief='groove',width=2)
o97 = Label(window,relief='groove',width=2)
o98 = Label(window,relief='groove',width=2)
o99 = Label(window,relief='groove',width=2)
scanBtn = Button(window, width = 5)
#Functions
#Set it up
def scan():
    puzzlenums[0][0] = int(e11.get())
    puzzlenums[0][1] = int(e12.get())
    puzzlenums[0][2] = int(e13.get())
    puzzlenums[0][3] = int(e14.get())
    puzzlenums[0][4] = int(e15.get())
    puzzlenums[0][5] = int(e16.get())
    puzzlenums[0][6] = int(e17.get())
    puzzlenums[0][7] = int(e18.get())
    puzzlenums[0][8] = int(e19.get())
    puzzlenums[1][0] = int(e21.get())
    puzzlenums[1][1] = int(e22.get())
    puzzlenums[1][2] = int(e23.get())
    puzzlenums[1][3] = int(e24.get())
    puzzlenums[1][4] = int(e25.get())
    puzzlenums[1][5] = int(e26.get())
    puzzlenums[1][6] = int(e27.get())
    puzzlenums[1][7] = int(e28.get())
    puzzlenums[1][8] = int(e29.get())
    puzzlenums[2][0] = int(e31.get())
    puzzlenums[2][1] = int(e32.get())
    puzzlenums[2][2] = int(e33.get())
    puzzlenums[2][3] = int(e34.get())
    puzzlenums[2][4] = int(e35.get())
    puzzlenums[2][5] = int(e36.get())
    puzzlenums[2][6] = int(e37.get())
    puzzlenums[2][7] = int(e38.get())
    puzzlenums[2][8] = int(e39.get())
    puzzlenums[3][0] = int(e41.get())
    puzzlenums[3][1] = int(e42.get())
    puzzlenums[3][2] = int(e43.get())
    puzzlenums[3][3] = int(e44.get())
    puzzlenums[3][4] = int(e45.get())
    puzzlenums[3][5] = int(e46.get())
    puzzlenums[3][6] = int(e47.get())
    puzzlenums[3][7] = int(e48.get())
    puzzlenums[3][8] = int(e49.get())
    puzzlenums[4][0] = int(e51.get())
    puzzlenums[4][1] = int(e52.get())
    puzzlenums[4][2] = int(e53.get())
    puzzlenums[4][3] = int(e54.get())
    puzzlenums[4][4] = int(e55.get())
    puzzlenums[4][5] = int(e56.get())
    puzzlenums[4][6] = int(e57.get())
    puzzlenums[4][7] = int(e58.get())
    puzzlenums[4][8] = int(e59.get())
    puzzlenums[5][0] = int(e61.get())
    puzzlenums[5][1] = int(e62.get())
    puzzlenums[5][2] = int(e63.get())
    puzzlenums[5][3] = int(e64.get())
    puzzlenums[5][4] = int(e65.get())
    puzzlenums[5][5] = int(e66.get())
    puzzlenums[5][6] = int(e67.get())
    puzzlenums[5][7] = int(e68.get())
    puzzlenums[5][8] = int(e69.get())
    puzzlenums[6][0] = int(e71.get())
    puzzlenums[6][1] = int(e72.get())
    puzzlenums[6][2] = int(e73.get())
    puzzlenums[6][3] = int(e74.get())
    puzzlenums[6][4] = int(e75.get())
    puzzlenums[6][5] = int(e76.get())
    puzzlenums[6][6] = int(e77.get())
    puzzlenums[6][7] = int(e78.get())
    puzzlenums[6][8] = int(e79.get())
    puzzlenums[7][0] = int(e81.get())
    puzzlenums[7][1] = int(e82.get())
    puzzlenums[7][2] = int(e83.get())
    puzzlenums[7][3] = int(e84.get())
    puzzlenums[7][4] = int(e85.get())
    puzzlenums[7][5] = int(e86.get())
    puzzlenums[7][6] = int(e87.get())
    puzzlenums[7][7] = int(e88.get())
    puzzlenums[7][8] = int(e89.get())
    puzzlenums[8][0] = int(e91.get())
    puzzlenums[8][1] = int(e92.get())
    puzzlenums[8][2] = int(e93.get())
    puzzlenums[8][3] = int(e94.get())
    puzzlenums[8][4] = int(e95.get())
    puzzlenums[8][5] = int(e96.get())
    puzzlenums[8][6] = int(e97.get())
    puzzlenums[8][7] = int(e98.get())
    puzzlenums[8][8] = int(e99.get())
    print(puzzlenums)
    return
#misc
solveBtn.configure(text = "Solve")
scanBtn.configure(text="Scan",command = scan)
# THE GRID
solveBtn.grid(row=10,column=9,columnspan=3)
scanBtn.grid(row=10,column=6,columnspan=3)
e11.grid(row=0,column=0)
e12.grid(row=0,column=1)
e13.grid(row=0,column=2)
e14.grid(row=0,column=3)
e15.grid(row=0,column=4)
e16.grid(row=0,column=5)
e17.grid(row=0,column=6)
e18.grid(row=0,column=7)
e19.grid(row=0,column=8)
e21.grid(row=1,column=0)
e22.grid(row=1,column=1)
e23.grid(row=1,column=2)
e24.grid(row=1,column=3)
e25.grid(row=1,column=4)
e26.grid(row=1,column=5)
e27.grid(row=1,column=6)
e28.grid(row=1,column=7)
e29.grid(row=1,column=8)
e31.grid(row=2,column=0)
e32.grid(row=2,column=1)
e33.grid(row=2,column=2)
e34.grid(row=2,column=3)
e35.grid(row=2,column=4)
e36.grid(row=2,column=5)
e37.grid(row=2,column=6)
e38.grid(row=2,column=7)
e39.grid(row=2,column=8)
e41.grid(row=3,column=0)
e42.grid(row=3,column=1)
e43.grid(row=3,column=2)
e44.grid(row=3,column=3)
e45.grid(row=3,column=4)
e46.grid(row=3,column=5)
e47.grid(row=3,column=6)
e48.grid(row=3,column=7)
e49.grid(row=3,column=8)
e51.grid(row=4,column=0)
e52.grid(row=4,column=1)
e53.grid(row=4,column=2)
e54.grid(row=4,column=3)
e55.grid(row=4,column=4)
e56.grid(row=4,column=5)
e57.grid(row=4,column=6)
e58.grid(row=4,column=7)
e59.grid(row=4,column=8)
e61.grid(row=5,column=0)
e62.grid(row=5,column=1)
e63.grid(row=5,column=2)
e64.grid(row=5,column=3)
e65.grid(row=5,column=4)
e66.grid(row=5,column=5)
e67.grid(row=5,column=6)
e68.grid(row=5,column=7)
e69.grid(row=5,column=8)
e71.grid(row=6,column=0)
e72.grid(row=6,column=1)
e73.grid(row=6,column=2)
e74.grid(row=6,column=3)
e75.grid(row=6,column=4)
e76.grid(row=6,column=5)
e77.grid(row=6,column=6)
e78.grid(row=6,column=7)
e79.grid(row=6,column=8)
e81.grid(row=7,column=0)
e82.grid(row=7,column=1)
e83.grid(row=7,column=2)
e84.grid(row=7,column=3)
e85.grid(row=7,column=4)
e86.grid(row=7,column=5)
e87.grid(row=7,column=6)
e88.grid(row=7,column=7)
e89.grid(row=7,column=8)
e91.grid(row=8,column=0)
e92.grid(row=8,column=1)
e93.grid(row=8,column=2)
e94.grid(row=8,column=3)
e95.grid(row=8,column=4)
e96.grid(row=8,column=5)
e97.grid(row=8,column=6)
e98.grid(row=8,column=7)
e99.grid(row=8,column=8)
o11.grid(row=0,column=9)
o12.grid(row=0,column=10)
o13.grid(row=0,column=11)
o14.grid(row=0,column=12)
o15.grid(row=0,column=13)
o16.grid(row=0,column=14)
o17.grid(row=0,column=15)
o18.grid(row=0,column=16)
o19.grid(row=0,column=17)
o21.grid(row=1,column=9)
o22.grid(row=1,column=10)
o23.grid(row=1,column=11)
o24.grid(row=1,column=12)
o25.grid(row=1,column=13)
o26.grid(row=1,column=14)
o27.grid(row=1,column=15)
o28.grid(row=1,column=16)
o29.grid(row=1,column=17)
o31.grid(row=2,column=9)
o32.grid(row=2,column=10)
o33.grid(row=2,column=11)
o34.grid(row=2,column=12)
o35.grid(row=2,column=13)
o36.grid(row=2,column=14)
o37.grid(row=2,column=15)
o38.grid(row=2,column=16)
o39.grid(row=2,column=17)
o41.grid(row=3,column=9)
o42.grid(row=3,column=10)
o43.grid(row=3,column=11)
o44.grid(row=3,column=12)
o45.grid(row=3,column=13)
o46.grid(row=3,column=14)
o47.grid(row=3,column=15)
o48.grid(row=3,column=16)
o49.grid(row=3,column=17)
o51.grid(row=4,column=9)
o52.grid(row=4,column=10)
o53.grid(row=4,column=11)
o54.grid(row=4,column=12)
o55.grid(row=4,column=13)
o56.grid(row=4,column=14)
o57.grid(row=4,column=15)
o58.grid(row=4,column=16)
o59.grid(row=4,column=17)
o61.grid(row=5,column=9)
o62.grid(row=5,column=10)
o63.grid(row=5,column=11)
o64.grid(row=5,column=12)
o65.grid(row=5,column=13)
o66.grid(row=5,column=14)
o67.grid(row=5,column=15)
o68.grid(row=5,column=16)
o69.grid(row=5,column=17)
o71.grid(row=6,column=9)
o72.grid(row=6,column=10)
o73.grid(row=6,column=11)
o74.grid(row=6,column=12)
o75.grid(row=6,column=13)
o76.grid(row=6,column=14)
o77.grid(row=6,column=15)
o78.grid(row=6,column=16)
o79.grid(row=6,column=17)
o81.grid(row=7,column=9)
o82.grid(row=7,column=10)
o83.grid(row=7,column=11)
o84.grid(row=7,column=12)
o85.grid(row=7,column=13)
o86.grid(row=7,column=14)
o87.grid(row=7,column=15)
o88.grid(row=7,column=16)
o89.grid(row=7,column=17)
o91.grid(row=8,column=9)
o92.grid(row=8,column=10)
o93.grid(row=8,column=11)
o94.grid(row=8,column=12)
o95.grid(row=8,column=13)
o96.grid(row=8,column=14)
o97.grid(row=8,column=15)
o98.grid(row=8,column=16)
o99.grid(row=8,column=17)
c11 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c12 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c13 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c14 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c15 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c16 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c17 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c18 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c19 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c21 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c22 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c23 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c24 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c25 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c26 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c27 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c28 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c29 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c31 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c32 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c33 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c34 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c35 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c36 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c37 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c38 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c39 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c41 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c42 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c43 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c44 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c45 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c46 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c47 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c48 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c49 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c51 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c52 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c53 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c54 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c55 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c56 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c57 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c58 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c59 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c61 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c62 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c63 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c64 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c65 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c66 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c67 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c68 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c69 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c71 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c72 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c73 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c74 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c75 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c76 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c77 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c78 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c79 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c81 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c82 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c83 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c84 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c85 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c86 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c87 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c88 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c89 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c91 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c92 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c93 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c94 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c95 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c96 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c97 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c98 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
c99 = {
    "1":True,
    "2":True,
    "3":True,
    "4":True,
    "5":True,
    "6":True,
    "7":True,
    "8":True,
    "9":True
}
print(c11)
e11do = True
e12do = True
e13do = True
e14do = True
e15do = True
e16do = True
e17do = True
e18do = True
e19do = True
e21do = True
e22do = True
e23do = True
e24do = True
e25do = True
e26do = True
e27do = True
e28do = True
e29do = True
e31do = True
e32do = True
e33do = True
e34do = True
e35do = True
e36do = True
e37do = True
e38do = True
e39do = True
e41do = True
e42do = True
e43do = True
e44do = True
e45do = True
e46do = True
e47do = True
e48do = True
e49do = True
e51do = True
e52do = True
e53do = True
e54do = True
e55do = True
e56do = True
e57do = True
e58do = True
e59do = True
e61do = True
e62do = True
e63do = True
e64do = True
e65do = True
e66do = True
e67do = True
e68do = True
e69do = True
e71do = True
e72do = True
e73do = True
e74do = True
e75do = True
e76do = True
e77do = True
e78do = True
e79do = True
e81do = True
e82do = True
e83do = True
e84do = True
e85do = True
e86do = True
e87do = True
e88do = True
e89do = True
e91do = True
e92do = True
e93do = True
e94do = True
e95do = True
e96do = True
e97do = True
e98do = True
e99do = True
solvednums = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
def solve():
    """Solve Dat Puzzle"""
    sleep(1)
    if puzzlenums[0][0] > 0 and e11do == True:
        solvednums[0][0] = puzzlenums[0][0]
        e11do = False
        sleep(1)
    elif e11do == True and c11['1'] == True and c11['2'] == False and c11['3'] == False and c11['4'] == False and c11['5'] == False and c11['6'] == False and c11['7'] == False and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 1
    elif e11do == True and c11['1'] == False and c11['2'] == True and c11['3'] == False and c11['4'] == False and c11['5'] == False and c11['6'] == False and c11['7'] == False and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 2
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == True and c11['4'] == False and c11['5'] == False and c11['6'] == False and c11['7'] == False and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 3
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == False and c11['4'] == True and c11['5'] == False and c11['6'] == False and c11['7'] == False and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 4
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == False and c11['4'] == False and c11['5'] == True and c11['6'] == False and c11['7'] == False and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 5
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == False and c11['4'] == False and c11['5'] == False and c11['6'] == True and c11['7'] == False and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 6
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == False and c11['4'] == False and c11['5'] == False and c11['6'] == False and c11['7'] == True and c11['8'] == False and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 7
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == False and c11['4'] == False and c11['5'] == False and c11['6'] == False and c11['7'] == False and c11['8'] == True and c11['9'] == False:
        e11do = False
        solvednums[0][0] = 8
    elif e11do == True and c11['1'] == False and c11['2'] == False and c11['3'] == False and c11['4'] == False and c11['5'] == False and c11['6'] == False and c11['7'] == False and c11['8'] == False and c11['9'] == True:
        e11do = False
        solvednums[0][0] = 9
    else:
        if solvednums[0][0] == 1:
            c11['1'] = False
            c11['2'] = False
            c11['3'] = False
            c11['4'] = False
            c11['5'] = False
            c11['6'] = False
            c11['7'] = False
            c11['8'] = False
            c11['9'] = False
            c12['1'] = False
            c13['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c41['1'] = False
            c51['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[0][0] == 2:
            c11['1'] = False
            c11['2'] = False
            c11['3'] = False
            c11['4'] = False
            c11['5'] = False
            c11['6'] = False
            c11['7'] = False
            c11['8'] = False
            c11['9'] = False
            c12['2'] = False
            c13['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c41['2'] = False
            c51['2'] = False
            c61['2'] = False
            c71['2'] = False
            c81['2'] = False
            c91['2'] = False
        elif solvednums[0][0] == 3:
            c12['3'] = False
            c13['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c41['3'] = False
            c51['3'] = False
            c61['3'] = False
            c71['3'] = False
            c81['3'] = False
            c91['3'] = False
        elif solvednums[0][0] == 4:
            c12['4'] = False
            c13['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c31['4'] = False
            c34['4'] = False
            c33['4'] = False
            c41['4'] = False
            c51['4'] = False
            c61['4'] = False
            c71['4'] = False
            c81['4'] = False
            c91['4'] = False
        elif solvednums[0][0] == 5:
            c12['5'] = False
            c13['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c41['5'] = False
            c51['5'] = False
            c61['5'] = False
            c71['5'] = False
            c81['5'] = False
            c91['5'] = False
        elif solvednums[0][0] == 6:
            c12['6'] = False
            c13['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c41['6'] = False
            c51['6'] = False
            c61['6'] = False
            c71['6'] = False
            c81['6'] = False
            c91['6'] = False
        elif solvednums[0][0] == 7:
            c12['7'] = False
            c13['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c41['7'] = False
            c51['7'] = False
            c61['7'] = False
            c71['7'] = False
            c81['7'] = False
            c91['7'] = False
        elif solvednums[0][0] == 8:
            c12['8'] = False
            c13['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c41['8'] = False
            c51['8'] = False
            c61['8'] = False
            c71['8'] = False
            c81['8'] = False
            c91['8'] = False
        elif solvednums[0][0] == 9:
            c12['9'] = False
            c13['9'] = False
            c14['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c41['9'] = False
            c51['9'] = False
            c61['9'] = False
            c71['9'] = False   
            c81['9'] = False
            c91['9'] = False
    if puzzlenums[0][1] > 0 and e12do == True:
        solvednums[0][1] = puzzlenums[0][1]
        e12do = False
        sleep(1)
    elif e12do == True and c12['1'] == True and c12['2'] == False and c12['3'] == False and c12['4'] == False and c12['5'] == False and c12['6'] == False and c12['7'] == False and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 1
    elif e12do == True and c12['1'] == False and c12['2'] == True and c12['3'] == False and c12['4'] == False and c12['5'] == False and c12['6'] == False and c12['7'] == False and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 2
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == True and c12['4'] == False and c12['5'] == False and c12['6'] == False and c12['7'] == False and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 3
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == False and c12['4'] == True and c12['5'] == False and c12['6'] == False and c12['7'] == False and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 4
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == False and c12['4'] == False and c12['5'] == True and c12['6'] == False and c12['7'] == False and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 5
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == False and c12['4'] == False and c12['5'] == False and c12['6'] == True and c12['7'] == False and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 6
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == False and c12['4'] == False and c12['5'] == False and c12['6'] == False and c12['7'] == True and c12['8'] == False and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 7
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == False and c12['4'] == False and c12['5'] == False and c12['6'] == False and c12['7'] == False and c12['8'] == True and c12['9'] == False:
        e12do = False
        solvednums[0][1] = 8
    elif e12do == True and c12['1'] == False and c12['2'] == False and c12['3'] == False and c12['4'] == False and c12['5'] == False and c12['6'] == False and c12['7'] == False and c12['8'] == False and c12['9'] == True:
        e12do = False
        solvednums[0][1] = 9
    else:
        if solvednums[0][1] == 1:
            c11['1'] = False
            c13['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c42['1'] = False
            c52['1'] = False
            c62['1'] = False
            c72['1'] = False
            c82['1'] = False
            c92['1'] = False
        elif solvednums[0][1] == 2:
            c11['2'] = False
            c13['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c42['2'] = False
            c52['2'] = False
            c62['2'] = False
            c72['2'] = False
            c82['2'] = False
            c92['2'] = False
        elif solvednums[0][1] == 3:
            c11['3'] = False
            c13['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c42['3'] = False
            c52['3'] = False
            c62['3'] = False
            c72['3'] = False
            c82['3'] = False
            c92['3'] = False
        elif solvednums[0][1] == 4:
            c11['4'] = False
            c13['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c31['4'] = False
            c34['4'] = False
            c33['4'] = False
            c42['4'] = False
            c52['4'] = False
            c62['4'] = False
            c72['4'] = False
            c82['4'] = False
            c92['4'] = False
        elif solvednums[0][1] == 5:
            c11['5'] = False
            c13['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c42['5'] = False
            c52['5'] = False
            c62['5'] = False
            c72['5'] = False
            c82['5'] = False
            c92['5'] = False
        elif solvednums[0][1] == 6:
            c11['6'] = False
            c13['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c42['6'] = False
            c52['6'] = False
            c62['6'] = False
            c72['6'] = False
            c82['6'] = False
            c92['6'] = False
        elif solvednums[0][1] == 7:
            c11['7'] = False
            c13['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c42['7'] = False
            c52['7'] = False
            c62['7'] = False
            c72['7'] = False
            c82['7'] = False
            c92['7'] = False
        elif solvednums[0][1] == 8:
            c11['8'] = False
            c13['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c42['8'] = False
            c52['8'] = False
            c62['8'] = False
            c72['8'] = False
            c82['8'] = False
            c92['8'] = False
        elif solvednums[0][1] == 9:
            c11['9'] = False
            c13['9'] = False
            c14['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c42['9'] = False
            c52['9'] = False
            c62['9'] = False
            c72['9'] = False   
            c82['9'] = False
            c92['9'] = False
    if puzzlenums[0][2] > 0 and e13do == True:
        solvednums[0][2] = puzzlenums[0][2]
        e13do = False
        sleep(1)
    elif e13do == True and c13['1'] == True and c13['2'] == False and c13['3'] == False and c13['4'] == False and c13['5'] == False and c13['6'] == False and c13['7'] == False and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 1
    elif e13do == True and c13['1'] == False and c13['2'] == True and c13['3'] == False and c13['4'] == False and c13['5'] == False and c13['6'] == False and c13['7'] == False and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 2
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == True and c13['4'] == False and c13['5'] == False and c13['6'] == False and c13['7'] == False and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 3
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == False and c13['4'] == True and c13['5'] == False and c13['6'] == False and c13['7'] == False and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 4
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == False and c13['4'] == False and c13['5'] == True and c13['6'] == False and c13['7'] == False and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 5
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == False and c13['4'] == False and c13['5'] == False and c13['6'] == True and c13['7'] == False and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 6
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == False and c13['4'] == False and c13['5'] == False and c13['6'] == False and c13['7'] == True and c13['8'] == False and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 7
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == False and c13['4'] == False and c13['5'] == False and c13['6'] == False and c13['7'] == False and c13['8'] == True and c13['9'] == False:
        e13do = False
        solvednums[0][2] = 8
    elif e13do == True and c13['1'] == False and c13['2'] == False and c13['3'] == False and c13['4'] == False and c13['5'] == False and c13['6'] == False and c13['7'] == False and c13['8'] == False and c13['9'] == True:
        e13do = False
        solvednums[0][2] = 9
    else:
        if solvednums[0][2] == 1:
            c11['1'] = False
            c12['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c43['1'] = False
            c53['1'] = False
            c63['1'] = False
            c73['1'] = False
            c83['1'] = False
            c93['1'] = False
        elif solvednums[0][2] == 2:
            c11['2'] = False
            c12['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c43['2'] = False
            c53['2'] = False
            c63['2'] = False
            c73['2'] = False
            c83['2'] = False
            c93['2'] = False
        elif solvednums[0][2] == 3:
            c11['3'] = False
            c12['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c43['3'] = False
            c53['3'] = False
            c63['3'] = False
            c73['3'] = False
            c83['3'] = False
            c93['3'] = False
        elif solvednums[0][2] == 4:
            c11['4'] = False
            c12['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c31['4'] = False
            c34['4'] = False
            c33['4'] = False
            c43['4'] = False
            c53['4'] = False
            c63['4'] = False
            c73['4'] = False
            c83['4'] = False
            c93['4'] = False
        elif solvednums[0][2] == 5:
            c11['5'] = False
            c12['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c43['5'] = False
            c53['5'] = False
            c63['5'] = False
            c73['5'] = False
            c83['5'] = False
            c93['5'] = False
        elif solvednums[0][2] == 6:
            c11['6'] = False
            c12['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c43['6'] = False
            c53['6'] = False
            c63['6'] = False
            c73['6'] = False
            c83['6'] = False
            c93['6'] = False
        elif solvednums[0][2] == 7:
            c11['7'] = False
            c12['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c43['7'] = False
            c53['7'] = False
            c63['7'] = False
            c73['7'] = False
            c83['7'] = False
            c93['7'] = False
        elif solvednums[0][2] == 8:
            c11['8'] = False
            c12['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c43['8'] = False
            c53['8'] = False
            c63['8'] = False
            c73['8'] = False
            c83['8'] = False
            c93['8'] = False
        elif solvednums[0][2] == 9:
            c11['9'] = False
            c12['9'] = False
            c14['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c43['9'] = False
            c53['9'] = False
            c63['9'] = False
            c73['9'] = False   
            c83['9'] = False
            c93['9'] = False
    if puzzlenums[0][3] > 0 and e14do == True:
        solvednums[0][3] = puzzlenums[0][3]
        e14do = False
        sleep(1)
    elif e14do == True and c14['1'] == True and c14['2'] == False and c14['3'] == False and c14['4'] == False and c14['5'] == False and c14['6'] == False and c14['7'] == False and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 1
    elif e14do == True and c14['1'] == False and c14['2'] == True and c14['3'] == False and c14['4'] == False and c14['5'] == False and c14['6'] == False and c14['7'] == False and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 2
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == True and c14['4'] == False and c14['5'] == False and c14['6'] == False and c14['7'] == False and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 3
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == False and c14['4'] == True and c14['5'] == False and c14['6'] == False and c14['7'] == False and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 4
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == False and c14['4'] == False and c14['5'] == True and c14['6'] == False and c14['7'] == False and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 5
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == False and c14['4'] == False and c14['5'] == False and c14['6'] == True and c14['7'] == False and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 6
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == False and c14['4'] == False and c14['5'] == False and c14['6'] == False and c14['7'] == True and c14['8'] == False and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 7
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == False and c14['4'] == False and c14['5'] == False and c14['6'] == False and c14['7'] == False and c14['8'] == True and c14['9'] == False:
        e14do = False
        solvednums[0][3] = 8
    elif e14do == True and c14['1'] == False and c14['2'] == False and c14['3'] == False and c14['4'] == False and c14['5'] == False and c14['6'] == False and c14['7'] == False and c14['8'] == False and c14['9'] == True:
        e14do = False
        solvednums[0][3] = 9
    else:
        if solvednums[0][3] == 1:
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c44['1'] = False
            c54['1'] = False
            c64['1'] = False
            c74['1'] = False
            c84['1'] = False
            c94['1'] = False
        elif solvednums[0][3] == 2:
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c44['2'] = False
            c54['2'] = False
            c64['2'] = False
            c74['2'] = False
            c84['2'] = False
            c94['2'] = False
        elif solvednums[0][3] == 3:
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c44['3'] = False
            c54['3'] = False
            c64['3'] = False
            c74['3'] = False
            c84['3'] = False
            c94['3'] = False
        elif solvednums[0][3] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c44['4'] = False
            c54['4'] = False
            c64['4'] = False
            c74['4'] = False
            c84['4'] = False
            c94['4'] = False
        elif solvednums[0][3] == 5:
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c44['5'] = False
            c54['5'] = False
            c64['5'] = False
            c74['5'] = False
            c84['5'] = False
            c94['5'] = False
        elif solvednums[0][3] == 6:
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c44['6'] = False
            c54['6'] = False
            c64['6'] = False
            c74['6'] = False
            c84['6'] = False
            c94['6'] = False
        elif solvednums[0][3] == 7:
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c44['7'] = False
            c54['7'] = False
            c64['7'] = False
            c74['7'] = False
            c84['7'] = False
            c94['7'] = False
        elif solvednums[0][3] == 8:
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c44['8'] = False
            c54['8'] = False
            c64['8'] = False
            c74['8'] = False
            c84['8'] = False
            c94['8'] = False
        elif solvednums[0][3] == 9:
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c24['9'] = False
            c25['9'] = False
            c26['9'] = False
            c34['9'] = False
            c35['9'] = False
            c36['9'] = False
            c44['9'] = False
            c54['9'] = False
            c64['9'] = False
            c74['9'] = False   
            c84['9'] = False
            c94['9'] = False
    if puzzlenums[0][4] > 0 and e15do == True:
        solvednums[0][4] = puzzlenums[0][4]
        e15do = False
        sleep(1)
    elif e15do == True and c15['1'] == True and c15['2'] == False and c15['3'] == False and c15['4'] == False and c15['5'] == False and c15['6'] == False and c15['7'] == False and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 1
    elif e15do == True and c15['1'] == False and c15['2'] == True and c15['3'] == False and c15['4'] == False and c15['5'] == False and c15['6'] == False and c15['7'] == False and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 2
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == True and c15['4'] == False and c15['5'] == False and c15['6'] == False and c15['7'] == False and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 3
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == False and c15['4'] == True and c15['5'] == False and c15['6'] == False and c15['7'] == False and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 4
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == False and c15['4'] == False and c15['5'] == True and c15['6'] == False and c15['7'] == False and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 5
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == False and c15['4'] == False and c15['5'] == False and c15['6'] == True and c15['7'] == False and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 6
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == False and c15['4'] == False and c15['5'] == False and c15['6'] == False and c15['7'] == True and c15['8'] == False and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 7
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == False and c15['4'] == False and c15['5'] == False and c15['6'] == False and c15['7'] == False and c15['8'] == True and c15['9'] == False:
        e15do = False
        solvednums[0][4] = 8
    elif e15do == True and c15['1'] == False and c15['2'] == False and c15['3'] == False and c15['4'] == False and c15['5'] == False and c15['6'] == False and c15['7'] == False and c15['8'] == False and c15['9'] == True:
        e15do = False
        solvednums[0][4] = 9
    else:
        if solvednums[0][4] == 1:
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c45['1'] = False
            c55['1'] = False
            c65['1'] = False
            c75['1'] = False
            c85['1'] = False
            c95['1'] = False
        elif solvednums[0][4] == 2:
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c45['2'] = False
            c55['2'] = False
            c65['2'] = False
            c75['2'] = False
            c85['2'] = False
            c95['2'] = False
        elif solvednums[0][4] == 3:
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c45['3'] = False
            c55['3'] = False
            c65['3'] = False
            c75['3'] = False
            c85['3'] = False
            c95['3'] = False
        elif solvednums[0][4] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c45['4'] = False
            c55['4'] = False
            c65['4'] = False
            c75['4'] = False
            c85['4'] = False
            c95['4'] = False
        elif solvednums[0][4] == 5:
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c45['5'] = False
            c55['5'] = False
            c65['5'] = False
            c75['5'] = False
            c85['5'] = False
            c95['5'] = False
        elif solvednums[0][4] == 6:
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c45['6'] = False
            c55['6'] = False
            c65['6'] = False
            c75['6'] = False
            c85['6'] = False
            c95['6'] = False
        elif solvednums[0][4] == 7:
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c45['7'] = False
            c55['7'] = False
            c65['7'] = False
            c75['7'] = False
            c85['7'] = False
            c95['7'] = False
        elif solvednums[0][4] == 8:
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c45['8'] = False
            c55['8'] = False
            c65['8'] = False
            c75['8'] = False
            c85['8'] = False
            c95['8'] = False
        elif solvednums[0][4] == 9:
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c24['9'] = False
            c25['9'] = False
            c26['9'] = False
            c34['9'] = False
            c35['9'] = False
            c36['9'] = False
            c45['9'] = False
            c55['9'] = False
            c65['9'] = False
            c75['9'] = False   
            c85['9'] = False
            c95['9'] = False
    if puzzlenums[0][5] > 0 and e16do == True:
        solvednums[0][5] = puzzlenums[0][5]
        e16do = False
        sleep(1)
    elif e16do == True and c16['1'] == True and c16['2'] == False and c16['3'] == False and c16['4'] == False and c16['5'] == False and c16['6'] == False and c16['7'] == False and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 1
    elif e16do == True and c16['1'] == False and c16['2'] == True and c16['3'] == False and c16['4'] == False and c16['5'] == False and c16['6'] == False and c16['7'] == False and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 2
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == True and c16['4'] == False and c16['5'] == False and c16['6'] == False and c16['7'] == False and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 3
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == False and c16['4'] == True and c16['5'] == False and c16['6'] == False and c16['7'] == False and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][6] = 4
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == False and c16['4'] == False and c16['5'] == True and c16['6'] == False and c16['7'] == False and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 5
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == False and c16['4'] == False and c16['5'] == False and c16['6'] == True and c16['7'] == False and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 6
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == False and c16['4'] == False and c16['5'] == False and c16['6'] == False and c16['7'] == True and c16['8'] == False and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 7
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == False and c16['4'] == False and c16['5'] == False and c16['6'] == False and c16['7'] == False and c16['8'] == True and c16['9'] == False:
        e16do = False
        solvednums[0][5] = 8
    elif e16do == True and c16['1'] == False and c16['2'] == False and c16['3'] == False and c16['4'] == False and c16['5'] == False and c16['6'] == False and c16['7'] == False and c16['8'] == False and c16['9'] == True:
        e16do = False
        solvednums[0][5] = 9     
    else:
        if solvednums[0][5] == 1:
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c46['1'] = False
            c56['1'] = False
            c66['1'] = False
            c76['1'] = False
            c86['1'] = False
            c96['1'] = False
        elif solvednums[0][5] == 2:
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c46['2'] = False
            c56['2'] = False
            c66['2'] = False
            c76['2'] = False
            c86['2'] = False
            c96['2'] = False
        elif solvednums[0][5] == 3:
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c46['3'] = False
            c56['3'] = False
            c66['3'] = False
            c76['3'] = False
            c86['3'] = False
            c96['3'] = False
        elif solvednums[0][5] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c46['4'] = False
            c56['4'] = False
            c66['4'] = False
            c76['4'] = False
            c86['4'] = False
            c96['4'] = False
        elif solvednums[0][5] == 5:
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c46['5'] = False
            c56['5'] = False
            c66['5'] = False
            c76['5'] = False
            c86['5'] = False
            c96['5'] = False
        elif solvednums[0][5] == 6:
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c46['6'] = False
            c56['6'] = False
            c66['6'] = False
            c76['6'] = False
            c86['6'] = False
            c96['6'] = False
        elif solvednums[0][5] == 7:
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c46['7'] = False
            c56['7'] = False
            c66['7'] = False
            c76['7'] = False
            c86['7'] = False
            c96['7'] = False
        elif solvednums[0][5] == 8:
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c46['8'] = False
            c56['8'] = False
            c66['8'] = False
            c76['8'] = False
            c86['8'] = False
            c96['8'] = False
        elif solvednums[0][5] == 9:
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c24['9'] = False
            c25['9'] = False
            c26['9'] = False
            c34['9'] = False
            c35['9'] = False
            c36['9'] = False
            c46['9'] = False
            c56['9'] = False
            c66['9'] = False
            c76['9'] = False   
            c86['9'] = False
            c96['9'] = False
    if puzzlenums[0][6] > 0 and e17do == True:
        solvednums[0][6] = puzzlenums[0][6]
        e17do = False
        sleep(1)
    elif e17do == True and c17['1'] == True and c17['2'] == False and c17['3'] == False and c17['4'] == False and c17['5'] == False and c17['6'] == False and c17['7'] == False and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 1
    elif e17do == True and c17['1'] == False and c17['2'] == True and c17['3'] == False and c17['4'] == False and c17['5'] == False and c17['6'] == False and c17['7'] == False and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 2
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == True and c17['4'] == False and c17['5'] == False and c17['6'] == False and c17['7'] == False and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 3
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == False and c17['4'] == True and c17['5'] == False and c17['6'] == False and c17['7'] == False and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 4
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == False and c17['4'] == False and c17['5'] == True and c17['6'] == False and c17['7'] == False and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 5
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == False and c17['4'] == False and c17['5'] == False and c17['6'] == True and c17['7'] == False and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 6
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == False and c17['4'] == False and c17['5'] == False and c17['6'] == False and c17['7'] == True and c17['8'] == False and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 7
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == False and c17['4'] == False and c17['5'] == False and c17['6'] == False and c17['7'] == False and c17['8'] == True and c17['9'] == False:
        e17do = False
        solvednums[0][6] = 8
    elif e17do == True and c17['1'] == False and c17['2'] == False and c17['3'] == False and c17['4'] == False and c17['5'] == False and c17['6'] == False and c17['7'] == False and c17['8'] == False and c17['9'] == True:
        e17do = False
        solvednums[0][6] = 9
    else:
        if solvednums[0][6] == 1:
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c47['1'] = False
            c57['1'] = False
            c67['1'] = False
            c77['1'] = False
            c87['1'] = False
            c97['1'] = False
        elif solvednums[0][6] == 2:
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c47['2'] = False
            c57['2'] = False
            c67['2'] = False
            c77['2'] = False
            c87['2'] = False
            c97['2'] = False
        elif solvednums[0][6] == 3:
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c47['3'] = False
            c57['3'] = False
            c67['3'] = False
            c77['3'] = False
            c87['3'] = False
            c97['3'] = False
        elif solvednums[0][6] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c47['4'] = False
            c57['4'] = False
            c67['4'] = False
            c77['4'] = False
            c87['4'] = False
            c97['4'] = False
        elif solvednums[0][6] == 5:
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c47['5'] = False
            c57['5'] = False
            c67['5'] = False
            c77['5'] = False
            c87['5'] = False
            c97['5'] = False
        elif solvednums[0][6] == 6:
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c47['6'] = False
            c57['6'] = False
            c67['6'] = False
            c77['6'] = False
            c87['6'] = False
            c97['6'] = False
        elif solvednums[0][6] == 7:
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c47['7'] = False
            c57['7'] = False
            c67['7'] = False
            c77['7'] = False
            c87['7'] = False
            c97['7'] = False
        elif solvednums[0][6] == 8:
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c47['8'] = False
            c57['8'] = False
            c67['8'] = False
            c77['8'] = False
            c87['8'] = False
            c97['8'] = False
        elif solvednums[0][6] == 9:
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c47['9'] = False
            c57['9'] = False
            c67['9'] = False
            c77['9'] = False   
            c87['9'] = False
            c97['9'] = False
    if puzzlenums[0][7] > 0 and e18do == True:
        solvednums[0][7] = puzzlenums[0][7]
        e18do = False
        sleep(1)
    elif e18do == True and c18['1'] == True and c18['2'] == False and c18['3'] == False and c18['4'] == False and c18['5'] == False and c18['6'] == False and c18['7'] == False and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 1
    elif e18do == True and c18['1'] == False and c18['2'] == True and c18['3'] == False and c18['4'] == False and c18['5'] == False and c18['6'] == False and c18['7'] == False and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 2
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == True and c18['4'] == False and c18['5'] == False and c18['6'] == False and c18['7'] == False and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 3
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == False and c18['4'] == True and c18['5'] == False and c18['6'] == False and c18['7'] == False and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 4
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == False and c18['4'] == False and c18['5'] == True and c18['6'] == False and c18['7'] == False and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 5
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == False and c18['4'] == False and c18['5'] == False and c18['6'] == True and c18['7'] == False and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 6
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == False and c18['4'] == False and c18['5'] == False and c18['6'] == False and c18['7'] == True and c18['8'] == False and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 7
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == False and c18['4'] == False and c18['5'] == False and c18['6'] == False and c18['7'] == False and c18['8'] == True and c18['9'] == False:
        e18do = False
        solvednums[0][7] = 8
    elif e18do == True and c18['1'] == False and c18['2'] == False and c18['3'] == False and c18['4'] == False and c18['5'] == False and c18['6'] == False and c18['7'] == False and c18['8'] == False and c18['9'] == True:
        e18do = False
        solvednums[0][7] = 9
    else:
        if solvednums[0][7] == 1:
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c48['1'] = False
            c58['1'] = False
            c68['1'] = False
            c78['1'] = False
            c88['1'] = False
            c98['1'] = False
        elif solvednums[0][7] == 2:
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c48['2'] = False
            c58['2'] = False
            c68['2'] = False
            c78['2'] = False
            c88['2'] = False
            c98['2'] = False
        elif solvednums[0][7] == 3:
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c48['3'] = False
            c58['3'] = False
            c68['3'] = False
            c78['3'] = False
            c88['3'] = False
            c98['3'] = False
        elif solvednums[0][7] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c48['4'] = False
            c58['4'] = False
            c68['4'] = False
            c78['4'] = False
            c88['4'] = False
            c98['4'] = False
        elif solvednums[0][7] == 5:
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c48['5'] = False
            c58['5'] = False
            c68['5'] = False
            c78['5'] = False
            c88['5'] = False
            c98['5'] = False
        elif solvednums[0][7] == 6:
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c48['6'] = False
            c58['6'] = False
            c68['6'] = False
            c78['6'] = False
            c88['6'] = False
            c98['6'] = False
        elif solvednums[0][7] == 7:
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c48['7'] = False
            c58['7'] = False
            c68['7'] = False
            c78['7'] = False
            c88['7'] = False
            c98['7'] = False
        elif solvednums[0][7] == 8:
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c48['8'] = False
            c58['8'] = False
            c68['8'] = False
            c78['8'] = False
            c88['8'] = False
            c98['8'] = False
        elif solvednums[0][7] == 9:
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c48['9'] = False
            c58['9'] = False
            c68['9'] = False
            c78['9'] = False   
            c88['9'] = False
            c98['9'] = False
    if puzzlenums[0][8] > 0 and e19do == True:
        solvednums[0][8] = puzzlenums[0][8]
        e19do = False
        sleep(1)
    elif e19do == True and c19['1'] == True and c19['2'] == False and c19['3'] == False and c19['4'] == False and c19['5'] == False and c19['6'] == False and c19['7'] == False and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 1
    elif e19do == True and c19['1'] == False and c19['2'] == True and c19['3'] == False and c19['4'] == False and c19['5'] == False and c19['6'] == False and c19['7'] == False and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 2
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == True and c19['4'] == False and c19['5'] == False and c19['6'] == False and c19['7'] == False and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 3
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == False and c19['4'] == True and c19['5'] == False and c19['6'] == False and c19['7'] == False and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 4
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == False and c19['4'] == False and c19['5'] == True and c19['6'] == False and c19['7'] == False and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 5
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == False and c19['4'] == False and c19['5'] == False and c19['6'] == True and c19['7'] == False and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 6
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == False and c19['4'] == False and c19['5'] == False and c19['6'] == False and c19['7'] == True and c19['8'] == False and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 7
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == False and c19['4'] == False and c19['5'] == False and c19['6'] == False and c19['7'] == False and c19['8'] == True and c19['9'] == False:
        e19do = False
        solvednums[0][8] = 8
    elif e19do == True and c19['1'] == False and c19['2'] == False and c19['3'] == False and c19['4'] == False and c19['5'] == False and c19['6'] == False and c19['7'] == False and c19['8'] == False and c19['9'] == True:
        e19do = False
        solvednums[0][8] = 9
    else:
        if solvednums[0][8] == 1:
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c15['1'] = False
            c16['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c49['1'] = False
            c59['1'] = False
            c69['1'] = False
            c79['1'] = False
            c89['1'] = False
            c99['1'] = False
        elif solvednums[0][8] == 2:
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c15['2'] = False
            c16['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c49['2'] = False
            c59['2'] = False
            c69['2'] = False
            c79['2'] = False
            c89['2'] = False
            c99['2'] = False
        elif solvednums[0][8] == 3:
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c15['3'] = False
            c16['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c49['3'] = False
            c59['3'] = False
            c69['3'] = False
            c79['3'] = False
            c89['3'] = False
            c99['3'] = False
        elif solvednums[0][8] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c49['4'] = False
            c59['4'] = False
            c69['4'] = False
            c79['4'] = False
            c89['4'] = False
            c99['4'] = False
        elif solvednums[0][8] == 5:
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c15['5'] = False
            c16['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c49['5'] = False
            c59['5'] = False
            c69['5'] = False
            c79['5'] = False
            c89['5'] = False
            c99['5'] = False
        elif solvednums[0][8] == 6:
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c15['6'] = False
            c16['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c49['6'] = False
            c59['6'] = False
            c69['6'] = False
            c79['6'] = False
            c89['6'] = False
            c99['6'] = False
        elif solvednums[0][8] == 7:
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c15['7'] = False
            c16['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c49['7'] = False
            c59['7'] = False
            c69['7'] = False
            c79['7'] = False
            c89['7'] = False
            c99['7'] = False
        elif solvednums[0][8] == 8:
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c15['8'] = False
            c16['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c49['8'] = False
            c59['8'] = False
            c69['8'] = False
            c79['8'] = False
            c89['8'] = False
            c99['8'] = False
        elif solvednums[0][8] == 9:
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c15['9'] = False 
            c16['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c49['9'] = False
            c59['9'] = False
            c69['9'] = False
            c79['9'] = False   
            c89['9'] = False
            c99['9'] = False
    if puzzlenums[1][0] > 0 and e21do == True:
        solvednums[1][0] = puzzlenums[1][0]
        e21do = False
        sleep(1)
    elif e21do == True and c21['1'] == True and c21['2'] == False and c21['3'] == False and c21['4'] == False and c21['5'] == False and c21['6'] == False and c21['7'] == False and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 1
    elif e21do == True and c21['1'] == False and c21['2'] == True and c21['3'] == False and c21['4'] == False and c21['5'] == False and c21['6'] == False and c21['7'] == False and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 2
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == True and c21['4'] == False and c21['5'] == False and c21['6'] == False and c21['7'] == False and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 3
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == False and c21['4'] == True and c21['5'] == False and c21['6'] == False and c21['7'] == False and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 4
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == False and c21['4'] == False and c21['5'] == True and c21['6'] == False and c21['7'] == False and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 5
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == False and c21['4'] == False and c21['5'] == False and c21['6'] == True and c21['7'] == False and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 6
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == False and c21['4'] == False and c21['5'] == False and c21['6'] == False and c21['7'] == True and c21['8'] == False and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 7
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == False and c21['4'] == False and c21['5'] == False and c21['6'] == False and c21['7'] == False and c21['8'] == True and c21['9'] == False:
        e21do = False
        solvednums[1][0] = 8
    elif e21do == True and c21['1'] == False and c21['2'] == False and c21['3'] == False and c21['4'] == False and c21['5'] == False and c21['6'] == False and c21['7'] == False and c21['8'] == False and c21['9'] == True:
        e21do = False
        solvednums[1][0] = 9
    else:
        if solvednums[1][0] == 1:
            c21['1'] = False
            c21['2'] = False
            c21['3'] = False
            c21['4'] = False
            c21['5'] = False
            c21['6'] = False
            c21['7'] = False
            c21['8'] = False
            c21['9'] = False
            c22['1'] = False
            c23['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c41['1'] = False
            c51['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[1][0] == 2:
            c21['1'] = False
            c21['2'] = False
            c21['3'] = False
            c21['4'] = False
            c21['5'] = False
            c21['6'] = False
            c21['7'] = False
            c21['8'] = False
            c21['9'] = False
            c22['2'] = False
            c23['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c41['2'] = False
            c51['2'] = False
            c61['2'] = False
            c71['2'] = False
            c81['2'] = False
            c91['2'] = False
        elif solvednums[1][0] == 3:
            c22['3'] = False
            c23['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c41['3'] = False
            c51['3'] = False
            c61['3'] = False
            c71['3'] = False
            c81['3'] = False
            c91['3'] = False
        elif solvednums[1][0] == 4:
            c22['4'] = False
            c23['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c31['4'] = False
            c34['4'] = False
            c33['4'] = False
            c41['4'] = False
            c51['4'] = False
            c61['4'] = False
            c71['4'] = False
            c81['4'] = False
            c91['4'] = False
        elif solvednums[1][0] == 5:
            c22['5'] = False
            c23['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c41['5'] = False
            c51['5'] = False
            c61['5'] = False
            c71['5'] = False
            c81['5'] = False
            c91['5'] = False
        elif solvednums[1][0] == 6:
            c22['6'] = False
            c23['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c41['6'] = False
            c51['6'] = False
            c61['6'] = False
            c71['6'] = False
            c81['6'] = False
            c91['6'] = False
        elif solvednums[1][0] == 7:
            c22['7'] = False
            c23['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c41['7'] = False
            c51['7'] = False
            c61['7'] = False
            c71['7'] = False
            c81['7'] = False
            c91['7'] = False
        elif solvednums[1][0] == 8:
            c22['8'] = False
            c23['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c41['8'] = False
            c51['8'] = False
            c61['8'] = False
            c71['8'] = False
            c81['8'] = False
            c91['8'] = False
        elif solvednums[1][0] == 9:
            c22['9'] = False
            c23['9'] = False
            c24['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c41['9'] = False
            c51['9'] = False
            c61['9'] = False
            c71['9'] = False   
            c81['9'] = False
            c91['9'] = False
    if puzzlenums[1][1] > 0 and e22do == True:
        solvednums[1][1] = puzzlenums[1][1]
        e22do = False
        sleep(1)
    elif e22do == True and c22['1'] == True and c22['2'] == False and c22['3'] == False and c22['4'] == False and c22['5'] == False and c22['6'] == False and c22['7'] == False and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 1
    elif e22do == True and c22['1'] == False and c22['2'] == True and c22['3'] == False and c22['4'] == False and c22['5'] == False and c22['6'] == False and c22['7'] == False and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 2
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == True and c22['4'] == False and c22['5'] == False and c22['6'] == False and c22['7'] == False and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 3
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == False and c22['4'] == True and c22['5'] == False and c22['6'] == False and c22['7'] == False and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 4
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == False and c22['4'] == False and c22['5'] == True and c22['6'] == False and c22['7'] == False and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 5
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == False and c22['4'] == False and c22['5'] == False and c22['6'] == True and c22['7'] == False and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 6
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == False and c22['4'] == False and c22['5'] == False and c22['6'] == False and c22['7'] == True and c22['8'] == False and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 7
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == False and c22['4'] == False and c22['5'] == False and c22['6'] == False and c22['7'] == False and c22['8'] == True and c22['9'] == False:
        e22do = False
        solvednums[1][1] = 8
    elif e22do == True and c22['1'] == False and c22['2'] == False and c22['3'] == False and c22['4'] == False and c22['5'] == False and c22['6'] == False and c22['7'] == False and c22['8'] == False and c22['9'] == True:
        e22do = False
        solvednums[1][1] = 9
    else:
        if solvednums[1][1] == 1:
            c21['1'] = False
            c23['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c42['1'] = False
            c52['1'] = False
            c62['1'] = False
            c72['1'] = False
            c82['1'] = False
            c92['1'] = False
        elif solvednums[1][1] == 2:
            c21['2'] = False
            c23['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c42['2'] = False
            c52['2'] = False
            c62['2'] = False
            c72['2'] = False
            c82['2'] = False
            c92['2'] = False
        elif solvednums[1][1] == 3:
            c21['3'] = False
            c23['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c42['3'] = False
            c52['3'] = False
            c62['3'] = False
            c72['3'] = False
            c82['3'] = False
            c92['3'] = False
        elif solvednums[1][1] == 4:
            c21['4'] = False
            c23['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c31['4'] = False
            c34['4'] = False
            c33['4'] = False
            c42['4'] = False
            c52['4'] = False
            c62['4'] = False
            c72['4'] = False
            c82['4'] = False
            c92['4'] = False
        elif solvednums[1][1] == 5:
            c21['5'] = False
            c23['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c42['5'] = False
            c52['5'] = False
            c62['5'] = False
            c72['5'] = False
            c82['5'] = False
            c92['5'] = False
        elif solvednums[1][1] == 6:
            c21['6'] = False
            c23['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c42['6'] = False
            c52['6'] = False
            c62['6'] = False
            c72['6'] = False
            c82['6'] = False
            c92['6'] = False
        elif solvednums[1][1] == 7:
            c21['7'] = False
            c23['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c42['7'] = False
            c52['7'] = False
            c62['7'] = False
            c72['7'] = False
            c82['7'] = False
            c92['7'] = False
        elif solvednums[1][1] == 8:
            c21['8'] = False
            c23['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c42['8'] = False
            c52['8'] = False
            c62['8'] = False
            c72['8'] = False
            c82['8'] = False
            c92['8'] = False
        elif solvednums[1][1] == 9:
            c21['9'] = False
            c23['9'] = False
            c24['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c42['9'] = False
            c52['9'] = False
            c62['9'] = False
            c72['9'] = False   
            c82['9'] = False
            c92['9'] = False
    if puzzlenums[1][2] > 0 and e23do == True:
        solvednums[1][2] = puzzlenums[1][2]
        e23do = False
        sleep(1)
    elif e23do == True and c23['1'] == True and c23['2'] == False and c23['3'] == False and c23['4'] == False and c23['5'] == False and c23['6'] == False and c23['7'] == False and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 1
    elif e23do == True and c23['1'] == False and c23['2'] == True and c23['3'] == False and c23['4'] == False and c23['5'] == False and c23['6'] == False and c23['7'] == False and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 2
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == True and c23['4'] == False and c23['5'] == False and c23['6'] == False and c23['7'] == False and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 3
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == False and c23['4'] == True and c23['5'] == False and c23['6'] == False and c23['7'] == False and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 4
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == False and c23['4'] == False and c23['5'] == True and c23['6'] == False and c23['7'] == False and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 5
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == False and c23['4'] == False and c23['5'] == False and c23['6'] == True and c23['7'] == False and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 6
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == False and c23['4'] == False and c23['5'] == False and c23['6'] == False and c23['7'] == True and c23['8'] == False and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 7
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == False and c23['4'] == False and c23['5'] == False and c23['6'] == False and c23['7'] == False and c23['8'] == True and c23['9'] == False:
        e23do = False
        solvednums[1][2] = 8
    elif e23do == True and c23['1'] == False and c23['2'] == False and c23['3'] == False and c23['4'] == False and c23['5'] == False and c23['6'] == False and c23['7'] == False and c23['8'] == False and c23['9'] == True:
        e23do = False
        solvednums[1][2] = 9
    else:
        if solvednums[1][2] == 1:
            c21['1'] = False
            c22['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c43['1'] = False
            c53['1'] = False
            c63['1'] = False
            c73['1'] = False
            c83['1'] = False
            c93['1'] = False
        elif solvednums[1][2] == 2:
            c21['2'] = False
            c22['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c43['2'] = False
            c53['2'] = False
            c63['2'] = False
            c73['2'] = False
            c83['2'] = False
            c93['2'] = False
        elif solvednums[1][2] == 3:
            c21['3'] = False
            c22['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c43['3'] = False
            c53['3'] = False
            c63['3'] = False
            c73['3'] = False
            c83['3'] = False
            c93['3'] = False
        elif solvednums[1][2] == 4:
            c21['4'] = False
            c22['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c31['4'] = False
            c34['4'] = False
            c33['4'] = False
            c43['4'] = False
            c53['4'] = False
            c63['4'] = False
            c73['4'] = False
            c83['4'] = False
            c93['4'] = False
        elif solvednums[1][2] == 5:
            c21['5'] = False
            c22['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c43['5'] = False
            c53['5'] = False
            c63['5'] = False
            c73['5'] = False
            c83['5'] = False
            c93['5'] = False
        elif solvednums[1][2] == 6:
            c21['6'] = False
            c22['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c43['6'] = False
            c53['6'] = False
            c63['6'] = False
            c73['6'] = False
            c83['6'] = False
            c93['6'] = False
        elif solvednums[1][2] == 7:
            c21['7'] = False
            c22['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c43['7'] = False
            c53['7'] = False
            c63['7'] = False
            c73['7'] = False
            c83['7'] = False
            c93['7'] = False
        elif solvednums[1][2] == 8:
            c21['8'] = False
            c22['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c43['8'] = False
            c53['8'] = False
            c63['8'] = False
            c73['8'] = False
            c83['8'] = False
            c93['8'] = False
        elif solvednums[1][2] == 9:
            c21['9'] = False
            c22['9'] = False
            c24['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c43['9'] = False
            c53['9'] = False
            c63['9'] = False
            c73['9'] = False   
            c83['9'] = False
            c93['9'] = False
    if puzzlenums[1][3] > 0 and e24do == True:
        solvednums[1][3] = puzzlenums[1][3]
        e24do = False
        sleep(1)
    elif e24do == True and c24['1'] == True and c24['2'] == False and c24['3'] == False and c24['4'] == False and c24['5'] == False and c24['6'] == False and c24['7'] == False and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 1
    elif e24do == True and c24['1'] == False and c24['2'] == True and c24['3'] == False and c24['4'] == False and c24['5'] == False and c24['6'] == False and c24['7'] == False and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 2
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == True and c24['4'] == False and c24['5'] == False and c24['6'] == False and c24['7'] == False and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 3
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == False and c24['4'] == True and c24['5'] == False and c24['6'] == False and c24['7'] == False and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 4
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == False and c24['4'] == False and c24['5'] == True and c24['6'] == False and c24['7'] == False and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 5
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == False and c24['4'] == False and c24['5'] == False and c24['6'] == True and c24['7'] == False and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 6
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == False and c24['4'] == False and c24['5'] == False and c24['6'] == False and c24['7'] == True and c24['8'] == False and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 7
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == False and c24['4'] == False and c24['5'] == False and c24['6'] == False and c24['7'] == False and c24['8'] == True and c24['9'] == False:
        e24do = False
        solvednums[1][3] = 8
    elif e24do == True and c24['1'] == False and c24['2'] == False and c24['3'] == False and c24['4'] == False and c24['5'] == False and c24['6'] == False and c24['7'] == False and c24['8'] == False and c24['9'] == True:
        e24do = False
        solvednums[1][3] = 9
    else:
        if solvednums[1][3] == 1:
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c44['1'] = False
            c54['1'] = False
            c64['1'] = False
            c74['1'] = False
            c84['1'] = False
            c94['1'] = False
        elif solvednums[1][3] == 2:
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c44['2'] = False
            c54['2'] = False
            c64['2'] = False
            c74['2'] = False
            c84['2'] = False
            c94['2'] = False
        elif solvednums[1][3] == 3:
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c44['3'] = False
            c54['3'] = False
            c64['3'] = False
            c74['3'] = False
            c84['3'] = False
            c94['3'] = False
        elif solvednums[1][3] == 4:
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c44['4'] = False
            c54['4'] = False
            c64['4'] = False
            c74['4'] = False
            c84['4'] = False
            c94['4'] = False
        elif solvednums[1][3] == 5:
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c44['5'] = False
            c54['5'] = False
            c64['5'] = False
            c74['5'] = False
            c84['5'] = False
            c94['5'] = False
        elif solvednums[1][3] == 6:
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c44['6'] = False
            c54['6'] = False
            c64['6'] = False
            c74['6'] = False
            c84['6'] = False
            c94['6'] = False
        elif solvednums[1][3] == 7:
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c44['7'] = False
            c54['7'] = False
            c64['7'] = False
            c74['7'] = False
            c84['7'] = False
            c94['7'] = False
        elif solvednums[1][3] == 8:
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c44['8'] = False
            c54['8'] = False
            c64['8'] = False
            c74['8'] = False
            c84['8'] = False
            c94['8'] = False
        elif solvednums[1][3] == 9:
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c14['9'] = False
            c15['9'] = False
            c16['9'] = False
            c34['9'] = False
            c35['9'] = False
            c36['9'] = False
            c44['9'] = False
            c54['9'] = False
            c64['9'] = False
            c74['9'] = False   
            c84['9'] = False
            c94['9'] = False
    if puzzlenums[1][4] > 0 and e25do == True:
        solvednums[1][4] = puzzlenums[1][4]
        e25do = False
        sleep(1)
    elif e25do == True and c25['1'] == True and c25['2'] == False and c25['3'] == False and c25['4'] == False and c25['5'] == False and c25['6'] == False and c25['7'] == False and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 1
    elif e25do == True and c25['1'] == False and c25['2'] == True and c25['3'] == False and c25['4'] == False and c25['5'] == False and c25['6'] == False and c25['7'] == False and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 2
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == True and c25['4'] == False and c25['5'] == False and c25['6'] == False and c25['7'] == False and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 3
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == False and c25['4'] == True and c25['5'] == False and c25['6'] == False and c25['7'] == False and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 4
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == False and c25['4'] == False and c25['5'] == True and c25['6'] == False and c25['7'] == False and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 5
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == False and c25['4'] == False and c25['5'] == False and c25['6'] == True and c25['7'] == False and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 6
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == False and c25['4'] == False and c25['5'] == False and c25['6'] == False and c25['7'] == True and c25['8'] == False and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 7
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == False and c25['4'] == False and c25['5'] == False and c25['6'] == False and c25['7'] == False and c25['8'] == True and c25['9'] == False:
        e25do = False
        solvednums[1][4] = 8
    elif e25do == True and c25['1'] == False and c25['2'] == False and c25['3'] == False and c25['4'] == False and c25['5'] == False and c25['6'] == False and c25['7'] == False and c25['8'] == False and c25['9'] == True:
        e25do = False
        solvednums[1][4] = 9
    else:
        if solvednums[1][4] == 1:
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c45['1'] = False
            c55['1'] = False
            c65['1'] = False
            c75['1'] = False
            c85['1'] = False
            c95['1'] = False
        elif solvednums[1][4] == 2:
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c45['2'] = False
            c55['2'] = False
            c65['2'] = False
            c75['2'] = False
            c85['2'] = False
            c95['2'] = False
        elif solvednums[1][4] == 3:
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c45['3'] = False
            c55['3'] = False
            c65['3'] = False
            c75['3'] = False
            c85['3'] = False
            c95['3'] = False
        elif solvednums[1][4] == 4:
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c45['4'] = False
            c55['4'] = False
            c65['4'] = False
            c75['4'] = False
            c85['4'] = False
            c95['4'] = False
        elif solvednums[1][4] == 5:
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c45['5'] = False
            c55['5'] = False
            c65['5'] = False
            c75['5'] = False
            c85['5'] = False
            c95['5'] = False
        elif solvednums[1][4] == 6:
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c45['6'] = False
            c55['6'] = False
            c65['6'] = False
            c75['6'] = False
            c85['6'] = False
            c95['6'] = False
        elif solvednums[1][4] == 7:
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c45['7'] = False
            c55['7'] = False
            c65['7'] = False
            c75['7'] = False
            c85['7'] = False
            c95['7'] = False
        elif solvednums[1][4] == 8:
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c45['8'] = False
            c55['8'] = False
            c65['8'] = False
            c75['8'] = False
            c85['8'] = False
            c95['8'] = False
        elif solvednums[1][4] == 9:
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c14['9'] = False
            c15['9'] = False
            c16['9'] = False
            c34['9'] = False
            c35['9'] = False
            c36['9'] = False
            c45['9'] = False
            c55['9'] = False
            c65['9'] = False
            c75['9'] = False   
            c85['9'] = False
            c95['9'] = False
    if puzzlenums[1][5] > 0 and e26do == True:
        solvednums[1][5] = puzzlenums[1][5]
        e26do = False
        sleep(1)
    elif e26do == True and c26['1'] == True and c26['2'] == False and c26['3'] == False and c26['4'] == False and c26['5'] == False and c26['6'] == False and c26['7'] == False and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 1
    elif e26do == True and c26['1'] == False and c26['2'] == True and c26['3'] == False and c26['4'] == False and c26['5'] == False and c26['6'] == False and c26['7'] == False and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 2
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == True and c26['4'] == False and c26['5'] == False and c26['6'] == False and c26['7'] == False and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 3
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == False and c26['4'] == True and c26['5'] == False and c26['6'] == False and c26['7'] == False and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][6] = 4
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == False and c26['4'] == False and c26['5'] == True and c26['6'] == False and c26['7'] == False and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 5
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == False and c26['4'] == False and c26['5'] == False and c26['6'] == True and c26['7'] == False and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 6
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == False and c26['4'] == False and c26['5'] == False and c26['6'] == False and c26['7'] == True and c26['8'] == False and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 7
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == False and c26['4'] == False and c26['5'] == False and c26['6'] == False and c26['7'] == False and c26['8'] == True and c26['9'] == False:
        e26do = False
        solvednums[1][5] = 8
    elif e26do == True and c26['1'] == False and c26['2'] == False and c26['3'] == False and c26['4'] == False and c26['5'] == False and c26['6'] == False and c26['7'] == False and c26['8'] == False and c26['9'] == True:
        e26do = False
        solvednums[1][5] = 9     
    else:
        if solvednums[1][5] == 1:
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c46['1'] = False
            c56['1'] = False
            c66['1'] = False
            c76['1'] = False
            c86['1'] = False
            c96['1'] = False
        elif solvednums[1][5] == 2: 
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c46['2'] = False
            c56['2'] = False
            c66['2'] = False
            c76['2'] = False
            c86['2'] = False
            c96['2'] = False
        elif solvednums[1][5] == 3:
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c46['3'] = False
            c56['3'] = False
            c66['3'] = False
            c76['3'] = False
            c86['3'] = False
            c96['3'] = False
        elif solvednums[1][5] == 4:
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c46['4'] = False
            c56['4'] = False
            c66['4'] = False
            c76['4'] = False
            c86['4'] = False
            c96['4'] = False
        elif solvednums[1][5] == 5:
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c46['5'] = False
            c56['5'] = False
            c66['5'] = False
            c76['5'] = False
            c86['5'] = False
            c96['5'] = False
        elif solvednums[1][5] == 6:
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c46['6'] = False
            c56['6'] = False
            c66['6'] = False
            c76['6'] = False
            c86['6'] = False
            c96['6'] = False
        elif solvednums[1][5] == 7:
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c46['7'] = False
            c56['7'] = False
            c66['7'] = False
            c76['7'] = False
            c86['7'] = False
            c96['7'] = False
        elif solvednums[1][5] == 8:
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c46['8'] = False
            c56['8'] = False
            c66['8'] = False
            c76['8'] = False
            c86['8'] = False
            c96['8'] = False
        elif solvednums[1][5] == 9:
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c14['9'] = False
            c15['9'] = False
            c16['9'] = False
            c34['9'] = False
            c35['9'] = False
            c36['9'] = False
            c46['9'] = False
            c56['9'] = False
            c66['9'] = False
            c76['9'] = False   
            c86['9'] = False
            c96['9'] = False
    if puzzlenums[1][6] > 0 and e27do == True:
        solvednums[1][6] = puzzlenums[1][6]
        e27do = False
        sleep(1)
    elif e27do == True and c27['1'] == True and c27['2'] == False and c27['3'] == False and c27['4'] == False and c27['5'] == False and c27['6'] == False and c27['7'] == False and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 1
    elif e27do == True and c27['1'] == False and c27['2'] == True and c27['3'] == False and c27['4'] == False and c27['5'] == False and c27['6'] == False and c27['7'] == False and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 2
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == True and c27['4'] == False and c27['5'] == False and c27['6'] == False and c27['7'] == False and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 3
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == False and c27['4'] == True and c27['5'] == False and c27['6'] == False and c27['7'] == False and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 4
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == False and c27['4'] == False and c27['5'] == True and c27['6'] == False and c27['7'] == False and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 5
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == False and c27['4'] == False and c27['5'] == False and c27['6'] == True and c27['7'] == False and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 6
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == False and c27['4'] == False and c27['5'] == False and c27['6'] == False and c27['7'] == True and c27['8'] == False and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 7
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == False and c27['4'] == False and c27['5'] == False and c27['6'] == False and c27['7'] == False and c27['8'] == True and c27['9'] == False:
        e27do = False
        solvednums[1][6] = 8
    elif e27do == True and c27['1'] == False and c27['2'] == False and c27['3'] == False and c27['4'] == False and c27['5'] == False and c27['6'] == False and c27['7'] == False and c27['8'] == False and c27['9'] == True:
        e27do = False
        solvednums[1][6] = 9
    else:
        if solvednums[1][6] == 1:
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c47['1'] = False
            c57['1'] = False
            c67['1'] = False
            c77['1'] = False
            c87['1'] = False
            c97['1'] = False
        elif solvednums[1][6] == 2:
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c47['2'] = False
            c57['2'] = False
            c67['2'] = False
            c77['2'] = False
            c87['2'] = False
            c97['2'] = False
        elif solvednums[1][6] == 3:
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c47['3'] = False
            c57['3'] = False
            c67['3'] = False
            c77['3'] = False
            c87['3'] = False
            c97['3'] = False
        elif solvednums[1][6] == 4:
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c47['4'] = False
            c57['4'] = False
            c67['4'] = False
            c77['4'] = False
            c87['4'] = False
            c97['4'] = False
        elif solvednums[1][6] == 5:
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c47['5'] = False
            c57['5'] = False
            c67['5'] = False
            c77['5'] = False
            c87['5'] = False
            c97['5'] = False
        elif solvednums[1][6] == 6:
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c47['6'] = False
            c57['6'] = False
            c67['6'] = False
            c77['6'] = False
            c87['6'] = False
            c97['6'] = False
        elif solvednums[1][6] == 7:
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c47['7'] = False
            c57['7'] = False
            c67['7'] = False
            c77['7'] = False
            c87['7'] = False
            c97['7'] = False
        elif solvednums[1][6] == 8:
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c47['8'] = False
            c57['8'] = False
            c67['8'] = False
            c77['8'] = False
            c87['8'] = False
            c97['8'] = False
        elif solvednums[1][6] == 9:
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c47['9'] = False
            c57['9'] = False
            c67['9'] = False
            c77['9'] = False   
            c87['9'] = False
            c97['9'] = False
    if puzzlenums[1][7] > 0 and e28do == True:
        solvednums[1][7] = puzzlenums[1][7]
        e28do = False
        sleep(1)
    elif e28do == True and c28['1'] == True and c28['2'] == False and c28['3'] == False and c28['4'] == False and c28['5'] == False and c28['6'] == False and c28['7'] == False and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 1
    elif e28do == True and c28['1'] == False and c28['2'] == True and c28['3'] == False and c28['4'] == False and c28['5'] == False and c28['6'] == False and c28['7'] == False and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 2
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == True and c28['4'] == False and c28['5'] == False and c28['6'] == False and c28['7'] == False and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 3
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == False and c28['4'] == True and c28['5'] == False and c28['6'] == False and c28['7'] == False and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 4
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == False and c28['4'] == False and c28['5'] == True and c28['6'] == False and c28['7'] == False and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 5
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == False and c28['4'] == False and c28['5'] == False and c28['6'] == True and c28['7'] == False and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 6
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == False and c28['4'] == False and c28['5'] == False and c28['6'] == False and c28['7'] == True and c28['8'] == False and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 7
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == False and c28['4'] == False and c28['5'] == False and c28['6'] == False and c28['7'] == False and c28['8'] == True and c28['9'] == False:
        e28do = False
        solvednums[1][7] = 8
    elif e28do == True and c28['1'] == False and c28['2'] == False and c28['3'] == False and c28['4'] == False and c28['5'] == False and c28['6'] == False and c28['7'] == False and c28['8'] == False and c28['9'] == True:
        e28do = False
        solvednums[1][7] = 9
    else:
        if solvednums[1][7] == 1:
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c48['1'] = False
            c58['1'] = False
            c68['1'] = False
            c78['1'] = False
            c88['1'] = False
            c98['1'] = False
        elif solvednums[1][7] == 2:
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c48['2'] = False
            c58['2'] = False
            c68['2'] = False
            c78['2'] = False
            c88['2'] = False
            c98['2'] = False
        elif solvednums[1][7] == 3:
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c48['3'] = False
            c58['3'] = False
            c68['3'] = False
            c78['3'] = False
            c88['3'] = False
            c98['3'] = False
        elif solvednums[1][7] == 4:
            c21['4'] = False
            c22['4'] = False
            c23['4'] = False
            c25['4'] = False
            c26['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c48['4'] = False
            c58['4'] = False
            c68['4'] = False
            c78['4'] = False
            c88['4'] = False
            c98['4'] = False
        elif solvednums[1][7] == 5:
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c39['5'] = False
            c38['5'] = False
            c39['5'] = False
            c48['5'] = False
            c58['5'] = False
            c68['5'] = False
            c78['5'] = False
            c88['5'] = False
            c98['5'] = False
        elif solvednums[1][7] == 6:
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c48['6'] = False
            c58['6'] = False
            c68['6'] = False
            c78['6'] = False
            c88['6'] = False
            c98['6'] = False
        elif solvednums[1][7] == 7:
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c48['7'] = False
            c58['7'] = False
            c68['7'] = False
            c78['7'] = False
            c88['7'] = False
            c98['7'] = False
        elif solvednums[1][7] == 8:
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c48['8'] = False
            c58['8'] = False
            c68['8'] = False
            c78['8'] = False
            c88['8'] = False
            c98['8'] = False
        elif solvednums[1][7] == 9:
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c48['9'] = False
            c58['9'] = False
            c68['9'] = False
            c78['9'] = False   
            c88['9'] = False
            c98['9'] = False
    if puzzlenums[1][8] > 0 and e29do == True:
        solvednums[1][8] = puzzlenums[1][8]
        e29do = False
        sleep(1)
    elif e29do == True and c29['1'] == True and c29['2'] == False and c29['3'] == False and c29['4'] == False and c29['5'] == False and c29['6'] == False and c29['7'] == False and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 1
    elif e29do == True and c29['1'] == False and c29['2'] == True and c29['3'] == False and c29['4'] == False and c29['5'] == False and c29['6'] == False and c29['7'] == False and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 2
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == True and c29['4'] == False and c29['5'] == False and c29['6'] == False and c29['7'] == False and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 3
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == False and c29['4'] == True and c29['5'] == False and c29['6'] == False and c29['7'] == False and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 4
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == False and c29['4'] == False and c29['5'] == True and c29['6'] == False and c29['7'] == False and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 5
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == False and c29['4'] == False and c29['5'] == False and c29['6'] == True and c29['7'] == False and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 6
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == False and c29['4'] == False and c29['5'] == False and c29['6'] == False and c29['7'] == True and c29['8'] == False and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 7
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == False and c29['4'] == False and c29['5'] == False and c29['6'] == False and c29['7'] == False and c29['8'] == True and c29['9'] == False:
        e29do = False
        solvednums[1][8] = 8
    elif e29do == True and c29['1'] == False and c29['2'] == False and c29['3'] == False and c29['4'] == False and c29['5'] == False and c29['6'] == False and c29['7'] == False and c29['8'] == False and c29['9'] == True:
        e29do = False
        solvednums[1][8] = 9
    else:
        if solvednums[1][8] == 1:
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c25['1'] = False
            c26['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c49['1'] = False
            c59['1'] = False
            c69['1'] = False
            c79['1'] = False
            c89['1'] = False
            c99['1'] = False
        elif solvednums[1][8] == 2:
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c25['2'] = False
            c26['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c49['2'] = False
            c59['2'] = False
            c69['2'] = False
            c79['2'] = False
            c89['2'] = False
            c99['2'] = False
        elif solvednums[1][8] == 3:
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c25['3'] = False
            c26['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c49['3'] = False
            c59['3'] = False
            c69['3'] = False
            c79['3'] = False
            c89['3'] = False
            c99['3'] = False
        elif solvednums[1][8] == 4:
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c15['4'] = False
            c16['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c49['4'] = False
            c59['4'] = False
            c69['4'] = False
            c79['4'] = False
            c89['4'] = False
            c99['4'] = False
        elif solvednums[1][8] == 5:
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c25['5'] = False
            c26['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c49['5'] = False
            c59['5'] = False
            c69['5'] = False
            c79['5'] = False
            c89['5'] = False
            c99['5'] = False
        elif solvednums[1][8] == 6:
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c25['6'] = False
            c26['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c49['6'] = False
            c59['6'] = False
            c69['6'] = False
            c79['6'] = False
            c89['6'] = False
            c99['6'] = False
        elif solvednums[1][8] == 7:
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c25['7'] = False
            c26['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c49['7'] = False
            c59['7'] = False
            c69['7'] = False
            c79['7'] = False
            c89['7'] = False
            c99['7'] = False
        elif solvednums[1][8] == 8:
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c25['8'] = False
            c26['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c49['8'] = False
            c59['8'] = False
            c69['8'] = False
            c79['8'] = False
            c89['8'] = False
            c99['8'] = False
        elif solvednums[1][8] == 9:
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c25['9'] = False 
            c26['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c49['9'] = False
            c59['9'] = False
            c69['9'] = False
            c79['9'] = False   
            c89['9'] = False
            c99['9'] = False
    if puzzlenums[2][0] > 0 and e31do == True:
        solvednums[2][0] = puzzlenums[2][0]
        e31do = False
        sleep(1)
    elif e31do == True and c31['1'] == True and c31['2'] == False and c31['3'] == False and c31['4'] == False and c31['5'] == False and c31['6'] == False and c31['7'] == False and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 1
    elif e31do == True and c31['1'] == False and c31['2'] == True and c31['3'] == False and c31['4'] == False and c31['5'] == False and c31['6'] == False and c31['7'] == False and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 2
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == True and c31['4'] == False and c31['5'] == False and c31['6'] == False and c31['7'] == False and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 3
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == False and c31['4'] == True and c31['5'] == False and c31['6'] == False and c31['7'] == False and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 4
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == False and c31['4'] == False and c31['5'] == True and c31['6'] == False and c31['7'] == False and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 5
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == False and c31['4'] == False and c31['5'] == False and c31['6'] == True and c31['7'] == False and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 6
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == False and c31['4'] == False and c31['5'] == False and c31['6'] == False and c31['7'] == True and c31['8'] == False and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 7
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == False and c31['4'] == False and c31['5'] == False and c31['6'] == False and c31['7'] == False and c31['8'] == True and c31['9'] == False:
        e31do = False
        solvednums[2][0] = 8
    elif e31do == True and c31['1'] == False and c31['2'] == False and c31['3'] == False and c31['4'] == False and c31['5'] == False and c31['6'] == False and c31['7'] == False and c31['8'] == False and c31['9'] == True:
        e31do = False
        solvednums[2][0] = 9
    else:
        if solvednums[2][0] == 1:
            c31['1'] = False
            c31['2'] = False
            c31['3'] = False
            c31['4'] = False
            c31['5'] = False
            c31['6'] = False
            c31['7'] = False
            c31['8'] = False
            c31['9'] = False
            c32['1'] = False
            c33['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c41['1'] = False
            c51['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[2][0] == 2:
            c31['1'] = False
            c31['2'] = False
            c31['3'] = False
            c31['4'] = False
            c31['5'] = False
            c31['6'] = False
            c31['7'] = False
            c31['8'] = False
            c31['9'] = False
            c32['2'] = False
            c33['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c41['2'] = False
            c51['2'] = False
            c61['2'] = False
            c71['2'] = False
            c81['2'] = False
            c91['2'] = False
        elif solvednums[2][0] == 3:
            c32['3'] = False
            c33['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c41['3'] = False
            c51['3'] = False
            c61['3'] = False
            c71['3'] = False
            c81['3'] = False
            c91['3'] = False
        elif solvednums[2][0] == 4:
            c32['4'] = False
            c33['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c21['4'] = False
            c24['4'] = False
            c23['4'] = False
            c41['4'] = False
            c51['4'] = False
            c61['4'] = False
            c71['4'] = False
            c81['4'] = False
            c91['4'] = False
        elif solvednums[2][0] == 5:
            c32['5'] = False
            c33['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c41['5'] = False
            c51['5'] = False
            c61['5'] = False
            c71['5'] = False
            c81['5'] = False
            c91['5'] = False
        elif solvednums[2][0] == 6:
            c32['6'] = False
            c33['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c41['6'] = False
            c51['6'] = False
            c61['6'] = False
            c71['6'] = False
            c81['6'] = False
            c91['6'] = False
        elif solvednums[2][0] == 7:
            c32['7'] = False
            c33['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c41['7'] = False
            c51['7'] = False
            c61['7'] = False
            c71['7'] = False
            c81['7'] = False
            c91['7'] = False
        elif solvednums[2][0] == 8:
            c32['8'] = False
            c33['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c41['8'] = False
            c51['8'] = False
            c61['8'] = False
            c71['8'] = False
            c81['8'] = False
            c91['8'] = False
        elif solvednums[2][0] == 9:
            c32['9'] = False
            c33['9'] = False
            c34['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c41['9'] = False
            c51['9'] = False
            c61['9'] = False
            c71['9'] = False   
            c81['9'] = False
            c91['9'] = False
    if puzzlenums[2][2] > 0 and e32do == True:
        solvednums[2][2] = puzzlenums[2][2]
        e32do = False
        sleep(1)
    elif e32do == True and c32['1'] == True and c32['2'] == False and c32['3'] == False and c32['4'] == False and c32['5'] == False and c32['6'] == False and c32['7'] == False and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 1
    elif e32do == True and c32['1'] == False and c32['2'] == True and c32['3'] == False and c32['4'] == False and c32['5'] == False and c32['6'] == False and c32['7'] == False and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 2
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == True and c32['4'] == False and c32['5'] == False and c32['6'] == False and c32['7'] == False and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 3
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == False and c32['4'] == True and c32['5'] == False and c32['6'] == False and c32['7'] == False and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 4
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == False and c32['4'] == False and c32['5'] == True and c32['6'] == False and c32['7'] == False and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 5
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == False and c32['4'] == False and c32['5'] == False and c32['6'] == True and c32['7'] == False and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 6
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == False and c32['4'] == False and c32['5'] == False and c32['6'] == False and c32['7'] == True and c32['8'] == False and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 7
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == False and c32['4'] == False and c32['5'] == False and c32['6'] == False and c32['7'] == False and c32['8'] == True and c32['9'] == False:
        e32do = False
        solvednums[2][2] = 8
    elif e32do == True and c32['1'] == False and c32['2'] == False and c32['3'] == False and c32['4'] == False and c32['5'] == False and c32['6'] == False and c32['7'] == False and c32['8'] == False and c32['9'] == True:
        e32do = False
        solvednums[2][2] = 9
    else:
        if solvednums[2][2] == 1:
            c31['1'] = False
            c33['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c42['1'] = False
            c52['1'] = False
            c62['1'] = False
            c72['1'] = False
            c82['1'] = False
            c92['1'] = False
        elif solvednums[2][2] == 2:
            c31['2'] = False
            c33['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c42['2'] = False
            c52['2'] = False
            c62['2'] = False
            c72['2'] = False
            c82['2'] = False
            c92['2'] = False
        elif solvednums[2][2] == 3:
            c31['3'] = False
            c33['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c42['3'] = False
            c52['3'] = False
            c62['3'] = False
            c72['3'] = False
            c82['3'] = False
            c92['3'] = False
        elif solvednums[2][2] == 4:
            c31['4'] = False
            c33['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c21['4'] = False
            c24['4'] = False
            c23['4'] = False
            c42['4'] = False
            c52['4'] = False
            c62['4'] = False
            c72['4'] = False
            c82['4'] = False
            c92['4'] = False
        elif solvednums[2][2] == 5:
            c31['5'] = False
            c33['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c42['5'] = False
            c52['5'] = False
            c62['5'] = False
            c72['5'] = False
            c82['5'] = False
            c92['5'] = False
        elif solvednums[2][2] == 6:
            c31['6'] = False
            c33['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c42['6'] = False
            c52['6'] = False
            c62['6'] = False
            c72['6'] = False
            c82['6'] = False
            c92['6'] = False
        elif solvednums[2][2] == 7:
            c31['7'] = False
            c33['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c42['7'] = False
            c52['7'] = False
            c62['7'] = False
            c72['7'] = False
            c82['7'] = False
            c92['7'] = False
        elif solvednums[2][2] == 8:
            c31['8'] = False
            c33['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c28['8'] = False
            c22['8'] = False
            c23['8'] = False
            c42['8'] = False
            c52['8'] = False
            c62['8'] = False
            c72['8'] = False
            c82['8'] = False
            c92['8'] = False
        elif solvednums[2][2] == 9:
            c31['9'] = False
            c33['9'] = False
            c34['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c42['9'] = False
            c52['9'] = False
            c62['9'] = False
            c72['9'] = False   
            c82['9'] = False
            c92['9'] = False
    if puzzlenums[2][2] > 0 and e33do == True:
        solvednums[2][2] = puzzlenums[2][2]
        e33do = False
        sleep(1)
    elif e33do == True and c33['1'] == True and c33['2'] == False and c33['3'] == False and c33['4'] == False and c33['5'] == False and c33['6'] == False and c33['7'] == False and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 1
    elif e33do == True and c33['1'] == False and c33['2'] == True and c33['3'] == False and c33['4'] == False and c33['5'] == False and c33['6'] == False and c33['7'] == False and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 2
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == True and c33['4'] == False and c33['5'] == False and c33['6'] == False and c33['7'] == False and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 3
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == False and c33['4'] == True and c33['5'] == False and c33['6'] == False and c33['7'] == False and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 4
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == False and c33['4'] == False and c33['5'] == True and c33['6'] == False and c33['7'] == False and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 5
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == False and c33['4'] == False and c33['5'] == False and c33['6'] == True and c33['7'] == False and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 6
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == False and c33['4'] == False and c33['5'] == False and c33['6'] == False and c33['7'] == True and c33['8'] == False and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 7
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == False and c33['4'] == False and c33['5'] == False and c33['6'] == False and c33['7'] == False and c33['8'] == True and c33['9'] == False:
        e33do = False
        solvednums[2][2] = 8
    elif e33do == True and c33['1'] == False and c33['2'] == False and c33['3'] == False and c33['4'] == False and c33['5'] == False and c33['6'] == False and c33['7'] == False and c33['8'] == False and c33['9'] == True:
        e33do = False
        solvednums[2][2] = 9
    else:
        if solvednums[2][2] == 1:
            c31['1'] = False
            c32['1'] = False
            c34['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c11['1'] = False
            c12['1'] = False
            c13['1'] = False
            c21['1'] = False
            c22['1'] = False
            c23['1'] = False
            c43['1'] = False
            c53['1'] = False
            c63['1'] = False
            c73['1'] = False
            c83['1'] = False
            c93['1'] = False
        elif solvednums[2][2] == 2:
            c31['2'] = False
            c32['2'] = False
            c34['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c11['2'] = False
            c12['2'] = False
            c13['2'] = False
            c21['2'] = False
            c22['2'] = False
            c23['2'] = False
            c43['2'] = False
            c53['2'] = False
            c63['2'] = False
            c73['2'] = False
            c83['2'] = False
            c93['2'] = False
        elif solvednums[2][2] == 3:
            c31['3'] = False
            c32['3'] = False
            c34['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c11['3'] = False
            c12['3'] = False
            c13['3'] = False
            c21['3'] = False
            c22['3'] = False
            c23['3'] = False
            c43['3'] = False
            c53['3'] = False
            c63['3'] = False
            c73['3'] = False
            c83['3'] = False
            c93['3'] = False
        elif solvednums[2][2] == 4:
            c31['4'] = False
            c32['4'] = False
            c34['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c11['4'] = False
            c12['4'] = False
            c13['4'] = False
            c21['4'] = False
            c34['4'] = False
            c23['4'] = False
            c43['4'] = False
            c53['4'] = False
            c63['4'] = False
            c73['4'] = False
            c83['4'] = False
            c93['4'] = False
        elif solvednums[2][2] == 5:
            c31['5'] = False
            c32['5'] = False
            c34['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c11['5'] = False
            c12['5'] = False
            c13['5'] = False
            c21['5'] = False
            c22['5'] = False
            c23['5'] = False
            c43['5'] = False
            c53['5'] = False
            c63['5'] = False
            c73['5'] = False
            c83['5'] = False
            c93['5'] = False
        elif solvednums[2][2] == 6:
            c31['6'] = False
            c32['6'] = False
            c34['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c11['6'] = False
            c12['6'] = False
            c13['6'] = False
            c21['6'] = False
            c22['6'] = False
            c23['6'] = False
            c43['6'] = False
            c53['6'] = False
            c63['6'] = False
            c73['6'] = False
            c83['6'] = False
            c93['6'] = False
        elif solvednums[2][2] == 7:
            c31['7'] = False
            c32['7'] = False
            c34['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c11['7'] = False
            c12['7'] = False
            c13['7'] = False
            c21['7'] = False
            c22['7'] = False
            c23['7'] = False
            c43['7'] = False
            c53['7'] = False
            c63['7'] = False
            c73['7'] = False
            c83['7'] = False
            c93['7'] = False
        elif solvednums[2][2] == 8:
            c31['8'] = False
            c32['8'] = False
            c34['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c11['8'] = False
            c12['8'] = False
            c13['8'] = False
            c21['8'] = False
            c22['8'] = False
            c23['8'] = False
            c43['8'] = False
            c53['8'] = False
            c63['8'] = False
            c73['8'] = False
            c83['8'] = False
            c93['8'] = False
        elif solvednums[2][2] == 9:
            c31['9'] = False
            c32['9'] = False
            c34['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c11['9'] = False
            c12['9'] = False
            c13['9'] = False
            c21['9'] = False
            c22['9'] = False
            c23['9'] = False
            c43['9'] = False
            c53['9'] = False
            c63['9'] = False
            c73['9'] = False   
            c83['9'] = False
            c93['9'] = False
    if puzzlenums[2][3] > 0 and e34do == True:
        solvednums[2][3] = puzzlenums[2][3]
        e34do = False
        sleep(1)
    elif e34do == True and c34['1'] == True and c34['2'] == False and c34['3'] == False and c34['4'] == False and c34['5'] == False and c34['6'] == False and c34['7'] == False and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 1
    elif e34do == True and c34['1'] == False and c34['2'] == True and c34['3'] == False and c34['4'] == False and c34['5'] == False and c34['6'] == False and c34['7'] == False and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 2
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == True and c34['4'] == False and c34['5'] == False and c34['6'] == False and c34['7'] == False and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 3
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == False and c34['4'] == True and c34['5'] == False and c34['6'] == False and c34['7'] == False and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 4
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == False and c34['4'] == False and c34['5'] == True and c34['6'] == False and c34['7'] == False and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 5
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == False and c34['4'] == False and c34['5'] == False and c34['6'] == True and c34['7'] == False and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 6
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == False and c34['4'] == False and c34['5'] == False and c34['6'] == False and c34['7'] == True and c34['8'] == False and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 7
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == False and c34['4'] == False and c34['5'] == False and c34['6'] == False and c34['7'] == False and c34['8'] == True and c34['9'] == False:
        e34do = False
        solvednums[2][3] = 8
    elif e34do == True and c34['1'] == False and c34['2'] == False and c34['3'] == False and c34['4'] == False and c34['5'] == False and c34['6'] == False and c34['7'] == False and c34['8'] == False and c34['9'] == True:
        e34do = False
        solvednums[2][3] = 9
    else:
        if solvednums[2][3] == 1:
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c24['1'] = False
            c25['1'] = False
            c36['1'] = False
            c44['1'] = False
            c54['1'] = False
            c64['1'] = False
            c74['1'] = False
            c84['1'] = False
            c94['1'] = False
        elif solvednums[2][3] == 2:
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c24['2'] = False
            c25['2'] = False
            c36['2'] = False
            c44['2'] = False
            c54['2'] = False
            c64['2'] = False
            c74['2'] = False
            c84['2'] = False
            c94['2'] = False
        elif solvednums[2][3] == 3:
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c24['3'] = False
            c25['3'] = False
            c36['3'] = False
            c44['3'] = False
            c54['3'] = False
            c64['3'] = False
            c74['3'] = False
            c84['3'] = False
            c94['3'] = False
        elif solvednums[2][3] == 4:
            c31['4'] = False
            c32['4'] = False
            c33['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c24['4'] = False
            c25['4'] = False
            c36['4'] = False
            c44['4'] = False
            c54['4'] = False
            c64['4'] = False
            c74['4'] = False
            c84['4'] = False
            c94['4'] = False
        elif solvednums[2][3] == 5:
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c24['5'] = False
            c25['5'] = False
            c36['5'] = False
            c44['5'] = False
            c54['5'] = False
            c64['5'] = False
            c74['5'] = False
            c84['5'] = False
            c94['5'] = False
        elif solvednums[2][3] == 6:
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c24['6'] = False
            c25['6'] = False
            c36['6'] = False
            c44['6'] = False
            c54['6'] = False
            c64['6'] = False
            c74['6'] = False
            c84['6'] = False
            c94['6'] = False
        elif solvednums[2][3] == 7:
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c24['7'] = False
            c25['7'] = False
            c36['7'] = False
            c44['7'] = False
            c54['7'] = False
            c64['7'] = False
            c74['7'] = False
            c84['7'] = False
            c94['7'] = False
        elif solvednums[2][3] == 8:
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c24['8'] = False
            c25['8'] = False
            c36['8'] = False
            c44['8'] = False
            c54['8'] = False
            c64['8'] = False
            c74['8'] = False
            c84['8'] = False
            c94['8'] = False
        elif solvednums[2][3] == 9:
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c14['9'] = False
            c15['9'] = False
            c16['9'] = False
            c24['9'] = False
            c25['9'] = False
            c36['9'] = False
            c44['9'] = False
            c54['9'] = False
            c64['9'] = False
            c74['9'] = False   
            c84['9'] = False
            c94['9'] = False
    if puzzlenums[2][4] > 0 and e35do == True:
        solvednums[2][4] = puzzlenums[2][4]
        e35do = False
        sleep(1)
    elif e35do == True and c35['1'] == True and c35['2'] == False and c35['3'] == False and c35['4'] == False and c35['5'] == False and c35['6'] == False and c35['7'] == False and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 1
    elif e35do == True and c35['1'] == False and c35['2'] == True and c35['3'] == False and c35['4'] == False and c35['5'] == False and c35['6'] == False and c35['7'] == False and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 2
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == True and c35['4'] == False and c35['5'] == False and c35['6'] == False and c35['7'] == False and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 3
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == False and c35['4'] == True and c35['5'] == False and c35['6'] == False and c35['7'] == False and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 4
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == False and c35['4'] == False and c35['5'] == True and c35['6'] == False and c35['7'] == False and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 5
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == False and c35['4'] == False and c35['5'] == False and c35['6'] == True and c35['7'] == False and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 6
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == False and c35['4'] == False and c35['5'] == False and c35['6'] == False and c35['7'] == True and c35['8'] == False and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 7
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == False and c35['4'] == False and c35['5'] == False and c35['6'] == False and c35['7'] == False and c35['8'] == True and c35['9'] == False:
        e35do = False
        solvednums[2][4] = 8
    elif e35do == True and c35['1'] == False and c35['2'] == False and c35['3'] == False and c35['4'] == False and c35['5'] == False and c35['6'] == False and c35['7'] == False and c35['8'] == False and c35['9'] == True:
        e35do = False
        solvednums[2][4] = 9
    else:
        if solvednums[2][4] == 1:
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c24['1'] = False
            c25['1'] = False
            c36['1'] = False
            c45['1'] = False
            c55['1'] = False
            c65['1'] = False
            c75['1'] = False
            c85['1'] = False
            c95['1'] = False
        elif solvednums[2][4] == 2:
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c24['2'] = False
            c25['2'] = False
            c36['2'] = False
            c45['2'] = False
            c55['2'] = False
            c65['2'] = False
            c75['2'] = False
            c85['2'] = False
            c95['2'] = False
        elif solvednums[2][4] == 3:
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c24['3'] = False
            c25['3'] = False
            c36['3'] = False
            c45['3'] = False
            c55['3'] = False
            c65['3'] = False
            c75['3'] = False
            c85['3'] = False
            c95['3'] = False
        elif solvednums[2][4] == 4:
            c31['4'] = False
            c32['4'] = False
            c33['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c24['4'] = False
            c25['4'] = False
            c36['4'] = False
            c45['4'] = False
            c55['4'] = False
            c65['4'] = False
            c75['4'] = False
            c85['4'] = False
            c95['4'] = False
        elif solvednums[2][4] == 5:
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c24['5'] = False
            c25['5'] = False
            c36['5'] = False
            c45['5'] = False
            c55['5'] = False
            c65['5'] = False
            c75['5'] = False
            c85['5'] = False
            c95['5'] = False
        elif solvednums[2][4] == 6:
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c24['6'] = False
            c25['6'] = False
            c36['6'] = False
            c45['6'] = False
            c55['6'] = False
            c65['6'] = False
            c75['6'] = False
            c85['6'] = False
            c95['6'] = False
        elif solvednums[2][4] == 7:
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c24['7'] = False
            c25['7'] = False
            c36['7'] = False
            c45['7'] = False
            c55['7'] = False
            c65['7'] = False
            c75['7'] = False
            c85['7'] = False
            c95['7'] = False
        elif solvednums[2][4] == 8:
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c24['8'] = False
            c25['8'] = False
            c36['8'] = False
            c45['8'] = False
            c55['8'] = False
            c65['8'] = False
            c75['8'] = False
            c85['8'] = False
            c95['8'] = False
        elif solvednums[2][4] == 9:
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c14['9'] = False
            c15['9'] = False
            c16['9'] = False
            c24['9'] = False
            c25['9'] = False
            c36['9'] = False
            c45['9'] = False
            c55['9'] = False
            c65['9'] = False
            c75['9'] = False   
            c85['9'] = False
            c95['9'] = False
    if puzzlenums[2][5] > 0 and e36do == True:
        solvednums[2][5] = puzzlenums[2][5]
        e36do = False
        sleep(1)
    elif e36do == True and c36['1'] == True and c36['2'] == False and c36['3'] == False and c36['4'] == False and c36['5'] == False and c36['6'] == False and c36['7'] == False and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 1
    elif e36do == True and c36['1'] == False and c36['2'] == True and c36['3'] == False and c36['4'] == False and c36['5'] == False and c36['6'] == False and c36['7'] == False and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 2
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == True and c36['4'] == False and c36['5'] == False and c36['6'] == False and c36['7'] == False and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 3
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == False and c36['4'] == True and c36['5'] == False and c36['6'] == False and c36['7'] == False and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][6] = 4
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == False and c36['4'] == False and c36['5'] == True and c36['6'] == False and c36['7'] == False and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 5
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == False and c36['4'] == False and c36['5'] == False and c36['6'] == True and c36['7'] == False and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 6
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == False and c36['4'] == False and c36['5'] == False and c36['6'] == False and c36['7'] == True and c36['8'] == False and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 7
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == False and c36['4'] == False and c36['5'] == False and c36['6'] == False and c36['7'] == False and c36['8'] == True and c36['9'] == False:
        e36do = False
        solvednums[2][5] = 8
    elif e36do == True and c36['1'] == False and c36['2'] == False and c36['3'] == False and c36['4'] == False and c36['5'] == False and c36['6'] == False and c36['7'] == False and c36['8'] == False and c36['9'] == True:
        e36do = False
        solvednums[2][5] = 9     
    else:
        if solvednums[2][5] == 1:
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c14['1'] = False
            c15['1'] = False
            c16['1'] = False
            c24['1'] = False
            c25['1'] = False
            c26['1'] = False
            c46['1'] = False
            c56['1'] = False
            c66['1'] = False
            c76['1'] = False
            c86['1'] = False
            c96['1'] = False
        elif solvednums[2][5] == 2: 
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c14['2'] = False
            c15['2'] = False
            c16['2'] = False
            c24['2'] = False
            c25['2'] = False
            c26['2'] = False
            c46['2'] = False
            c56['2'] = False
            c66['2'] = False
            c76['2'] = False
            c86['2'] = False
            c96['2'] = False
        elif solvednums[2][5] == 3:
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c14['3'] = False
            c15['3'] = False
            c16['3'] = False
            c24['3'] = False
            c25['3'] = False
            c26['3'] = False
            c46['3'] = False
            c56['3'] = False
            c66['3'] = False
            c76['3'] = False
            c86['3'] = False
            c96['3'] = False
        elif solvednums[2][5] == 4:
            c31['4'] = False
            c32['4'] = False
            c33['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c14['4'] = False
            c15['4'] = False
            c16['4'] = False
            c24['4'] = False
            c25['4'] = False
            c26['4'] = False
            c46['4'] = False
            c56['4'] = False
            c66['4'] = False
            c76['4'] = False
            c86['4'] = False
            c96['4'] = False
        elif solvednums[2][5] == 5:
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c14['5'] = False
            c15['5'] = False
            c16['5'] = False
            c24['5'] = False
            c25['5'] = False
            c26['5'] = False
            c46['5'] = False
            c56['5'] = False
            c66['5'] = False
            c76['5'] = False
            c86['5'] = False
            c96['5'] = False
        elif solvednums[2][5] == 6:
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c14['6'] = False
            c15['6'] = False
            c16['6'] = False
            c24['6'] = False
            c25['6'] = False
            c26['6'] = False
            c46['6'] = False
            c56['6'] = False
            c66['6'] = False
            c76['6'] = False
            c86['6'] = False
            c96['6'] = False
        elif solvednums[2][5] == 7:
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c14['7'] = False
            c15['7'] = False
            c16['7'] = False
            c24['7'] = False
            c25['7'] = False
            c26['7'] = False
            c46['7'] = False
            c56['7'] = False
            c66['7'] = False
            c76['7'] = False
            c86['7'] = False
            c96['7'] = False
        elif solvednums[2][5] == 8:
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c14['8'] = False
            c15['8'] = False
            c16['8'] = False
            c24['8'] = False
            c25['8'] = False
            c26['8'] = False
            c46['8'] = False
            c56['8'] = False
            c66['8'] = False
            c76['8'] = False
            c86['8'] = False
            c96['8'] = False
        elif solvednums[2][5] == 9:
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c14['9'] = False
            c15['9'] = False
            c16['9'] = False
            c24['9'] = False
            c25['9'] = False
            c26['9'] = False
            c46['9'] = False
            c56['9'] = False
            c66['9'] = False
            c76['9'] = False   
            c86['9'] = False
            c96['9'] = False
    if puzzlenums[2][6] > 0 and e37do == True:
        solvednums[2][6] = puzzlenums[2][6]
        e37do = False
        sleep(1)
    elif e37do == True and c37['1'] == True and c37['2'] == False and c37['3'] == False and c37['4'] == False and c37['5'] == False and c37['6'] == False and c37['7'] == False and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 1
    elif e37do == True and c37['1'] == False and c37['2'] == True and c37['3'] == False and c37['4'] == False and c37['5'] == False and c37['6'] == False and c37['7'] == False and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 2
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == True and c37['4'] == False and c37['5'] == False and c37['6'] == False and c37['7'] == False and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 3
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == False and c37['4'] == True and c37['5'] == False and c37['6'] == False and c37['7'] == False and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 4
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == False and c37['4'] == False and c37['5'] == True and c37['6'] == False and c37['7'] == False and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 5
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == False and c37['4'] == False and c37['5'] == False and c37['6'] == True and c37['7'] == False and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 6
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == False and c37['4'] == False and c37['5'] == False and c37['6'] == False and c37['7'] == True and c37['8'] == False and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 7
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == False and c37['4'] == False and c37['5'] == False and c37['6'] == False and c37['7'] == False and c37['8'] == True and c37['9'] == False:
        e37do = False
        solvednums[2][6] = 8
    elif e37do == True and c37['1'] == False and c37['2'] == False and c37['3'] == False and c37['4'] == False and c37['5'] == False and c37['6'] == False and c37['7'] == False and c37['8'] == False and c37['9'] == True:
        e37do = False
        solvednums[2][6] = 9
    else:
        if solvednums[2][6] == 1:
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c47['1'] = False
            c57['1'] = False
            c67['1'] = False
            c77['1'] = False
            c87['1'] = False
            c97['1'] = False
        elif solvednums[2][6] == 2:
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c47['2'] = False
            c57['2'] = False
            c67['2'] = False
            c77['2'] = False
            c87['2'] = False
            c97['2'] = False
        elif solvednums[2][6] == 3:
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c47['3'] = False
            c57['3'] = False
            c67['3'] = False
            c77['3'] = False
            c87['3'] = False
            c97['3'] = False
        elif solvednums[2][6] == 4:
            c31['4'] = False
            c32['4'] = False
            c33['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c47['4'] = False
            c57['4'] = False
            c67['4'] = False
            c77['4'] = False
            c87['4'] = False
            c97['4'] = False
        elif solvednums[2][6] == 5:
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c47['5'] = False
            c57['5'] = False
            c67['5'] = False
            c77['5'] = False
            c87['5'] = False
            c97['5'] = False
        elif solvednums[2][6] == 6:
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c47['6'] = False
            c57['6'] = False
            c67['6'] = False
            c77['6'] = False
            c87['6'] = False
            c97['6'] = False
        elif solvednums[2][6] == 7:
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c47['7'] = False
            c57['7'] = False
            c67['7'] = False
            c77['7'] = False
            c87['7'] = False
            c97['7'] = False
        elif solvednums[2][6] == 8:
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c47['8'] = False
            c57['8'] = False
            c67['8'] = False
            c77['8'] = False
            c87['8'] = False
            c97['8'] = False
        elif solvednums[2][6] == 9:
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c47['9'] = False
            c57['9'] = False
            c67['9'] = False
            c77['9'] = False   
            c87['9'] = False
            c97['9'] = False
    if puzzlenums[2][7] > 0 and e38do == True:
        solvednums[2][7] = puzzlenums[2][7]
        e38do = False
        sleep(1)
    elif e38do == True and c38['1'] == True and c38['2'] == False and c38['3'] == False and c38['4'] == False and c38['5'] == False and c38['6'] == False and c38['7'] == False and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 1
    elif e38do == True and c38['1'] == False and c38['2'] == True and c38['3'] == False and c38['4'] == False and c38['5'] == False and c38['6'] == False and c38['7'] == False and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 2
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == True and c38['4'] == False and c38['5'] == False and c38['6'] == False and c38['7'] == False and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 3
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == False and c38['4'] == True and c38['5'] == False and c38['6'] == False and c38['7'] == False and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 4
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == False and c38['4'] == False and c38['5'] == True and c38['6'] == False and c38['7'] == False and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 5
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == False and c38['4'] == False and c38['5'] == False and c38['6'] == True and c38['7'] == False and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 6
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == False and c38['4'] == False and c38['5'] == False and c38['6'] == False and c38['7'] == True and c38['8'] == False and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 7
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == False and c38['4'] == False and c38['5'] == False and c38['6'] == False and c38['7'] == False and c38['8'] == True and c38['9'] == False:
        e38do = False
        solvednums[2][7] = 8
    elif e38do == True and c38['1'] == False and c38['2'] == False and c38['3'] == False and c38['4'] == False and c38['5'] == False and c38['6'] == False and c38['7'] == False and c38['8'] == False and c38['9'] == True:
        e38do = False
        solvednums[2][7] = 9
    else:
        if solvednums[2][7] == 1:
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c48['1'] = False
            c58['1'] = False
            c68['1'] = False
            c78['1'] = False
            c88['1'] = False
            c98['1'] = False
        elif solvednums[2][7] == 2:
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c48['2'] = False
            c58['2'] = False
            c68['2'] = False
            c78['2'] = False
            c88['2'] = False
            c98['2'] = False
        elif solvednums[2][7] == 3:
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c48['3'] = False
            c58['3'] = False
            c68['3'] = False
            c78['3'] = False
            c88['3'] = False
            c98['3'] = False
        elif solvednums[2][7] == 4:
            c31['4'] = False
            c32['4'] = False
            c33['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c48['4'] = False
            c58['4'] = False
            c68['4'] = False
            c78['4'] = False
            c88['4'] = False
            c98['4'] = False
        elif solvednums[2][7] == 5:
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c29['5'] = False
            c28['5'] = False
            c29['5'] = False
            c48['5'] = False
            c58['5'] = False
            c68['5'] = False
            c78['5'] = False
            c88['5'] = False
            c98['5'] = False
        elif solvednums[2][7] == 6:
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c48['6'] = False
            c58['6'] = False
            c68['6'] = False
            c78['6'] = False
            c88['6'] = False
            c98['6'] = False
        elif solvednums[2][7] == 7:
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c48['7'] = False
            c58['7'] = False
            c68['7'] = False
            c78['7'] = False
            c88['7'] = False
            c98['7'] = False
        elif solvednums[2][7] == 8:
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c48['8'] = False
            c58['8'] = False
            c68['8'] = False
            c78['8'] = False
            c88['8'] = False
            c98['8'] = False
        elif solvednums[2][7] == 9:
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c48['9'] = False
            c58['9'] = False
            c68['9'] = False
            c78['9'] = False   
            c88['9'] = False
            c98['9'] = False
    if puzzlenums[2][8] > 0 and e39do == True:
        solvednums[2][8] = puzzlenums[2][8]
        e39do = False
        sleep(1)
    elif e39do == True and c39['1'] == True and c39['2'] == False and c39['3'] == False and c39['4'] == False and c39['5'] == False and c39['6'] == False and c39['7'] == False and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 1
    elif e39do == True and c39['1'] == False and c39['2'] == True and c39['3'] == False and c39['4'] == False and c39['5'] == False and c39['6'] == False and c39['7'] == False and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 2
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == True and c39['4'] == False and c39['5'] == False and c39['6'] == False and c39['7'] == False and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 3
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == False and c39['4'] == True and c39['5'] == False and c39['6'] == False and c39['7'] == False and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 4
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == False and c39['4'] == False and c39['5'] == True and c39['6'] == False and c39['7'] == False and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 5
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == False and c39['4'] == False and c39['5'] == False and c39['6'] == True and c39['7'] == False and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 6
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == False and c39['4'] == False and c39['5'] == False and c39['6'] == False and c39['7'] == True and c39['8'] == False and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 7
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == False and c39['4'] == False and c39['5'] == False and c39['6'] == False and c39['7'] == False and c39['8'] == True and c39['9'] == False:
        e39do = False
        solvednums[2][8] = 8
    elif e39do == True and c39['1'] == False and c39['2'] == False and c39['3'] == False and c39['4'] == False and c39['5'] == False and c39['6'] == False and c39['7'] == False and c39['8'] == False and c39['9'] == True:
        e39do = False
        solvednums[2][8] = 9
    else:
        if solvednums[2][8] == 1:
            c31['1'] = False
            c32['1'] = False
            c33['1'] = False
            c35['1'] = False
            c36['1'] = False
            c37['1'] = False
            c38['1'] = False
            c39['1'] = False
            c17['1'] = False
            c18['1'] = False
            c19['1'] = False
            c27['1'] = False
            c28['1'] = False
            c29['1'] = False
            c49['1'] = False
            c59['1'] = False
            c69['1'] = False
            c79['1'] = False
            c89['1'] = False
            c99['1'] = False
        elif solvednums[2][8] == 2:
            c31['2'] = False
            c32['2'] = False
            c33['2'] = False
            c35['2'] = False
            c36['2'] = False
            c37['2'] = False
            c38['2'] = False
            c39['2'] = False
            c17['2'] = False
            c18['2'] = False
            c19['2'] = False
            c27['2'] = False
            c28['2'] = False
            c29['2'] = False
            c49['2'] = False
            c59['2'] = False
            c69['2'] = False
            c79['2'] = False
            c89['2'] = False
            c99['2'] = False
        elif solvednums[2][8] == 3:
            c31['3'] = False
            c32['3'] = False
            c33['3'] = False
            c35['3'] = False
            c36['3'] = False
            c37['3'] = False
            c38['3'] = False
            c39['3'] = False
            c17['3'] = False
            c18['3'] = False
            c19['3'] = False
            c27['3'] = False
            c28['3'] = False
            c29['3'] = False
            c49['3'] = False
            c59['3'] = False
            c69['3'] = False
            c79['3'] = False
            c89['3'] = False
            c99['3'] = False
        elif solvednums[2][8] == 4:
            c31['4'] = False
            c32['4'] = False
            c33['4'] = False
            c35['4'] = False
            c36['4'] = False
            c37['4'] = False
            c38['4'] = False
            c39['4'] = False
            c17['4'] = False
            c18['4'] = False
            c19['4'] = False
            c27['4'] = False
            c28['4'] = False
            c29['4'] = False
            c49['4'] = False
            c59['4'] = False
            c69['4'] = False
            c79['4'] = False
            c89['4'] = False
            c99['4'] = False
        elif solvednums[2][8] == 5:
            c31['5'] = False
            c32['5'] = False
            c33['5'] = False
            c35['5'] = False
            c36['5'] = False
            c37['5'] = False
            c38['5'] = False
            c39['5'] = False
            c17['5'] = False
            c18['5'] = False
            c19['5'] = False
            c27['5'] = False
            c28['5'] = False
            c29['5'] = False
            c49['5'] = False
            c59['5'] = False
            c69['5'] = False
            c79['5'] = False
            c89['5'] = False
            c99['5'] = False
        elif solvednums[2][8] == 6:
            c31['6'] = False
            c32['6'] = False
            c33['6'] = False
            c35['6'] = False
            c36['6'] = False
            c37['6'] = False
            c38['6'] = False
            c39['6'] = False
            c17['6'] = False
            c18['6'] = False
            c19['6'] = False
            c27['6'] = False
            c28['6'] = False
            c29['6'] = False
            c49['6'] = False
            c59['6'] = False
            c69['6'] = False
            c79['6'] = False
            c89['6'] = False
            c99['6'] = False
        elif solvednums[2][8] == 7:
            c31['7'] = False
            c32['7'] = False
            c33['7'] = False
            c35['7'] = False
            c36['7'] = False
            c37['7'] = False
            c38['7'] = False
            c39['7'] = False
            c17['7'] = False
            c18['7'] = False
            c19['7'] = False
            c27['7'] = False
            c28['7'] = False
            c29['7'] = False
            c49['7'] = False
            c59['7'] = False
            c69['7'] = False
            c79['7'] = False
            c89['7'] = False
            c99['7'] = False
        elif solvednums[2][8] == 8:
            c31['8'] = False
            c32['8'] = False
            c33['8'] = False
            c35['8'] = False
            c36['8'] = False
            c37['8'] = False
            c38['8'] = False
            c39['8'] = False
            c17['8'] = False
            c18['8'] = False
            c19['8'] = False
            c27['8'] = False
            c28['8'] = False
            c29['8'] = False
            c49['8'] = False
            c59['8'] = False
            c69['8'] = False
            c79['8'] = False
            c89['8'] = False
            c99['8'] = False
        elif solvednums[2][8] == 9:
            c31['9'] = False
            c32['9'] = False
            c33['9'] = False
            c35['9'] = False 
            c36['9'] = False
            c37['9'] = False
            c38['9'] = False
            c39['9'] = False
            c17['9'] = False
            c18['9'] = False
            c19['9'] = False
            c27['9'] = False
            c28['9'] = False
            c29['9'] = False
            c49['9'] = False
            c59['9'] = False
            c69['9'] = False
            c79['9'] = False   
            c89['9'] = False
            c99['9'] = False
    if puzzlenums[3][0] > 0 and e41do == True:
        solvednums[3][0] = puzzlenums[3][0]
        e41do = False
        sleep(1)
    elif e41do == True and c41['1'] == True and c41['2'] == False and c41['3'] == False and c41['4'] == False and c41['5'] == False and c41['6'] == False and c41['7'] == False and c41['8'] == False and c31['9'] == False:
        e41do = False
        solvednums[3][0] = 1
    elif e41do == True and c41['1'] == False and c41['2'] == True and c41['3'] == False and c41['4'] == False and c41['5'] == False and c41['6'] == False and c41['7'] == False and c41['8'] == False and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 2
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == True and c41['4'] == False and c41['5'] == False and c41['6'] == False and c41['7'] == False and c41['8'] == False and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 3
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == False and c41['4'] == True and c41['5'] == False and c41['6'] == False and c41['7'] == False and c41['8'] == False and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 4
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == False and c41['4'] == False and c41['5'] == True and c41['6'] == False and c41['7'] == False and c41['8'] == False and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 5
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == False and c41['4'] == False and c41['5'] == False and c41['6'] == True and c41['7'] == False and c41['8'] == False and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 6
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == False and c41['4'] == False and c41['5'] == False and c41['6'] == False and c41['7'] == True and c41['8'] == False and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 7
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == False and c41['4'] == False and c41['5'] == False and c41['6'] == False and c41['7'] == False and c41['8'] == True and c41['9'] == False:
        e41do = False
        solvednums[3][0] = 8
    elif e41do == True and c41['1'] == False and c41['2'] == False and c41['3'] == False and c41['4'] == False and c41['5'] == False and c41['6'] == False and c41['7'] == False and c41['8'] == False and c41['9'] == True:
        e41do = False
        solvednums[3][0] = 9
    else:
        if solvednums[3][0] == 1:
            c41['1'] = False
            c41['2'] = False
            c41['3'] = False
            c41['4'] = False
            c41['5'] = False
            c41['6'] = False
            c41['7'] = False
            c41['8'] = False
            c41['9'] = False
            c42['1'] = False
            c43['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c11['1'] = False
            c21['1'] = False
            c31['1'] = False
            c51['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[3][0] == 2:
            c41['1'] = False
            c41['2'] = False
            c41['3'] = False
            c41['4'] = False
            c41['5'] = False
            c41['6'] = False
            c41['7'] = False
            c41['8'] = False
            c41['9'] = False
            c42['2'] = False
            c43['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c11['2'] = False
            c21['2'] = False
            c31['2'] = False
            c71['2'] = False
            c81['2'] = False
            c91['2'] = False
        elif solvednums[3][0] == 3:
            c42['3'] = False
            c43['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c11['3'] = False
            c21['3'] = False
            c31['3'] = False
            c71['3'] = False
            c81['3'] = False
            c91['3'] = False
        elif solvednums[3][0] == 4:
            c42['4'] = False
            c43['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c11['4'] = False
            c21['4'] = False
            c31['4'] = False
            c71['4'] = False
            c81['4'] = False
            c91['4'] = False
        elif solvednums[3][0] == 5:
            c42['5'] = False
            c43['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c11['5'] = False
            c21['5'] = False
            c31['5'] = False
            c71['5'] = False
            c81['5'] = False
            c91['5'] = False
        elif solvednums[3][0] == 6:
            c42['6'] = False
            c43['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c11['6'] = False
            c21['6'] = False
            c31['6'] = False
            c71['6'] = False
            c81['6'] = False
            c91['6'] = False
        elif solvednums[3][0] == 7:
            c42['7'] = False
            c43['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c11['7'] = False
            c21['7'] = False
            c31['7'] = False
            c71['7'] = False
            c81['7'] = False
            c91['7'] = False
        elif solvednums[3][0] == 8:
            c42['8'] = False
            c43['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c11['8'] = False
            c21['8'] = False
            c31['8'] = False
            c71['8'] = False
            c81['8'] = False
            c91['8'] = False
        elif solvednums[3][0] == 9:
            c42['9'] = False
            c43['9'] = False
            c44['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c11['9'] = False
            c21['9'] = False
            c31['9'] = False
            c71['9'] = False   
            c81['9'] = False
            c91['9'] = False
    if puzzlenums[3][1] > 0 and e42do == True:
        solvednums[3][1] = puzzlenums[3][1]
        e42do = False
        sleep(1)
    elif e42do == True and c42['1'] == True and c42['2'] == False and c42['3'] == False and c42['4'] == False and c42['5'] == False and c42['6'] == False and c42['7'] == False and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 1
    elif e42do == True and c42['1'] == False and c42['2'] == True and c42['3'] == False and c42['4'] == False and c42['5'] == False and c42['6'] == False and c42['7'] == False and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 2
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == True and c42['4'] == False and c42['5'] == False and c42['6'] == False and c42['7'] == False and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 3
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == False and c42['4'] == True and c42['5'] == False and c42['6'] == False and c42['7'] == False and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 4
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == False and c42['4'] == False and c42['5'] == True and c42['6'] == False and c42['7'] == False and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 5
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == False and c42['4'] == False and c42['5'] == False and c42['6'] == True and c42['7'] == False and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 6
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == False and c42['4'] == False and c42['5'] == False and c42['6'] == False and c42['7'] == True and c42['8'] == False and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 7
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == False and c42['4'] == False and c42['5'] == False and c42['6'] == False and c42['7'] == False and c42['8'] == True and c42['9'] == False:
        e42do = False
        solvednums[3][1] = 8
    elif e42do == True and c42['1'] == False and c42['2'] == False and c42['3'] == False and c42['4'] == False and c42['5'] == False and c42['6'] == False and c42['7'] == False and c42['8'] == False and c42['9'] == True:
        e42do = False
        solvednums[3][1] = 9
    else:
        if solvednums[3][1] == 1:
            c41['1'] = False
            c43['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c12['1'] = False
            c22['1'] = False
            c32['1'] = False
            c72['1'] = False
            c82['1'] = False
            c92['1'] = False
        elif solvednums[3][1] == 2:
            c41['2'] = False
            c43['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c12['2'] = False
            c22['2'] = False
            c32['2'] = False
            c72['2'] = False
            c82['2'] = False
            c92['2'] = False
        elif solvednums[3][1] == 3:
            c41['3'] = False
            c43['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c12['3'] = False
            c22['3'] = False
            c32['3'] = False
            c72['3'] = False
            c82['3'] = False
            c92['3'] = False
        elif solvednums[3][1] == 4:
            c41['4'] = False
            c43['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c12['4'] = False
            c22['4'] = False
            c32['4'] = False
            c72['4'] = False
            c82['4'] = False
            c92['4'] = False
        elif solvednums[3][1] == 5:
            c41['5'] = False
            c43['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c12['5'] = False
            c22['5'] = False
            c32['5'] = False
            c72['5'] = False
            c82['5'] = False
            c92['5'] = False
        elif solvednums[3][1] == 6:
            c41['6'] = False
            c43['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c12['6'] = False
            c22['6'] = False
            c32['6'] = False
            c72['6'] = False
            c82['6'] = False
            c92['6'] = False
        elif solvednums[3][1] == 7:
            c41['7'] = False
            c43['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c12['7'] = False
            c22['7'] = False
            c32['7'] = False
            c72['7'] = False
            c82['7'] = False
            c92['7'] = False
        elif solvednums[3][1] == 8:
            c41['8'] = False
            c43['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c68['8'] = False
            c62['8'] = False
            c63['8'] = False
            c12['8'] = False
            c22['8'] = False
            c32['8'] = False
            c72['8'] = False
            c82['8'] = False
            c92['8'] = False
        elif solvednums[3][1] == 9:
            c41['9'] = False
            c43['9'] = False
            c44['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c12['9'] = False
            c22['9'] = False
            c32['9'] = False
            c72['9'] = False   
            c82['9'] = False
            c92['9'] = False
    if puzzlenums[3][2] > 0 and e43do == True:
        solvednums[3][2] = puzzlenums[3][2]
        e43do = False
        sleep(1)
    elif e43do == True and c43['1'] == True and c43['2'] == False and c43['3'] == False and c43['4'] == False and c43['5'] == False and c43['6'] == False and c43['7'] == False and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 1
    elif e43do == True and c43['1'] == False and c43['2'] == True and c43['3'] == False and c43['4'] == False and c43['5'] == False and c43['6'] == False and c43['7'] == False and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 2
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == True and c43['4'] == False and c43['5'] == False and c43['6'] == False and c43['7'] == False and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 3
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == False and c43['4'] == True and c43['5'] == False and c43['6'] == False and c43['7'] == False and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 4
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == False and c43['4'] == False and c43['5'] == True and c43['6'] == False and c43['7'] == False and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 5
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == False and c43['4'] == False and c43['5'] == False and c43['6'] == True and c43['7'] == False and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 6
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == False and c43['4'] == False and c43['5'] == False and c43['6'] == False and c43['7'] == True and c43['8'] == False and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 7
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == False and c43['4'] == False and c43['5'] == False and c43['6'] == False and c43['7'] == False and c43['8'] == True and c43['9'] == False:
        e43do = False
        solvednums[3][2] = 8
    elif e43do == True and c43['1'] == False and c43['2'] == False and c43['3'] == False and c43['4'] == False and c43['5'] == False and c43['6'] == False and c43['7'] == False and c43['8'] == False and c43['9'] == True:
        e43do = False
        solvednums[3][2] = 9
    else:
        if solvednums[3][2] == 1:
            c41['1'] = False
            c42['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c13['1'] = False
            c23['1'] = False
            c33['1'] = False
            c73['1'] = False
            c83['1'] = False
            c93['1'] = False
        elif solvednums[3][2] == 2:
            c41['2'] = False
            c42['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c43['2'] = False
            c13['2'] = False
            c23['2'] = False
            c33['2'] = False
            c83['2'] = False
            c93['2'] = False
        elif solvednums[3][2] == 3:
            c41['3'] = False
            c42['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c13['3'] = False
            c23['3'] = False
            c33['3'] = False
            c73['3'] = False
            c83['3'] = False
            c93['3'] = False
        elif solvednums[3][2] == 4:
            c41['4'] = False
            c42['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c61['4'] = False
            c64['4'] = False
            c63['4'] = False
            c13['4'] = False
            c23['4'] = False
            c33['4'] = False
            c73['4'] = False
            c83['4'] = False
            c93['4'] = False
        elif solvednums[3][2] == 5:
            c41['5'] = False
            c42['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c13['5'] = False
            c23['5'] = False
            c33['5'] = False
            c73['5'] = False
            c83['5'] = False
            c93['5'] = False
        elif solvednums[3][2] == 6:
            c41['6'] = False
            c42['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c13['6'] = False
            c23['6'] = False
            c33['6'] = False
            c73['6'] = False
            c83['6'] = False
            c93['6'] = False
        elif solvednums[3][2] == 7:
            c41['7'] = False
            c42['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c13['7'] = False
            c23['7'] = False
            c33['7'] = False
            c73['7'] = False
            c83['7'] = False
            c93['7'] = False
        elif solvednums[3][2] == 8:
            c41['8'] = False
            c42['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c13['8'] = False
            c23['8'] = False
            c33['8'] = False
            c73['8'] = False
            c83['8'] = False
            c93['8'] = False
        elif solvednums[3][2] == 9:
            c41['9'] = False
            c42['9'] = False
            c44['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c13['9'] = False
            c23['9'] = False
            c33['9'] = False
            c73['9'] = False   
            c83['9'] = False
            c93['9'] = False
    if puzzlenums[3][3] > 0 and e44do == True:
        solvednums[3][3] = puzzlenums[3][3]
        e44do = False
        sleep(1)
    elif e44do == True and c44['1'] == True and c44['2'] == False and c44['3'] == False and c44['4'] == False and c44['5'] == False and c44['6'] == False and c44['7'] == False and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 1
    elif e44do == True and c44['1'] == False and c44['2'] == True and c44['3'] == False and c44['4'] == False and c44['5'] == False and c44['6'] == False and c44['7'] == False and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 2
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == True and c44['4'] == False and c44['5'] == False and c44['6'] == False and c44['7'] == False and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 3
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == False and c44['4'] == True and c44['5'] == False and c44['6'] == False and c44['7'] == False and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 4
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == False and c44['4'] == False and c44['5'] == True and c44['6'] == False and c44['7'] == False and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 5
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == False and c44['4'] == False and c44['5'] == False and c44['6'] == True and c44['7'] == False and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 6
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == False and c44['4'] == False and c44['5'] == False and c44['6'] == False and c44['7'] == True and c44['8'] == False and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 7
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == False and c44['4'] == False and c44['5'] == False and c44['6'] == False and c44['7'] == False and c44['8'] == True and c44['9'] == False:
        e44do = False
        solvednums[3][3] = 8
    elif e44do == True and c44['1'] == False and c44['2'] == False and c44['3'] == False and c44['4'] == False and c44['5'] == False and c44['6'] == False and c44['7'] == False and c44['8'] == False and c44['9'] == True:
        e44do = False
        solvednums[3][3] = 9
    else:
        if solvednums[3][3] == 1:
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c14['1'] = False
            c24['1'] = False
            c34['1'] = False
            c74['1'] = False
            c84['1'] = False
            c94['1'] = False
        elif solvednums[3][3] == 2:
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c14['2'] = False
            c24['2'] = False
            c34['2'] = False
            c74['2'] = False
            c84['2'] = False
            c94['2'] = False
        elif solvednums[3][3] == 3:
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c14['3'] = False
            c24['3'] = False
            c34['3'] = False
            c74['3'] = False
            c84['3'] = False
            c94['3'] = False
        elif solvednums[3][3] == 4:
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c14['4'] = False
            c24['4'] = False
            c34['4'] = False
            c74['4'] = False
            c84['4'] = False
            c94['4'] = False
        elif solvednums[3][3] == 5:
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c14['5'] = False
            c24['5'] = False
            c34['5'] = False
            c74['5'] = False
            c84['5'] = False
            c94['5'] = False
        elif solvednums[3][3] == 6:
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c14['6'] = False
            c24['6'] = False
            c34['6'] = False
            c74['6'] = False
            c84['6'] = False
            c94['6'] = False
        elif solvednums[3][3] == 7:
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c14['7'] = False
            c24['7'] = False
            c34['7'] = False
            c74['7'] = False
            c84['7'] = False
            c94['7'] = False
        elif solvednums[3][3] == 8:
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c14['8'] = False
            c24['8'] = False
            c34['8'] = False
            c74['8'] = False
            c84['8'] = False
            c94['8'] = False
        elif solvednums[3][3] == 9:
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c54['9'] = False
            c55['9'] = False
            c56['9'] = False
            c64['9'] = False
            c65['9'] = False
            c66['9'] = False
            c14['9'] = False
            c24['9'] = False
            c34['9'] = False
            c74['9'] = False   
            c84['9'] = False
            c94['9'] = False
    if puzzlenums[3][4] > 0 and e45do == True:
        solvednums[3][4] = puzzlenums[3][4]
        e45do = False
        sleep(1)
    elif e45do == True and c45['1'] == True and c45['2'] == False and c45['3'] == False and c45['4'] == False and c45['5'] == False and c45['6'] == False and c45['7'] == False and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 1
    elif e45do == True and c45['1'] == False and c45['2'] == True and c45['3'] == False and c45['4'] == False and c45['5'] == False and c45['6'] == False and c45['7'] == False and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 2
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == True and c45['4'] == False and c45['5'] == False and c45['6'] == False and c45['7'] == False and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 3
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == False and c45['4'] == True and c45['5'] == False and c45['6'] == False and c45['7'] == False and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 4
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == False and c45['4'] == False and c45['5'] == True and c45['6'] == False and c45['7'] == False and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 5
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == False and c45['4'] == False and c45['5'] == False and c45['6'] == True and c45['7'] == False and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 6
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == False and c45['4'] == False and c45['5'] == False and c45['6'] == False and c45['7'] == True and c45['8'] == False and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 7
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == False and c45['4'] == False and c45['5'] == False and c45['6'] == False and c45['7'] == False and c45['8'] == True and c45['9'] == False:
        e45do = False
        solvednums[3][4] = 8
    elif e45do == True and c45['1'] == False and c45['2'] == False and c45['3'] == False and c45['4'] == False and c45['5'] == False and c45['6'] == False and c45['7'] == False and c45['8'] == False and c45['9'] == True:
        e45do = False
        solvednums[3][4] = 9
    else:
        if solvednums[3][4] == 1:
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c15['1'] = False
            c25['1'] = False
            c35['1'] = False
            c75['1'] = False
            c85['1'] = False
            c95['1'] = False
        elif solvednums[3][4] == 2:
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c15['2'] = False
            c25['2'] = False
            c35['2'] = False
            c75['2'] = False
            c85['2'] = False
            c95['2'] = False
        elif solvednums[3][4] == 3:
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c15['3'] = False
            c25['3'] = False
            c35['3'] = False
            c75['3'] = False
            c85['3'] = False
            c95['3'] = False
        elif solvednums[3][4] == 4:
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c15['4'] = False
            c25['4'] = False
            c35['4'] = False
            c75['4'] = False
            c85['4'] = False
            c95['4'] = False
        elif solvednums[3][4] == 5:
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c15['5'] = False
            c25['5'] = False
            c35['5'] = False
            c75['5'] = False
            c85['5'] = False
            c95['5'] = False
        elif solvednums[3][4] == 6:
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c15['6'] = False
            c25['6'] = False
            c35['6'] = False
            c75['6'] = False
            c85['6'] = False
            c95['6'] = False
        elif solvednums[3][4] == 7:
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c15['7'] = False
            c25['7'] = False
            c35['7'] = False
            c75['7'] = False
            c85['7'] = False
            c95['7'] = False
        elif solvednums[3][4] == 8:
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c15['8'] = False
            c25['8'] = False
            c35['8'] = False
            c75['8'] = False
            c85['8'] = False
            c95['8'] = False
        elif solvednums[3][4] == 9:
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c54['9'] = False
            c55['9'] = False
            c56['9'] = False
            c64['9'] = False
            c65['9'] = False
            c66['9'] = False
            c15['9'] = False
            c25['9'] = False
            c35['9'] = False
            c75['9'] = False   
            c85['9'] = False
            c95['9'] = False
    if puzzlenums[3][5] > 0 and e46do == True:
        solvednums[3][5] = puzzlenums[3][5]
        e46do = False
        sleep(1)
    elif e46do == True and c46['1'] == True and c46['2'] == False and c46['3'] == False and c46['4'] == False and c46['5'] == False and c46['6'] == False and c46['7'] == False and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 1
    elif e46do == True and c46['1'] == False and c46['2'] == True and c46['3'] == False and c46['4'] == False and c46['5'] == False and c46['6'] == False and c46['7'] == False and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 2
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == True and c46['4'] == False and c46['5'] == False and c46['6'] == False and c46['7'] == False and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 3
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == False and c46['4'] == True and c46['5'] == False and c46['6'] == False and c46['7'] == False and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][6] = 4
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == False and c46['4'] == False and c46['5'] == True and c46['6'] == False and c46['7'] == False and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 5
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == False and c46['4'] == False and c46['5'] == False and c46['6'] == True and c46['7'] == False and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 6
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == False and c46['4'] == False and c46['5'] == False and c46['6'] == False and c46['7'] == True and c46['8'] == False and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 7
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == False and c46['4'] == False and c46['5'] == False and c46['6'] == False and c46['7'] == False and c46['8'] == True and c46['9'] == False:
        e46do = False
        solvednums[3][5] = 8
    elif e46do == True and c46['1'] == False and c46['2'] == False and c46['3'] == False and c46['4'] == False and c46['5'] == False and c46['6'] == False and c46['7'] == False and c46['8'] == False and c46['9'] == True:
        e46do = False
        solvednums[3][5] = 9     
    else:
        if solvednums[3][5] == 1:
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c16['1'] = False
            c26['1'] = False
            c36['1'] = False
            c76['1'] = False
            c86['1'] = False
            c96['1'] = False
        elif solvednums[3][5] == 2: 
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c16['2'] = False
            c26['2'] = False
            c36['2'] = False
            c76['2'] = False
            c86['2'] = False
            c96['2'] = False
        elif solvednums[3][5] == 3:
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c16['3'] = False
            c26['3'] = False
            c36['3'] = False
            c76['3'] = False
            c86['3'] = False
            c96['3'] = False
        elif solvednums[3][5] == 4:
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c16['4'] = False
            c26['4'] = False
            c36['4'] = False
            c76['4'] = False
            c86['4'] = False
            c96['4'] = False
        elif solvednums[3][5] == 5:
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c16['5'] = False
            c26['5'] = False
            c36['5'] = False
            c76['5'] = False
            c86['5'] = False
            c96['5'] = False
        elif solvednums[3][5] == 6:
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c16['6'] = False
            c26['6'] = False
            c36['6'] = False
            c76['6'] = False
            c86['6'] = False
            c96['6'] = False
        elif solvednums[3][5] == 7:
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c16['7'] = False
            c26['7'] = False
            c36['7'] = False
            c76['7'] = False
            c86['7'] = False
            c96['7'] = False
        elif solvednums[3][5] == 8:
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c16['8'] = False
            c26['8'] = False
            c36['8'] = False
            c76['8'] = False
            c86['8'] = False
            c96['8'] = False
        elif solvednums[3][5] == 9:
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c54['9'] = False
            c55['9'] = False
            c56['9'] = False
            c64['9'] = False
            c65['9'] = False
            c66['9'] = False
            c16['9'] = False
            c26['9'] = False
            c36['9'] = False
            c76['9'] = False   
            c86['9'] = False
            c96['9'] = False
    if puzzlenums[3][6] > 0 and e47do == True:
        solvednums[3][6] = puzzlenums[3][6]
        e47do = False
        sleep(1)
    elif e47do == True and c47['1'] == True and c47['2'] == False and c47['3'] == False and c47['4'] == False and c47['5'] == False and c47['6'] == False and c47['7'] == False and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 1
    elif e47do == True and c47['1'] == False and c47['2'] == True and c47['3'] == False and c47['4'] == False and c47['5'] == False and c47['6'] == False and c47['7'] == False and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 2
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == True and c47['4'] == False and c47['5'] == False and c47['6'] == False and c47['7'] == False and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 3
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == False and c47['4'] == True and c47['5'] == False and c47['6'] == False and c47['7'] == False and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 4
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == False and c47['4'] == False and c47['5'] == True and c47['6'] == False and c47['7'] == False and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 5
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == False and c47['4'] == False and c47['5'] == False and c47['6'] == True and c47['7'] == False and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 6
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == False and c47['4'] == False and c47['5'] == False and c47['6'] == False and c47['7'] == True and c47['8'] == False and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 7
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == False and c47['4'] == False and c47['5'] == False and c47['6'] == False and c47['7'] == False and c47['8'] == True and c47['9'] == False:
        e47do = False
        solvednums[3][6] = 8
    elif e47do == True and c47['1'] == False and c47['2'] == False and c47['3'] == False and c47['4'] == False and c47['5'] == False and c47['6'] == False and c47['7'] == False and c47['8'] == False and c47['9'] == True:
        e47do = False
        solvednums[3][6] = 9
    else:
        if solvednums[3][6] == 1:
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c17['1'] = False
            c27['1'] = False
            c37['1'] = False
            c77['1'] = False
            c87['1'] = False
            c97['1'] = False
        elif solvednums[3][6] == 2:
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c17['2'] = False
            c27['2'] = False
            c37['2'] = False
            c77['2'] = False
            c87['2'] = False
            c97['2'] = False
        elif solvednums[3][6] == 3:
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c17['3'] = False
            c27['3'] = False
            c37['3'] = False
            c77['3'] = False
            c87['3'] = False
            c97['3'] = False
        elif solvednums[3][6] == 4:
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c17['4'] = False
            c27['4'] = False
            c37['4'] = False
            c77['4'] = False
            c87['4'] = False
            c97['4'] = False
        elif solvednums[3][6] == 5:
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c17['5'] = False
            c27['5'] = False
            c37['5'] = False
            c77['5'] = False
            c87['5'] = False
            c97['5'] = False
        elif solvednums[3][6] == 6:
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c17['6'] = False
            c27['6'] = False
            c37['6'] = False
            c77['6'] = False
            c87['6'] = False
            c97['6'] = False
        elif solvednums[3][6] == 7:
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c17['7'] = False
            c27['7'] = False
            c37['7'] = False
            c77['7'] = False
            c87['7'] = False
            c97['7'] = False
        elif solvednums[3][6] == 8:
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c17['8'] = False
            c27['8'] = False
            c37['8'] = False
            c77['8'] = False
            c87['8'] = False
            c97['8'] = False
        elif solvednums[3][6] == 9:
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c17['9'] = False
            c27['9'] = False
            c37['9'] = False
            c77['9'] = False   
            c87['9'] = False
            c97['9'] = False
    if puzzlenums[3][7] > 0 and e48do == True:
        solvednums[3][7] = puzzlenums[3][7]
        e48do = False
        sleep(1)
    elif e48do == True and c48['1'] == True and c48['2'] == False and c48['3'] == False and c48['4'] == False and c48['5'] == False and c48['6'] == False and c48['7'] == False and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 1
    elif e48do == True and c48['1'] == False and c48['2'] == True and c48['3'] == False and c48['4'] == False and c48['5'] == False and c48['6'] == False and c48['7'] == False and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 2
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == True and c48['4'] == False and c48['5'] == False and c48['6'] == False and c48['7'] == False and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 3
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == False and c48['4'] == True and c48['5'] == False and c48['6'] == False and c48['7'] == False and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 4
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == False and c48['4'] == False and c48['5'] == True and c48['6'] == False and c48['7'] == False and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 5
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == False and c48['4'] == False and c48['5'] == False and c48['6'] == True and c48['7'] == False and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 6
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == False and c48['4'] == False and c48['5'] == False and c48['6'] == False and c48['7'] == True and c48['8'] == False and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 7
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == False and c48['4'] == False and c48['5'] == False and c48['6'] == False and c48['7'] == False and c48['8'] == True and c48['9'] == False:
        e48do = False
        solvednums[3][7] = 8
    elif e48do == True and c48['1'] == False and c48['2'] == False and c48['3'] == False and c48['4'] == False and c48['5'] == False and c48['6'] == False and c48['7'] == False and c48['8'] == False and c48['9'] == True:
        e48do = False
        solvednums[3][7] = 9
    else:
        if solvednums[3][7] == 1:
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c18['1'] = False
            c28['1'] = False
            c38['1'] = False
            c78['1'] = False
            c88['1'] = False
            c98['1'] = False
        elif solvednums[3][7] == 2:
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c18['2'] = False
            c28['2'] = False
            c38['2'] = False
            c78['2'] = False
            c88['2'] = False
            c98['2'] = False
        elif solvednums[3][7] == 3:
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c18['3'] = False
            c28['3'] = False
            c38['3'] = False
            c78['3'] = False
            c88['3'] = False
            c98['3'] = False
        elif solvednums[3][7] == 4:
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c18['4'] = False
            c28['4'] = False
            c38['4'] = False
            c78['4'] = False
            c88['4'] = False
            c98['4'] = False
        elif solvednums[3][7] == 5:
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c69['5'] = False
            c68['5'] = False
            c69['5'] = False
            c18['5'] = False
            c28['5'] = False
            c38['5'] = False
            c78['5'] = False
            c88['5'] = False
            c98['5'] = False
        elif solvednums[3][7] == 6:
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c18['6'] = False
            c28['6'] = False
            c38['6'] = False
            c78['6'] = False
            c88['6'] = False
            c98['6'] = False
        elif solvednums[3][7] == 7:
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c18['7'] = False
            c28['7'] = False
            c38['7'] = False
            c78['7'] = False
            c88['7'] = False
            c98['7'] = False
        elif solvednums[3][7] == 8:
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c18['8'] = False
            c28['8'] = False
            c38['8'] = False
            c78['8'] = False
            c88['8'] = False
            c98['8'] = False
        elif solvednums[3][7] == 9:
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c18['9'] = False
            c28['9'] = False
            c38['9'] = False
            c78['9'] = False   
            c88['9'] = False
            c98['9'] = False
    if puzzlenums[3][8] > 0 and e49do == True:
        solvednums[3][8] = puzzlenums[3][8]
        e49do = False
        sleep(1)
    elif e49do == True and c49['1'] == True and c49['2'] == False and c49['3'] == False and c49['4'] == False and c49['5'] == False and c49['6'] == False and c49['7'] == False and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 1
    elif e49do == True and c49['1'] == False and c49['2'] == True and c49['3'] == False and c49['4'] == False and c49['5'] == False and c49['6'] == False and c49['7'] == False and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 2
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == True and c49['4'] == False and c49['5'] == False and c49['6'] == False and c49['7'] == False and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 3
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == False and c49['4'] == True and c49['5'] == False and c49['6'] == False and c49['7'] == False and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 4
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == False and c49['4'] == False and c49['5'] == True and c49['6'] == False and c49['7'] == False and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 5
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == False and c49['4'] == False and c49['5'] == False and c49['6'] == True and c49['7'] == False and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 6
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == False and c49['4'] == False and c49['5'] == False and c49['6'] == False and c49['7'] == True and c49['8'] == False and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 7
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == False and c49['4'] == False and c49['5'] == False and c49['6'] == False and c49['7'] == False and c49['8'] == True and c49['9'] == False:
        e49do = False
        solvednums[3][8] = 8
    elif e49do == True and c49['1'] == False and c49['2'] == False and c49['3'] == False and c49['4'] == False and c49['5'] == False and c49['6'] == False and c49['7'] == False and c49['8'] == False and c49['9'] == True:
        e49do = False
        solvednums[3][8] = 9
    else:
        if solvednums[3][8] == 1:
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c45['1'] = False
            c46['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c19['1'] = False
            c29['1'] = False
            c39['1'] = False
            c79['1'] = False
            c89['1'] = False
            c99['1'] = False
        elif solvednums[3][8] == 2:
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c45['2'] = False
            c46['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c19['2'] = False
            c29['2'] = False
            c39['2'] = False
            c79['2'] = False
            c89['2'] = False
            c99['2'] = False
        elif solvednums[3][8] == 3:
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c45['3'] = False
            c46['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c19['3'] = False
            c29['3'] = False
            c39['3'] = False
            c79['3'] = False
            c89['3'] = False
            c99['3'] = False
        elif solvednums[3][8] == 4:
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c45['4'] = False
            c46['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c19['4'] = False
            c29['4'] = False
            c39['4'] = False
            c79['4'] = False
            c89['4'] = False
            c99['4'] = False
        elif solvednums[3][8] == 5:
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c45['5'] = False
            c46['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c19['5'] = False
            c29['5'] = False
            c39['5'] = False
            c79['5'] = False
            c89['5'] = False
            c99['5'] = False
        elif solvednums[3][8] == 6:
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c45['6'] = False
            c46['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c19['6'] = False
            c29['6'] = False
            c39['6'] = False
            c79['6'] = False
            c89['6'] = False
            c99['6'] = False
        elif solvednums[3][8] == 7:
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c45['7'] = False
            c46['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c19['7'] = False
            c29['7'] = False
            c39['7'] = False
            c79['7'] = False
            c89['7'] = False
            c99['7'] = False
        elif solvednums[3][8] == 8:
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c45['8'] = False
            c46['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c19['8'] = False
            c29['8'] = False
            c39['8'] = False
            c79['8'] = False
            c89['8'] = False
            c99['8'] = False
        elif solvednums[3][8] == 9:
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c45['9'] = False 
            c46['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c19['9'] = False
            c29['9'] = False
            c39['9'] = False
            c79['9'] = False   
            c89['9'] = False
            c99['9'] = False
    if puzzlenums[4][0] > 0 and e51do == True:
        solvednums[4][0] = puzzlenums[4][0]
        e51do = False
        sleep(1)
    elif e51do == True and c51['1'] == True and c51['2'] == False and c51['3'] == False and c51['4'] == False and c51['5'] == False and c51['6'] == False and c51['7'] == False and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 1
    elif e51do == True and c51['1'] == False and c51['2'] == True and c51['3'] == False and c51['4'] == False and c51['5'] == False and c51['6'] == False and c51['7'] == False and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 2
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == True and c51['4'] == False and c51['5'] == False and c51['6'] == False and c51['7'] == False and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 3
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == False and c51['4'] == True and c51['5'] == False and c51['6'] == False and c51['7'] == False and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 4
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == False and c51['4'] == False and c51['5'] == True and c51['6'] == False and c51['7'] == False and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 5
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == False and c51['4'] == False and c51['5'] == False and c51['6'] == True and c51['7'] == False and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 6
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == False and c51['4'] == False and c51['5'] == False and c51['6'] == False and c51['7'] == True and c51['8'] == False and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 7
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == False and c51['4'] == False and c51['5'] == False and c51['6'] == False and c51['7'] == False and c51['8'] == True and c51['9'] == False:
        e51do = False
        solvednums[4][0] = 8
    elif e51do == True and c51['1'] == False and c51['2'] == False and c51['3'] == False and c51['4'] == False and c51['5'] == False and c51['6'] == False and c51['7'] == False and c51['8'] == False and c51['9'] == True:
        e51do = False
        solvednums[4][0] = 9
    else:
        if solvednums[4][0] == 1:
            c51['1'] = False
            c51['2'] = False
            c51['3'] = False
            c51['4'] = False
            c51['5'] = False
            c51['6'] = False
            c51['7'] = False
            c51['8'] = False
            c51['9'] = False
            c52['1'] = False
            c53['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c11['1'] = False
            c21['1'] = False
            c31['1'] = False
            c41['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[4][0] == 2:
            c51['1'] = False
            c51['2'] = False
            c51['3'] = False
            c51['4'] = False
            c51['5'] = False
            c51['6'] = False
            c51['7'] = False
            c51['8'] = False
            c51['9'] = False
            c52['2'] = False
            c53['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c11['2'] = False
            c21['2'] = False
            c31['2'] = False
            c71['2'] = False
            c81['2'] = False
            c91['2'] = False
        elif solvednums[4][0] == 3:
            c52['3'] = False
            c53['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c11['3'] = False
            c21['3'] = False
            c31['3'] = False
            c71['3'] = False
            c81['3'] = False
            c91['3'] = False
        elif solvednums[4][0] == 4:
            c52['4'] = False
            c53['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c11['4'] = False
            c21['4'] = False
            c31['4'] = False
            c71['4'] = False
            c81['4'] = False
            c91['4'] = False
        elif solvednums[3][0] == 5:
            c52['5'] = False
            c53['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c11['5'] = False
            c21['5'] = False
            c31['5'] = False
            c71['5'] = False
            c81['5'] = False
            c91['5'] = False
        elif solvednums[4][0] == 6:
            c52['6'] = False
            c53['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c11['6'] = False
            c21['6'] = False
            c31['6'] = False
            c71['6'] = False
            c81['6'] = False
            c91['6'] = False
        elif solvednums[4][0] == 7:
            c52['7'] = False
            c53['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c11['7'] = False
            c21['7'] = False
            c31['7'] = False
            c71['7'] = False
            c81['7'] = False
            c91['7'] = False
        elif solvednums[4][0] == 8:
            c52['8'] = False
            c53['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c41['8'] = False
            c62['8'] = False
            c63['8'] = False
            c11['8'] = False
            c21['8'] = False
            c31['8'] = False
            c71['8'] = False
            c81['8'] = False
            c91['8'] = False
        elif solvednums[4][0] == 9:
            c52['9'] = False
            c53['9'] = False
            c54['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c11['9'] = False
            c21['9'] = False
            c31['9'] = False
            c71['9'] = False   
            c81['9'] = False
            c91['9'] = False
    if puzzlenums[4][1] > 0 and e52do == True:
        solvednums[4][1] = puzzlenums[4][1]
        e52do = False
        sleep(1)
    elif e52do == True and c52['1'] == True and c52['2'] == False and c52['3'] == False and c52['4'] == False and c52['5'] == False and c52['6'] == False and c52['7'] == False and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 1
    elif e52do == True and c52['1'] == False and c52['2'] == True and c52['3'] == False and c52['4'] == False and c52['5'] == False and c52['6'] == False and c52['7'] == False and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 2
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == True and c52['4'] == False and c52['5'] == False and c52['6'] == False and c52['7'] == False and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 3
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == False and c52['4'] == True and c52['5'] == False and c52['6'] == False and c52['7'] == False and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 4
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == False and c52['4'] == False and c52['5'] == True and c52['6'] == False and c52['7'] == False and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 5
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == False and c52['4'] == False and c52['5'] == False and c52['6'] == True and c52['7'] == False and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 6
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == False and c52['4'] == False and c52['5'] == False and c52['6'] == False and c52['7'] == True and c52['8'] == False and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 7
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == False and c52['4'] == False and c52['5'] == False and c52['6'] == False and c52['7'] == False and c52['8'] == True and c52['9'] == False:
        e52do = False
        solvednums[4][1] = 8
    elif e52do == True and c52['1'] == False and c52['2'] == False and c52['3'] == False and c52['4'] == False and c52['5'] == False and c52['6'] == False and c52['7'] == False and c52['8'] == False and c52['9'] == True:
        e52do = False
        solvednums[4][1] = 9
    else:
        if solvednums[4][1] == 1:
            c51['1'] = False
            c53['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c12['1'] = False
            c22['1'] = False
            c32['1'] = False
            c72['1'] = False
            c82['1'] = False
            c92['1'] = False
        elif solvednums[4][1] == 2:
            c51['2'] = False
            c53['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c12['2'] = False
            c22['2'] = False
            c32['2'] = False
            c72['2'] = False
            c82['2'] = False
            c92['2'] = False
        elif solvednums[4][1] == 3:
            c51['3'] = False
            c53['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c12['3'] = False
            c22['3'] = False
            c32['3'] = False
            c72['3'] = False
            c82['3'] = False
            c92['3'] = False
        elif solvednums[4][1] == 4:
            c51['4'] = False
            c53['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c12['4'] = False
            c22['4'] = False
            c32['4'] = False
            c72['4'] = False
            c82['4'] = False
            c92['4'] = False
        elif solvednums[4][1] == 5:
            c51['5'] = False
            c53['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c12['5'] = False
            c22['5'] = False
            c32['5'] = False
            c72['5'] = False
            c82['5'] = False
            c92['5'] = False
        elif solvednums[4][1] == 6:
            c51['6'] = False
            c53['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c12['6'] = False
            c22['6'] = False
            c32['6'] = False
            c72['6'] = False
            c82['6'] = False
            c92['6'] = False
        elif solvednums[4][1] == 7:
            c51['7'] = False
            c53['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c12['7'] = False
            c22['7'] = False
            c32['7'] = False
            c72['7'] = False
            c82['7'] = False
            c92['7'] = False
        elif solvednums[4][1] == 8:
            c51['8'] = False
            c53['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c68['8'] = False
            c62['8'] = False
            c63['8'] = False
            c12['8'] = False
            c22['8'] = False
            c32['8'] = False
            c72['8'] = False
            c82['8'] = False
            c92['8'] = False
        elif solvednums[4][1] == 9:
            c51['9'] = False
            c53['9'] = False
            c54['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c12['9'] = False
            c22['9'] = False
            c32['9'] = False
            c72['9'] = False   
            c82['9'] = False
            c92['9'] = False
    if puzzlenums[4][2] > 0 and e53do == True:
        solvednums[4][2] = puzzlenums[4][2]
        e53do = False
        sleep(1)
    elif e53do == True and c53['1'] == True and c53['2'] == False and c53['3'] == False and c53['4'] == False and c53['5'] == False and c53['6'] == False and c53['7'] == False and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 1
    elif e53do == True and c53['1'] == False and c53['2'] == True and c53['3'] == False and c53['4'] == False and c53['5'] == False and c53['6'] == False and c53['7'] == False and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 2
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == True and c53['4'] == False and c53['5'] == False and c53['6'] == False and c53['7'] == False and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 3
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == False and c53['4'] == True and c53['5'] == False and c53['6'] == False and c53['7'] == False and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 4
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == False and c53['4'] == False and c53['5'] == True and c53['6'] == False and c53['7'] == False and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 5
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == False and c53['4'] == False and c53['5'] == False and c53['6'] == True and c53['7'] == False and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 6
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == False and c53['4'] == False and c53['5'] == False and c53['6'] == False and c53['7'] == True and c53['8'] == False and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 7
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == False and c53['4'] == False and c53['5'] == False and c53['6'] == False and c53['7'] == False and c53['8'] == True and c53['9'] == False:
        e53do = False
        solvednums[4][2] = 8
    elif e53do == True and c53['1'] == False and c53['2'] == False and c53['3'] == False and c53['4'] == False and c53['5'] == False and c53['6'] == False and c53['7'] == False and c53['8'] == False and c53['9'] == True:
        e53do = False
        solvednums[4][2] = 9
    else:
        if solvednums[4][2] == 1:
            c51['1'] = False
            c52['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c13['1'] = False
            c23['1'] = False
            c33['1'] = False
            c73['1'] = False
            c83['1'] = False
            c93['1'] = False
        elif solvednums[4][2] == 2:
            c51['2'] = False
            c52['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c43['2'] = False
            c13['2'] = False
            c23['2'] = False
            c33['2'] = False
            c83['2'] = False
            c93['2'] = False
        elif solvednums[4][2] == 3:
            c51['3'] = False
            c52['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c13['3'] = False
            c23['3'] = False
            c33['3'] = False
            c73['3'] = False
            c83['3'] = False
            c93['3'] = False
        elif solvednums[4][2] == 4:
            c51['4'] = False
            c52['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c61['4'] = False
            c64['4'] = False
            c63['4'] = False
            c13['4'] = False
            c23['4'] = False
            c33['4'] = False
            c73['4'] = False
            c83['4'] = False
            c93['4'] = False
        elif solvednums[4][2] == 5:
            c51['5'] = False
            c52['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c13['5'] = False
            c23['5'] = False
            c33['5'] = False
            c73['5'] = False
            c83['5'] = False
            c93['5'] = False
        elif solvednums[4][2] == 6:
            c51['6'] = False
            c52['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c13['6'] = False
            c23['6'] = False
            c33['6'] = False
            c73['6'] = False
            c83['6'] = False
            c93['6'] = False
        elif solvednums[4][2] == 7:
            c51['7'] = False
            c52['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c13['7'] = False
            c23['7'] = False
            c33['7'] = False
            c73['7'] = False
            c83['7'] = False
            c93['7'] = False
        elif solvednums[4][2] == 8:
            c51['8'] = False
            c52['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c13['8'] = False
            c23['8'] = False
            c33['8'] = False
            c73['8'] = False
            c83['8'] = False
            c93['8'] = False
        elif solvednums[4][2] == 9:
            c51['9'] = False
            c52['9'] = False
            c54['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c13['9'] = False
            c23['9'] = False
            c33['9'] = False
            c73['9'] = False   
            c83['9'] = False
            c93['9'] = False
    if puzzlenums[4][3] > 0 and e54do == True:
        solvednums[4][3] = puzzlenums[4][3]
        e54do = False
        sleep(1)
    elif e54do == True and c54['1'] == True and c54['2'] == False and c54['3'] == False and c54['4'] == False and c54['5'] == False and c54['6'] == False and c54['7'] == False and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 1
    elif e54do == True and c54['1'] == False and c54['2'] == True and c54['3'] == False and c54['4'] == False and c54['5'] == False and c54['6'] == False and c54['7'] == False and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 2
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == True and c54['4'] == False and c54['5'] == False and c54['6'] == False and c54['7'] == False and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 3
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == False and c54['4'] == True and c54['5'] == False and c54['6'] == False and c54['7'] == False and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 4
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == False and c54['4'] == False and c54['5'] == True and c54['6'] == False and c54['7'] == False and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 5
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == False and c54['4'] == False and c54['5'] == False and c54['6'] == True and c54['7'] == False and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 6
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == False and c54['4'] == False and c54['5'] == False and c54['6'] == False and c54['7'] == True and c54['8'] == False and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 7
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == False and c54['4'] == False and c54['5'] == False and c54['6'] == False and c54['7'] == False and c54['8'] == True and c54['9'] == False:
        e54do = False
        solvednums[4][3] = 8
    elif e54do == True and c54['1'] == False and c54['2'] == False and c54['3'] == False and c54['4'] == False and c54['5'] == False and c54['6'] == False and c54['7'] == False and c54['8'] == False and c54['9'] == True:
        e54do = False
        solvednums[4][3] = 9
    else:
        if solvednums[4][3] == 1:
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c14['1'] = False
            c24['1'] = False
            c34['1'] = False
            c74['1'] = False
            c84['1'] = False
            c94['1'] = False
        elif solvednums[4][3] == 2:
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c14['2'] = False
            c24['2'] = False
            c34['2'] = False
            c74['2'] = False
            c84['2'] = False
            c94['2'] = False
        elif solvednums[4][3] == 3:
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c14['3'] = False
            c24['3'] = False
            c34['3'] = False
            c74['3'] = False
            c84['3'] = False
            c94['3'] = False
        elif solvednums[4][3] == 4:
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c14['4'] = False
            c24['4'] = False
            c34['4'] = False
            c74['4'] = False
            c84['4'] = False
            c94['4'] = False
        elif solvednums[4][3] == 5:
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c14['5'] = False
            c24['5'] = False
            c34['5'] = False
            c74['5'] = False
            c84['5'] = False
            c94['5'] = False
        elif solvednums[4][3] == 6:
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c14['6'] = False
            c24['6'] = False
            c34['6'] = False
            c74['6'] = False
            c84['6'] = False
            c94['6'] = False
        elif solvednums[4][3] == 7:
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c14['7'] = False
            c24['7'] = False
            c34['7'] = False
            c74['7'] = False
            c84['7'] = False
            c94['7'] = False
        elif solvednums[4][3] == 8:
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c14['8'] = False
            c24['8'] = False
            c34['8'] = False
            c74['8'] = False
            c84['8'] = False
            c94['8'] = False
        elif solvednums[4][3] == 9:
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c44['9'] = False
            c45['9'] = False
            c46['9'] = False
            c64['9'] = False
            c65['9'] = False
            c66['9'] = False
            c14['9'] = False
            c24['9'] = False
            c34['9'] = False
            c74['9'] = False   
            c84['9'] = False
            c94['9'] = False
    if puzzlenums[4][4] > 0 and e55do == True:
        solvednums[4][4] = puzzlenums[4][4]
        e55do = False
        sleep(1)
    elif e55do == True and c55['1'] == True and c55['2'] == False and c55['3'] == False and c55['4'] == False and c55['5'] == False and c55['6'] == False and c55['7'] == False and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 1
    elif e55do == True and c55['1'] == False and c55['2'] == True and c55['3'] == False and c55['4'] == False and c55['5'] == False and c55['6'] == False and c55['7'] == False and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 2
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == True and c55['4'] == False and c55['5'] == False and c55['6'] == False and c55['7'] == False and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 3
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == False and c55['4'] == True and c55['5'] == False and c55['6'] == False and c55['7'] == False and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 4
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == False and c55['4'] == False and c55['5'] == True and c55['6'] == False and c55['7'] == False and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 5
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == False and c55['4'] == False and c55['5'] == False and c55['6'] == True and c55['7'] == False and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 6
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == False and c55['4'] == False and c55['5'] == False and c55['6'] == False and c55['7'] == True and c55['8'] == False and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 7
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == False and c55['4'] == False and c55['5'] == False and c55['6'] == False and c55['7'] == False and c55['8'] == True and c55['9'] == False:
        e55do = False
        solvednums[4][4] = 8
    elif e55do == True and c55['1'] == False and c55['2'] == False and c55['3'] == False and c55['4'] == False and c55['5'] == False and c55['6'] == False and c55['7'] == False and c55['8'] == False and c55['9'] == True:
        e55do = False
        solvednums[4][4] = 9
    else:
        if solvednums[4][4] == 1:
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c15['1'] = False
            c25['1'] = False
            c35['1'] = False
            c75['1'] = False
            c85['1'] = False
            c95['1'] = False
        elif solvednums[4][4] == 2:
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c15['2'] = False
            c25['2'] = False
            c35['2'] = False
            c75['2'] = False
            c85['2'] = False
            c95['2'] = False
        elif solvednums[4][4] == 3:
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c15['3'] = False
            c25['3'] = False
            c35['3'] = False
            c75['3'] = False
            c85['3'] = False
            c95['3'] = False
        elif solvednums[4][4] == 4:
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c15['4'] = False
            c25['4'] = False
            c35['4'] = False
            c75['4'] = False
            c85['4'] = False
            c95['4'] = False
        elif solvednums[4][4] == 5:
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c15['5'] = False
            c25['5'] = False
            c35['5'] = False
            c75['5'] = False
            c85['5'] = False
            c95['5'] = False
        elif solvednums[4][4] == 6:
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c15['6'] = False
            c25['6'] = False
            c35['6'] = False
            c75['6'] = False
            c85['6'] = False
            c95['6'] = False
        elif solvednums[4][4] == 7:
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c15['7'] = False
            c25['7'] = False
            c35['7'] = False
            c75['7'] = False
            c85['7'] = False
            c95['7'] = False
        elif solvednums[4][4] == 8:
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c15['8'] = False
            c25['8'] = False
            c35['8'] = False
            c75['8'] = False
            c85['8'] = False
            c95['8'] = False
        elif solvednums[4][4] == 9:
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c44['9'] = False
            c45['9'] = False
            c46['9'] = False
            c64['9'] = False
            c65['9'] = False
            c66['9'] = False
            c15['9'] = False
            c25['9'] = False
            c35['9'] = False
            c75['9'] = False   
            c85['9'] = False
            c95['9'] = False
    if puzzlenums[4][5] > 0 and e56do == True:
        solvednums[4][5] = puzzlenums[4][5]
        e56do = False
        sleep(1)
    elif e56do == True and c56['1'] == True and c56['2'] == False and c56['3'] == False and c56['4'] == False and c56['5'] == False and c56['6'] == False and c56['7'] == False and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 1
    elif e56do == True and c56['1'] == False and c56['2'] == True and c56['3'] == False and c56['4'] == False and c56['5'] == False and c56['6'] == False and c56['7'] == False and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 2
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == True and c56['4'] == False and c56['5'] == False and c56['6'] == False and c56['7'] == False and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 3
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == False and c56['4'] == True and c56['5'] == False and c56['6'] == False and c56['7'] == False and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][6] = 4
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == False and c56['4'] == False and c56['5'] == True and c56['6'] == False and c56['7'] == False and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 5
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == False and c56['4'] == False and c56['5'] == False and c56['6'] == True and c56['7'] == False and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 6
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == False and c56['4'] == False and c56['5'] == False and c56['6'] == False and c56['7'] == True and c56['8'] == False and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 7
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == False and c56['4'] == False and c56['5'] == False and c56['6'] == False and c56['7'] == False and c56['8'] == True and c56['9'] == False:
        e56do = False
        solvednums[4][5] = 8
    elif e56do == True and c56['1'] == False and c56['2'] == False and c56['3'] == False and c56['4'] == False and c56['5'] == False and c56['6'] == False and c56['7'] == False and c56['8'] == False and c56['9'] == True:
        e56do = False
        solvednums[4][5] = 9     
    else:
        if solvednums[4][5] == 1:
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c16['1'] = False
            c26['1'] = False
            c36['1'] = False
            c76['1'] = False
            c86['1'] = False
            c96['1'] = False
        elif solvednums[4][5] == 2: 
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c16['2'] = False
            c26['2'] = False
            c36['2'] = False
            c76['2'] = False
            c86['2'] = False
            c96['2'] = False
        elif solvednums[4][5] == 3:
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c16['3'] = False
            c26['3'] = False
            c36['3'] = False
            c76['3'] = False
            c86['3'] = False
            c96['3'] = False
        elif solvednums[4][5] == 4:
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c16['4'] = False
            c26['4'] = False
            c36['4'] = False
            c76['4'] = False
            c86['4'] = False
            c96['4'] = False
        elif solvednums[4][5] == 5:
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c16['5'] = False
            c26['5'] = False
            c36['5'] = False
            c76['5'] = False
            c86['5'] = False
            c96['5'] = False
        elif solvednums[4][5] == 6:
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c16['6'] = False
            c26['6'] = False
            c36['6'] = False
            c76['6'] = False
            c86['6'] = False
            c96['6'] = False
        elif solvednums[4][5] == 7:
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c16['7'] = False
            c26['7'] = False
            c36['7'] = False
            c76['7'] = False
            c86['7'] = False
            c96['7'] = False
        elif solvednums[4][5] == 8:
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c16['8'] = False
            c26['8'] = False
            c36['8'] = False
            c76['8'] = False
            c86['8'] = False
            c96['8'] = False
        elif solvednums[4][5] == 9:
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c44['9'] = False
            c45['9'] = False
            c46['9'] = False
            c64['9'] = False
            c65['9'] = False
            c66['9'] = False
            c16['9'] = False
            c26['9'] = False
            c36['9'] = False
            c76['9'] = False   
            c86['9'] = False
            c96['9'] = False
    if puzzlenums[4][6] > 0 and e57do == True:
        solvednums[4][6] = puzzlenums[4][6]
        e57do = False
        sleep(1)
    elif e57do == True and c57['1'] == True and c57['2'] == False and c57['3'] == False and c57['4'] == False and c57['5'] == False and c57['6'] == False and c57['7'] == False and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 1
    elif e57do == True and c57['1'] == False and c57['2'] == True and c57['3'] == False and c57['4'] == False and c57['5'] == False and c57['6'] == False and c57['7'] == False and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 2
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == True and c57['4'] == False and c57['5'] == False and c57['6'] == False and c57['7'] == False and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 3
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == False and c57['4'] == True and c57['5'] == False and c57['6'] == False and c57['7'] == False and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 4
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == False and c57['4'] == False and c57['5'] == True and c57['6'] == False and c57['7'] == False and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 5
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == False and c57['4'] == False and c57['5'] == False and c57['6'] == True and c57['7'] == False and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 6
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == False and c57['4'] == False and c57['5'] == False and c57['6'] == False and c57['7'] == True and c57['8'] == False and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 7
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == False and c57['4'] == False and c57['5'] == False and c57['6'] == False and c57['7'] == False and c57['8'] == True and c57['9'] == False:
        e57do = False
        solvednums[4][6] = 8
    elif e57do == True and c57['1'] == False and c57['2'] == False and c57['3'] == False and c57['4'] == False and c57['5'] == False and c57['6'] == False and c57['7'] == False and c57['8'] == False and c57['9'] == True:
        e57do = False
        solvednums[4][6] = 9
    else:
        if solvednums[4][6] == 1:
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c17['1'] = False
            c27['1'] = False
            c37['1'] = False
            c77['1'] = False
            c87['1'] = False
            c97['1'] = False
        elif solvednums[4][6] == 2:
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c17['2'] = False
            c27['2'] = False
            c37['2'] = False
            c77['2'] = False
            c87['2'] = False
            c97['2'] = False
        elif solvednums[4][6] == 3:
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c17['3'] = False
            c27['3'] = False
            c37['3'] = False
            c77['3'] = False
            c87['3'] = False
            c97['3'] = False
        elif solvednums[4][6] == 4:
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c17['4'] = False
            c27['4'] = False
            c37['4'] = False
            c77['4'] = False
            c87['4'] = False
            c97['4'] = False
        elif solvednums[4][6] == 5:
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c17['5'] = False
            c27['5'] = False
            c37['5'] = False
            c77['5'] = False
            c87['5'] = False
            c97['5'] = False
        elif solvednums[4][6] == 6:
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c17['6'] = False
            c27['6'] = False
            c37['6'] = False
            c77['6'] = False
            c87['6'] = False
            c97['6'] = False
        elif solvednums[4][6] == 7:
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c17['7'] = False
            c27['7'] = False
            c37['7'] = False
            c77['7'] = False
            c87['7'] = False
            c97['7'] = False
        elif solvednums[4][6] == 8:
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c17['8'] = False
            c27['8'] = False
            c37['8'] = False
            c77['8'] = False
            c87['8'] = False
            c97['8'] = False
        elif solvednums[4][6] == 9:
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c17['9'] = False
            c27['9'] = False
            c37['9'] = False
            c77['9'] = False   
            c87['9'] = False
            c97['9'] = False
    if puzzlenums[4][7] > 0 and e58do == True:
        solvednums[4][7] = puzzlenums[4][7]
        e58do = False
        sleep(1)
    elif e58do == True and c58['1'] == True and c58['2'] == False and c58['3'] == False and c58['4'] == False and c58['5'] == False and c58['6'] == False and c58['7'] == False and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 1
    elif e58do == True and c58['1'] == False and c58['2'] == True and c58['3'] == False and c58['4'] == False and c58['5'] == False and c58['6'] == False and c58['7'] == False and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 2
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == True and c58['4'] == False and c58['5'] == False and c58['6'] == False and c58['7'] == False and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 3
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == False and c58['4'] == True and c58['5'] == False and c58['6'] == False and c58['7'] == False and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 4
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == False and c58['4'] == False and c58['5'] == True and c58['6'] == False and c58['7'] == False and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 5
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == False and c58['4'] == False and c58['5'] == False and c58['6'] == True and c58['7'] == False and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 6
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == False and c58['4'] == False and c58['5'] == False and c58['6'] == False and c58['7'] == True and c58['8'] == False and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 7
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == False and c58['4'] == False and c58['5'] == False and c58['6'] == False and c58['7'] == False and c58['8'] == True and c58['9'] == False:
        e58do = False
        solvednums[4][7] = 8
    elif e58do == True and c58['1'] == False and c58['2'] == False and c58['3'] == False and c58['4'] == False and c58['5'] == False and c58['6'] == False and c58['7'] == False and c58['8'] == False and c58['9'] == True:
        e58do = False
        solvednums[4][7] = 9
    else:
        if solvednums[4][7] == 1:
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c18['1'] = False
            c28['1'] = False
            c38['1'] = False
            c78['1'] = False
            c88['1'] = False
            c98['1'] = False
        elif solvednums[4][7] == 2:
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c18['2'] = False
            c28['2'] = False
            c38['2'] = False
            c78['2'] = False
            c88['2'] = False
            c98['2'] = False
        elif solvednums[4][7] == 3:
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c18['3'] = False
            c28['3'] = False
            c38['3'] = False
            c78['3'] = False
            c88['3'] = False
            c98['3'] = False
        elif solvednums[4][7] == 4:
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c18['4'] = False
            c28['4'] = False
            c38['4'] = False
            c78['4'] = False
            c88['4'] = False
            c98['4'] = False
        elif solvednums[4][7] == 5:
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c69['5'] = False
            c68['5'] = False
            c69['5'] = False
            c18['5'] = False
            c28['5'] = False
            c38['5'] = False
            c78['5'] = False
            c88['5'] = False
            c98['5'] = False
        elif solvednums[4][7] == 6:
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c18['6'] = False
            c28['6'] = False
            c38['6'] = False
            c78['6'] = False
            c88['6'] = False
            c98['6'] = False
        elif solvednums[4][7] == 7:
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c18['7'] = False
            c28['7'] = False
            c38['7'] = False
            c78['7'] = False
            c88['7'] = False
            c98['7'] = False
        elif solvednums[4][7] == 8:
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c18['8'] = False
            c28['8'] = False
            c38['8'] = False
            c78['8'] = False
            c88['8'] = False
            c98['8'] = False
        elif solvednums[4][7] == 9:
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c18['9'] = False
            c28['9'] = False
            c38['9'] = False
            c78['9'] = False   
            c88['9'] = False
            c98['9'] = False
    if puzzlenums[4][8] > 0 and e59do == True:
        solvednums[4][8] = puzzlenums[4][8]
        e59do = False
        sleep(1)
    elif e59do == True and c59['1'] == True and c59['2'] == False and c59['3'] == False and c59['4'] == False and c59['5'] == False and c59['6'] == False and c59['7'] == False and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 1
    elif e59do == True and c59['1'] == False and c59['2'] == True and c59['3'] == False and c59['4'] == False and c59['5'] == False and c59['6'] == False and c59['7'] == False and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 2
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == True and c59['4'] == False and c59['5'] == False and c59['6'] == False and c59['7'] == False and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 3
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == False and c59['4'] == True and c59['5'] == False and c59['6'] == False and c59['7'] == False and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 4
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == False and c59['4'] == False and c59['5'] == True and c59['6'] == False and c59['7'] == False and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 5
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == False and c59['4'] == False and c59['5'] == False and c59['6'] == True and c59['7'] == False and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 6
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == False and c59['4'] == False and c59['5'] == False and c59['6'] == False and c59['7'] == True and c59['8'] == False and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 7
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == False and c59['4'] == False and c59['5'] == False and c59['6'] == False and c59['7'] == False and c59['8'] == True and c59['9'] == False:
        e59do = False
        solvednums[4][8] = 8
    elif e59do == True and c59['1'] == False and c59['2'] == False and c59['3'] == False and c59['4'] == False and c59['5'] == False and c59['6'] == False and c59['7'] == False and c59['8'] == False and c59['9'] == True:
        e59do = False
        solvednums[4][8] = 9
    else:
        if solvednums[4][8] == 1:
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c55['1'] = False
            c56['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c19['1'] = False
            c29['1'] = False
            c39['1'] = False
            c79['1'] = False
            c89['1'] = False
            c99['1'] = False
        elif solvednums[4][8] == 2:
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c55['2'] = False
            c56['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c19['2'] = False
            c29['2'] = False
            c39['2'] = False
            c79['2'] = False
            c89['2'] = False
            c99['2'] = False
        elif solvednums[4][8] == 3:
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c55['3'] = False
            c56['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c19['3'] = False
            c29['3'] = False
            c39['3'] = False
            c79['3'] = False
            c89['3'] = False
            c99['3'] = False
        elif solvednums[4][8] == 4:
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c55['4'] = False
            c56['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c19['4'] = False
            c29['4'] = False
            c39['4'] = False
            c79['4'] = False
            c89['4'] = False
            c99['4'] = False
        elif solvednums[4][8] == 5:
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c55['5'] = False
            c56['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c19['5'] = False
            c29['5'] = False
            c39['5'] = False
            c79['5'] = False
            c89['5'] = False
            c99['5'] = False
        elif solvednums[4][8] == 6:
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c55['6'] = False
            c56['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c19['6'] = False
            c29['6'] = False
            c39['6'] = False
            c79['6'] = False
            c89['6'] = False
            c99['6'] = False
        elif solvednums[4][8] == 7:
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c55['7'] = False
            c56['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c19['7'] = False
            c29['7'] = False
            c39['7'] = False
            c79['7'] = False
            c89['7'] = False
            c99['7'] = False
        elif solvednums[4][8] == 8:
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c55['8'] = False
            c56['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c19['8'] = False
            c29['8'] = False
            c39['8'] = False
            c79['8'] = False
            c89['8'] = False
            c99['8'] = False
        elif solvednums[4][8] == 9:
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c55['9'] = False 
            c56['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c19['9'] = False
            c29['9'] = False
            c39['9'] = False
            c79['9'] = False   
            c89['9'] = False
            c99['9'] = False
    if puzzlenums[5][0] > 0 and e61do == True:
        solvednums[5][0] = puzzlenums[5][0]
        e61do = False
        sleep(1)
    elif e61do == True and c61['1'] == True and c61['2'] == False and c61['3'] == False and c61['4'] == False and c61['5'] == False and c61['6'] == False and c61['7'] == False and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 1
    elif e61do == True and c61['1'] == False and c61['2'] == True and c61['3'] == False and c61['4'] == False and c61['5'] == False and c61['6'] == False and c61['7'] == False and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 2
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == True and c61['4'] == False and c61['5'] == False and c61['6'] == False and c61['7'] == False and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 3
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == False and c61['4'] == True and c61['5'] == False and c61['6'] == False and c61['7'] == False and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 4
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == False and c61['4'] == False and c61['5'] == True and c61['6'] == False and c61['7'] == False and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 5
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == False and c61['4'] == False and c61['5'] == False and c61['6'] == True and c61['7'] == False and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 6
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == False and c61['4'] == False and c61['5'] == False and c61['6'] == False and c61['7'] == True and c61['8'] == False and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 7
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == False and c61['4'] == False and c61['5'] == False and c61['6'] == False and c61['7'] == False and c61['8'] == True and c61['9'] == False:
        e61do = False
        solvednums[5][0] = 8
    elif e61do == True and c61['1'] == False and c61['2'] == False and c61['3'] == False and c61['4'] == False and c61['5'] == False and c61['6'] == False and c61['7'] == False and c61['8'] == False and c61['9'] == True:
        e61do = False
        solvednums[5][0] = 9
    else:
        if solvednums[5][0] == 1:
            c61['1'] = False
            c61['2'] = False
            c61['3'] = False
            c61['4'] = False
            c61['5'] = False
            c61['6'] = False
            c61['7'] = False
            c61['8'] = False
            c61['9'] = False
            c62['1'] = False
            c63['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c11['1'] = False
            c21['1'] = False
            c31['1'] = False
            c41['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[5][0] == 2:
            c61['1'] = False
            c61['2'] = False
            c61['3'] = False
            c61['4'] = False
            c61['5'] = False
            c61['6'] = False
            c61['7'] = False
            c61['8'] = False
            c61['9'] = False
            c62['2'] = False
            c63['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c11['2'] = False
            c21['2'] = False
            c31['2'] = False
            c71['2'] = False
            c81['2'] = False
            c91['2'] = False
        elif solvednums[5][0] == 3:
            c62['3'] = False
            c63['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c11['3'] = False
            c21['3'] = False
            c31['3'] = False
            c71['3'] = False
            c81['3'] = False
            c91['3'] = False
        elif solvednums[5][0] == 4:
            c62['4'] = False
            c63['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c11['4'] = False
            c21['4'] = False
            c31['4'] = False
            c71['4'] = False
            c81['4'] = False
            c91['4'] = False
        elif solvednums[5][0] == 5:
            c62['5'] = False
            c63['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c11['5'] = False
            c21['5'] = False
            c31['5'] = False
            c71['5'] = False
            c81['5'] = False
            c91['5'] = False
        elif solvednums[5][0] == 6:
            c62['6'] = False
            c63['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c11['6'] = False
            c21['6'] = False
            c31['6'] = False
            c71['6'] = False
            c81['6'] = False
            c91['6'] = False
        elif solvednums[5][0] == 7:
            c62['7'] = False
            c63['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c11['7'] = False
            c21['7'] = False
            c31['7'] = False
            c71['7'] = False
            c81['7'] = False
            c91['7'] = False
        elif solvednums[5][0] == 8:
            c62['8'] = False
            c63['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c11['8'] = False
            c21['8'] = False
            c31['8'] = False
            c71['8'] = False
            c81['8'] = False
            c91['8'] = False
        elif solvednums[5][0] == 9:
            c62['9'] = False
            c63['9'] = False
            c64['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c11['9'] = False
            c21['9'] = False
            c31['9'] = False
            c71['9'] = False   
            c81['9'] = False
            c91['9'] = False
    if puzzlenums[5][1] > 0 and e62do == True:
        solvednums[5][1] = puzzlenums[5][1]
        e62do = False
        sleep(1)
    elif e62do == True and c62['1'] == True and c62['2'] == False and c62['3'] == False and c62['4'] == False and c62['5'] == False and c62['6'] == False and c62['7'] == False and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 1
    elif e62do == True and c62['1'] == False and c62['2'] == True and c62['3'] == False and c62['4'] == False and c62['5'] == False and c62['6'] == False and c62['7'] == False and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 2
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == True and c62['4'] == False and c62['5'] == False and c62['6'] == False and c62['7'] == False and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 3
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == False and c62['4'] == True and c62['5'] == False and c62['6'] == False and c62['7'] == False and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 4
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == False and c62['4'] == False and c62['5'] == True and c62['6'] == False and c62['7'] == False and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 5
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == False and c62['4'] == False and c62['5'] == False and c62['6'] == True and c62['7'] == False and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 6
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == False and c62['4'] == False and c62['5'] == False and c62['6'] == False and c62['7'] == True and c62['8'] == False and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 7
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == False and c62['4'] == False and c62['5'] == False and c62['6'] == False and c62['7'] == False and c62['8'] == True and c62['9'] == False:
        e62do = False
        solvednums[5][1] = 8
    elif e62do == True and c62['1'] == False and c62['2'] == False and c62['3'] == False and c62['4'] == False and c62['5'] == False and c62['6'] == False and c62['7'] == False and c62['8'] == False and c62['9'] == True:
        e62do = False
        solvednums[5][1] = 9
    else:
        if solvednums[5][1] == 1:
            c61['1'] = False
            c63['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c12['1'] = False
            c22['1'] = False
            c32['1'] = False
            c72['1'] = False
            c82['1'] = False
            c92['1'] = False
        elif solvednums[5][1] == 2:
            c61['2'] = False
            c63['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c12['2'] = False
            c22['2'] = False
            c32['2'] = False
            c72['2'] = False
            c82['2'] = False
            c92['2'] = False
        elif solvednums[5][1] == 3:
            c61['3'] = False
            c63['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c12['3'] = False
            c22['3'] = False
            c32['3'] = False
            c72['3'] = False
            c82['3'] = False
            c92['3'] = False
        elif solvednums[5][1] == 4:
            c61['4'] = False
            c63['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c51['4'] = False
            c52['4'] = False
            c53['4'] = False
            c12['4'] = False
            c22['4'] = False
            c32['4'] = False
            c72['4'] = False
            c82['4'] = False
            c92['4'] = False
        elif solvednums[5][1] == 5:
            c61['5'] = False
            c63['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c12['5'] = False
            c22['5'] = False
            c32['5'] = False
            c72['5'] = False
            c82['5'] = False
            c92['5'] = False
        elif solvednums[5][1] == 6:
            c61['6'] = False
            c63['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c12['6'] = False
            c22['6'] = False
            c32['6'] = False
            c72['6'] = False
            c82['6'] = False
            c92['6'] = False
        elif solvednums[5][1] == 7:
            c61['7'] = False
            c63['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c12['7'] = False
            c22['7'] = False
            c32['7'] = False
            c72['7'] = False
            c82['7'] = False
            c92['7'] = False
        elif solvednums[5][1] == 8:
            c61['8'] = False
            c63['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c12['8'] = False
            c22['8'] = False
            c32['8'] = False
            c72['8'] = False
            c82['8'] = False
            c92['8'] = False
        elif solvednums[5][1] == 9:
            c61['9'] = False
            c63['9'] = False
            c64['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c12['9'] = False
            c22['9'] = False
            c32['9'] = False
            c72['9'] = False   
            c82['9'] = False
            c92['9'] = False
    if puzzlenums[5][2] > 0 and e63do == True:
        solvednums[5][2] = puzzlenums[5][2]
        e63do = False
        sleep(1)
    elif e63do == True and c63['1'] == True and c63['2'] == False and c63['3'] == False and c63['4'] == False and c63['5'] == False and c63['6'] == False and c63['7'] == False and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 1
    elif e63do == True and c63['1'] == False and c63['2'] == True and c63['3'] == False and c63['4'] == False and c63['5'] == False and c63['6'] == False and c63['7'] == False and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 2
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == True and c63['4'] == False and c63['5'] == False and c63['6'] == False and c63['7'] == False and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 3
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == False and c63['4'] == True and c63['5'] == False and c63['6'] == False and c63['7'] == False and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 4
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == False and c63['4'] == False and c63['5'] == True and c63['6'] == False and c63['7'] == False and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 5
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == False and c63['4'] == False and c63['5'] == False and c63['6'] == True and c63['7'] == False and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 6
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == False and c63['4'] == False and c63['5'] == False and c63['6'] == False and c63['7'] == True and c63['8'] == False and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 7
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == False and c63['4'] == False and c63['5'] == False and c63['6'] == False and c63['7'] == False and c63['8'] == True and c63['9'] == False:
        e63do = False
        solvednums[5][2] = 8
    elif e63do == True and c63['1'] == False and c63['2'] == False and c63['3'] == False and c63['4'] == False and c63['5'] == False and c63['6'] == False and c63['7'] == False and c63['8'] == False and c63['9'] == True:
        e63do = False
        solvednums[5][2] = 9
    else:
        if solvednums[5][2] == 1:
            c61['1'] = False
            c62['1'] = False
            c64['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c41['1'] = False
            c42['1'] = False
            c43['1'] = False
            c51['1'] = False
            c52['1'] = False
            c53['1'] = False
            c13['1'] = False
            c23['1'] = False
            c33['1'] = False
            c73['1'] = False
            c83['1'] = False
            c93['1'] = False
        elif solvednums[5][2] == 2:
            c61['2'] = False
            c62['2'] = False
            c64['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c41['2'] = False
            c42['2'] = False
            c43['2'] = False
            c51['2'] = False
            c52['2'] = False
            c53['2'] = False
            c43['2'] = False
            c13['2'] = False
            c23['2'] = False
            c33['2'] = False
            c83['2'] = False
            c93['2'] = False
        elif solvednums[5][2] == 3:
            c61['3'] = False
            c62['3'] = False
            c64['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c41['3'] = False
            c42['3'] = False
            c43['3'] = False
            c51['3'] = False
            c52['3'] = False
            c53['3'] = False
            c13['3'] = False
            c23['3'] = False
            c33['3'] = False
            c73['3'] = False
            c83['3'] = False
            c93['3'] = False
        elif solvednums[5][2] == 4:
            c61['4'] = False
            c62['4'] = False
            c64['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c41['4'] = False
            c42['4'] = False
            c43['4'] = False
            c51['4'] = False
            c54['4'] = False
            c53['4'] = False
            c13['4'] = False
            c23['4'] = False
            c33['4'] = False
            c73['4'] = False
            c83['4'] = False
            c93['4'] = False
        elif solvednums[5][2] == 5:
            c61['5'] = False
            c62['5'] = False
            c64['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c41['5'] = False
            c42['5'] = False
            c43['5'] = False
            c51['5'] = False
            c52['5'] = False
            c53['5'] = False
            c13['5'] = False
            c23['5'] = False
            c33['5'] = False
            c73['5'] = False
            c83['5'] = False
            c93['5'] = False
        elif solvednums[5][2] == 6:
            c61['6'] = False
            c62['6'] = False
            c64['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c41['6'] = False
            c42['6'] = False
            c43['6'] = False
            c51['6'] = False
            c52['6'] = False
            c53['6'] = False
            c13['6'] = False
            c23['6'] = False
            c33['6'] = False
            c73['6'] = False
            c83['6'] = False
            c93['6'] = False
        elif solvednums[5][2] == 7:
            c61['7'] = False
            c62['7'] = False
            c64['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c41['7'] = False
            c42['7'] = False
            c43['7'] = False
            c51['7'] = False
            c52['7'] = False
            c53['7'] = False
            c13['7'] = False
            c23['7'] = False
            c33['7'] = False
            c73['7'] = False
            c83['7'] = False
            c93['7'] = False
        elif solvednums[5][2] == 8:
            c61['8'] = False
            c62['8'] = False
            c64['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c41['8'] = False
            c42['8'] = False
            c43['8'] = False
            c51['8'] = False
            c52['8'] = False
            c53['8'] = False
            c13['8'] = False
            c23['8'] = False
            c33['8'] = False
            c73['8'] = False
            c83['8'] = False
            c93['8'] = False
        elif solvednums[5][2] == 9:
            c61['9'] = False
            c62['9'] = False
            c64['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c41['9'] = False
            c42['9'] = False
            c43['9'] = False
            c51['9'] = False
            c52['9'] = False
            c53['9'] = False
            c13['9'] = False
            c23['9'] = False
            c33['9'] = False
            c73['9'] = False   
            c83['9'] = False
            c93['9'] = False
    if puzzlenums[5][3] > 0 and e64do == True:
        solvednums[5][3] = puzzlenums[5][3]
        e64do = False
        sleep(1)
    elif e64do == True and c64['1'] == True and c64['2'] == False and c64['3'] == False and c64['4'] == False and c64['5'] == False and c64['6'] == False and c64['7'] == False and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 1
    elif e64do == True and c64['1'] == False and c64['2'] == True and c64['3'] == False and c64['4'] == False and c64['5'] == False and c64['6'] == False and c64['7'] == False and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 2
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == True and c64['4'] == False and c64['5'] == False and c64['6'] == False and c64['7'] == False and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 3
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == False and c64['4'] == True and c64['5'] == False and c64['6'] == False and c64['7'] == False and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 4
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == False and c64['4'] == False and c64['5'] == True and c64['6'] == False and c64['7'] == False and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 5
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == False and c64['4'] == False and c64['5'] == False and c64['6'] == True and c64['7'] == False and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 6
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == False and c64['4'] == False and c64['5'] == False and c64['6'] == False and c64['7'] == True and c64['8'] == False and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 7
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == False and c64['4'] == False and c64['5'] == False and c64['6'] == False and c64['7'] == False and c64['8'] == True and c64['9'] == False:
        e64do = False
        solvednums[5][3] = 8
    elif e64do == True and c64['1'] == False and c64['2'] == False and c64['3'] == False and c64['4'] == False and c64['5'] == False and c64['6'] == False and c64['7'] == False and c64['8'] == False and c64['9'] == True:
        e64do = False
        solvednums[5][3] = 9
    else:
        if solvednums[5][3] == 1:
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c14['1'] = False
            c24['1'] = False
            c34['1'] = False
            c74['1'] = False
            c84['1'] = False
            c94['1'] = False
        elif solvednums[5][3] == 2:
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c14['2'] = False
            c24['2'] = False
            c34['2'] = False
            c74['2'] = False
            c84['2'] = False
            c94['2'] = False
        elif solvednums[5][3] == 3:
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c14['3'] = False
            c24['3'] = False
            c34['3'] = False
            c74['3'] = False
            c84['3'] = False
            c94['3'] = False
        elif solvednums[5][3] == 4:
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c14['4'] = False
            c24['4'] = False
            c34['4'] = False
            c74['4'] = False
            c84['4'] = False
            c94['4'] = False
        elif solvednums[5][3] == 5:
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c14['5'] = False
            c24['5'] = False
            c34['5'] = False
            c74['5'] = False
            c84['5'] = False
            c94['5'] = False
        elif solvednums[5][3] == 6:
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c14['6'] = False
            c24['6'] = False
            c34['6'] = False
            c74['6'] = False
            c84['6'] = False
            c94['6'] = False
        elif solvednums[5][3] == 7:
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c14['7'] = False
            c24['7'] = False
            c34['7'] = False
            c74['7'] = False
            c84['7'] = False
            c94['7'] = False
        elif solvednums[5][3] == 8:
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c14['8'] = False
            c24['8'] = False
            c34['8'] = False
            c74['8'] = False
            c84['8'] = False
            c94['8'] = False
        elif solvednums[5][3] == 9:
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c44['9'] = False
            c45['9'] = False
            c46['9'] = False
            c54['9'] = False
            c55['9'] = False
            c56['9'] = False
            c14['9'] = False
            c24['9'] = False
            c34['9'] = False
            c74['9'] = False   
            c84['9'] = False
            c94['9'] = False
    if puzzlenums[5][5] > 0 and e65do == True:
        solvednums[5][4] = puzzlenums[5][4]
        e65do = False
        sleep(1)
    elif e65do == True and c65['1'] == True and c65['2'] == False and c65['3'] == False and c65['4'] == False and c65['5'] == False and c65['6'] == False and c65['7'] == False and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 1
    elif e65do == True and c65['1'] == False and c65['2'] == True and c65['3'] == False and c65['4'] == False and c65['5'] == False and c65['6'] == False and c65['7'] == False and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 2
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == True and c65['4'] == False and c65['5'] == False and c65['6'] == False and c65['7'] == False and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 3
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == False and c65['4'] == True and c65['5'] == False and c65['6'] == False and c65['7'] == False and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 4
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == False and c65['4'] == False and c65['5'] == True and c65['6'] == False and c65['7'] == False and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 5
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == False and c65['4'] == False and c65['5'] == False and c65['6'] == True and c65['7'] == False and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 6
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == False and c65['4'] == False and c65['5'] == False and c65['6'] == False and c65['7'] == True and c65['8'] == False and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 7
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == False and c65['4'] == False and c65['5'] == False and c65['6'] == False and c65['7'] == False and c65['8'] == True and c65['9'] == False:
        e65do = False
        solvednums[5][4] = 8
    elif e65do == True and c65['1'] == False and c65['2'] == False and c65['3'] == False and c65['4'] == False and c65['5'] == False and c65['6'] == False and c65['7'] == False and c65['8'] == False and c65['9'] == True:
        e65do = False
        solvednums[5][4] = 9
    else:
        if solvednums[5][4] == 1:
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c15['1'] = False
            c25['1'] = False
            c35['1'] = False
            c75['1'] = False
            c85['1'] = False
            c95['1'] = False
        elif solvednums[5][4] == 2:
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c15['2'] = False
            c25['2'] = False
            c35['2'] = False
            c75['2'] = False
            c85['2'] = False
            c95['2'] = False
        elif solvednums[5][4] == 3:
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c15['3'] = False
            c25['3'] = False
            c35['3'] = False
            c75['3'] = False
            c85['3'] = False
            c95['3'] = False
        elif solvednums[5][4] == 4:
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c15['4'] = False
            c25['4'] = False
            c35['4'] = False
            c75['4'] = False
            c85['4'] = False
            c95['4'] = False
        elif solvednums[5][4] == 5:
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c15['5'] = False
            c25['5'] = False
            c35['5'] = False
            c75['5'] = False
            c85['5'] = False
            c95['5'] = False
        elif solvednums[5][4] == 6:
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c15['6'] = False
            c25['6'] = False
            c35['6'] = False
            c75['6'] = False
            c85['6'] = False
            c95['6'] = False
        elif solvednums[5][4] == 7:
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c15['7'] = False
            c25['7'] = False
            c35['7'] = False
            c75['7'] = False
            c85['7'] = False
            c95['7'] = False
        elif solvednums[5][4] == 8:
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c15['8'] = False
            c25['8'] = False
            c35['8'] = False
            c75['8'] = False
            c85['8'] = False
            c95['8'] = False
        elif solvednums[5][4] == 9:
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c44['9'] = False
            c45['9'] = False
            c46['9'] = False
            c54['9'] = False
            c55['9'] = False
            c56['9'] = False
            c15['9'] = False
            c25['9'] = False
            c35['9'] = False
            c75['9'] = False   
            c85['9'] = False
            c95['9'] = False
    if puzzlenums[5][5] > 0 and e66do == True:
        solvednums[5][5] = puzzlenums[5][5]
        e66do = False
        sleep(1)
    elif e66do == True and c66['1'] == True and c66['2'] == False and c66['3'] == False and c66['4'] == False and c66['5'] == False and c66['6'] == False and c66['7'] == False and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 1
    elif e66do == True and c66['1'] == False and c66['2'] == True and c66['3'] == False and c66['4'] == False and c66['5'] == False and c66['6'] == False and c66['7'] == False and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 2
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == True and c66['4'] == False and c66['5'] == False and c66['6'] == False and c66['7'] == False and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 3
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == False and c66['4'] == True and c66['5'] == False and c66['6'] == False and c66['7'] == False and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][6] = 4
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == False and c66['4'] == False and c66['5'] == True and c66['6'] == False and c66['7'] == False and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 5
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == False and c66['4'] == False and c66['5'] == False and c66['6'] == True and c66['7'] == False and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 6
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == False and c66['4'] == False and c66['5'] == False and c66['6'] == False and c66['7'] == True and c66['8'] == False and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 7
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == False and c66['4'] == False and c66['5'] == False and c66['6'] == False and c66['7'] == False and c66['8'] == True and c66['9'] == False:
        e66do = False
        solvednums[5][5] = 8
    elif e66do == True and c66['1'] == False and c66['2'] == False and c66['3'] == False and c66['4'] == False and c66['5'] == False and c66['6'] == False and c66['7'] == False and c66['8'] == False and c66['9'] == True:
        e66do = False
        solvednums[5][5] = 9     
    else:
        if solvednums[5][5] == 1:
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c44['1'] = False
            c45['1'] = False
            c46['1'] = False
            c54['1'] = False
            c55['1'] = False
            c56['1'] = False
            c16['1'] = False
            c26['1'] = False
            c36['1'] = False
            c76['1'] = False
            c86['1'] = False
            c96['1'] = False
        elif solvednums[5][5] == 2: 
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c44['2'] = False
            c45['2'] = False
            c46['2'] = False
            c54['2'] = False
            c55['2'] = False
            c56['2'] = False
            c16['2'] = False
            c26['2'] = False
            c36['2'] = False
            c76['2'] = False
            c86['2'] = False
            c96['2'] = False
        elif solvednums[5][5] == 3:
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c44['3'] = False
            c45['3'] = False
            c46['3'] = False
            c54['3'] = False
            c55['3'] = False
            c56['3'] = False
            c16['3'] = False
            c26['3'] = False
            c36['3'] = False
            c76['3'] = False
            c86['3'] = False
            c96['3'] = False
        elif solvednums[5][5] == 4:
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c44['4'] = False
            c45['4'] = False
            c46['4'] = False
            c54['4'] = False
            c55['4'] = False
            c56['4'] = False
            c16['4'] = False
            c26['4'] = False
            c36['4'] = False
            c76['4'] = False
            c86['4'] = False
            c96['4'] = False
        elif solvednums[5][5] == 5:
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c44['5'] = False
            c45['5'] = False
            c46['5'] = False
            c54['5'] = False
            c55['5'] = False
            c56['5'] = False
            c16['5'] = False
            c26['5'] = False
            c36['5'] = False
            c76['5'] = False
            c86['5'] = False
            c96['5'] = False
        elif solvednums[5][5] == 6:
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c44['6'] = False
            c45['6'] = False
            c46['6'] = False
            c54['6'] = False
            c55['6'] = False
            c56['6'] = False
            c16['6'] = False
            c26['6'] = False
            c36['6'] = False
            c76['6'] = False
            c86['6'] = False
            c96['6'] = False
        elif solvednums[5][5] == 7:
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c44['7'] = False
            c45['7'] = False
            c46['7'] = False
            c54['7'] = False
            c55['7'] = False
            c56['7'] = False
            c16['7'] = False
            c26['7'] = False
            c36['7'] = False
            c76['7'] = False
            c86['7'] = False
            c96['7'] = False
        elif solvednums[5][5] == 8:
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c44['8'] = False
            c45['8'] = False
            c46['8'] = False
            c54['8'] = False
            c55['8'] = False
            c56['8'] = False
            c16['8'] = False
            c26['8'] = False
            c36['8'] = False
            c76['8'] = False
            c86['8'] = False
            c96['8'] = False
        elif solvednums[5][5] == 9:
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c44['9'] = False
            c45['9'] = False
            c46['9'] = False
            c54['9'] = False
            c55['9'] = False
            c56['9'] = False
            c16['9'] = False
            c26['9'] = False
            c36['9'] = False
            c76['9'] = False   
            c86['9'] = False
            c96['9'] = False
    if puzzlenums[5][6] > 0 and e67do == True:
        solvednums[5][6] = puzzlenums[5][6]
        e67do = False
        sleep(1)
    elif e67do == True and c67['1'] == True and c67['2'] == False and c67['3'] == False and c67['4'] == False and c67['5'] == False and c67['6'] == False and c67['7'] == False and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 1
    elif e67do == True and c67['1'] == False and c67['2'] == True and c67['3'] == False and c67['4'] == False and c67['5'] == False and c67['6'] == False and c67['7'] == False and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 2
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == True and c67['4'] == False and c67['5'] == False and c67['6'] == False and c67['7'] == False and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 3
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == False and c67['4'] == True and c67['5'] == False and c67['6'] == False and c67['7'] == False and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 4
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == False and c67['4'] == False and c67['5'] == True and c67['6'] == False and c67['7'] == False and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 5
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == False and c67['4'] == False and c67['5'] == False and c67['6'] == True and c67['7'] == False and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 6
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == False and c67['4'] == False and c67['5'] == False and c67['6'] == False and c67['7'] == True and c67['8'] == False and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 7
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == False and c67['4'] == False and c67['5'] == False and c67['6'] == False and c67['7'] == False and c67['8'] == True and c67['9'] == False:
        e67do = False
        solvednums[5][6] = 8
    elif e67do == True and c67['1'] == False and c67['2'] == False and c67['3'] == False and c67['4'] == False and c67['5'] == False and c67['6'] == False and c67['7'] == False and c67['8'] == False and c67['9'] == True:
        e67do = False
        solvednums[5][6] = 9
    else:
        if solvednums[5][6] == 1:
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c17['1'] = False
            c27['1'] = False
            c37['1'] = False
            c77['1'] = False
            c87['1'] = False
            c97['1'] = False
        elif solvednums[5][6] == 2:
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c17['2'] = False
            c27['2'] = False
            c37['2'] = False
            c77['2'] = False
            c87['2'] = False
            c97['2'] = False
        elif solvednums[5][6] == 3:
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c17['3'] = False
            c27['3'] = False
            c37['3'] = False
            c77['3'] = False
            c87['3'] = False
            c97['3'] = False
        elif solvednums[5][6] == 4:
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c17['4'] = False
            c27['4'] = False
            c37['4'] = False
            c77['4'] = False
            c87['4'] = False
            c97['4'] = False
        elif solvednums[5][6] == 5:
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c17['5'] = False
            c27['5'] = False
            c37['5'] = False
            c77['5'] = False
            c87['5'] = False
            c97['5'] = False
        elif solvednums[5][6] == 6:
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c17['6'] = False
            c27['6'] = False
            c37['6'] = False
            c77['6'] = False
            c87['6'] = False
            c97['6'] = False
        elif solvednums[5][6] == 7:
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c17['7'] = False
            c27['7'] = False
            c37['7'] = False
            c77['7'] = False
            c87['7'] = False
            c97['7'] = False
        elif solvednums[5][6] == 8:
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c17['8'] = False
            c27['8'] = False
            c37['8'] = False
            c77['8'] = False
            c87['8'] = False
            c97['8'] = False
        elif solvednums[5][6] == 9:
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c17['9'] = False
            c27['9'] = False
            c37['9'] = False
            c77['9'] = False   
            c87['9'] = False
            c97['9'] = False
    if puzzlenums[5][7] > 0 and e68do == True:
        solvednums[5][7] = puzzlenums[5][7]
        e68do = False
        sleep(1)
    elif e68do == True and c68['1'] == True and c68['2'] == False and c68['3'] == False and c68['4'] == False and c68['5'] == False and c68['6'] == False and c68['7'] == False and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 1
    elif e68do == True and c68['1'] == False and c68['2'] == True and c68['3'] == False and c68['4'] == False and c68['5'] == False and c68['6'] == False and c68['7'] == False and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 2
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == True and c68['4'] == False and c68['5'] == False and c68['6'] == False and c68['7'] == False and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 3
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == False and c68['4'] == True and c68['5'] == False and c68['6'] == False and c68['7'] == False and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 4
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == False and c68['4'] == False and c68['5'] == True and c68['6'] == False and c68['7'] == False and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 5
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == False and c68['4'] == False and c68['5'] == False and c68['6'] == True and c68['7'] == False and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 6
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == False and c68['4'] == False and c68['5'] == False and c68['6'] == False and c68['7'] == True and c68['8'] == False and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 7
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == False and c68['4'] == False and c68['5'] == False and c68['6'] == False and c68['7'] == False and c68['8'] == True and c68['9'] == False:
        e68do = False
        solvednums[5][7] = 8
    elif e68do == True and c68['1'] == False and c68['2'] == False and c68['3'] == False and c68['4'] == False and c68['5'] == False and c68['6'] == False and c68['7'] == False and c68['8'] == False and c68['9'] == True:
        e68do = False
        solvednums[5][7] = 9
    else:
        if solvednums[5][7] == 1:
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c18['1'] = False
            c28['1'] = False
            c38['1'] = False
            c78['1'] = False
            c88['1'] = False
            c98['1'] = False
        elif solvednums[5][7] == 2:
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c18['2'] = False
            c28['2'] = False
            c38['2'] = False
            c78['2'] = False
            c88['2'] = False
            c98['2'] = False
        elif solvednums[5][7] == 3:
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c18['3'] = False
            c28['3'] = False
            c38['3'] = False
            c78['3'] = False
            c88['3'] = False
            c98['3'] = False
        elif solvednums[5][7] == 4:
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c18['4'] = False
            c28['4'] = False
            c38['4'] = False
            c78['4'] = False
            c88['4'] = False
            c98['4'] = False
        elif solvednums[5][7] == 5:
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c59['5'] = False
            c58['5'] = False
            c59['5'] = False
            c18['5'] = False
            c28['5'] = False
            c38['5'] = False
            c78['5'] = False
            c88['5'] = False
            c98['5'] = False
        elif solvednums[5][7] == 6:
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c18['6'] = False
            c28['6'] = False
            c38['6'] = False
            c78['6'] = False
            c88['6'] = False
            c98['6'] = False
        elif solvednums[5][7] == 7:
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c18['7'] = False
            c28['7'] = False
            c38['7'] = False
            c78['7'] = False
            c88['7'] = False
            c98['7'] = False
        elif solvednums[5][7] == 8:
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c18['8'] = False
            c28['8'] = False
            c38['8'] = False
            c78['8'] = False
            c88['8'] = False
            c98['8'] = False
        elif solvednums[5][7] == 9:
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c65['9'] = False 
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c18['9'] = False
            c28['9'] = False
            c38['9'] = False
            c78['9'] = False   
            c88['9'] = False
            c98['9'] = False
    if puzzlenums[5][8] > 0 and e69do == True:
        solvednums[5][8] = puzzlenums[5][8]
        e69do = False
        sleep(1)
    elif e69do == True and c69['1'] == True and c69['2'] == False and c69['3'] == False and c69['4'] == False and c69['5'] == False and c69['6'] == False and c69['7'] == False and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 1
    elif e69do == True and c69['1'] == False and c69['2'] == True and c69['3'] == False and c69['4'] == False and c69['5'] == False and c69['6'] == False and c69['7'] == False and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 2
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == True and c69['4'] == False and c69['5'] == False and c69['6'] == False and c69['7'] == False and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 3
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == False and c69['4'] == True and c69['5'] == False and c69['6'] == False and c69['7'] == False and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 4
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == False and c69['4'] == False and c69['5'] == True and c69['6'] == False and c69['7'] == False and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 5
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == False and c69['4'] == False and c69['5'] == False and c69['6'] == True and c69['7'] == False and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 6
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == False and c69['4'] == False and c69['5'] == False and c69['6'] == False and c69['7'] == True and c69['8'] == False and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 7
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == False and c69['4'] == False and c69['5'] == False and c69['6'] == False and c69['7'] == False and c69['8'] == True and c69['9'] == False:
        e69do = False
        solvednums[5][8] = 8
    elif e69do == True and c69['1'] == False and c69['2'] == False and c69['3'] == False and c69['4'] == False and c69['5'] == False and c69['6'] == False and c69['7'] == False and c69['8'] == False and c69['9'] == True:
        e69do = False
        solvednums[5][8] = 9
    else:
        if solvednums[5][8] == 1:
            c61['1'] = False
            c62['1'] = False
            c63['1'] = False
            c65['1'] = False
            c66['1'] = False
            c67['1'] = False
            c68['1'] = False
            c69['1'] = False
            c47['1'] = False
            c48['1'] = False
            c49['1'] = False
            c57['1'] = False
            c58['1'] = False
            c59['1'] = False
            c19['1'] = False
            c29['1'] = False
            c39['1'] = False
            c79['1'] = False
            c89['1'] = False
            c99['1'] = False
        elif solvednums[5][8] == 2:
            c61['2'] = False
            c62['2'] = False
            c63['2'] = False
            c65['2'] = False
            c66['2'] = False
            c67['2'] = False
            c68['2'] = False
            c69['2'] = False
            c47['2'] = False
            c48['2'] = False
            c49['2'] = False
            c57['2'] = False
            c58['2'] = False
            c59['2'] = False
            c19['2'] = False
            c29['2'] = False
            c39['2'] = False
            c79['2'] = False
            c89['2'] = False
            c99['2'] = False
        elif solvednums[5][8] == 3:
            c61['3'] = False
            c62['3'] = False
            c63['3'] = False
            c65['3'] = False
            c66['3'] = False
            c67['3'] = False
            c68['3'] = False
            c69['3'] = False
            c47['3'] = False
            c48['3'] = False
            c49['3'] = False
            c57['3'] = False
            c58['3'] = False
            c59['3'] = False
            c19['3'] = False
            c29['3'] = False
            c39['3'] = False
            c79['3'] = False
            c89['3'] = False
            c99['3'] = False
        elif solvednums[5][8] == 4:
            c61['4'] = False
            c62['4'] = False
            c63['4'] = False
            c65['4'] = False
            c66['4'] = False
            c67['4'] = False
            c68['4'] = False
            c69['4'] = False
            c47['4'] = False
            c48['4'] = False
            c49['4'] = False
            c57['4'] = False
            c58['4'] = False
            c59['4'] = False
            c19['4'] = False
            c29['4'] = False
            c39['4'] = False
            c79['4'] = False
            c89['4'] = False
            c99['4'] = False
        elif solvednums[5][8] == 5:
            c61['5'] = False
            c62['5'] = False
            c63['5'] = False
            c65['5'] = False
            c66['5'] = False
            c67['5'] = False
            c68['5'] = False
            c69['5'] = False
            c47['5'] = False
            c48['5'] = False
            c49['5'] = False
            c57['5'] = False
            c58['5'] = False
            c59['5'] = False
            c19['5'] = False
            c29['5'] = False
            c39['5'] = False
            c79['5'] = False
            c89['5'] = False
            c99['5'] = False
        elif solvednums[5][8] == 6:
            c61['6'] = False
            c62['6'] = False
            c63['6'] = False
            c65['6'] = False
            c66['6'] = False
            c67['6'] = False
            c68['6'] = False
            c69['6'] = False
            c47['6'] = False
            c48['6'] = False
            c49['6'] = False
            c57['6'] = False
            c58['6'] = False
            c59['6'] = False
            c19['6'] = False
            c29['6'] = False
            c39['6'] = False
            c79['6'] = False
            c89['6'] = False
            c99['6'] = False
        elif solvednums[5][8] == 7:
            c61['7'] = False
            c62['7'] = False
            c63['7'] = False
            c65['7'] = False
            c66['7'] = False
            c67['7'] = False
            c68['7'] = False
            c69['7'] = False
            c47['7'] = False
            c48['7'] = False
            c49['7'] = False
            c57['7'] = False
            c58['7'] = False
            c59['7'] = False
            c19['7'] = False
            c29['7'] = False
            c39['7'] = False
            c79['7'] = False
            c89['7'] = False
            c99['7'] = False
        elif solvednums[5][8] == 8:
            c61['8'] = False
            c62['8'] = False
            c63['8'] = False
            c65['8'] = False
            c66['8'] = False
            c67['8'] = False
            c68['8'] = False
            c69['8'] = False
            c47['8'] = False
            c48['8'] = False
            c49['8'] = False
            c57['8'] = False
            c58['8'] = False
            c59['8'] = False
            c19['8'] = False
            c29['8'] = False
            c39['8'] = False
            c79['8'] = False
            c89['8'] = False
            c99['8'] = False
        elif solvednums[5][8] == 9:
            c61['9'] = False
            c62['9'] = False
            c63['9'] = False
            c66['9'] = False
            c67['9'] = False
            c68['9'] = False
            c69['9'] = False
            c47['9'] = False
            c48['9'] = False
            c49['9'] = False
            c57['9'] = False
            c58['9'] = False
            c59['9'] = False
            c19['9'] = False
            c29['9'] = False
            c39['9'] = False
            c79['9'] = False   
            c89['9'] = False
            c99['9'] = False    
    if puzzlenums[6][0] > 0 and e71do == True:
        solvednums[6][0] = puzzlenums[6][0]
        e71do = False
        sleep(1)
    elif e71do == True and c71['1'] == True and c71['2'] == False and c71['3'] == False and c71['4'] == False and c71['5'] == False and c71['6'] == False and c71['7'] == False and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 1
    elif e71do == True and c71['1'] == False and c71['2'] == True and c71['3'] == False and c71['4'] == False and c71['5'] == False and c71['6'] == False and c71['7'] == False and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 2
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == True and c71['4'] == False and c71['5'] == False and c71['6'] == False and c71['7'] == False and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 3
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == False and c71['4'] == True and c71['5'] == False and c71['6'] == False and c71['7'] == False and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 4
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == False and c71['4'] == False and c71['5'] == True and c71['6'] == False and c71['7'] == False and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 5
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == False and c71['4'] == False and c71['5'] == False and c71['6'] == True and c71['7'] == False and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 6
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == False and c71['4'] == False and c71['5'] == False and c71['6'] == False and c71['7'] == True and c71['8'] == False and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 7
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == False and c71['4'] == False and c71['5'] == False and c71['6'] == False and c71['7'] == False and c71['8'] == True and c71['9'] == False:
        e71do = False
        solvednums[6][0] = 8
    elif e71do == True and c71['1'] == False and c71['2'] == False and c71['3'] == False and c71['4'] == False and c71['5'] == False and c71['6'] == False and c71['7'] == False and c71['8'] == False and c71['9'] == True:
        e71do = False
        solvednums[6][0] = 9
    else:
        if solvednums[6][0] == 1:
            c71['1'] = False
            c71['2'] = False
            c71['3'] = False
            c71['4'] = False
            c71['5'] = False
            c71['6'] = False
            c71['7'] = False
            c71['8'] = False
            c71['9'] = False
            c72['1'] = False
            c73['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c11['1'] = False
            c21['1'] = False
            c31['1'] = False
            c41['1'] = False
            c51['1'] = False
            c61['1'] = False
            c71['1'] = False
            c81['1'] = False
        elif solvednums[6][0] == 2:
            c71['1'] = False
            c71['2'] = False
            c71['3'] = False
            c71['4'] = False
            c71['5'] = False
            c71['6'] = False
            c71['7'] = False
            c71['8'] = False
            c71['9'] = False
            c72['2'] = False
            c73['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c11['2'] = False
            c21['2'] = False
            c31['2'] = False
            c41['2'] = False
            c51['2'] = False
            c61['2'] = False
        elif solvednums[6][0] == 3:
            c72['3'] = False
            c73['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c11['3'] = False
            c21['3'] = False
            c31['3'] = False
            c41['3'] = False
            c51['3'] = False
            c61['3'] = False
        elif solvednums[6][0] == 4:
            c72['4'] = False
            c73['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c11['4'] = False
            c21['4'] = False
            c31['4'] = False
            c41['4'] = False
            c51['4'] = False
            c61['4'] = False
        elif solvednums[6][0] == 5:
            c72['5'] = False
            c73['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c11['5'] = False
            c21['5'] = False
            c31['5'] = False
            c41['5'] = False
            c51['5'] = False
            c61['5'] = False
        elif solvednums[6][0] == 6:
            c72['6'] = False
            c73['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c11['6'] = False
            c21['6'] = False
            c31['6'] = False
            c41['6'] = False
            c51['6'] = False
            c61['6'] = False
        elif solvednums[6][0] == 7:
            c72['7'] = False
            c73['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c11['7'] = False
            c21['7'] = False
            c31['7'] = False
            c41['7'] = False
            c51['7'] = False
            c61['7'] = False
        elif solvednums[6][0] == 8:
            c72['8'] = False
            c73['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c11['8'] = False
            c21['8'] = False
            c31['8'] = False
            c41['8'] = False
            c51['8'] = False
            c61['8'] = False
        elif solvednums[6][0] == 9:
            c72['9'] = False
            c73['9'] = False
            c74['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c11['9'] = False
            c21['9'] = False
            c31['9'] = False
            c41['9'] = False   
            c51['9'] = False
            c61['9'] = False
    if puzzlenums[6][1] > 0 and e72do == True:
        solvednums[6][1] = puzzlenums[6][1]
        e72do = False
        sleep(1)
    elif e72do == True and c72['1'] == True and c72['2'] == False and c72['3'] == False and c72['4'] == False and c72['5'] == False and c72['6'] == False and c72['7'] == False and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 1
    elif e72do == True and c72['1'] == False and c72['2'] == True and c72['3'] == False and c72['4'] == False and c72['5'] == False and c72['6'] == False and c72['7'] == False and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 2
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == True and c72['4'] == False and c72['5'] == False and c72['6'] == False and c72['7'] == False and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 3
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == False and c72['4'] == True and c72['5'] == False and c72['6'] == False and c72['7'] == False and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 4
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == False and c72['4'] == False and c72['5'] == True and c72['6'] == False and c72['7'] == False and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 5
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == False and c72['4'] == False and c72['5'] == False and c72['6'] == True and c72['7'] == False and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 6
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == False and c72['4'] == False and c72['5'] == False and c72['6'] == False and c72['7'] == True and c72['8'] == False and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 7
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == False and c72['4'] == False and c72['5'] == False and c72['6'] == False and c72['7'] == False and c72['8'] == True and c72['9'] == False:
        e72do = False
        solvednums[6][1] = 8
    elif e72do == True and c72['1'] == False and c72['2'] == False and c72['3'] == False and c72['4'] == False and c72['5'] == False and c72['6'] == False and c72['7'] == False and c72['8'] == False and c72['9'] == True:
        e72do = False
        solvednums[6][1] = 9
    else:
        if solvednums[6][1] == 1:
            c71['1'] = False
            c73['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c12['1'] = False
            c22['1'] = False
            c32['1'] = False
            c42['1'] = False
            c52['1'] = False
            c62['1'] = False
        elif solvednums[6][1] == 2:
            c71['2'] = False
            c73['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c12['2'] = False
            c22['2'] = False
            c32['2'] = False
            c42['2'] = False
            c52['2'] = False
            c62['2'] = False
        elif solvednums[6][1] == 3:
            c71['3'] = False
            c73['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c12['3'] = False
            c22['3'] = False
            c32['3'] = False
            c42['3'] = False
            c52['3'] = False
            c62['3'] = False
        elif solvednums[6][1] == 4:
            c71['4'] = False
            c73['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c12['4'] = False
            c22['4'] = False
            c32['4'] = False
            c42['4'] = False
            c52['4'] = False
            c62['4'] = False
        elif solvednums[6][1] == 5:
            c71['5'] = False
            c73['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c12['5'] = False
            c22['5'] = False
            c32['5'] = False
            c42['5'] = False
            c52['5'] = False
            c62['5'] = False
        elif solvednums[6][1] == 6:
            c71['6'] = False
            c73['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c12['6'] = False
            c22['6'] = False
            c32['6'] = False
            c42['6'] = False
            c52['6'] = False
            c62['6'] = False
        elif solvednums[6][1] == 7:
            c71['7'] = False
            c73['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c12['7'] = False
            c22['7'] = False
            c32['7'] = False
            c42['7'] = False
            c52['7'] = False
            c62['7'] = False
        elif solvednums[6][1] == 8:
            c71['8'] = False
            c73['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c12['8'] = False
            c22['8'] = False
            c32['8'] = False
            c42['8'] = False
            c52['8'] = False
            c62['8'] = False
        elif solvednums[6][1] == 9:
            c71['9'] = False
            c73['9'] = False
            c74['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c12['9'] = False
            c22['9'] = False
            c32['9'] = False
            c42['9'] = False   
            c52['9'] = False
            c62['9'] = False
    if puzzlenums[6][2] > 0 and e73do == True:
        solvednums[6][2] = puzzlenums[6][2]
        e73do = False
        sleep(1)
    elif e73do == True and c73['1'] == True and c73['2'] == False and c73['3'] == False and c73['4'] == False and c73['5'] == False and c73['6'] == False and c73['7'] == False and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 1
    elif e73do == True and c73['1'] == False and c73['2'] == True and c73['3'] == False and c73['4'] == False and c73['5'] == False and c73['6'] == False and c73['7'] == False and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 2
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == True and c73['4'] == False and c73['5'] == False and c73['6'] == False and c73['7'] == False and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 3
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == False and c73['4'] == True and c73['5'] == False and c73['6'] == False and c73['7'] == False and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 4
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == False and c73['4'] == False and c73['5'] == True and c73['6'] == False and c73['7'] == False and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 5
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == False and c73['4'] == False and c73['5'] == False and c73['6'] == True and c73['7'] == False and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 6
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == False and c73['4'] == False and c73['5'] == False and c73['6'] == False and c73['7'] == True and c73['8'] == False and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 7
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == False and c73['4'] == False and c73['5'] == False and c73['6'] == False and c73['7'] == False and c73['8'] == True and c73['9'] == False:
        e73do = False
        solvednums[6][2] = 8
    elif e73do == True and c73['1'] == False and c73['2'] == False and c73['3'] == False and c73['4'] == False and c73['5'] == False and c73['6'] == False and c73['7'] == False and c73['8'] == False and c73['9'] == True:
        e73do = False
        solvednums[6][2] = 9
    else:
        if solvednums[6][2] == 1:
            c71['1'] = False
            c72['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c13['1'] = False
            c23['1'] = False
            c33['1'] = False
            c43['1'] = False
            c53['1'] = False
            c63['1'] = False
        elif solvednums[6][2] == 2:
            c71['2'] = False
            c72['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c13['2'] = False
            c23['2'] = False
            c33['2'] = False
            c43['2'] = False
            c53['2'] = False
            c63['2'] = False
        elif solvednums[6][2] == 3:
            c71['3'] = False
            c72['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c13['3'] = False
            c23['3'] = False
            c33['3'] = False
            c43['3'] = False
            c53['3'] = False
            c63['3'] = False
        elif solvednums[6][2] == 4:
            c71['4'] = False
            c72['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c81['4'] = False
            c84['4'] = False
            c83['4'] = False
            c13['4'] = False
            c23['4'] = False
            c33['4'] = False
            c43['4'] = False
            c53['4'] = False
            c63['4'] = False
        elif solvednums[6][2] == 5:
            c71['5'] = False
            c72['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c13['5'] = False
            c23['5'] = False
            c33['5'] = False
            c43['5'] = False
            c53['5'] = False
            c63['5'] = False
        elif solvednums[6][2] == 6:
            c71['6'] = False
            c72['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c13['6'] = False
            c23['6'] = False
            c33['6'] = False
            c43['6'] = False
            c53['6'] = False
            c63['6'] = False
        elif solvednums[6][2] == 7:
            c71['7'] = False
            c72['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c13['7'] = False
            c23['7'] = False
            c33['7'] = False
            c43['7'] = False
            c53['7'] = False
            c63['7'] = False
        elif solvednums[6][2] == 8:
            c71['8'] = False
            c72['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c13['8'] = False
            c23['8'] = False
            c33['8'] = False
            c43['8'] = False
            c53['8'] = False
            c63['8'] = False
        elif solvednums[6][2] == 9:
            c71['9'] = False
            c72['9'] = False
            c74['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c13['9'] = False
            c23['9'] = False
            c33['9'] = False
            c43['9'] = False   
            c53['9'] = False
            c63['9'] = False
    if puzzlenums[6][3] > 0 and e74do == True:
        solvednums[6][3] = puzzlenums[6][3]
        e74do = False
        sleep(1)
    elif e74do == True and c74['1'] == True and c74['2'] == False and c74['3'] == False and c74['4'] == False and c74['5'] == False and c74['6'] == False and c74['7'] == False and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 1
    elif e74do == True and c74['1'] == False and c74['2'] == True and c74['3'] == False and c74['4'] == False and c74['5'] == False and c74['6'] == False and c74['7'] == False and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 2
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == True and c74['4'] == False and c74['5'] == False and c74['6'] == False and c74['7'] == False and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 3
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == False and c74['4'] == True and c74['5'] == False and c74['6'] == False and c74['7'] == False and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 4
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == False and c74['4'] == False and c74['5'] == True and c74['6'] == False and c74['7'] == False and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 5
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == False and c74['4'] == False and c74['5'] == False and c74['6'] == True and c74['7'] == False and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 6
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == False and c74['4'] == False and c74['5'] == False and c74['6'] == False and c74['7'] == True and c74['8'] == False and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 7
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == False and c74['4'] == False and c74['5'] == False and c74['6'] == False and c74['7'] == False and c74['8'] == True and c74['9'] == False:
        e74do = False
        solvednums[6][3] = 8
    elif e74do == True and c74['1'] == False and c74['2'] == False and c74['3'] == False and c74['4'] == False and c74['5'] == False and c74['6'] == False and c74['7'] == False and c74['8'] == False and c74['9'] == True:
        e74do = False
        solvednums[6][3] = 9
    else:
        if solvednums[6][3] == 1:
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c14['1'] = False
            c24['1'] = False
            c34['1'] = False
            c44['1'] = False
            c54['1'] = False
            c64['1'] = False
        elif solvednums[6][3] == 2:
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c14['2'] = False
            c24['2'] = False
            c34['2'] = False
            c44['2'] = False
            c54['2'] = False
            c64['2'] = False
        elif solvednums[6][3] == 3:
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c14['3'] = False
            c24['3'] = False
            c34['3'] = False
            c44['3'] = False
            c54['3'] = False
            c64['3'] = False
        elif solvednums[6][3] == 4:
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c14['4'] = False
            c24['4'] = False
            c34['4'] = False
            c44['4'] = False
            c54['4'] = False
            c64['4'] = False
        elif solvednums[6][3] == 5:
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c14['5'] = False
            c24['5'] = False
            c34['5'] = False
            c44['5'] = False
            c54['5'] = False
            c64['5'] = False
        elif solvednums[6][3] == 6:
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c14['6'] = False
            c24['6'] = False
            c34['6'] = False
            c44['6'] = False
            c54['6'] = False
            c64['6'] = False
        elif solvednums[6][3] == 7:
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c14['7'] = False
            c24['7'] = False
            c34['7'] = False
            c44['7'] = False
            c54['7'] = False
            c64['7'] = False
        elif solvednums[6][3] == 8:
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c14['8'] = False
            c24['8'] = False
            c34['8'] = False
            c44['8'] = False
            c54['8'] = False
            c64['8'] = False
        elif solvednums[6][3] == 9:
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c94['9'] = False
            c95['9'] = False
            c96['9'] = False
            c84['9'] = False
            c85['9'] = False
            c86['9'] = False
            c14['9'] = False
            c24['9'] = False
            c34['9'] = False
            c44['9'] = False   
            c54['9'] = False
            c64['9'] = False
    if puzzlenums[6][5] > 0 and e75do == True:
        solvednums[6][4] = puzzlenums[6][4]
        e75do = False
        sleep(1)
    elif e75do == True and c75['1'] == True and c75['2'] == False and c75['3'] == False and c75['4'] == False and c75['5'] == False and c75['6'] == False and c75['7'] == False and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 1
    elif e75do == True and c75['1'] == False and c75['2'] == True and c75['3'] == False and c75['4'] == False and c75['5'] == False and c75['6'] == False and c75['7'] == False and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 2
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == True and c75['4'] == False and c75['5'] == False and c75['6'] == False and c75['7'] == False and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 3
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == False and c75['4'] == True and c75['5'] == False and c75['6'] == False and c75['7'] == False and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 4
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == False and c75['4'] == False and c75['5'] == True and c75['6'] == False and c75['7'] == False and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 5
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == False and c75['4'] == False and c75['5'] == False and c75['6'] == True and c75['7'] == False and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 6
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == False and c75['4'] == False and c75['5'] == False and c75['6'] == False and c75['7'] == True and c75['8'] == False and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 7
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == False and c75['4'] == False and c75['5'] == False and c75['6'] == False and c75['7'] == False and c75['8'] == True and c75['9'] == False:
        e75do = False
        solvednums[6][4] = 8
    elif e75do == True and c75['1'] == False and c75['2'] == False and c75['3'] == False and c75['4'] == False and c75['5'] == False and c75['6'] == False and c75['7'] == False and c75['8'] == False and c75['9'] == True:
        e75do = False
        solvednums[6][4] = 9
    else:
        if solvednums[6][4] == 1:
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c15['1'] = False
            c25['1'] = False
            c35['1'] = False
            c45['1'] = False
            c55['1'] = False
            c65['1'] = False
        elif solvednums[6][4] == 2:
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c15['2'] = False
            c25['2'] = False
            c35['2'] = False
            c45['2'] = False
            c55['2'] = False
            c65['2'] = False
        elif solvednums[6][4] == 3:
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c15['3'] = False
            c25['3'] = False
            c35['3'] = False
            c45['3'] = False
            c55['3'] = False
            c65['3'] = False
        elif solvednums[6][4] == 4:
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c54['4'] = False
            c85['4'] = False
            c86['4'] = False
            c85['4'] = False
            c25['4'] = False
            c35['4'] = False
            c45['4'] = False
            c55['4'] = False
            c65['4'] = False
        elif solvednums[6][4] == 5:
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c15['5'] = False
            c25['5'] = False
            c35['5'] = False
            c45['5'] = False
            c55['5'] = False
            c65['5'] = False
        elif solvednums[6][4] == 6:
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c15['6'] = False
            c25['6'] = False
            c35['6'] = False
            c45['6'] = False
            c55['6'] = False
            c65['6'] = False
        elif solvednums[6][4] == 7:
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c15['7'] = False
            c25['7'] = False
            c35['7'] = False
            c45['7'] = False
            c55['7'] = False
            c65['7'] = False
        elif solvednums[6][4] == 8:
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c15['8'] = False
            c25['8'] = False
            c35['8'] = False
            c45['8'] = False
            c55['8'] = False
            c65['8'] = False
        elif solvednums[6][4] == 9:
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c94['9'] = False
            c95['9'] = False
            c96['9'] = False
            c84['9'] = False
            c85['9'] = False
            c86['9'] = False
            c15['9'] = False
            c25['9'] = False
            c35['9'] = False
            c45['9'] = False   
            c55['9'] = False
            c65['9'] = False
    if puzzlenums[6][5] > 0 and e76do == True:
        solvednums[6][5] = puzzlenums[6][5]
        e76do = False
        sleep(1)
    elif e76do == True and c76['1'] == True and c76['2'] == False and c76['3'] == False and c76['4'] == False and c76['5'] == False and c76['6'] == False and c76['7'] == False and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 1
    elif e76do == True and c76['1'] == False and c76['2'] == True and c76['3'] == False and c76['4'] == False and c76['5'] == False and c76['6'] == False and c76['7'] == False and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 2
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == True and c76['4'] == False and c76['5'] == False and c76['6'] == False and c76['7'] == False and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 3
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == False and c76['4'] == True and c76['5'] == False and c76['6'] == False and c76['7'] == False and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][6] = 4
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == False and c76['4'] == False and c76['5'] == True and c76['6'] == False and c76['7'] == False and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 5
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == False and c76['4'] == False and c76['5'] == False and c76['6'] == True and c76['7'] == False and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 6
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == False and c76['4'] == False and c76['5'] == False and c76['6'] == False and c76['7'] == True and c76['8'] == False and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 7
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == False and c76['4'] == False and c76['5'] == False and c76['6'] == False and c76['7'] == False and c76['8'] == True and c76['9'] == False:
        e76do = False
        solvednums[6][5] = 8
    elif e76do == True and c76['1'] == False and c76['2'] == False and c76['3'] == False and c76['4'] == False and c76['5'] == False and c76['6'] == False and c76['7'] == False and c76['8'] == False and c76['9'] == True:
        e76do = False
        solvednums[6][5] = 9     
    else:
        if solvednums[6][5] == 1:
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c16['1'] = False
            c26['1'] = False
            c36['1'] = False
            c46['1'] = False
            c56['1'] = False
            c66['1'] = False
        elif solvednums[6][5] == 2: 
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c16['2'] = False
            c26['2'] = False
            c36['2'] = False
            c46['2'] = False
            c56['2'] = False
            c66['2'] = False
        elif solvednums[6][5] == 3:
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c16['3'] = False
            c26['3'] = False
            c36['3'] = False
            c46['3'] = False
            c56['3'] = False
            c66['3'] = False
        elif solvednums[6][5] == 4:
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c16['4'] = False
            c26['4'] = False
            c36['4'] = False
            c46['4'] = False
            c56['4'] = False
            c66['4'] = False
        elif solvednums[6][5] == 5:
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c16['5'] = False
            c26['5'] = False
            c36['5'] = False
            c46['5'] = False
            c56['5'] = False
            c66['5'] = False
        elif solvednums[6][5] == 6:
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c16['6'] = False
            c26['6'] = False
            c36['6'] = False
            c46['6'] = False
            c56['6'] = False
            c66['6'] = False
        elif solvednums[6][5] == 7:
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c16['7'] = False
            c26['7'] = False
            c36['7'] = False
            c46['7'] = False
            c56['7'] = False
            c66['7'] = False
        elif solvednums[6][5] == 8:
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c16['8'] = False
            c26['8'] = False
            c36['8'] = False
            c46['8'] = False
            c56['8'] = False
            c66['8'] = False
        elif solvednums[6][5] == 9:
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c94['9'] = False
            c95['9'] = False
            c96['9'] = False
            c84['9'] = False
            c85['9'] = False
            c86['9'] = False
            c16['9'] = False
            c26['9'] = False
            c36['9'] = False
            c46['9'] = False   
            c56['9'] = False
            c66['9'] = False
    if puzzlenums[6][6] > 0 and e77do == True:
        solvednums[6][6] = puzzlenums[6][6]
        e77do = False
        sleep(1)
    elif e77do == True and c77['1'] == True and c77['2'] == False and c77['3'] == False and c77['4'] == False and c77['5'] == False and c77['6'] == False and c77['7'] == False and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 1
    elif e77do == True and c77['1'] == False and c77['2'] == True and c77['3'] == False and c77['4'] == False and c77['5'] == False and c77['6'] == False and c77['7'] == False and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 2
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == True and c77['4'] == False and c77['5'] == False and c77['6'] == False and c77['7'] == False and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 3
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == False and c77['4'] == True and c77['5'] == False and c77['6'] == False and c77['7'] == False and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 4
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == False and c77['4'] == False and c77['5'] == True and c77['6'] == False and c77['7'] == False and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 5
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == False and c77['4'] == False and c77['5'] == False and c77['6'] == True and c77['7'] == False and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 6
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == False and c77['4'] == False and c77['5'] == False and c77['6'] == False and c77['7'] == True and c77['8'] == False and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 7
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == False and c77['4'] == False and c77['5'] == False and c77['6'] == False and c77['7'] == False and c77['8'] == True and c77['9'] == False:
        e77do = False
        solvednums[6][6] = 8
    elif e77do == True and c77['1'] == False and c77['2'] == False and c77['3'] == False and c77['4'] == False and c77['5'] == False and c77['6'] == False and c77['7'] == False and c77['8'] == False and c77['9'] == True:
        e77do = False
        solvednums[6][6] = 9
    else:
        if solvednums[6][6] == 1:
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c17['1'] = False
            c27['1'] = False
            c37['1'] = False
            c47['1'] = False
            c57['1'] = False
            c67['1'] = False
        elif solvednums[6][6] == 2:
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c17['2'] = False
            c27['2'] = False
            c37['2'] = False
            c47['2'] = False
            c57['2'] = False
            c67['2'] = False
        elif solvednums[6][6] == 3:
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c17['3'] = False
            c27['3'] = False
            c37['3'] = False
            c47['3'] = False
            c57['3'] = False
            c67['3'] = False
        elif solvednums[6][6] == 4:
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c17['4'] = False
            c27['4'] = False
            c37['4'] = False
            c47['4'] = False
            c57['4'] = False
            c67['4'] = False
        elif solvednums[6][6] == 5:
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c17['5'] = False
            c27['5'] = False
            c37['5'] = False
            c47['5'] = False
            c57['5'] = False
            c67['5'] = False
        elif solvednums[6][6] == 6:
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c17['6'] = False
            c27['6'] = False
            c37['6'] = False
            c47['6'] = False
            c57['6'] = False
            c67['6'] = False
        elif solvednums[6][6] == 7:
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c17['7'] = False
            c27['7'] = False
            c37['7'] = False
            c47['7'] = False
            c57['7'] = False
            c67['7'] = False
        elif solvednums[6][6] == 8:
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c17['8'] = False
            c27['8'] = False
            c37['8'] = False
            c47['8'] = False
            c57['8'] = False
            c67['8'] = False
        elif solvednums[6][6] == 9:
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c17['9'] = False
            c27['9'] = False
            c37['9'] = False
            c47['9'] = False   
            c57['9'] = False
            c67['9'] = False
    if puzzlenums[6][7] > 0 and e78do == True:
        solvednums[6][7] = puzzlenums[6][7]
        e78do = False
        sleep(1)
    elif e78do == True and c78['1'] == True and c78['2'] == False and c78['3'] == False and c78['4'] == False and c78['5'] == False and c78['6'] == False and c78['7'] == False and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 1
    elif e78do == True and c78['1'] == False and c78['2'] == True and c78['3'] == False and c78['4'] == False and c78['5'] == False and c78['6'] == False and c78['7'] == False and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 2
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == True and c78['4'] == False and c78['5'] == False and c78['6'] == False and c78['7'] == False and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 3
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == False and c78['4'] == True and c78['5'] == False and c78['6'] == False and c78['7'] == False and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 4
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == False and c78['4'] == False and c78['5'] == True and c78['6'] == False and c78['7'] == False and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 5
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == False and c78['4'] == False and c78['5'] == False and c78['6'] == True and c78['7'] == False and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 6
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == False and c78['4'] == False and c78['5'] == False and c78['6'] == False and c78['7'] == True and c78['8'] == False and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 7
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == False and c78['4'] == False and c78['5'] == False and c78['6'] == False and c78['7'] == False and c78['8'] == True and c78['9'] == False:
        e78do = False
        solvednums[6][7] = 8
    elif e78do == True and c78['1'] == False and c78['2'] == False and c78['3'] == False and c78['4'] == False and c78['5'] == False and c78['6'] == False and c78['7'] == False and c78['8'] == False and c78['9'] == True:
        e78do = False
        solvednums[6][7] = 9
    else:
        if solvednums[6][7] == 1:
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c18['1'] = False
            c28['1'] = False
            c38['1'] = False
            c48['1'] = False
            c58['1'] = False
            c68['1'] = False
        elif solvednums[6][7] == 2:
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c18['2'] = False
            c28['2'] = False
            c38['2'] = False
            c48['2'] = False
            c58['2'] = False
            c68['2'] = False
        elif solvednums[6][7] == 3:
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c18['3'] = False
            c28['3'] = False
            c38['3'] = False
            c48['3'] = False
            c58['3'] = False
            c68['3'] = False
        elif solvednums[6][7] == 4:
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c18['4'] = False
            c28['4'] = False
            c38['4'] = False
            c48['4'] = False
            c58['4'] = False
            c68['4'] = False
        elif solvednums[6][7] == 5:
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c89['5'] = False
            c88['5'] = False
            c89['5'] = False
            c18['5'] = False
            c28['5'] = False
            c38['5'] = False
            c48['5'] = False
            c58['5'] = False
            c68['5'] = False
        elif solvednums[6][7] == 6:
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c18['6'] = False
            c28['6'] = False
            c38['6'] = False
            c48['6'] = False
            c58['6'] = False
            c68['6'] = False
        elif solvednums[6][7] == 7:
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c75['7'] = False
            c76['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c18['7'] = False
            c28['7'] = False
            c38['7'] = False
            c48['7'] = False
            c58['7'] = False
            c68['7'] = False
        elif solvednums[6][7] == 8:
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c18['8'] = False
            c28['8'] = False
            c38['8'] = False
            c48['8'] = False
            c58['8'] = False
            c68['8'] = False
        elif solvednums[6][7] == 9:
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c75['9'] = False 
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c18['9'] = False
            c28['9'] = False
            c38['9'] = False
            c48['9'] = False   
            c58['9'] = False
            c68['9'] = False
    if puzzlenums[6][8] > 0 and e79do == True:
        solvednums[6][8] = puzzlenums[6][8]
        e79do = False
        sleep(1)
    elif e79do == True and c79['1'] == True and c79['2'] == False and c79['3'] == False and c79['4'] == False and c79['5'] == False and c79['6'] == False and c79['7'] == False and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 1
    elif e79do == True and c79['1'] == False and c79['2'] == True and c79['3'] == False and c79['4'] == False and c79['5'] == False and c79['6'] == False and c79['7'] == False and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 2
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == True and c79['4'] == False and c79['5'] == False and c79['6'] == False and c79['7'] == False and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 3
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == False and c79['4'] == True and c79['5'] == False and c79['6'] == False and c79['7'] == False and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 4
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == False and c79['4'] == False and c79['5'] == True and c79['6'] == False and c79['7'] == False and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 5
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == False and c79['4'] == False and c79['5'] == False and c79['6'] == True and c79['7'] == False and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 6
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == False and c79['4'] == False and c79['5'] == False and c79['6'] == False and c79['7'] == True and c79['8'] == False and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 7
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == False and c79['4'] == False and c79['5'] == False and c79['6'] == False and c79['7'] == False and c79['8'] == True and c79['9'] == False:
        e79do = False
        solvednums[6][8] = 8
    elif e79do == True and c79['1'] == False and c79['2'] == False and c79['3'] == False and c79['4'] == False and c79['5'] == False and c79['6'] == False and c79['7'] == False and c79['8'] == False and c79['9'] == True:
        e79do = False
        solvednums[6][8] = 9
    else:
        if solvednums[6][8] == 1:
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c75['1'] = False
            c76['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c19['1'] = False
            c29['1'] = False
            c39['1'] = False
            c49['1'] = False
            c59['1'] = False
            c69['1'] = False
        elif solvednums[6][8] == 2:
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c75['2'] = False
            c76['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c19['2'] = False
            c29['2'] = False
            c39['2'] = False
            c49['2'] = False
            c59['2'] = False
            c69['2'] = False
        elif solvednums[6][8] == 3:
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c75['3'] = False
            c76['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c19['3'] = False
            c29['3'] = False
            c39['3'] = False
            c49['3'] = False
            c59['3'] = False
            c69['3'] = False
        elif solvednums[6][8] == 4:
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c75['4'] = False
            c76['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c19['4'] = False
            c29['4'] = False
            c39['4'] = False
            c49['4'] = False
            c59['4'] = False
            c69['4'] = False
        elif solvednums[6][8] == 5:
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c75['5'] = False
            c76['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c19['5'] = False
            c29['5'] = False
            c39['5'] = False
            c49['5'] = False
            c59['5'] = False
            c69['5'] = False
        elif solvednums[6][8] == 6:
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c75['6'] = False
            c76['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c19['6'] = False
            c29['6'] = False
            c39['6'] = False
            c49['6'] = False
            c59['6'] = False
            c69['6'] = False
        elif solvednums[6][8] == 7:
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c75['8'] = False
            c76['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c19['8'] = False
            c29['8'] = False
            c39['8'] = False
            c49['8'] = False
            c59['8'] = False
            c69['8'] = False
        elif solvednums[6][8] == 9:
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c76['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c19['9'] = False
            c29['9'] = False
            c39['9'] = False
            c49['9'] = False   
            c59['9'] = False
            c69['9'] = False
    if puzzlenums[7][0] > 0 and e81do == True:
        solvednums[7][0] = puzzlenums[7][0]
        e81do = False
        sleep(1)
    elif e81do == True and c81['1'] == True and c81['2'] == False and c81['3'] == False and c81['4'] == False and c81['5'] == False and c81['6'] == False and c81['7'] == False and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 1
    elif e81do == True and c81['1'] == False and c81['2'] == True and c81['3'] == False and c81['4'] == False and c81['5'] == False and c81['6'] == False and c81['7'] == False and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 2
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == True and c81['4'] == False and c81['5'] == False and c81['6'] == False and c81['7'] == False and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 3
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == False and c81['4'] == True and c81['5'] == False and c81['6'] == False and c81['7'] == False and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 4
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == False and c81['4'] == False and c81['5'] == True and c81['6'] == False and c81['7'] == False and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 5
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == False and c81['4'] == False and c81['5'] == False and c81['6'] == True and c81['7'] == False and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 6
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == False and c81['4'] == False and c81['5'] == False and c81['6'] == False and c81['7'] == True and c81['8'] == False and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 7
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == False and c81['4'] == False and c81['5'] == False and c81['6'] == False and c81['7'] == False and c81['8'] == True and c81['9'] == False:
        e81do = False
        solvednums[7][0] = 8
    elif e81do == True and c81['1'] == False and c81['2'] == False and c81['3'] == False and c81['4'] == False and c81['5'] == False and c81['6'] == False and c81['7'] == False and c81['8'] == False and c81['9'] == True:
        e81do = False
        solvednums[7][0] = 9
    else:
        if solvednums[7][0] == 1:
            c81['1'] = False
            c81['2'] = False
            c81['3'] = False
            c81['4'] = False
            c81['5'] = False
            c81['6'] = False
            c81['7'] = False
            c81['8'] = False
            c81['9'] = False
            c82['1'] = False
            c83['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c11['1'] = False
            c21['1'] = False
            c31['1'] = False
            c41['1'] = False
            c51['1'] = False
            c61['1'] = False
            c81['1'] = False
            c91['1'] = False
        elif solvednums[7][0] == 2:
            c81['1'] = False
            c81['2'] = False
            c81['3'] = False
            c81['4'] = False
            c81['5'] = False
            c81['6'] = False
            c81['7'] = False
            c81['8'] = False
            c81['9'] = False
            c82['2'] = False
            c83['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c11['2'] = False
            c21['2'] = False
            c31['2'] = False
            c41['2'] = False
            c51['2'] = False
            c61['2'] = False
        elif solvednums[7][0] == 3:
            c82['3'] = False
            c83['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c11['3'] = False
            c21['3'] = False
            c31['3'] = False
            c41['3'] = False
            c51['3'] = False
            c61['3'] = False
        elif solvednums[7][0] == 4:
            c82['4'] = False
            c83['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c11['4'] = False
            c21['4'] = False
            c31['4'] = False
            c41['4'] = False
            c51['4'] = False
            c61['4'] = False
        elif solvednums[7][0] == 5:
            c82['5'] = False
            c83['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c11['5'] = False
            c21['5'] = False
            c31['5'] = False
            c41['5'] = False
            c51['5'] = False
            c61['5'] = False
        elif solvednums[7][0] == 6:
            c82['6'] = False
            c83['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c11['6'] = False
            c21['6'] = False
            c31['6'] = False
            c41['6'] = False
            c51['6'] = False
            c61['6'] = False
        elif solvednums[7][0] == 7:
            c82['7'] = False
            c83['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c11['7'] = False
            c21['7'] = False
            c31['7'] = False
            c41['7'] = False
            c51['7'] = False
            c61['7'] = False
        elif solvednums[7][0] == 8:
            c82['8'] = False
            c83['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c11['8'] = False
            c21['8'] = False
            c31['8'] = False
            c41['8'] = False
            c51['8'] = False
            c61['8'] = False
        elif solvednums[7][0] == 9:
            c82['9'] = False
            c83['9'] = False
            c84['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c11['9'] = False
            c21['9'] = False
            c31['9'] = False
            c41['9'] = False   
            c51['9'] = False
            c61['9'] = False
    if puzzlenums[7][1] > 0 and e82do == True:
        solvednums[7][1] = puzzlenums[7][1]
        e82do = False
        sleep(1)
    elif e82do == True and c82['1'] == True and c82['2'] == False and c82['3'] == False and c82['4'] == False and c82['5'] == False and c82['6'] == False and c82['7'] == False and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 1
    elif e82do == True and c82['1'] == False and c82['2'] == True and c82['3'] == False and c82['4'] == False and c82['5'] == False and c82['6'] == False and c82['7'] == False and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 2
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == True and c82['4'] == False and c82['5'] == False and c82['6'] == False and c82['7'] == False and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 3
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == False and c82['4'] == True and c82['5'] == False and c82['6'] == False and c82['7'] == False and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 4
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == False and c82['4'] == False and c82['5'] == True and c82['6'] == False and c82['7'] == False and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 5
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == False and c82['4'] == False and c82['5'] == False and c82['6'] == True and c82['7'] == False and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 6
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == False and c82['4'] == False and c82['5'] == False and c82['6'] == False and c82['7'] == True and c82['8'] == False and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 7
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == False and c82['4'] == False and c82['5'] == False and c82['6'] == False and c82['7'] == False and c82['8'] == True and c82['9'] == False:
        e82do = False
        solvednums[7][1] = 8
    elif e82do == True and c82['1'] == False and c82['2'] == False and c82['3'] == False and c82['4'] == False and c82['5'] == False and c82['6'] == False and c82['7'] == False and c82['8'] == False and c82['9'] == True:
        e82do = False
        solvednums[7][1] = 9
    else:
        if solvednums[7][1] == 1:
            c81['1'] = False
            c83['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c12['1'] = False
            c22['1'] = False
            c32['1'] = False
            c42['1'] = False
            c52['1'] = False
            c62['1'] = False
        elif solvednums[7][1] == 2:
            c81['2'] = False
            c83['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c12['2'] = False
            c22['2'] = False
            c32['2'] = False
            c42['2'] = False
            c52['2'] = False
            c62['2'] = False
        elif solvednums[7][1] == 3:
            c81['3'] = False
            c83['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c12['3'] = False
            c22['3'] = False
            c32['3'] = False
            c42['3'] = False
            c52['3'] = False
            c62['3'] = False
        elif solvednums[7][1] == 4:
            c81['4'] = False
            c83['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c12['4'] = False
            c22['4'] = False
            c32['4'] = False
            c42['4'] = False
            c52['4'] = False
            c62['4'] = False
        elif solvednums[7][1] == 5:
            c81['5'] = False
            c83['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c12['5'] = False
            c22['5'] = False
            c32['5'] = False
            c42['5'] = False
            c52['5'] = False
            c62['5'] = False
        elif solvednums[7][1] == 6:
            c81['6'] = False
            c83['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c12['6'] = False
            c22['6'] = False
            c32['6'] = False
            c42['6'] = False
            c52['6'] = False
            c62['6'] = False
        elif solvednums[7][1] == 7:
            c81['7'] = False
            c83['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c12['7'] = False
            c22['7'] = False
            c32['7'] = False
            c42['7'] = False
            c52['7'] = False
            c62['7'] = False
        elif solvednums[7][1] == 8:
            c81['8'] = False
            c83['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c12['8'] = False
            c22['8'] = False
            c32['8'] = False
            c42['8'] = False
            c52['8'] = False
            c62['8'] = False
        elif solvednums[7][1] == 9:
            c81['9'] = False
            c83['9'] = False
            c84['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c12['9'] = False
            c22['9'] = False
            c32['9'] = False
            c42['9'] = False   
            c52['9'] = False
            c62['9'] = False
    if puzzlenums[7][2] > 0 and e83do == True:
        solvednums[7][2] = puzzlenums[7][2]
        e83do = False
        sleep(1)
    elif e83do == True and c83['1'] == True and c83['2'] == False and c83['3'] == False and c83['4'] == False and c83['5'] == False and c83['6'] == False and c83['7'] == False and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 1
    elif e83do == True and c83['1'] == False and c83['2'] == True and c83['3'] == False and c83['4'] == False and c83['5'] == False and c83['6'] == False and c83['7'] == False and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 2
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == True and c83['4'] == False and c83['5'] == False and c83['6'] == False and c83['7'] == False and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 3
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == False and c83['4'] == True and c83['5'] == False and c83['6'] == False and c83['7'] == False and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 4
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == False and c83['4'] == False and c83['5'] == True and c83['6'] == False and c83['7'] == False and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 5
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == False and c83['4'] == False and c83['5'] == False and c83['6'] == True and c83['7'] == False and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 6
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == False and c83['4'] == False and c83['5'] == False and c83['6'] == False and c83['7'] == True and c83['8'] == False and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 7
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == False and c83['4'] == False and c83['5'] == False and c83['6'] == False and c83['7'] == False and c83['8'] == True and c83['9'] == False:
        e83do = False
        solvednums[7][2] = 8
    elif e83do == True and c83['1'] == False and c83['2'] == False and c83['3'] == False and c83['4'] == False and c83['5'] == False and c83['6'] == False and c83['7'] == False and c83['8'] == False and c83['9'] == True:
        e83do = False
        solvednums[7][2] = 9
    else:
        if solvednums[7][2] == 1:
            c81['1'] = False
            c82['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c13['1'] = False
            c23['1'] = False
            c33['1'] = False
            c43['1'] = False
            c53['1'] = False
            c63['1'] = False
        elif solvednums[7][2] == 2:
            c81['2'] = False
            c82['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c13['2'] = False
            c23['2'] = False
            c33['2'] = False
            c43['2'] = False
            c53['2'] = False
            c63['2'] = False
        elif solvednums[7][2] == 3:
            c81['3'] = False
            c82['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c13['3'] = False
            c23['3'] = False
            c33['3'] = False
            c43['3'] = False
            c53['3'] = False
            c63['3'] = False
        elif solvednums[7][2] == 4:
            c81['4'] = False
            c82['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c13['4'] = False
            c23['4'] = False
            c33['4'] = False
            c43['4'] = False
            c53['4'] = False
            c63['4'] = False
        elif solvednums[7][2] == 5:
            c81['5'] = False
            c82['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c13['5'] = False
            c23['5'] = False
            c33['5'] = False
            c43['5'] = False
            c53['5'] = False
            c63['5'] = False
        elif solvednums[7][2] == 6:
            c81['6'] = False
            c82['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c13['6'] = False
            c23['6'] = False
            c33['6'] = False
            c43['6'] = False
            c53['6'] = False
            c63['6'] = False
        elif solvednums[7][2] == 7:
            c81['7'] = False
            c82['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c13['7'] = False
            c23['7'] = False
            c33['7'] = False
            c43['7'] = False
            c53['7'] = False
            c63['7'] = False
        elif solvednums[7][2] == 8:
            c81['8'] = False
            c82['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c13['8'] = False
            c23['8'] = False
            c33['8'] = False
            c43['8'] = False
            c53['8'] = False
            c63['8'] = False
        elif solvednums[7][2] == 9:
            c81['9'] = False
            c82['9'] = False
            c84['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c13['9'] = False
            c23['9'] = False
            c33['9'] = False
            c43['9'] = False   
            c53['9'] = False
            c63['9'] = False
    if puzzlenums[7][3] > 0 and e84do == True:
        solvednums[7][3] = puzzlenums[7][3]
        e84do = False
        sleep(1)
    elif e84do == True and c84['1'] == True and c84['2'] == False and c84['3'] == False and c84['4'] == False and c84['5'] == False and c84['6'] == False and c84['7'] == False and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 1
    elif e84do == True and c84['1'] == False and c84['2'] == True and c84['3'] == False and c84['4'] == False and c84['5'] == False and c84['6'] == False and c84['7'] == False and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 2
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == True and c84['4'] == False and c84['5'] == False and c84['6'] == False and c84['7'] == False and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 3
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == False and c84['4'] == True and c84['5'] == False and c84['6'] == False and c84['7'] == False and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 4
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == False and c84['4'] == False and c84['5'] == True and c84['6'] == False and c84['7'] == False and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 5
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == False and c84['4'] == False and c84['5'] == False and c84['6'] == True and c84['7'] == False and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 6
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == False and c84['4'] == False and c84['5'] == False and c84['6'] == False and c84['7'] == True and c84['8'] == False and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 7
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == False and c84['4'] == False and c84['5'] == False and c84['6'] == False and c84['7'] == False and c84['8'] == True and c84['9'] == False:
        e84do = False
        solvednums[7][3] = 8
    elif e84do == True and c84['1'] == False and c84['2'] == False and c84['3'] == False and c84['4'] == False and c84['5'] == False and c84['6'] == False and c84['7'] == False and c84['8'] == False and c84['9'] == True:
        e84do = False
        solvednums[7][3] = 9
    else:
        if solvednums[7][3] == 1:
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c14['1'] = False
            c24['1'] = False
            c34['1'] = False
            c44['1'] = False
            c54['1'] = False
            c64['1'] = False
        elif solvednums[7][3] == 2:
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c14['2'] = False
            c24['2'] = False
            c34['2'] = False
            c44['2'] = False
            c54['2'] = False
            c64['2'] = False
        elif solvednums[7][3] == 3:
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c14['3'] = False
            c24['3'] = False
            c34['3'] = False
            c44['3'] = False
            c54['3'] = False
            c64['3'] = False
        elif solvednums[7][3] == 4:
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c14['4'] = False
            c24['4'] = False
            c34['4'] = False
            c44['4'] = False
            c54['4'] = False
            c64['4'] = False
        elif solvednums[7][3] == 5:
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c14['5'] = False
            c24['5'] = False
            c34['5'] = False
            c44['5'] = False
            c54['5'] = False
            c64['5'] = False
        elif solvednums[7][3] == 6:
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c14['6'] = False
            c24['6'] = False
            c34['6'] = False
            c44['6'] = False
            c54['6'] = False
            c64['6'] = False
        elif solvednums[7][3] == 7:
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c14['7'] = False
            c24['7'] = False
            c34['7'] = False
            c44['7'] = False
            c54['7'] = False
            c64['7'] = False
        elif solvednums[7][3] == 8:
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c14['8'] = False
            c24['8'] = False
            c34['8'] = False
            c44['8'] = False
            c54['8'] = False
            c64['8'] = False
        elif solvednums[7][3] == 9:
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c94['9'] = False
            c95['9'] = False
            c96['9'] = False
            c74['9'] = False
            c75['9'] = False
            c76['9'] = False
            c14['9'] = False
            c24['9'] = False
            c34['9'] = False
            c44['9'] = False   
            c54['9'] = False
            c64['9'] = False
    if puzzlenums[7][5] > 0 and e85do == True:
        solvednums[7][4] = puzzlenums[7][4]
        e85do = False
        sleep(1)
    elif e85do == True and c85['1'] == True and c85['2'] == False and c85['3'] == False and c85['4'] == False and c85['5'] == False and c85['6'] == False and c85['7'] == False and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 1
    elif e85do == True and c85['1'] == False and c85['2'] == True and c85['3'] == False and c85['4'] == False and c85['5'] == False and c85['6'] == False and c85['7'] == False and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 2
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == True and c85['4'] == False and c85['5'] == False and c85['6'] == False and c85['7'] == False and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 3
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == False and c85['4'] == True and c85['5'] == False and c85['6'] == False and c85['7'] == False and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 4
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == False and c85['4'] == False and c85['5'] == True and c85['6'] == False and c85['7'] == False and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 5
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == False and c85['4'] == False and c85['5'] == False and c85['6'] == True and c85['7'] == False and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 6
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == False and c85['4'] == False and c85['5'] == False and c85['6'] == False and c85['7'] == True and c85['8'] == False and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 7
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == False and c85['4'] == False and c85['5'] == False and c85['6'] == False and c85['7'] == False and c85['8'] == True and c85['9'] == False:
        e85do = False
        solvednums[7][4] = 8
    elif e85do == True and c85['1'] == False and c85['2'] == False and c85['3'] == False and c85['4'] == False and c85['5'] == False and c85['6'] == False and c85['7'] == False and c85['8'] == False and c85['9'] == True:
        e85do = False
        solvednums[7][4] = 9
    else:
        if solvednums[7][4] == 1:
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c15['1'] = False
            c25['1'] = False
            c35['1'] = False
            c45['1'] = False
            c55['1'] = False
            c65['1'] = False
        elif solvednums[7][4] == 2:
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c15['2'] = False
            c25['2'] = False
            c35['2'] = False
            c45['2'] = False
            c55['2'] = False
            c65['2'] = False
        elif solvednums[7][4] == 3:
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c15['3'] = False
            c25['3'] = False
            c35['3'] = False
            c45['3'] = False
            c55['3'] = False
            c65['3'] = False
        elif solvednums[7][4] == 4:
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c15['4'] = False
            c25['4'] = False
            c35['4'] = False
            c45['4'] = False
            c55['4'] = False
            c65['4'] = False
        elif solvednums[7][4] == 5:
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c15['5'] = False
            c25['5'] = False
            c35['5'] = False
            c45['5'] = False
            c55['5'] = False
            c65['5'] = False
        elif solvednums[7][4] == 6:
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c15['6'] = False
            c25['6'] = False
            c35['6'] = False
            c45['6'] = False
            c55['6'] = False
            c65['6'] = False
        elif solvednums[7][4] == 7:
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c15['7'] = False
            c25['7'] = False
            c35['7'] = False
            c45['7'] = False
            c55['7'] = False
            c65['7'] = False
        elif solvednums[7][4] == 8:
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c15['8'] = False
            c25['8'] = False
            c35['8'] = False
            c45['8'] = False
            c55['8'] = False
            c65['8'] = False
        elif solvednums[7][4] == 9:
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c94['9'] = False
            c95['9'] = False
            c96['9'] = False
            c74['9'] = False
            c75['9'] = False
            c76['9'] = False
            c15['9'] = False
            c25['9'] = False
            c35['9'] = False
            c45['9'] = False   
            c55['9'] = False
            c65['9'] = False
    if puzzlenums[7][5] > 0 and e86do == True:
        solvednums[7][5] = puzzlenums[7][5]
        e86do = False
        sleep(1)
    elif e86do == True and c86['1'] == True and c86['2'] == False and c86['3'] == False and c86['4'] == False and c86['5'] == False and c86['6'] == False and c86['7'] == False and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 1
    elif e86do == True and c86['1'] == False and c86['2'] == True and c86['3'] == False and c86['4'] == False and c86['5'] == False and c86['6'] == False and c86['7'] == False and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 2
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == True and c86['4'] == False and c86['5'] == False and c86['6'] == False and c86['7'] == False and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 3
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == False and c86['4'] == True and c86['5'] == False and c86['6'] == False and c86['7'] == False and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][6] = 4
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == False and c86['4'] == False and c86['5'] == True and c86['6'] == False and c86['7'] == False and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 5
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == False and c86['4'] == False and c86['5'] == False and c86['6'] == True and c86['7'] == False and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 6
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == False and c86['4'] == False and c86['5'] == False and c86['6'] == False and c86['7'] == True and c86['8'] == False and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 7
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == False and c86['4'] == False and c86['5'] == False and c86['6'] == False and c86['7'] == False and c86['8'] == True and c86['9'] == False:
        e86do = False
        solvednums[7][5] = 8
    elif e86do == True and c86['1'] == False and c86['2'] == False and c86['3'] == False and c86['4'] == False and c86['5'] == False and c86['6'] == False and c86['7'] == False and c86['8'] == False and c86['9'] == True:
        e86do = False
        solvednums[7][5] = 9     
    else:
        if solvednums[7][5] == 1:
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c16['1'] = False
            c26['1'] = False
            c36['1'] = False
            c46['1'] = False
            c56['1'] = False
            c66['1'] = False
        elif solvednums[7][5] == 2: 
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c16['2'] = False
            c26['2'] = False
            c36['2'] = False
            c46['2'] = False
            c56['2'] = False
            c66['2'] = False
        elif solvednums[7][5] == 3:
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c16['3'] = False
            c26['3'] = False
            c36['3'] = False
            c46['3'] = False
            c56['3'] = False
            c66['3'] = False
        elif solvednums[7][5] == 4:
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c16['4'] = False
            c26['4'] = False
            c36['4'] = False
            c46['4'] = False
            c56['4'] = False
            c66['4'] = False
        elif solvednums[7][5] == 5:
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c16['5'] = False
            c26['5'] = False
            c36['5'] = False
            c46['5'] = False
            c56['5'] = False
            c66['5'] = False
        elif solvednums[7][5] == 6:
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c16['6'] = False
            c26['6'] = False
            c36['6'] = False
            c46['6'] = False
            c56['6'] = False
            c66['6'] = False
        elif solvednums[7][5] == 7:
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c16['7'] = False
            c26['7'] = False
            c36['7'] = False
            c46['7'] = False
            c56['7'] = False
            c66['7'] = False
        elif solvednums[7][5] == 8:
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c16['8'] = False
            c26['8'] = False
            c36['8'] = False
            c46['8'] = False
            c56['8'] = False
            c66['8'] = False
        elif solvednums[7][5] == 9:
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c94['9'] = False
            c95['9'] = False
            c96['9'] = False
            c74['9'] = False
            c75['9'] = False
            c76['9'] = False
            c16['9'] = False
            c26['9'] = False
            c36['9'] = False
            c46['9'] = False   
            c56['9'] = False
            c66['9'] = False
    if puzzlenums[7][6] > 0 and e87do == True:
        solvednums[7][6] = puzzlenums[7][6]
        e87do = False
        sleep(1)
    elif e87do == True and c87['1'] == True and c87['2'] == False and c87['3'] == False and c87['4'] == False and c87['5'] == False and c87['6'] == False and c87['7'] == False and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 1
    elif e87do == True and c87['1'] == False and c87['2'] == True and c87['3'] == False and c87['4'] == False and c87['5'] == False and c87['6'] == False and c87['7'] == False and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 2
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == True and c87['4'] == False and c87['5'] == False and c87['6'] == False and c87['7'] == False and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 3
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == False and c87['4'] == True and c87['5'] == False and c87['6'] == False and c87['7'] == False and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 4
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == False and c87['4'] == False and c87['5'] == True and c87['6'] == False and c87['7'] == False and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 5
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == False and c87['4'] == False and c87['5'] == False and c87['6'] == True and c87['7'] == False and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 6
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == False and c87['4'] == False and c87['5'] == False and c87['6'] == False and c87['7'] == True and c87['8'] == False and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 7
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == False and c87['4'] == False and c87['5'] == False and c87['6'] == False and c87['7'] == False and c87['8'] == True and c87['9'] == False:
        e87do = False
        solvednums[7][6] = 8
    elif e87do == True and c87['1'] == False and c87['2'] == False and c87['3'] == False and c87['4'] == False and c87['5'] == False and c87['6'] == False and c87['7'] == False and c87['8'] == False and c87['9'] == True:
        e87do = False
        solvednums[7][6] = 9
    else:
        if solvednums[7][6] == 1:
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c17['1'] = False
            c27['1'] = False
            c37['1'] = False
            c47['1'] = False
            c57['1'] = False
            c67['1'] = False
        elif solvednums[7][6] == 2:
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c17['2'] = False
            c27['2'] = False
            c37['2'] = False
            c47['2'] = False
            c57['2'] = False
            c67['2'] = False
        elif solvednums[7][6] == 3:
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c17['3'] = False
            c27['3'] = False
            c37['3'] = False
            c47['3'] = False
            c57['3'] = False
            c67['3'] = False
        elif solvednums[7][6] == 4:
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c17['4'] = False
            c27['4'] = False
            c37['4'] = False
            c47['4'] = False
            c57['4'] = False
            c67['4'] = False
        elif solvednums[7][6] == 5:
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c17['5'] = False
            c27['5'] = False
            c37['5'] = False
            c47['5'] = False
            c57['5'] = False
            c67['5'] = False
        elif solvednums[7][6] == 6:
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c17['6'] = False
            c27['6'] = False
            c37['6'] = False
            c47['6'] = False
            c57['6'] = False
            c67['6'] = False
        elif solvednums[7][6] == 7:
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c17['7'] = False
            c27['7'] = False
            c37['7'] = False
            c47['7'] = False
            c57['7'] = False
            c67['7'] = False
        elif solvednums[7][6] == 8:
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c17['8'] = False
            c27['8'] = False
            c37['8'] = False
            c47['8'] = False
            c57['8'] = False
            c67['8'] = False
        elif solvednums[7][6] == 9:
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c17['9'] = False
            c27['9'] = False
            c37['9'] = False
            c47['9'] = False   
            c57['9'] = False
            c67['9'] = False
    if puzzlenums[7][7] > 0 and e88do == True:
        solvednums[7][7] = puzzlenums[7][7]
        e88do = False
        sleep(1)
    elif e88do == True and c88['1'] == True and c88['2'] == False and c88['3'] == False and c88['4'] == False and c88['5'] == False and c88['6'] == False and c88['7'] == False and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 1
    elif e88do == True and c88['1'] == False and c88['2'] == True and c88['3'] == False and c88['4'] == False and c88['5'] == False and c88['6'] == False and c88['7'] == False and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 2
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == True and c88['4'] == False and c88['5'] == False and c88['6'] == False and c88['7'] == False and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 3
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == False and c88['4'] == True and c88['5'] == False and c88['6'] == False and c88['7'] == False and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 4
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == False and c88['4'] == False and c88['5'] == True and c88['6'] == False and c88['7'] == False and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 5
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == False and c88['4'] == False and c88['5'] == False and c88['6'] == True and c88['7'] == False and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 6
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == False and c88['4'] == False and c88['5'] == False and c88['6'] == False and c88['7'] == True and c88['8'] == False and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 7
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == False and c88['4'] == False and c88['5'] == False and c88['6'] == False and c88['7'] == False and c88['8'] == True and c88['9'] == False:
        e88do = False
        solvednums[7][7] = 8
    elif e88do == True and c88['1'] == False and c88['2'] == False and c88['3'] == False and c88['4'] == False and c88['5'] == False and c88['6'] == False and c88['7'] == False and c88['8'] == False and c88['9'] == True:
        e88do = False
        solvednums[7][7] = 9
    else:
        if solvednums[7][7] == 1:
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c18['1'] = False
            c28['1'] = False
            c38['1'] = False
            c48['1'] = False
            c58['1'] = False
            c68['1'] = False
        elif solvednums[7][7] == 2:
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c18['2'] = False
            c28['2'] = False
            c38['2'] = False
            c48['2'] = False
            c58['2'] = False
            c68['2'] = False
        elif solvednums[7][7] == 3:
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c18['3'] = False
            c28['3'] = False
            c38['3'] = False
            c48['3'] = False
            c58['3'] = False
            c68['3'] = False
        elif solvednums[7][7] == 4:
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c18['4'] = False
            c28['4'] = False
            c38['4'] = False
            c48['4'] = False
            c58['4'] = False
            c68['4'] = False
        elif solvednums[7][7] == 5:
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c18['5'] = False
            c28['5'] = False
            c38['5'] = False
            c48['5'] = False
            c58['5'] = False
            c68['5'] = False
        elif solvednums[7][7] == 6:
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c18['6'] = False
            c28['6'] = False
            c38['6'] = False
            c48['6'] = False
            c58['6'] = False
            c68['6'] = False
        elif solvednums[7][7] == 7:
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c85['7'] = False
            c86['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c18['7'] = False
            c28['7'] = False
            c38['7'] = False
            c48['7'] = False
            c58['7'] = False
            c68['7'] = False
        elif solvednums[7][7] == 8:
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c18['8'] = False
            c28['8'] = False
            c38['8'] = False
            c48['8'] = False
            c58['8'] = False
            c68['8'] = False
        elif solvednums[7][7] == 9:
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c85['9'] = False 
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c18['9'] = False
            c28['9'] = False
            c38['9'] = False
            c48['9'] = False   
            c58['9'] = False
            c68['9'] = False
    if puzzlenums[7][8] > 0 and e89do == True:
        solvednums[7][8] = puzzlenums[7][8]
        e89do = False
        sleep(1)
    elif e89do == True and c89['1'] == True and c89['2'] == False and c89['3'] == False and c89['4'] == False and c89['5'] == False and c89['6'] == False and c89['7'] == False and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 1
    elif e89do == True and c89['1'] == False and c89['2'] == True and c89['3'] == False and c89['4'] == False and c89['5'] == False and c89['6'] == False and c89['7'] == False and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 2
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == True and c89['4'] == False and c89['5'] == False and c89['6'] == False and c89['7'] == False and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 3
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == False and c89['4'] == True and c89['5'] == False and c89['6'] == False and c89['7'] == False and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 4
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == False and c89['4'] == False and c89['5'] == True and c89['6'] == False and c89['7'] == False and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 5
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == False and c89['4'] == False and c89['5'] == False and c89['6'] == True and c89['7'] == False and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 6
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == False and c89['4'] == False and c89['5'] == False and c89['6'] == False and c89['7'] == True and c89['8'] == False and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 7
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == False and c89['4'] == False and c89['5'] == False and c89['6'] == False and c89['7'] == False and c89['8'] == True and c89['9'] == False:
        e89do = False
        solvednums[7][8] = 8
    elif e89do == True and c89['1'] == False and c89['2'] == False and c89['3'] == False and c89['4'] == False and c89['5'] == False and c89['6'] == False and c89['7'] == False and c89['8'] == False and c89['9'] == True:
        e89do = False
        solvednums[7][8] = 9
    else:
        if solvednums[7][8] == 1:
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c85['1'] = False
            c86['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c19['1'] = False
            c29['1'] = False
            c39['1'] = False
            c49['1'] = False
            c59['1'] = False
            c69['1'] = False
        elif solvednums[7][8] == 2:
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c85['2'] = False
            c86['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c19['2'] = False
            c29['2'] = False
            c39['2'] = False
            c49['2'] = False
            c59['2'] = False
            c69['2'] = False
        elif solvednums[7][8] == 3:
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c85['3'] = False
            c86['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c19['3'] = False
            c29['3'] = False
            c39['3'] = False
            c49['3'] = False
            c59['3'] = False
            c69['3'] = False
        elif solvednums[7][8] == 4:
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c85['4'] = False
            c86['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c19['4'] = False
            c29['4'] = False
            c39['4'] = False
            c49['4'] = False
            c59['4'] = False
            c69['4'] = False
        elif solvednums[7][8] == 5:
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c85['5'] = False
            c86['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c19['5'] = False
            c29['5'] = False
            c39['5'] = False
            c49['5'] = False
            c59['5'] = False
            c69['5'] = False
        elif solvednums[7][8] == 6:
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c85['6'] = False
            c86['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c19['6'] = False
            c29['6'] = False
            c39['6'] = False
            c49['6'] = False
            c59['6'] = False
            c69['6'] = False
        elif solvednums[7][8] == 7:
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c85['8'] = False
            c86['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c19['8'] = False
            c29['8'] = False
            c39['8'] = False
            c49['8'] = False
            c59['8'] = False
            c69['8'] = False
        elif solvednums[7][8] == 9:
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c86['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c19['9'] = False
            c29['9'] = False
            c39['9'] = False
            c49['9'] = False   
            c59['9'] = False
            c69['9'] = False
    if puzzlenums[8][0] > 0 and e91do == True:
        solvednums[8][0] = puzzlenums[8][0]
        e91do = False
        sleep(1)
    elif e91do == True and c91['1'] == True and c91['2'] == False and c91['3'] == False and c91['4'] == False and c91['5'] == False and c91['6'] == False and c91['7'] == False and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 1
    elif e91do == True and c91['1'] == False and c91['2'] == True and c91['3'] == False and c91['4'] == False and c91['5'] == False and c91['6'] == False and c91['7'] == False and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 2
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == True and c91['4'] == False and c91['5'] == False and c91['6'] == False and c91['7'] == False and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 3
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == False and c91['4'] == True and c91['5'] == False and c91['6'] == False and c91['7'] == False and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 4
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == False and c91['4'] == False and c91['5'] == True and c91['6'] == False and c91['7'] == False and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 5
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == False and c91['4'] == False and c91['5'] == False and c91['6'] == True and c91['7'] == False and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 6
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == False and c91['4'] == False and c91['5'] == False and c91['6'] == False and c91['7'] == True and c91['8'] == False and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 7
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == False and c91['4'] == False and c91['5'] == False and c91['6'] == False and c91['7'] == False and c91['8'] == True and c91['9'] == False:
        e91do = False
        solvednums[8][0] = 8
    elif e91do == True and c91['1'] == False and c91['2'] == False and c91['3'] == False and c91['4'] == False and c91['5'] == False and c91['6'] == False and c91['7'] == False and c91['8'] == False and c91['9'] == True:
        e91do = False
        solvednums[8][0] = 9
    else:
        if solvednums[8][0] == 1:
            c91['1'] = False
            c91['2'] = False
            c91['3'] = False
            c91['4'] = False
            c91['5'] = False
            c91['6'] = False
            c91['7'] = False
            c91['8'] = False
            c91['9'] = False
            c92['1'] = False
            c93['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c11['1'] = False
            c21['1'] = False
            c31['1'] = False
            c41['1'] = False
            c51['1'] = False
            c61['1'] = False
            c91['1'] = False
            c91['1'] = False
        elif solvednums[8][0] == 2:
            c91['1'] = False
            c91['2'] = False
            c91['3'] = False
            c91['4'] = False
            c91['5'] = False
            c91['6'] = False
            c91['7'] = False
            c91['8'] = False
            c91['9'] = False
            c92['2'] = False
            c93['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c11['2'] = False
            c21['2'] = False
            c31['2'] = False
            c41['2'] = False
            c51['2'] = False
            c61['2'] = False
        elif solvednums[8][0] == 3:
            c92['3'] = False
            c93['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c11['3'] = False
            c21['3'] = False
            c31['3'] = False
            c41['3'] = False
            c51['3'] = False
            c61['3'] = False
        elif solvednums[8][0] == 4:
            c92['4'] = False
            c93['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c11['4'] = False
            c21['4'] = False
            c31['4'] = False
            c41['4'] = False
            c51['4'] = False
            c61['4'] = False
        elif solvednums[8][0] == 5:
            c92['5'] = False
            c93['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c11['5'] = False
            c21['5'] = False
            c31['5'] = False
            c41['5'] = False
            c51['5'] = False
            c61['5'] = False
        elif solvednums[8][0] == 6:
            c92['6'] = False
            c93['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c11['6'] = False
            c21['6'] = False
            c31['6'] = False
            c41['6'] = False
            c51['6'] = False
            c61['6'] = False
        elif solvednums[8][0] == 7:
            c92['7'] = False
            c93['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c11['7'] = False
            c21['7'] = False
            c31['7'] = False
            c41['7'] = False
            c51['7'] = False
            c61['7'] = False
        elif solvednums[8][0] == 8:
            c92['8'] = False
            c93['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c11['8'] = False
            c21['8'] = False
            c31['8'] = False
            c41['8'] = False
            c51['8'] = False
            c61['8'] = False
        elif solvednums[8][0] == 9:
            c92['9'] = False
            c93['9'] = False
            c94['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c11['9'] = False
            c21['9'] = False
            c31['9'] = False
            c41['9'] = False   
            c51['9'] = False
            c61['9'] = False
    if puzzlenums[8][1] > 0 and e92do == True:
        solvednums[8][1] = puzzlenums[8][1]
        e92do = False
        sleep(1)
    elif e92do == True and c92['1'] == True and c92['2'] == False and c92['3'] == False and c92['4'] == False and c92['5'] == False and c92['6'] == False and c92['7'] == False and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 1
    elif e92do == True and c92['1'] == False and c92['2'] == True and c92['3'] == False and c92['4'] == False and c92['5'] == False and c92['6'] == False and c92['7'] == False and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 2
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == True and c92['4'] == False and c92['5'] == False and c92['6'] == False and c92['7'] == False and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 3
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == False and c92['4'] == True and c92['5'] == False and c92['6'] == False and c92['7'] == False and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 4
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == False and c92['4'] == False and c92['5'] == True and c92['6'] == False and c92['7'] == False and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 5
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == False and c92['4'] == False and c92['5'] == False and c92['6'] == True and c92['7'] == False and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 6
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == False and c92['4'] == False and c92['5'] == False and c92['6'] == False and c92['7'] == True and c92['8'] == False and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 7
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == False and c92['4'] == False and c92['5'] == False and c92['6'] == False and c92['7'] == False and c92['8'] == True and c92['9'] == False:
        e92do = False
        solvednums[8][1] = 8
    elif e92do == True and c92['1'] == False and c92['2'] == False and c92['3'] == False and c92['4'] == False and c92['5'] == False and c92['6'] == False and c92['7'] == False and c92['8'] == False and c92['9'] == True:
        e92do = False
        solvednums[8][1] = 9
    else:
        if solvednums[8][1] == 1:
            c91['1'] = False
            c93['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c12['1'] = False
            c22['1'] = False
            c32['1'] = False
            c42['1'] = False
            c52['1'] = False
            c62['1'] = False
        elif solvednums[8][1] == 2:
            c91['2'] = False
            c93['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c12['2'] = False
            c22['2'] = False
            c32['2'] = False
            c42['2'] = False
            c52['2'] = False
            c62['2'] = False
        elif solvednums[8][1] == 3:
            c91['3'] = False
            c93['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c12['3'] = False
            c22['3'] = False
            c32['3'] = False
            c42['3'] = False
            c52['3'] = False
            c62['3'] = False
        elif solvednums[8][1] == 4:
            c91['4'] = False
            c93['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c12['4'] = False
            c22['4'] = False
            c32['4'] = False
            c42['4'] = False
            c52['4'] = False
            c62['4'] = False
        elif solvednums[8][1] == 5:
            c91['5'] = False
            c93['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c12['5'] = False
            c22['5'] = False
            c32['5'] = False
            c42['5'] = False
            c52['5'] = False
            c62['5'] = False
        elif solvednums[8][1] == 6:
            c91['6'] = False
            c93['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c12['6'] = False
            c22['6'] = False
            c32['6'] = False
            c42['6'] = False
            c52['6'] = False
            c62['6'] = False
        elif solvednums[8][1] == 7:
            c91['7'] = False
            c93['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c12['7'] = False
            c22['7'] = False
            c32['7'] = False
            c42['7'] = False
            c52['7'] = False
            c62['7'] = False
        elif solvednums[8][1] == 8:
            c91['8'] = False
            c93['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c12['8'] = False
            c22['8'] = False
            c32['8'] = False
            c42['8'] = False
            c52['8'] = False
            c62['8'] = False
        elif solvednums[8][1] == 9:
            c91['9'] = False
            c93['9'] = False
            c94['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c12['9'] = False
            c22['9'] = False
            c32['9'] = False
            c42['9'] = False   
            c52['9'] = False
            c62['9'] = False
    if puzzlenums[8][2] > 0 and e93do == True:
        solvednums[8][2] = puzzlenums[8][2]
        e93do = False
        sleep(1)
    elif e93do == True and c93['1'] == True and c93['2'] == False and c93['3'] == False and c93['4'] == False and c93['5'] == False and c93['6'] == False and c93['7'] == False and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 1
    elif e93do == True and c93['1'] == False and c93['2'] == True and c93['3'] == False and c93['4'] == False and c93['5'] == False and c93['6'] == False and c93['7'] == False and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 2
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == True and c93['4'] == False and c93['5'] == False and c93['6'] == False and c93['7'] == False and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 3
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == False and c93['4'] == True and c93['5'] == False and c93['6'] == False and c93['7'] == False and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 4
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == False and c93['4'] == False and c93['5'] == True and c93['6'] == False and c93['7'] == False and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 5
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == False and c93['4'] == False and c93['5'] == False and c93['6'] == True and c93['7'] == False and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 6
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == False and c93['4'] == False and c93['5'] == False and c93['6'] == False and c93['7'] == True and c93['8'] == False and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 7
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == False and c93['4'] == False and c93['5'] == False and c93['6'] == False and c93['7'] == False and c93['8'] == True and c93['9'] == False:
        e93do = False
        solvednums[8][2] = 8
    elif e93do == True and c93['1'] == False and c93['2'] == False and c93['3'] == False and c93['4'] == False and c93['5'] == False and c93['6'] == False and c93['7'] == False and c93['8'] == False and c93['9'] == True:
        e93do = False
        solvednums[8][2] = 9
    else:
        if solvednums[8][2] == 1:
            c91['1'] = False
            c92['1'] = False
            c94['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c81['1'] = False
            c82['1'] = False
            c83['1'] = False
            c71['1'] = False
            c72['1'] = False
            c73['1'] = False
            c13['1'] = False
            c23['1'] = False
            c33['1'] = False
            c43['1'] = False
            c53['1'] = False
            c63['1'] = False
        elif solvednums[8][2] == 2:
            c91['2'] = False
            c92['2'] = False
            c94['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c81['2'] = False
            c82['2'] = False
            c83['2'] = False
            c71['2'] = False
            c72['2'] = False
            c73['2'] = False
            c13['2'] = False
            c23['2'] = False
            c33['2'] = False
            c43['2'] = False
            c53['2'] = False
            c63['2'] = False
        elif solvednums[8][2] == 3:
            c91['3'] = False
            c92['3'] = False
            c94['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c71['3'] = False
            c72['3'] = False
            c73['3'] = False
            c81['3'] = False
            c82['3'] = False
            c83['3'] = False
            c13['3'] = False
            c23['3'] = False
            c33['3'] = False
            c43['3'] = False
            c53['3'] = False
            c63['3'] = False
        elif solvednums[8][2] == 4:
            c91['4'] = False
            c92['4'] = False
            c94['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c81['4'] = False
            c82['4'] = False
            c83['4'] = False
            c71['4'] = False
            c72['4'] = False
            c73['4'] = False
            c13['4'] = False
            c23['4'] = False
            c33['4'] = False
            c43['4'] = False
            c53['4'] = False
            c63['4'] = False
        elif solvednums[8][2] == 5:
            c91['5'] = False
            c92['5'] = False
            c94['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c81['5'] = False
            c82['5'] = False
            c83['5'] = False
            c71['5'] = False
            c72['5'] = False
            c73['5'] = False
            c13['5'] = False
            c23['5'] = False
            c33['5'] = False
            c43['5'] = False
            c53['5'] = False
            c63['5'] = False
        elif solvednums[8][2] == 6:
            c91['6'] = False
            c92['6'] = False
            c94['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c81['6'] = False
            c82['6'] = False
            c83['6'] = False
            c71['6'] = False
            c72['6'] = False
            c73['6'] = False
            c13['6'] = False
            c23['6'] = False
            c33['6'] = False
            c43['6'] = False
            c53['6'] = False
            c63['6'] = False
        elif solvednums[8][2] == 7:
            c91['7'] = False
            c92['7'] = False
            c94['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c81['7'] = False
            c82['7'] = False
            c83['7'] = False
            c71['7'] = False
            c72['7'] = False
            c73['7'] = False
            c13['7'] = False
            c23['7'] = False
            c33['7'] = False
            c43['7'] = False
            c53['7'] = False
            c63['7'] = False
        elif solvednums[8][2] == 8:
            c91['8'] = False
            c92['8'] = False
            c94['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c81['8'] = False
            c82['8'] = False
            c83['8'] = False
            c71['8'] = False
            c72['8'] = False
            c73['8'] = False
            c13['8'] = False
            c23['8'] = False
            c33['8'] = False
            c43['8'] = False
            c53['8'] = False
            c63['8'] = False
        elif solvednums[8][2] == 9:
            c91['9'] = False
            c92['9'] = False
            c94['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c71['9'] = False
            c72['9'] = False
            c73['9'] = False
            c81['9'] = False
            c82['9'] = False
            c83['9'] = False
            c13['9'] = False
            c23['9'] = False
            c33['9'] = False
            c43['9'] = False   
            c53['9'] = False
            c63['9'] = False
    if puzzlenums[8][3] > 0 and e94do == True:
        solvednums[8][3] = puzzlenums[8][3]
        e94do = False
        sleep(1)
    elif e94do == True and c94['1'] == True and c94['2'] == False and c94['3'] == False and c94['4'] == False and c94['5'] == False and c94['6'] == False and c94['7'] == False and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 1
    elif e94do == True and c94['1'] == False and c94['2'] == True and c94['3'] == False and c94['4'] == False and c94['5'] == False and c94['6'] == False and c94['7'] == False and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 2
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == True and c94['4'] == False and c94['5'] == False and c94['6'] == False and c94['7'] == False and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 3
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == False and c94['4'] == True and c94['5'] == False and c94['6'] == False and c94['7'] == False and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 4
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == False and c94['4'] == False and c94['5'] == True and c94['6'] == False and c94['7'] == False and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 5
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == False and c94['4'] == False and c94['5'] == False and c94['6'] == True and c94['7'] == False and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 6
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == False and c94['4'] == False and c94['5'] == False and c94['6'] == False and c94['7'] == True and c94['8'] == False and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 7
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == False and c94['4'] == False and c94['5'] == False and c94['6'] == False and c94['7'] == False and c94['8'] == True and c94['9'] == False:
        e94do = False
        solvednums[8][3] = 8
    elif e94do == True and c94['1'] == False and c94['2'] == False and c94['3'] == False and c94['4'] == False and c94['5'] == False and c94['6'] == False and c94['7'] == False and c94['8'] == False and c94['9'] == True:
        e94do = False
        solvednums[8][3] = 9
    else:
        if solvednums[8][3] == 1:
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c14['1'] = False
            c24['1'] = False
            c34['1'] = False
            c44['1'] = False
            c54['1'] = False
            c64['1'] = False
        elif solvednums[8][3] == 2:
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c14['2'] = False
            c24['2'] = False
            c34['2'] = False
            c44['2'] = False
            c54['2'] = False
            c64['2'] = False
        elif solvednums[8][3] == 3:
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c14['3'] = False
            c24['3'] = False
            c34['3'] = False
            c44['3'] = False
            c54['3'] = False
            c64['3'] = False
        elif solvednums[8][3] == 4:
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c14['4'] = False
            c24['4'] = False
            c34['4'] = False
            c44['4'] = False
            c54['4'] = False
            c64['4'] = False
        elif solvednums[8][3] == 5:
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c14['5'] = False
            c24['5'] = False
            c34['5'] = False
            c44['5'] = False
            c54['5'] = False
            c64['5'] = False
        elif solvednums[8][3] == 6:
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c14['6'] = False
            c24['6'] = False
            c34['6'] = False
            c44['6'] = False
            c54['6'] = False
            c64['6'] = False
        elif solvednums[8][3] == 7:
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c14['7'] = False
            c24['7'] = False
            c34['7'] = False
            c44['7'] = False
            c54['7'] = False
            c64['7'] = False
        elif solvednums[8][3] == 8:
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c14['8'] = False
            c24['8'] = False
            c34['8'] = False
            c44['8'] = False
            c54['8'] = False
            c64['8'] = False
        elif solvednums[8][3] == 9:
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c84['9'] = False
            c85['9'] = False
            c86['9'] = False
            c74['9'] = False
            c75['9'] = False
            c76['9'] = False
            c14['9'] = False
            c24['9'] = False
            c34['9'] = False
            c44['9'] = False   
            c54['9'] = False
            c64['9'] = False
    if puzzlenums[8][5] > 0 and e95do == True:
        solvednums[8][4] = puzzlenums[8][4]
        e95do = False
        sleep(1)
    elif e95do == True and c95['1'] == True and c95['2'] == False and c95['3'] == False and c95['4'] == False and c95['5'] == False and c95['6'] == False and c95['7'] == False and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 1
    elif e95do == True and c95['1'] == False and c95['2'] == True and c95['3'] == False and c95['4'] == False and c95['5'] == False and c95['6'] == False and c95['7'] == False and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 2
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == True and c95['4'] == False and c95['5'] == False and c95['6'] == False and c95['7'] == False and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 3
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == False and c95['4'] == True and c95['5'] == False and c95['6'] == False and c95['7'] == False and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 4
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == False and c95['4'] == False and c95['5'] == True and c95['6'] == False and c95['7'] == False and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 5
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == False and c95['4'] == False and c95['5'] == False and c95['6'] == True and c95['7'] == False and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 6
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == False and c95['4'] == False and c95['5'] == False and c95['6'] == False and c95['7'] == True and c95['8'] == False and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 7
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == False and c95['4'] == False and c95['5'] == False and c95['6'] == False and c95['7'] == False and c95['8'] == True and c95['9'] == False:
        e95do = False
        solvednums[8][4] = 8
    elif e95do == True and c95['1'] == False and c95['2'] == False and c95['3'] == False and c95['4'] == False and c95['5'] == False and c95['6'] == False and c95['7'] == False and c95['8'] == False and c95['9'] == True:
        e95do = False
        solvednums[8][4] = 9
    else:
        if solvednums[8][4] == 1:
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c15['1'] = False
            c25['1'] = False
            c35['1'] = False
            c45['1'] = False
            c55['1'] = False
            c65['1'] = False
        elif solvednums[8][4] == 2:
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c15['2'] = False
            c25['2'] = False
            c35['2'] = False
            c45['2'] = False
            c55['2'] = False
            c65['2'] = False
        elif solvednums[8][4] == 3:
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c15['3'] = False
            c25['3'] = False
            c35['3'] = False
            c45['3'] = False
            c55['3'] = False
            c65['3'] = False
        elif solvednums[8][4] == 4:
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c15['4'] = False
            c25['4'] = False
            c35['4'] = False
            c45['4'] = False
            c55['4'] = False
            c65['4'] = False
        elif solvednums[8][4] == 5:
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c15['5'] = False
            c25['5'] = False
            c35['5'] = False
            c45['5'] = False
            c55['5'] = False
            c65['5'] = False
        elif solvednums[8][4] == 6:
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c15['6'] = False
            c25['6'] = False
            c35['6'] = False
            c45['6'] = False
            c55['6'] = False
            c65['6'] = False
        elif solvednums[8][4] == 7:
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c15['7'] = False
            c25['7'] = False
            c35['7'] = False
            c45['7'] = False
            c55['7'] = False
            c65['7'] = False
        elif solvednums[8][4] == 8:
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c15['8'] = False
            c25['8'] = False
            c35['8'] = False
            c45['8'] = False
            c55['8'] = False
            c65['8'] = False
        elif solvednums[8][4] == 9:
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c84['9'] = False
            c85['9'] = False
            c86['9'] = False
            c74['9'] = False
            c75['9'] = False
            c76['9'] = False
            c15['9'] = False
            c25['9'] = False
            c35['9'] = False
            c45['9'] = False   
            c55['9'] = False
            c65['9'] = False
    if puzzlenums[8][5] > 0 and e96do == True:
        solvednums[8][5] = puzzlenums[8][5]
        e96do = False
        sleep(1)
    elif e96do == True and c96['1'] == True and c96['2'] == False and c96['3'] == False and c96['4'] == False and c96['5'] == False and c96['6'] == False and c96['7'] == False and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 1
    elif e96do == True and c96['1'] == False and c96['2'] == True and c96['3'] == False and c96['4'] == False and c96['5'] == False and c96['6'] == False and c96['7'] == False and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 2
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == True and c96['4'] == False and c96['5'] == False and c96['6'] == False and c96['7'] == False and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 3
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == False and c96['4'] == True and c96['5'] == False and c96['6'] == False and c96['7'] == False and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][6] = 4
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == False and c96['4'] == False and c96['5'] == True and c96['6'] == False and c96['7'] == False and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 5
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == False and c96['4'] == False and c96['5'] == False and c96['6'] == True and c96['7'] == False and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 6
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == False and c96['4'] == False and c96['5'] == False and c96['6'] == False and c96['7'] == True and c96['8'] == False and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 7
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == False and c96['4'] == False and c96['5'] == False and c96['6'] == False and c96['7'] == False and c96['8'] == True and c96['9'] == False:
        e96do = False
        solvednums[8][5] = 8
    elif e96do == True and c96['1'] == False and c96['2'] == False and c96['3'] == False and c96['4'] == False and c96['5'] == False and c96['6'] == False and c96['7'] == False and c96['8'] == False and c96['9'] == True:
        e96do = False
        solvednums[8][5] = 9     
    else:
        if solvednums[8][5] == 1:
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c84['1'] = False
            c85['1'] = False
            c86['1'] = False
            c74['1'] = False
            c75['1'] = False
            c76['1'] = False
            c16['1'] = False
            c26['1'] = False
            c36['1'] = False
            c46['1'] = False
            c56['1'] = False
            c66['1'] = False
        elif solvednums[8][5] == 2: 
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c84['2'] = False
            c85['2'] = False
            c86['2'] = False
            c74['2'] = False
            c75['2'] = False
            c76['2'] = False
            c16['2'] = False
            c26['2'] = False
            c36['2'] = False
            c46['2'] = False
            c56['2'] = False
            c66['2'] = False
        elif solvednums[8][5] == 3:
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c84['3'] = False
            c85['3'] = False
            c86['3'] = False
            c74['3'] = False
            c75['3'] = False
            c76['3'] = False
            c16['3'] = False
            c26['3'] = False
            c36['3'] = False
            c46['3'] = False
            c56['3'] = False
            c66['3'] = False
        elif solvednums[8][5] == 4:
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c74['4'] = False
            c75['4'] = False
            c76['4'] = False
            c84['4'] = False
            c85['4'] = False
            c86['4'] = False
            c16['4'] = False
            c26['4'] = False
            c36['4'] = False
            c46['4'] = False
            c56['4'] = False
            c66['4'] = False
        elif solvednums[8][5] == 5:
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c84['5'] = False
            c85['5'] = False
            c86['5'] = False
            c74['5'] = False
            c75['5'] = False
            c76['5'] = False
            c16['5'] = False
            c26['5'] = False
            c36['5'] = False
            c46['5'] = False
            c56['5'] = False
            c66['5'] = False
        elif solvednums[8][5] == 6:
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c84['6'] = False
            c85['6'] = False
            c86['6'] = False
            c74['6'] = False
            c75['6'] = False
            c76['6'] = False
            c16['6'] = False
            c26['6'] = False
            c36['6'] = False
            c46['6'] = False
            c56['6'] = False
            c66['6'] = False
        elif solvednums[8][5] == 7:
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c84['7'] = False
            c85['7'] = False
            c86['7'] = False
            c74['7'] = False
            c75['7'] = False
            c76['7'] = False
            c16['7'] = False
            c26['7'] = False
            c36['7'] = False
            c46['7'] = False
            c56['7'] = False
            c66['7'] = False
        elif solvednums[8][5] == 8:
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c84['8'] = False
            c85['8'] = False
            c86['8'] = False
            c74['8'] = False
            c75['8'] = False
            c76['8'] = False
            c16['8'] = False
            c26['8'] = False
            c36['8'] = False
            c46['8'] = False
            c56['8'] = False
            c66['8'] = False
        elif solvednums[8][5] == 9:
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c84['9'] = False
            c85['9'] = False
            c86['9'] = False
            c74['9'] = False
            c75['9'] = False
            c76['9'] = False
            c16['9'] = False
            c26['9'] = False
            c36['9'] = False
            c46['9'] = False   
            c56['9'] = False
            c66['9'] = False
    if puzzlenums[8][6] > 0 and e97do == True:
        solvednums[8][6] = puzzlenums[8][6]
        e97do = False
        sleep(1)
    elif e97do == True and c97['1'] == True and c97['2'] == False and c97['3'] == False and c97['4'] == False and c97['5'] == False and c97['6'] == False and c97['7'] == False and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 1
    elif e97do == True and c97['1'] == False and c97['2'] == True and c97['3'] == False and c97['4'] == False and c97['5'] == False and c97['6'] == False and c97['7'] == False and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 2
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == True and c97['4'] == False and c97['5'] == False and c97['6'] == False and c97['7'] == False and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 3
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == False and c97['4'] == True and c97['5'] == False and c97['6'] == False and c97['7'] == False and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 4
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == False and c97['4'] == False and c97['5'] == True and c97['6'] == False and c97['7'] == False and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 5
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == False and c97['4'] == False and c97['5'] == False and c97['6'] == True and c97['7'] == False and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 6
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == False and c97['4'] == False and c97['5'] == False and c97['6'] == False and c97['7'] == True and c97['8'] == False and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 7
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == False and c97['4'] == False and c97['5'] == False and c97['6'] == False and c97['7'] == False and c97['8'] == True and c97['9'] == False:
        e97do = False
        solvednums[8][6] = 8
    elif e97do == True and c97['1'] == False and c97['2'] == False and c97['3'] == False and c97['4'] == False and c97['5'] == False and c97['6'] == False and c97['7'] == False and c97['8'] == False and c97['9'] == True:
        e97do = False
        solvednums[8][6] = 9
    else:
        if solvednums[8][6] == 1:
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c17['1'] = False
            c27['1'] = False
            c37['1'] = False
            c47['1'] = False
            c57['1'] = False
            c67['1'] = False
        elif solvednums[8][6] == 2:
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c17['2'] = False
            c27['2'] = False
            c37['2'] = False
            c47['2'] = False
            c57['2'] = False
            c67['2'] = False
        elif solvednums[8][6] == 3:
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c17['3'] = False
            c27['3'] = False
            c37['3'] = False
            c47['3'] = False
            c57['3'] = False
            c67['3'] = False
        elif solvednums[8][6] == 4:
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c17['4'] = False
            c27['4'] = False
            c37['4'] = False
            c47['4'] = False
            c57['4'] = False
            c67['4'] = False
        elif solvednums[8][6] == 5:
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c17['5'] = False
            c27['5'] = False
            c37['5'] = False
            c47['5'] = False
            c57['5'] = False
            c67['5'] = False
        elif solvednums[8][6] == 6:
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c17['6'] = False
            c27['6'] = False
            c37['6'] = False
            c47['6'] = False
            c57['6'] = False
            c67['6'] = False
        elif solvednums[8][6] == 7:
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c77['7'] = False
            c78['7'] = False
            c79['7'] = False
            c17['7'] = False
            c27['7'] = False
            c37['7'] = False
            c47['7'] = False
            c57['7'] = False
            c67['7'] = False
        elif solvednums[8][6] == 8:
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c17['8'] = False
            c27['8'] = False
            c37['8'] = False
            c47['8'] = False
            c57['8'] = False
            c67['8'] = False
        elif solvednums[8][6] == 9:
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c17['9'] = False
            c27['9'] = False
            c37['9'] = False
            c47['9'] = False   
            c57['9'] = False
            c67['9'] = False
    if puzzlenums[8][7] > 0 and e98do == True:
        solvednums[8][7] = puzzlenums[8][7]
        e98do = False
        sleep(1)
    elif e98do == True and c98['1'] == True and c98['2'] == False and c98['3'] == False and c98['4'] == False and c98['5'] == False and c98['6'] == False and c98['7'] == False and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 1
    elif e98do == True and c98['1'] == False and c98['2'] == True and c98['3'] == False and c98['4'] == False and c98['5'] == False and c98['6'] == False and c98['7'] == False and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 2
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == True and c98['4'] == False and c98['5'] == False and c98['6'] == False and c98['7'] == False and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 3
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == False and c98['4'] == True and c98['5'] == False and c98['6'] == False and c98['7'] == False and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 4
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == False and c98['4'] == False and c98['5'] == True and c98['6'] == False and c98['7'] == False and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 5
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == False and c98['4'] == False and c98['5'] == False and c98['6'] == True and c98['7'] == False and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 6
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == False and c98['4'] == False and c98['5'] == False and c98['6'] == False and c98['7'] == True and c98['8'] == False and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 7
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == False and c98['4'] == False and c98['5'] == False and c98['6'] == False and c98['7'] == False and c98['8'] == True and c98['9'] == False:
        e98do = False
        solvednums[8][7] = 8
    elif e98do == True and c98['1'] == False and c98['2'] == False and c98['3'] == False and c98['4'] == False and c98['5'] == False and c98['6'] == False and c98['7'] == False and c98['8'] == False and c98['9'] == True:
        e98do = False
        solvednums[8][7] = 9
    else:
        if solvednums[8][7] == 1:
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c18['1'] = False
            c28['1'] = False
            c38['1'] = False
            c48['1'] = False
            c58['1'] = False
            c68['1'] = False
        elif solvednums[8][7] == 2:
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c18['2'] = False
            c28['2'] = False
            c38['2'] = False
            c48['2'] = False
            c58['2'] = False
            c68['2'] = False
        elif solvednums[8][7] == 3:
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c18['3'] = False
            c28['3'] = False
            c38['3'] = False
            c48['3'] = False
            c58['3'] = False
            c68['3'] = False
        elif solvednums[8][7] == 4:
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c18['4'] = False
            c28['4'] = False
            c38['4'] = False
            c48['4'] = False
            c58['4'] = False
            c68['4'] = False
        elif solvednums[8][7] == 5:
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c18['5'] = False
            c28['5'] = False
            c38['5'] = False
            c48['5'] = False
            c58['5'] = False
            c68['5'] = False
        elif solvednums[8][7] == 6:
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c18['6'] = False
            c28['6'] = False
            c38['6'] = False
            c48['6'] = False
            c58['6'] = False
            c68['6'] = False
        elif solvednums[8][7] == 7:
            c91['7'] = False
            c92['7'] = False
            c93['7'] = False
            c95['7'] = False
            c96['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c97['7'] = False
            c98['7'] = False
            c99['7'] = False
            c87['7'] = False
            c88['7'] = False
            c89['7'] = False
            c18['7'] = False
            c28['7'] = False
            c38['7'] = False
            c48['7'] = False
            c58['7'] = False
            c68['7'] = False
        elif solvednums[8][7] == 8:
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c18['8'] = False
            c28['8'] = False
            c38['8'] = False
            c48['8'] = False
            c58['8'] = False
            c68['8'] = False
        elif solvednums[8][7] == 9:
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c95['9'] = False 
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c18['9'] = False
            c28['9'] = False
            c38['9'] = False
            c48['9'] = False   
            c58['9'] = False
            c68['9'] = False
    if puzzlenums[8][8] > 0 and e99do == True:
        solvednums[8][8] = puzzlenums[8][8]
        e99do = False
        sleep(1)
    elif e99do == True and c99['1'] == True and c99['2'] == False and c99['3'] == False and c99['4'] == False and c99['5'] == False and c99['6'] == False and c99['7'] == False and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 1
    elif e99do == True and c99['1'] == False and c99['2'] == True and c99['3'] == False and c99['4'] == False and c99['5'] == False and c99['6'] == False and c99['7'] == False and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 2
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == True and c99['4'] == False and c99['5'] == False and c99['6'] == False and c99['7'] == False and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 3
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == False and c99['4'] == True and c99['5'] == False and c99['6'] == False and c99['7'] == False and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 4
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == False and c99['4'] == False and c99['5'] == True and c99['6'] == False and c99['7'] == False and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 5
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == False and c99['4'] == False and c99['5'] == False and c99['6'] == True and c99['7'] == False and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 6
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == False and c99['4'] == False and c99['5'] == False and c99['6'] == False and c99['7'] == True and c99['8'] == False and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 7
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == False and c99['4'] == False and c99['5'] == False and c99['6'] == False and c99['7'] == False and c99['8'] == True and c99['9'] == False:
        e99do = False
        solvednums[8][8] = 8
    elif e99do == True and c99['1'] == False and c99['2'] == False and c99['3'] == False and c99['4'] == False and c99['5'] == False and c99['6'] == False and c99['7'] == False and c99['8'] == False and c99['9'] == True:
        e99do = False
        solvednums[8][8] = 9
    else:
        if solvednums[8][8] == 1:
            c91['1'] = False
            c92['1'] = False
            c93['1'] = False
            c95['1'] = False
            c96['1'] = False
            c97['1'] = False
            c98['1'] = False
            c99['1'] = False
            c87['1'] = False
            c88['1'] = False
            c89['1'] = False
            c77['1'] = False
            c78['1'] = False
            c79['1'] = False
            c19['1'] = False
            c29['1'] = False
            c39['1'] = False
            c49['1'] = False
            c59['1'] = False
            c69['1'] = False
        elif solvednums[8][8] == 2:
            c91['2'] = False
            c92['2'] = False
            c93['2'] = False
            c95['2'] = False
            c96['2'] = False
            c97['2'] = False
            c98['2'] = False
            c99['2'] = False
            c87['2'] = False
            c88['2'] = False
            c89['2'] = False
            c77['2'] = False
            c78['2'] = False
            c79['2'] = False
            c19['2'] = False
            c29['2'] = False
            c39['2'] = False
            c49['2'] = False
            c59['2'] = False
            c69['2'] = False
        elif solvednums[8][8] == 3:
            c91['3'] = False
            c92['3'] = False
            c93['3'] = False
            c95['3'] = False
            c96['3'] = False
            c97['3'] = False
            c98['3'] = False
            c99['3'] = False
            c87['3'] = False
            c88['3'] = False
            c89['3'] = False
            c77['3'] = False
            c78['3'] = False
            c79['3'] = False
            c19['3'] = False
            c29['3'] = False
            c39['3'] = False
            c49['3'] = False
            c59['3'] = False
            c69['3'] = False
        elif solvednums[8][8] == 4:
            c91['4'] = False
            c92['4'] = False
            c93['4'] = False
            c95['4'] = False
            c96['4'] = False
            c97['4'] = False
            c98['4'] = False
            c99['4'] = False
            c87['4'] = False
            c88['4'] = False
            c89['4'] = False
            c77['4'] = False
            c78['4'] = False
            c79['4'] = False
            c19['4'] = False
            c29['4'] = False
            c39['4'] = False
            c49['4'] = False
            c59['4'] = False
            c69['4'] = False
        elif solvednums[8][8] == 5:
            c91['5'] = False
            c92['5'] = False
            c93['5'] = False
            c95['5'] = False
            c96['5'] = False
            c97['5'] = False
            c98['5'] = False
            c99['5'] = False
            c87['5'] = False
            c88['5'] = False
            c89['5'] = False
            c77['5'] = False
            c78['5'] = False
            c79['5'] = False
            c19['5'] = False
            c29['5'] = False
            c39['5'] = False
            c49['5'] = False
            c59['5'] = False
            c69['5'] = False
        elif solvednums[8][8] == 6:
            c91['6'] = False
            c92['6'] = False
            c93['6'] = False
            c95['6'] = False
            c96['6'] = False
            c97['6'] = False
            c98['6'] = False
            c99['6'] = False
            c87['6'] = False
            c88['6'] = False
            c89['6'] = False
            c77['6'] = False
            c78['6'] = False
            c79['6'] = False
            c19['6'] = False
            c29['6'] = False
            c39['6'] = False
            c49['6'] = False
            c59['6'] = False
            c69['6'] = False
        elif solvednums[8][8] == 7:
            c91['8'] = False
            c92['8'] = False
            c93['8'] = False
            c95['8'] = False
            c96['8'] = False
            c97['8'] = False
            c98['8'] = False
            c99['8'] = False
            c87['8'] = False
            c88['8'] = False
            c89['8'] = False
            c77['8'] = False
            c78['8'] = False
            c79['8'] = False
            c19['8'] = False
            c29['8'] = False
            c39['8'] = False
            c49['8'] = False
            c59['8'] = False
            c69['8'] = False
        elif solvednums[8][8] == 9:
            c91['9'] = False
            c92['9'] = False
            c93['9'] = False
            c96['9'] = False
            c97['9'] = False
            c98['9'] = False
            c99['9'] = False
            c87['9'] = False
            c88['9'] = False
            c89['9'] = False
            c77['9'] = False
            c78['9'] = False
            c79['9'] = False
            c19['9'] = False
            c29['9'] = False
            c39['9'] = False
            c49['9'] = False   
            c59['9'] = False
            c69['9'] = False
    print(solvednums)
    return
solveBtn.configure(command = solve)
window.mainloop()