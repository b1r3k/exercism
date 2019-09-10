WHITE = "W"
BLACK = "B"
NONE = " "


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self._board = board

    def get_neighbours(self, x, y):
        coords = (
            # row before
            (-1, -1),
            (-1, 0),
            (-1, 1),
            # same row
            (0, -1),
            (0, 1),
            # next row
            (1, -1),
            (1, 0),
            (1, 1)
        )
        neighbours = {}
        for dx, dy in coords:
            try:
                x_dx = x + dx
                y_dy = y + dy
                neighbours[(x_dx, y_dy)] = self._board[x_dx][y_dy]
            except:
                pass
        return neighbours


    def get_territory_ownership_map(self, x, y):
        territory_chains = []
        for ix, row in enumerate(self._board):
            for iy, col in enumerate(row):
                neighbours = self.get_neighbours(ix, iy)
        return

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        while True:
            distance = 1
            get_territory_owner(x, y, distance)

        return owner, set(territories)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        pass
