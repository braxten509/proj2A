from Grid import Grid
from sand_functional import *

grid = Grid.build([[None, 's',   'r'], [None, None, None]])
is_move_ok(grid, 1, 0, 1, 1)  # down ok