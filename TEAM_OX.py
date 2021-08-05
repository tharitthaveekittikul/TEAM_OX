#ธฤต ทวีกิตติกุล 6301012630079
#สรวิศ พึ่งเสมา 6301012630184
#ภคพงศ์ วรรณชมภู 6301012620073

class Board():

    def __init__(self):
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
        style = s.Playstyle()
        if style == True:
            print (                         'original style')
            while self.check_winner() == False:
                if self.turn_count == 9:
                    self.display_board()
                    print ("                         DRAW")
                    break
                self.display_board()
                try:
                    if s.Input_checker() == True and self.board_array[s.GetInput()-1][1] == str(s.GetInput()):
                        self.board_array[s.GetInput()-1][1] = self.player
                        self.change_player()
                        self.turn_count +=1
                    elif self.board_array[s.GetInput()-1][1] == "X" or self.board_array[s.GetInput()-1][1] == "O" :
                        print("this position already pick")
                except:
                    print("please insert number")

            if self.check_winner() == True:
                self.display_board()
                if self.player == "X":
                    print("                    Player O Win")
                else:
                    print("                    Player X Win")

        elif style == False:
            print (                     'Numpad style')
            while self.check_winner() == False:
                if self.turn_count == 9:
                    self.display_board()
                    print ("                         DRAW")
                    break
                self.display_numpad()
                try:
                    if s.Input_checker() == True and self.board_array[s.GetInput()-1][1] == str(s.GetInput()):
                        self.board_array[s.GetInput()-1][1] = self.player
                        self.change_player()
                        self.turn_count +=1
                    elif self.board_array[s.GetInput()-1][1] == "X" or self.board_array[s.GetInput()-1][1] == "O" :
                        print("this position already pick")
                except:
                    print("please insert number")

            if self.check_winner() == True:
                self.display_numpad()
                if self.player == "X":
                    print("                    Player O Win")
                else:
                    print("                    Player X Win")
            
    def change_player(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"
    