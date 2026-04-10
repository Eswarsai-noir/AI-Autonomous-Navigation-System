import pygame

CELL_SIZE = 80

# Colors
WHITE = (245, 245, 245)
GRID_LINE = (200, 200, 200)
OBSTACLE = (60, 60, 60)
PATH_COLOR = (255, 100, 100)
AGENT_COLOR = (50, 150, 255)
GOAL_COLOR = (50, 220, 100)
START_COLOR = (255, 200, 0)

FONT = None


def init_font():
    global FONT
    pygame.font.init()
    FONT = pygame.font.SysFont("Arial", 18)


def draw_grid(screen, grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            rect = (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if val == 1:
                pygame.draw.rect(screen, OBSTACLE, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

            pygame.draw.rect(screen, GRID_LINE, rect, 1)


def draw_path(screen, path):
    for p in path:
        pygame.draw.circle(screen, PATH_COLOR,
                           (p[1]*CELL_SIZE + CELL_SIZE//2,
                            p[0]*CELL_SIZE + CELL_SIZE//2), 8)


def draw_agent_and_goal(screen, agent, goal, start):
    # 🔵 Agent (smooth moving)
    pygame.draw.circle(screen, AGENT_COLOR,
                       (int(agent.pixel_position[0]),
                        int(agent.pixel_position[1])), 14)

    # 🟢 Goal
    pygame.draw.circle(screen, GOAL_COLOR,
                       (goal[1]*CELL_SIZE + CELL_SIZE//2,
                        goal[0]*CELL_SIZE + CELL_SIZE//2), 14)

    # 🟡 START (FIXED)
    pygame.draw.circle(screen, START_COLOR,
                       (start[1]*CELL_SIZE + CELL_SIZE//2,
                        start[0]*CELL_SIZE + CELL_SIZE//2), 10)

    # Labels
    if FONT:
        start_text = FONT.render("START", True, (0,0,0))
        goal_text = FONT.render("GOAL", True, (0,0,0))

        screen.blit(start_text,
                    (start[1]*CELL_SIZE + 5,
                     start[0]*CELL_SIZE + 5))

        screen.blit(goal_text,
                    (goal[1]*CELL_SIZE + 5,
                     goal[0]*CELL_SIZE + 5))


def draw_ui_panel(screen, agent, goal, steps):
    panel_x = 400

    pygame.draw.rect(screen, (30, 30, 30), (panel_x, 0, 200, 400))

    if FONT:
        title = FONT.render("NAVIGATION PANEL", True, (255,255,255))
        screen.blit(title, (panel_x + 10, 20))

        pos_text = FONT.render(f"Agent: {agent.position}", True, (200,200,200))
        screen.blit(pos_text, (panel_x + 10, 80))

        goal_text = FONT.render(f"Goal: {goal}", True, (200,200,200))
        screen.blit(goal_text, (panel_x + 10, 120))

        step_text = FONT.render(f"Steps: {steps}", True, (200,200,200))
        screen.blit(step_text, (panel_x + 10, 160))

        # ✅ STATUS CHANGE
        status = "Moving"
        color = (100,255,100)

        if agent.position == goal:
            status = "Goal Reached"
            color = (0,255,0)

        status_text = FONT.render(f"Status: {status}", True, color)
        screen.blit(status_text, (panel_x + 10, 220))

        hint = FONT.render("Press R to Restart", True, (150,150,150))
        screen.blit(hint, (panel_x + 10, 300))
