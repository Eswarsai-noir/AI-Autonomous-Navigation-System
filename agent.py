class Agent:
    def __init__(self, start):
        # Grid position (row, col)
        self.grid_position = start

        # Pixel position (x, y)
        self.pixel_position = [
            start[1]*80 + 40,
            start[0]*80 + 40
        ]

        # Path to follow
        self.path = []

        # Movement speed (adjust for faster/slower)
        self.speed = 12

    def set_path(self, path):
        self.path = path

    def move(self):
        moved = False  # Track real movement (cell-to-cell)

        if len(self.path) > 0:
            target = self.path[0]

            # Convert grid → pixel
            target_x = target[1]*80 + 40
            target_y = target[0]*80 + 40

            dx = target_x - self.pixel_position[0]
            dy = target_y - self.pixel_position[1]

            # Smooth movement
            if abs(dx) > 1:
                self.pixel_position[0] += self.speed * (dx / abs(dx))

            if abs(dy) > 1:
                self.pixel_position[1] += self.speed * (dy / abs(dy))

            # If close enough → snap to grid cell
            if abs(dx) < 5 and abs(dy) < 5:
                self.pixel_position[0] = target_x
                self.pixel_position[1] = target_y

                self.grid_position = target
                self.path.pop(0)

                moved = True  # ✅ Only when a cell is reached

        return moved

    @property
    def position(self):
        return self.grid_position
