from OpenGL.GL import *

class Uniform:
    def __init__(self, data_type, data) -> None:
        self.data_type = data_type
        self.data = data
        self.variable_id = None

    def find_variable(self, program_id, variable_name):
        self.variable_id = glGetUniformLocation(program_id, variable_name)
        a = 5

    def update_data(self, data):
        self.data = data

    def load(self):
        if self.data_type == "vec3":
            glUniform3f(self.variable_id, self.data[0], self.data[1], self.data[2])
        elif self.data_type == "mat4":
            glUniformMatrix4fv(self.variable_id, 1, GL_TRUE, self.data)