import curses

class Screen():
    
    def __init__(self):
        self.stdscr = curses.initscr()
        self.stack = []

    def drow_borders(self):
        self.stdscr.addstr(5, 9, '# ' * 20)
        self.stdscr.addstr(47, 9, '# ' * 20)
        for i in range(5, 48):
            self.stdscr.addstr(i, 9, '#')
            self.stdscr.addstr(i, 49, '#')

    def drow_stack(self):
        for i, string in enumerate(self.stack):
            print(type(i), type(string))
            self.stdscr.addstr(46 - i, 10, string)