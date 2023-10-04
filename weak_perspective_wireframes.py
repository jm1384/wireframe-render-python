import math
import random
import pygame
from wireframe import wireframe

class shape:    
    def plot_2d(focal_length: int, vertices: list[tuple]) -> list:
        
        #maps 3d coordinates to 2d plane
        td_vertices = []
        for x, y, z in vertices:
            x_proj = ((focal_length * x) / (focal_length + z))
            y_proj = ((focal_length * y) / (focal_length + z))
            td_vertices.append((x_proj, y_proj))
            
        return td_vertices
    
    
    def center(size: list[int, int], vertices) -> list:
        #accepts relative coordinates of vertices at returns real coordinates
        n_vertices = []
        center = size[0] / 2, size[1] / 2
        for x, y in vertices:
            n_vertices.append((center[0]-x,center[1]-y))
            
        return n_vertices
    
    
    def draw(edges, vertices):
        for start, end in edges:
            pygame.draw.line(screen, line_color, vertices[start], vertices[end],2)
    
    def rotate_3d(vertices, theta: int, axis: str) -> list:
        new_vertices = []
        if axis == 'x':
            for x, y, z in vertices:
                x = x
                y = y*math.cos(theta)- z * math.sin(theta) 
                z = y*math.sin(theta)+ z * math.cos(theta)
                
                new_vertices.append((x,y,z))
                
        elif axis == 'y':
            for x, y, z in vertices:
                x = x * math.cos(theta) + z * math.sin(theta)
                y = y
                z = z * math.cos(theta) - x * math.sin(theta)
                
                new_vertices.append((x,y,z))
                
        elif axis == 'z':
            for x, y, z in vertices:
                x = x * math.cos(theta) - y * math.sin(theta)
                y = x * math.sin(theta) + y * math.cos(theta)
                z = z
                
                new_vertices.append((x,y,z))
        return new_vertices
    
    #increase distance of vertices from each other
    def enlarge(vertices, scale_factor: float) -> list:
        new_vertices = []
        for x, y, z in vertices:
            new_x = x * scale_factor
            new_y = y * scale_factor
            new_z = z * scale_factor
            new_vertices.append((new_x, new_y, new_z))
        
        return new_vertices
            
