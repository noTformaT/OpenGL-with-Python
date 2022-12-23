from .Mesh import *

class SkyBox(Mesh):
    def __init__(self, 
            location=pygame.Vector3(0, 0, 0),
            material=None,
            world_cubemap=None
        ) -> None:

        sc = 1.0

        ts = [
            [-sc, sc, -sc],     #0
            [-sc, -sc, -sc],    #1
            [sc, sc, -sc],      #2
            [sc, -sc, -sc],     #3
            [-sc, sc, sc],      #4
            [sc, sc, sc],       #5
            [-sc, -sc, sc],     #6
            [sc, -sc, sc]       #7
        ]
        
        vertices = [
            [-sc, sc, -sc],
            [-sc, -sc, -sc],
            [sc, sc, -sc],
            [sc, sc, -sc],
            [-sc, -sc, -sc],
            [sc, -sc, -sc],

            [sc, sc, -sc],
            [sc, -sc, -sc],
            [sc, sc, sc],
            [sc, sc, sc],
            [sc, -sc, -sc],
            [sc, -sc, sc],

            [sc, sc, sc],
            [sc, -sc, sc],
            [-sc, sc, sc],
            [-sc, sc, sc],
            [sc, -sc, sc],
            [-sc, -sc, sc],

            [-sc, sc, sc],
            [-sc, -sc, sc],
            [-sc, sc, -sc],
            [-sc, sc, -sc],
            [-sc, -sc, sc],
            [-sc, -sc, -sc],

            [-sc, sc, sc], 
            [-sc, sc, -sc], 
            [sc, sc, sc],
            [sc, sc, sc],
            [-sc, sc, -sc],
            [sc, sc, -sc],

            [-sc, -sc, -sc], 
            [-sc, -sc, sc],
            [sc, -sc, -sc],

            [sc, -sc, -sc],
            [-sc, -sc, sc],
            [sc, -sc, sc]
        ]

        if True:
            vertices = [
                [-0.5, -0.5,  0.5],
                [ 0.5, -0.5,  0.5],
                [-0.5,  0.5,  0.5],
                [-0.5,  0.5,  0.5],
                [ 0.5, -0.5,  0.5],
                [ 0.5,  0.5,  0.5],

                [-0.5,  0.5,  0.5],
                [ 0.5,  0.5, 0.5],
                [-0.5,  0.5, -0.5],
                [-0.5,  0.5, -0.5],
                [ 0.5,  0.5,  0.5],
                [ 0.5,  0.5, -0.5],

                [-0.5,  0.5, -0.5],
                [ 0.5,  0.5, -0.5],
                [-0.5, -0.5, -0.5],
                [-0.5, -0.5, -0.5],
                [ 0.5,  0.5, -0.5],
                [ 0.5, -0.5, -0.5],

                [-0.5, -0.5, -0.5],
                [ 0.5, -0.5, -0.5],
                [-0.5, -0.5,  0.5],
                [-0.5, -0.5,  0.5],
                [ 0.5, -0.5, -0.5],
                [ 0.5, -0.5,  0.5],

                [ 0.5, -0.5,  0.5],
                [ 0.5, -0.5, -0.5],
                [ 0.5,  0.5,  0.5],
                [ 0.5,  0.5,  0.5],
                [ 0.5, -0.5, -0.5],
                [ 0.5,  0.5, -0.5],
                
                [-0.5, -0.5, -0.5],
                [-0.5, -0.5,  0.5],
                [-0.5,  0.5, -0.5],
                [-0.5,  0.5, -0.5],
                [-0.5, -0.5,  0.5],
                [-0.5,  0.5,  0.5],
            ]

        colors = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],

            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],

            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],

            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],

            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],

            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

        super().__init__(
            vertices=vertices, 
            vertex_colors=colors,
            draw_type=GL_TRIANGLES,
            translation=location,
            material=material,
            world_cube_map=world_cubemap)

    def draw(self, camera, lights):
        glDepthMask(GL_FALSE)
        super().draw(camera, lights)
        glDepthMask(GL_TRUE)