from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    
    def __init__(self, width: int, height: int):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, height, and array. Initially all locations hold None.
        """
        self.width = width
        self.height = height
        self.array = [[None for _ in range(width)] for _ in range(height)]
        
        
    def in_bounds(self, x, y):
        
        if x > self.width or y > self.height or x < 0 or y < 0:
            
            return False
            
        else:
            
            return True
        
    
    @staticmethod
    def check_list_malformed(nested_lists):
        
        if isinstance(nested_lists, list) == False:
            
            raise ValueError("Object is not a list.")
        
        if len(nested_lists) == 0:
            
            raise ValueError("List is empty.")
        
        for item in nested_lists:
            
            if isinstance(item, list) == False:
                
                raise ValueError(f"Inside object {item} is not a list.")
            
        if len(nested_lists[0]) == 0:
            
            raise ValueError("First list is empty.")
        
        base_length = len(nested_lists[0])
        
        for lst in nested_lists:
            
            if len(lst) != base_length:
                
                raise ValueError("Lengths of inner lists don't match.")
            
            
    @staticmethod
    def build(lst):
        
        Grid.check_list_malformed(lst)
        
        height = len(lst)
        width = len(lst[0])
        
        new_grid = Grid(width, height)
        
        new_grid.array = deepcopy(lst)
        
        return new_grid
        
        
    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y):
        
            return self.array[y][x]
        
        else:
            
            raise IndexError("Number out of bounds.")


    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y):
            
            self.array[y][x] = val
            
        else:
            
            raise IndexError("Number out of bounds.")
        
    
    def copy(self):
        return Grid.build(self.array)
        
        
    def __str__(self):  
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"


    def __repr__(self):
        
        new_grid = Grid.build(self.array)
        
        return f"Grid.build({new_grid.array})"
        
        
    def __eq__(self, other):
        
        if isinstance(other, Grid):
            
            return self.array == other.array
        
        elif isinstance(other, list):
            
            return self.array == other
        
        else:
            
            return False
        
        
# grid = Grid.build([[1, 2], [3, 4]])

print(len([]))