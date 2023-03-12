import curses
import sys

from Screen import Screen
from figures import *

def main():

    screen = Screen()
    current_figure = ZBlock(screen)
    current_figure.view_current_position()
    screen.drow_borders()
    screen.drow_stack()

    curses.curs_set(False)

    while True:
        key = screen.stdscr.getch()
        if key == 119:
            current_figure.rotate()
            screen.stdscr.clear()
            screen.drow_borders()
            current_figure.view_current_position()
            screen.drow_stack()
        elif key == 97:
            current_figure.move_left()
            screen.stdscr.clear()
            screen.drow_borders()
            current_figure.view_current_position()
            screen.drow_stack()
        elif key == 115:
            current_figure.move_right()
            screen.stdscr.clear()
            screen.drow_borders()
            current_figure.view_current_position()
            screen.drow_stack()
        elif key == 114:
            current_figure.move_down()
            screen.stdscr.clear()
            screen.drow_borders()
            current_figure.view_current_position()
            screen.drow_stack()
        else: break

    curses.curs_set(True)
    curses.endwin()

if __name__ == "__main__":
  main()