class button:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        
    def draw(self, surface):
        pygame.draw.rect(surface, (50,50,50), self.rect)
        font = pygame.font.Font(None, 20)
        text = font.render(self.text, True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        surface.blit(text, text_rect)

#functions
def check_angle_reset(angle_x, angle_y, angle_z) -> tuple[float, float, float]:
    if angle_y > 360:
        angle_y = 0
    elif angle_y < 0:
        angle_y = 360
    
    if angle_x > 360:
        angle_x = 0
    elif angle_x < 0:
        angle_x = 360
      
    if angle_z > 360:
        angle_z = 0
    elif angle_z < 0:
        angle_z = 360
    
    return round(angle_x,2), round(angle_y,2), round(angle_z,2)

#color setup
BLACK = (0,0,0)
WHITE = (255,255,255)

#pygame setup
pygame.init()
size = [1280, 720]
three_d_size = [1280, 720] 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("3d Wireframe Renderer")
bg_color = WHITE
line_color = BLACK
font = pygame.font.Font(None, 25)
big_font = pygame.font.Font(None, 60)


#camera and shape setup
focal_length = 500
vertices3d, edges, name = wireframe.cube()
angle_x = 0
angle_y = 0
angle_z = 0
scale = 1
shapes = ['Cube', 'Pyramid', 'Tetrahedron', 'Triangular Prism', 'Hexagonal Prism', 'Hexagonal Pyramid'] #list not used in code

#button setup
change_shape_button = button(1110, 10, 150, 30, 'Change Shape')
reset_shape_button = button(1110, 50, 150, 30, 'Reset Shape')
rand_linecolor_button = button(1110, 90, 150, 30, 'Random Line Color')
rand_backcolor_button = button(1110, 130, 150, 30, 'Random bg Color')
controls_settings_button = button(1110, 170, 150, 30, 'Control Settings')

quit_program_button = button(1110, 210, 150, 30, 'Quit Program')



back_button = button(1110, 10, 150, 30, 'Go Back')

shape_buttons = [button(10, 10, 150, 30, 'Cube'),
                 button(170, 10, 150, 30, 'Pyramid'),
                 button(330, 10, 150, 30, 'Tetrahedron'),
                 button(490, 10, 150, 30, 'Triangular Prism'),
                 button(650, 10, 150, 30, 'Hexagonal Prism'),
                 button(810, 10, 150, 30, 'Hexagonal Pyramid'),
                 button(970, 10, 150, 30, 'L Shaped Prism')]

# Run the main loop
running = True
current_mode = 'render shape'
while running:    
    #fill screen background
    screen.fill(bg_color)
    if current_mode == 'render shape':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if change_shape_button.rect.collidepoint(event.pos):
                    current_mode = 'choose shape'
                elif quit_program_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
                elif rand_backcolor_button.rect.collidepoint(event.pos):
                    bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                elif rand_linecolor_button.rect.collidepoint(event.pos):
                    line_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                elif controls_settings_button.rect.collidepoint(event.pos):
                    current_mode = 'shape settings'
                elif reset_shape_button.rect.collidepoint(event.pos):
                    angle_x, angle_y, angle_z = 0, 0, 0
                    focal_length = 500
                    line_color = BLACK
                    bg_color = WHITE
                    scale = 1
                    if name == 'Cube':
                        vertices3d, edges, name = wireframe.cube()
                    elif name == '4 Corner Pyramid':
                        vertices3d, edges, name = wireframe.pyramid()
                    elif name == 'Tetrahedron':
                        vertices3d, edges, name = wireframe.tetrahedron()
                    elif name == 'Triangular Prism':
                        vertices3d, edges, name = wireframe.triangular_prism()
                    elif name == 'Hexagonal Prism':
                        vertices3d, edges, name = wireframe.hexagonal_prism()
                    elif name == 'Hexagonal Pyramid':
                        vertices3d, edges, name = wireframe.hexagonal_pyramid()
                    elif name == 'L Shape Prism':
                        vertices3d, edges, name = wireframe.L_shape_prism()
                    
        #draw shape with vertices
        vertices2d = shape.plot_2d(focal_length, vertices3d)
        vertices2d = shape.center(three_d_size, vertices2d)
        shape.draw(edges, vertices2d)

        #handle transformations based on user input
        keys = pygame.key.get_pressed()
        rot_speed = 0.1 if keys[pygame.K_TAB] else 0.01
        enlarge_factor = 0.1 if keys[pygame.K_TAB] else 0.01
        
        if keys[pygame.K_LEFT]:
            vertices3d = shape.rotate_3d(vertices3d, -rot_speed, 'y')
            angle_y -= math.degrees(rot_speed)
        elif keys[pygame.K_RIGHT]:
            vertices3d = shape.rotate_3d(vertices3d, rot_speed, 'y')
            angle_y += math.degrees(rot_speed)
        elif keys[pygame.K_UP]:
            vertices3d = shape.rotate_3d(vertices3d, rot_speed, 'x')
            angle_x += math.degrees(rot_speed)

        elif keys[pygame.K_DOWN]:
            vertices3d = shape.rotate_3d(vertices3d, -rot_speed, 'x')
            angle_x -= math.degrees(rot_speed)
        elif keys[pygame.K_p]:
            vertices3d = shape.rotate_3d(vertices3d, rot_speed, 'z')
            angle_z += math.degrees(rot_speed)
        elif keys[pygame.K_i]:
            vertices3d = shape.rotate_3d(vertices3d, -rot_speed, 'z')
            angle_z -= math.degrees(rot_speed)
        
        elif keys[pygame.K_v]:
            focal_length -= 1
        elif keys[pygame.K_c]:
            focal_length = 500
        
        elif keys[pygame.K_e]:
            vertices3d = shape.enlarge(vertices3d, 1 + enlarge_factor)
            scale *= 1+enlarge_factor
        elif keys[pygame.K_q]:
            vertices3d = shape.enlarge(vertices3d, 1 - enlarge_factor)
            scale /= 1+enlarge_factor


        #reset angles if they are bigger than 360
        angle_x, angle_y, angle_z = check_angle_reset(angle_x, angle_y, angle_z)
        
        #update text on screen
        screen.blit(font.render(f"Angle X: {angle_x}", True, line_color), (20, 10)) #angle x
        screen.blit(font.render(f"Angle Y: {angle_y}", True, line_color), (20, 30)) #angle y
        screen.blit(font.render(f"Angle Z: {angle_z}", True, line_color), (20, 50)) #angle z
        screen.blit(font.render(f"Focal Length: {focal_length}", True, line_color), (20, 70)) #focal length
        screen.blit(font.render(f"Shape: {name}", True, line_color), (20, 90)) #shape name
        screen.blit(font.render(f"Scale: {round(scale,3)}", True, line_color), (20, 110)) #scale
        
        #draw buttons
        change_shape_button.draw(screen)
        reset_shape_button.draw(screen)
        quit_program_button.draw(screen)
        rand_linecolor_button.draw(screen)
        controls_settings_button.draw(screen)
        rand_backcolor_button.draw(screen)
        
    elif current_mode == 'choose shape': #select another shape menu
        scale = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in shape_buttons:
                    if button.rect.collidepoint(event.pos):
                        current_mode = 'render shape'
                        angle_x = 0
                        angle_y = 0
                        angle_z = 0
                        focal_length = 500
                        if button.text == 'Cube':
                            vertices3d, edges, name = wireframe.cube()
                        elif button.text == 'Pyramid':
                            vertices3d, edges, name = wireframe.pyramid()
                        elif button.text == 'Tetrahedron':
                            vertices3d, edges, name = wireframe.tetrahedron()
                        elif button.text == 'Triangular Prism':
                            vertices3d, edges, name = wireframe.triangular_prism()
                        elif button.text == 'Hexagonal Prism':
                            vertices3d, edges, name = wireframe.hexagonal_prism()
                        elif button.text == 'Hexagonal Pyramid':
                            vertices3d, edges, name = wireframe.hexagonal_pyramid()
                        elif button.text == 'L Shaped Prism':
                            vertices3d, edges, name = wireframe.L_shape_prism()
                            
                            
        for button in shape_buttons: #draw buttons on screen
            button.draw(screen)


    elif current_mode == 'shape settings':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button.rect.collidepoint(event.pos):
                    current_mode = 'render shape'
                

        screen.blit(big_font.render(f"Controls", True, line_color), (20, 20))
        screen.blit(font.render(f"TAB - Increase Speed of Transformations", True, line_color), (20, 80))
        screen.blit(font.render(f"Arrow Key Up/Down/Left/Right - Rotate X/Y Axis", True, line_color), (20, 100))
        screen.blit(font.render(f"I/P - Rotate Z Axis", True, line_color), (20, 120))
        screen.blit(font.render(f"V - Decrease Focal Length", True, line_color), (20, 140))
        screen.blit(font.render(f"C - Reset Focal Length", True, line_color), (20, 160))
        screen.blit(font.render(f"E/Q - Enlarge/Reduce", True, line_color), (20, 180))

        back_button.draw(screen)
                            
    #update the screen
    pygame.display.flip()

pygame.quit()