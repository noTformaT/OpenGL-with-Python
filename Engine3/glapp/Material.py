from .Utils import *

class Material:
    def __init__(self, vertex_shader_path, fragment_shader_path) -> None:
        
        vertex_code = open(vertex_shader_path).read()
        fragment_code = open(fragment_shader_path).read()

        self.program_id = create_program(vertex_code, fragment_code)

    def use(self):
        glUseProgram(self.program_id)