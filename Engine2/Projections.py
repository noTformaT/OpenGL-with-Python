from glapp.PyOGLApp import *
from glapp.GraphicsData import *
import numpy as np
from glapp.Utils import *
from glapp.Square import *
from glapp.Triangle import *
from glapp.Axes import *
from glapp.Cube import *
from glapp.LoadMesh import *

vertex_shader = r'''
#version 330

in vec3 position;
in vec3 vertex_normal;
in vec3 vertex_color;
in vec2 vertex_uv;

out vec3 color;
out vec3 normal;
out vec2 uv;
out vec3 frag_pos;
out vec3 light_pos;
out vec3 view_pos;

uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;

void main()
{
    light_pos = vec3(2, 2, 5);
    view_pos = vec3(vec4(view_mat[3][0], view_mat[3][1], view_mat[3][2], 1));
    //light_pos = vec3(view_mat[3][0], view_mat[3][1], view_mat[3][2]);
    gl_Position = projection_mat * inverse(view_mat)  * model_mat * vec4(position, 1);
    color = vertex_color;
    normal = mat3(transpose(inverse(model_mat))) * vertex_normal;;
    uv = vertex_uv;
    frag_pos = vec3(model_mat * vec4(position, 1));
}
'''

fragment_shader = r'''
#version 330 core

in vec3 color;
in vec3 normal;
in vec2 uv;
in vec3 frag_pos;
in vec3 light_pos;
in vec3 view_pos;

out vec4 frag_color;

void main()
{
    vec3 light_color = vec3(1, 0, 0);

    //ambient
    float a_strength = 0.1;
    vec3 ambient = a_strength * light_color;

    // diffuse
    float diff_strength = 0.3;
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - frag_pos);
    float dif = max(dot(norm, light_dir), 0.0);
    vec3 diffuse = light_color * dif * diff_strength;

    // specular
    float s_strenth = 1.0;
    vec3 view_dir = normalize(view_pos-frag_pos);
    vec3 reflect_dir = normalize(-light_dir -norm);
    float spec = pow(max(dot(view_dir, reflect_dir), 0), 128);
    

    vec3 direction = frag_pos - light_pos;
    vec3 fragToEye = normalize(view_pos - frag_pos);
    vec3 reflectedVertex = normalize(reflect(direction, normalize(normal)));
    float specularFactor = dot(fragToEye, reflectedVertex);

    if (specularFactor > 0.0f)
    {
        specularFactor = pow(specularFactor, 128);
    }
    else
    {
        specularFactor = 0;
    }

    vec3 specular = s_strenth * specularFactor * light_color;

    vec3 ee = vec3(specularFactor, specularFactor, specularFactor);


    frag_color = vec4(color * (ambient + diffuse + specular), 1);

    //frag_color = vec4(reflect_dir, 1);


}
'''

class Projections(PyOGLApp):
    def __init__(self) -> None:
        super().__init__(0, 0, 700, 700)
        self.axes = None
        self.square = None
        self.triangle = None
        self.cube = None
        self.teapot = None
        self.monkey = None
        self.crah = None
        self.cortex = None

    def initialize(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        #self.square = Square(self.program_id, pygame.Vector3(0, -1, -1))
        #self.triangle = Triangle(self.program_id, pygame.Vector3(0, 0, 0))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        #self.axes = Axes(self.program_id)
        #self.cube = Cube(self.program_id, pygame.Vector3(0, -2, 0))
        self.teapot = LoadMesh("Resources/teapot.obj", self.program_id, 
            location=pygame.Vector3(0, 0, 0),
            scale=pygame.Vector3(1,1,1), 
            rotation=Rotation(0, pygame.Vector3(0, 1, 0)))
        self.monkey = LoadMesh("Resources/monkey_hd.obj", self.program_id, location=pygame.Vector3(4, 1.5, 0))
        self.crash = LoadMesh("Resources/crash.obj", self.program_id, location=pygame.Vector3(-4, 0.0, 0))
        self.cortex = LoadMesh("Resources/donut.obj", self.program_id, location=pygame.Vector3(0, 4.5, 0))
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update()
        
        self.teapot.update()
        self.monkey.update()
        self.crash.update()
        self.cortex.update()
        
        #self.square.draw()
        #self.triangle.draw()
        #self.axes.draw()
        #self.cube.draw()
        self.teapot.draw()
        self.monkey.draw()
        self.crash.draw()
        self.cortex.draw()

Projections().mainLoop()