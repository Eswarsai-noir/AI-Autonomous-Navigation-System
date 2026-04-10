import pygame
from path_planning import astar
from agent import Agent
from simulation import draw_grid, draw_path, draw_agent_and_goal, draw_ui_panel, init_font

# Grid map
grid = [
 [0,0,0,0,0],
 [0,1,1,0,0],
 [0,0,0,0,0],
 [0,1,0,1,0],
 [0,0,0,0,0]
]

start = (0,0)
goal = (4,4)

# 🔒 FIXED START POSITION (IMPORTANT)
start_pos = start

pygame.init()
init_font()

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("AI Autonomous Navigation System")

clock = pygame.time.Clock()

# Agent setup
agent = Agent(start)
path = astar(grid, start, goal)
agent.set_path(path.copy())

steps = 0

running = True
while running:
    screen.fill((230,230,230))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🔁 Restart button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                agent = Agent(start)
                agent.set_path(path.copy())
                steps = 0

    # Move agent smoothly
    if agent.position != goal:
        moved = agent.move()
        if moved:
            steps += 1

    # 🎨 DRAW ORDER (IMPORTANT)
    draw_grid(screen, grid)
    draw_path(screen, path)
    draw_agent_and_goal(screen, agent, goal, start_pos)
    draw_ui_panel(screen, agent, goal, steps)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
