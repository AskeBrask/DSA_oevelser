import pygame
import sys
import heapq

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 600
rows, cols = 20, 20
cell_size = width // rows

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dijkstra's Algorithm Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Node class to represent each cell on the grid
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * cell_size
        self.y = col * cell_size
        self.color = WHITE
        self.neighbors = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, cell_size, cell_size))

    def add_neighbors(self, grid):
        self.neighbors = []
        if self.row < rows - 1 and grid[self.row + 1][self.col].color != BLACK:  # Down
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and grid[self.row - 1][self.col].color != BLACK:  # Up
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < cols - 1 and grid[self.row][self.col + 1].color != BLACK:  # Right
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and grid[self.row][self.col - 1].color != BLACK:  # Left
            self.neighbors.append(grid[self.row][self.col - 1])

# Create grid
def create_grid():
    return [[Node(i, j) for j in range(cols)] for i in range(rows)]

# Draw grid lines
def draw_grid(screen):
    for i in range(rows):
        pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size))
        pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height))

# Dijkstra's Algorithm
def dijkstra(draw, grid, start, end):
    count = 0
    queue = [(0, count, start)]
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0
    came_from = {}

    while queue:
        current_distance, _, current = heapq.heappop(queue)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.color = RED
            return True

        for neighbor in current.neighbors:
            temp_distance = current_distance + 1

            if temp_distance < distances[neighbor]:
                came_from[neighbor] = current
                distances[neighbor] = temp_distance
                heapq.heappush(queue, (temp_distance, count, neighbor))
                neighbor.color = BLUE
                count += 1
        draw()

        if current != start:
            current.color = YELLOW

    return False

# Reconstruct path from end to start
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.color = GREEN
        draw()

# Main draw function
def draw(screen, grid):
    screen.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(screen)
    draw_grid(screen)
    pygame.display.update()

# Main loop
def main(screen):
    grid = create_grid()
    start, end = None, None

    running = True
    while running:
        draw(screen, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Left click to add start, end, and obstacles
            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // cell_size, pos[1] // cell_size
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.color = GREEN
                elif not end and node != start:
                    end = node
                    end.color = RED
                elif node != end and node != start:
                    node.color = BLACK

            # Right click to remove a node or obstacle
            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // cell_size, pos[1] // cell_size
                node = grid[row][col]
                node.color = WHITE
                if node == start:
                    start = None
                elif node == end:
                    end = None

            # Start the algorithm when pressing the space bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.add_neighbors(grid)
                    dijkstra(lambda: draw(screen, grid), grid, start, end)

main(screen)
