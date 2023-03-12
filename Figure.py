class Figure():
    def __init__(self, screen):
        self.current_Y = 6
        self.current_X = 26
        self.rotation_position = 0
        self.count_rotation_position = 4
        self.screen = screen

    def move_right(self):
        if self.current_X < 50:
            self.current_X += 2
    
    def move_left(self):
        self.current_X -= 2

    def rotate(self):
        self.rotation_position = (self.rotation_position + 1) % self.rotation_position
    

class LBlock(Figure):
    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 2
        
    def view_current_position(self):
        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X,  '@ @ \n'*8)
        else:
            self.screen.stdscr.addstr(self.current_Y, self. current_X, ('@ @ '* 4 + '\n') * 2)


class TBlock(Figure):

    def view_current_position(self):
        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X,  '@ @ ' * 3)
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X,  '@ @ ' * 3)
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X + 4, '@ @ ')
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X + 4, '@ @ ')

        elif self.rotation_position == 1:
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X, '@ @ ' )
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X, '@ @ ' )
            for i in range(8):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X + 4, '@ @ ' )
        
        elif self.rotation_position == 2:
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X + 4, '@ @ ' )
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X + 4, '@ @ ' )
            for i in range(8):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X, '@ @ ' )

        else: 
            self.screen.stdscr.addstr(self.current_Y , self.current_X + 4, '@ @ ')
            self.screen.stdscr.addstr(self.current_Y, self.current_X + 4, '@ @ ')
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X,  '@ @ ' * 3)
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X,  '@ @ ' * 3)

class SBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 2

    def view_current_position(self):
        pass

class ZBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 2

    def view_current_position(self):
        pass

class OBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 1

    def view_current_position(self):
        pass

class LBlock(Figure):

    def view_current_position(self):
        pass

class JBlock(Figure):

    def view_current_position(self):
        pass


