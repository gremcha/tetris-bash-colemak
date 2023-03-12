class Figure():

    def __init__(self, screen):
        self.current_Y = 6
        self.current_X = 26
        self.rotation_position = 0
        self.sizes = [{'len_X': 11, 'len_Y': 4}, 
                      {'len_X': 7, 'len_Y': 6},
            ]
        self.count_rotation_position = 4
        self.screen = screen

    def move_right(self):
        if self.current_X + self.sizes[self.rotation_position % 2]['len_X'] < 49:
            self.current_X += 4
    
    def move_left(self):
        if self.current_X > 10:
            self.current_X -= 4

    def move_down(self):
        pass

    def rotate(self):
        self.rotation_position = (self.rotation_position + 1) % self.count_rotation_position
    

class IBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 2
        self.sizes = [{'len_X': 3, 'len_Y': 8}, {'len_X': 15, 'len_Y': 2}]
        
    def view_current_position(self):
        if self.rotation_position == 0:
            for i in range(8):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X,  '@ @')
        else:
            self.screen.stdscr.addstr(self.current_Y, self. current_X, ('@ @ '* 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self. current_X, ('@ @ '* 4)[:-1])

    def move_down(self):
        bottom_Y = self.current_Y + self.sizes[self.rotation_position]['len_Y']
        if self.rotation_position == 0:
            bottom_X = self.current_X
            bottom_len = 3
        elif self.rotation_position == 1:
            bottom_X = self.current_X
            bottom_len = 15

        # for i in range(0, bottom_len + 2, 4): # 
        #     if 



class TBlock(Figure):

    def view_current_position(self):
        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X,  ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X,  ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X + 4, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X + 4, '@ @')

        elif self.rotation_position == 1:
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X, '@ @' )
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X, '@ @' )
            for i in range(6):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X + 4, '@ @' )
        
        elif self.rotation_position == 2: 
            self.screen.stdscr.addstr(self.current_Y , self.current_X + 4, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X + 4, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X,  ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X,  ('@ ' * 6)[:-1])

        elif self.rotation_position == 3:
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X + 4, '@ @' )
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X + 4, '@ @' )
            for i in range(6):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X, '@ @' )


class SBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 2

    def view_current_position(self):
        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X + 4, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X + 4, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X, ('@ ' * 4)[:-1])

        else:
            for i in range(4):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X, '@ @')
            for i in range(4):
                self.screen.stdscr.addstr(self.current_Y + 2 + i, self.current_X + 4, '@ @')


class ZBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 2

    def view_current_position(self):
        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X + 4, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X + 4, ('@ ' * 4)[:-1])
        else:
            for i in range(4):
                self.screen.stdscr.addstr(self.current_Y + 2 + i, self.current_X, '@ @')
            for i in range(4):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X + 4, '@ @')

class OBlock(Figure):

    def __init__(self, screen):
        super().__init__(screen)
        self.count_rotation_position = 1
        self.sizes = [{'len_X': 7, 'len_Y': 4}]

    def view_current_position(self):
        for i in range(4):
            self.screen.stdscr.addstr(self.current_Y + i, self.current_X, ('@ ' * 4)[:-1])

class LBlock(Figure):

    def view_current_position(self):
        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X, ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X, ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X, '@ @')
            
        elif self.rotation_position == 1:
            self.screen.stdscr.addstr(self.current_Y, self.current_X, ('@ ' * 4)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X, ('@ ' * 4)[:-1])
            for i in range(4):
                self.screen.stdscr.addstr(self.current_Y + 2 + i, self.current_X + 4, '@ @')
        elif self.rotation_position == 2:
            self.screen.stdscr.addstr(self.current_Y, self.current_X + 8, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X + 8, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X, ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X, ('@ ' * 6)[:-1])
        else: 
            for i in range(6):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 4, self.current_X + 4, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 5, self.current_X + 4, '@ @')
            

class JBlock(Figure):

    def view_current_position(self):

        if self.rotation_position == 0:
            self.screen.stdscr.addstr(self.current_Y, self.current_X, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X, ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X, ('@ ' * 6)[:-1])
            

        elif self.rotation_position == 1:
            for i in range(6):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X, '@ @')
            self.screen.stdscr.addstr(self.current_Y, self.current_X + 4, ('@ @' ))
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X + 4, '@ @' )

        elif self.rotation_position == 2:
            self.screen.stdscr.addstr(self.current_Y + 0, self.current_X, ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 1, self.current_X, ('@ ' * 6)[:-1])
            self.screen.stdscr.addstr(self.current_Y + 2, self.current_X + 8, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 3, self.current_X + 8, '@ @')

        else: 
            self.screen.stdscr.addstr(self.current_Y + 4, self.current_X, '@ @')
            self.screen.stdscr.addstr(self.current_Y + 5, self.current_X, '@ @')
            for i in range(6):
                self.screen.stdscr.addstr(self.current_Y + i, self.current_X + 4, '@ @')

