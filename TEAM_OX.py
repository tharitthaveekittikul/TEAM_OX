#ธฤต ทวีกิตติกุล 6301012630079
#สรวิศ พึ่งเสมา 6301012630184
#ภคพงศ์ วรรณชมภู 6301012620073


class Board():

    def __init__(self):
        super().__init__()
        self.board_array = [[1,"1"],[2,"2"],[3,"3"],[4,"4"],[5,"5"],[6,"6"],[7,"7"],[8,"8"],[9,"9"]]
        self.player = "X"
        self.turn_count = 0  

    def display_board(self):
        print("                 -------------------")
        print("                 |  "+ self.board_array[0][1] +"  |  "+ self.board_array[1][1] +"  |  "+ self.board_array[2][1] +"  |")
        print("                 -------------------")
        print("                 |  "+ self.board_array[3][1] +"  |  "+ self.board_array[4][1] +"  |  "+ self.board_array[5][1] +"  |")
        print("                 -------------------")
        print("                 |  "+ self.board_array[6][1] +"  |  "+ self.board_array[7][1]  +"  |  "+ self.board_array[8][1] +"  |")
        print("                 -------------------")

    def display_numpad(self):
        print("                 -------------------")
        print("                 |  "+ self.board_array[6][1] +"  |  "+ self.board_array[7][1] +"  |  "+ self.board_array[8][1] +"  |")
        print("                 -------------------")
        print("                 |  "+ self.board_array[3][1] +"  |  "+ self.board_array[4][1] +"  |  "+ self.board_array[5][1] +"  |")
        print("                 -------------------")
        print("                 |  "+ self.board_array[0][1] +"  |  "+ self.board_array[1][1]  +"  |  "+ self.board_array[2][1] +"  |")
        print("                 -------------------")

    def check_winner(self):
        if (self.board_array[0][1] == self.board_array[1][1] == self.board_array[2][1] or self.board_array[3][1] == self.board_array[4][1] == self.board_array[5][1] or self.board_array[6][1] == self.board_array[7][1] == self.board_array[8][1] or
            self.board_array[0][1] == self.board_array[3][1] == self.board_array[6][1] or self.board_array[1][1] == self.board_array[4][1] == self.board_array[7][1] or self.board_array[2][1] == self.board_array[5][1] == self.board_array[8][1] or
            self.board_array[0][1] == self.board_array[4][1] == self.board_array[8][1] or self.board_array[2][1] == self.board_array[4][1] == self.board_array[6][1]):
            return True
        else:
            return False

    def add_position(self):
        s = Input_Processor()
        if s.Playstyle() == True:
            print (                         'original style')
            while self.check_winner() == False:
                self.display_board()
                if s.Input_checker() == True and self.board_array[s.GetInput()-1][1] == str(s.GetInput()):
                    self.board_array[s.GetInput()-1][1] = self.player
                    self.change_player()
                    self.turn_count +=1
                elif self.board_array[s.GetInput()-1][1] == "X" or self.board_array[s.GetInput()-1][1] == "O" :
                    print("Same position")

            if self.check_winner() == True:
                self.display_board()
                if self.player == "X":
                    print("                    Player O Win")
                else:
                    print("                    Player X Win")
            elif self.turn_count == 9:
                self.display_board()
                print ("                           DRAW")

        elif s.Playstyle() == False:
            print (                     'Numpad style')
            while self.check_winner() == False:
                self.display_numpad()
                if s.Input_checker() == True and self.board_array[s.GetInput()-1][1] == str(s.GetInput()):
                    self.board_array[s.GetInput()-1][1] = self.player
                    self.change_player()
                    self.turn_count +=1
                elif self.board_array[s.GetInput()-1][1] == "X" or self.board_array[s.GetInput()-1][1] == "O" :
                    print("Same position")

            if self.check_winner() == True:
                self.display_numpad()
                if self.player == "X":
                    print("                    Player O Win")
                else:
                    print("                    Player X Win")
            elif self.turn_count == 9:
                self.display_numpad()
                print ("                           DRAW")
            
    def change_player(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"
    
class Input_Processor():

    def __init__(self):
        self.t = 0
        self.s = 0
        

    def Input_checker(self):
        try:
            self.s = int(input('Please select your position:'))
            if self.s in range(1,10):
                return True
            elif self.s >= 10:
                print ('Please select number between 1-9')
        except:
            print("please insert number")

        
    def GetInput(self):
        return int(self.s)
    
    def Playstyle(self):
        while(True):
            try:
                self.t = int(input('Please select your play style (original: press 1) (numpad : press 2)'))
                if self.t == 1 :
                    return True
                elif self  .t == 2:
                    return False
            except:
                print("please insert number 1 or 2")

a = Board()
a.add_position()