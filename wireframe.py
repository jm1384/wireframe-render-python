import math
class wireframe:
    def cube():
        vertices = [
        (100, 100, 100),
        (100, 100, -100),
        (100, -100, 100),
        (100, -100, -100),
        (-100, 100, 100),
        (-100, 100, -100),
        (-100, -100, 100),
        (-100, -100, -100)
        ]
        
        edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 7),
        (4, 5),
        (4, 6),
        (5, 7),
        (6, 7)
        ]
        return vertices, edges, 'Cube'
        
    def pyramid():
        vertices = [
        (100, -100, 100),    # vertex 0 
        (100, -100, -100),   # vertex 1
        (-100, -100, 100),   # vertex 2
        (-100, -100, -100),  # vertex 3
        (0, 100, 0)          # vertex 4 (apex)
        ]

        edges = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4)
        ]
        return vertices, edges, '4 Corner Pyramid'
    
    def tetrahedron():
        size = 100
        vertices = [(size, size, size),
                    (-size, -size, size),
                    (-size, size, -size),
                    (size, -size, -size)
                    ]
        
        edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
        return vertices, edges, 'Tetrahedron'
    
    def triangular_prism():
        size = 100
        vertices = [(size, 0, size),
                    (-size, 0, size),
                    (0, 0, -size),
                    (size, size, size),
                    (-size, size, size),
                    (0, size, -size)
                   ]
        edges = [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5), (0,3), (1, 4), (2,5)]
        return vertices, edges, 'Triangular Prism'
    
    def hexagonal_prism():
        size = 100
        h = size * (3**(0.5)) / 2
        vertices = [(size, 0, 0),
                    (size/2, 0, h),
                    (-size/2, 0, h),
                    (-size, 0, 0),
                    (-size/2, 0, -h),
                    (size/2, 0, -h),
                    (size, h, 0),
                    (size/2, h, h),
                    (-size/2, h, h),
                    (-size, h, 0),
                    (-size/2, h, -h),
                    (size/2, h, -h)
                   ]
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 6), (0, 6), (1, 7), (2, 8), (3, 9), (4, 10), (5, 11)]
        return vertices, edges, 'Hexagonal Prism'
    
    def hexagonal_pyramid():
        size = 100
        h = size * (3**(0.5)) / 2
        vertices = [(size, 0, 0),
                    (size/2, 0, h),
                    (-size/2, 0, h),
                    (-size, 0, 0),
                    (-size/2, 0, -h),
                    (size/2, 0, -h),
                    (0, h, 0)
                   ]
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]
        return vertices, edges, 'Hexagonal Pyramid'
    
    def L_shape_prism():
        vertices = [
            (100, 100, 0),
            (-100, 100, 0),
            (100, 0, 0),
            (-100, 0, 0),
            
            (100, 100, 100),
            (0, 100, 100),
            (100,0, 100),
            (0, 0, 100),
            
            (0, 100, 200),
            (-100, 100, 200),
            (0,0,200),
            (-100,0,200)
            
        ]

        edges = [
            (0,1),
            (1,3),
            (2,0),
            (3,2),
            
            (4,5),
            (5,7),
            (7,6),
            (6,4),
            
            (8,9),
            (9,11),
            (11,10),
            (10,8),
            
            (1,9),
            (3,11),
            (0,4),
            (7,10),
            (5,8),
            (1,9),
            (2,6)
            
        ]
        return vertices, edges, 'L Shape Prism'

    
