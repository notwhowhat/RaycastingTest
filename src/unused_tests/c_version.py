import glfw
from OpenGL.GL import *
import math

# --- Map ---
map_x, map_y: int = 8
map_s: int = 64
map = [
    [1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
]

def draw_map() -> None:
    x, y, xo, yo: int = 0
    for y in y < map_y:
        for x in x < map_x:
            if y * map_x + x == 1: glColor3f(1, 1, 1)
            else: glColor3f(0, 0, 0)
            
            xo = x * map_s
            yo = y * map_s

            glBegin(GL_QUADS)
            glVertex2i(0 + xo + 1, 0 + yo + 1)
            glVertex2i(0 + xo + 1, map_s + yo - 1)
            glVertex2i(map_s + xo - 1, map_s + yo - 1)
            glVertex2i(map_s + xo - 1, 0 + yo + 1)
            glEnd()

# --- Player ---
def deg_to_rad(a: int) -> float:
    return a * math.pi / 180.0

def fix_ang(a: int) -> int:
    if a > 359:
        a -= 360
    if a < 0:
        a += 360
    return a

px, py, pdx, pdy, pa: float = 0

def draw_player_2d() -> None:
    glColor3f(1, 1, 0)
    glPointSize(8)
    glLineWidth(4)

    glBegin(GL_POINTS)
    glVertex2i(px, py)
    glEnd()

    glBegin()
    glVertex2i(px, py)
    glVertex2i(px + pdx * 20, py + pdy * 20)
    glEnd()

def buttons(key: str, x: int, y: int) -> None:
    if key == 'a':
        pa += 5
        pa = fix_ang(pa)
        pdx = math.cos(deg_to_rad(pa))
        pdy = -math.sin(deg_to_rad(pa))
    if key == 'd':
        pa -= 5
        pa = fix_ang(pa)
        pdx = math.cos(deg_to_rad(pa))
        pdy = -math.sin(deg_to_rad(pa))
    if key == 'w':
        px += pdx * 5
        py += pdy * 5
    if key == 's':
        px -= pdx * 5
        py -= pdy * 5

# --- Rays and walls ---
def distance(ax, ay, bx, by, ang) -> float:
    return math.cos(deg_to_rad(ang)) * (bx - ax) -math.sin(deg_to_rad(ang)) * (by - ay)

def draw_rays_2d() -> None:
    glColor3f(0, 1, 1)
    
    glBegin(GL_QUADS)
    glVertex2i(526, 0)
    glVertex2i(1006, 0)
    glVertex2i(1006, 160)
    glVertex2i(256, 160)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)
    glVertex2i(560, 160)
    glVertex2i(1006, 160)
    glVertex2i(1006, 320)
    glVertex2i(526, 320)
    glEnd()

    r, mx, my, mp, dof, side: int = 0
    vx, vy, rx, ry, ra, xo, yo, dist_v, dist_h: float = 0
    ra = fix_ang(pa + 30) # set back the ray 30 deg

    for r in r < 60:
        # --- Vertical ---
        dof = 0
        side = 0