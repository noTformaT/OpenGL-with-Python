from OpenGL.GL import *
import numpy as np

def format_vertices(coordirates, triangels):
    all_triangles = []
    for t in range(0, len(triangels), 3):
        all_triangles.append(coordirates[triangels[t]])
        all_triangles.append(coordirates[triangels[t+1]])
        all_triangles.append(coordirates[triangels[t+2]])
    return np.array(all_triangles, np.float32)

def compile_shader(shader_type, shader_source):
    shader_id = glCreateShader(shader_type)
    glShaderSource(shader_id, shader_source)
    glCompileShader(shader_id)
    compile_success = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
    if not compile_success:
        error_message = glGetShaderInfoLog(shader_id)
        glDeleteShader(shader_id)
        error_message = "\n" + error_message.decode("utf-8")
        raise Exception(error_message)
    return shader_id

def create_program(vertex_shader_code, fragment_shader_code):
    vertext_shader_id = compile_shader(GL_VERTEX_SHADER, vertex_shader_code)
    fragment_shader_id = compile_shader(GL_FRAGMENT_SHADER, fragment_shader_code)
    program_id = glCreateProgram()
    glAttachShader(program_id, vertext_shader_id)
    glAttachShader(program_id, fragment_shader_id)
    glLinkProgram(program_id)
    link_success = glGetProgramiv(program_id, GL_LINK_STATUS)
    if not link_success:
        info = glGetProgramInfoLog(program_id)
        raise RuntimeError(info)

    glDeleteShader(vertext_shader_id)
    glDeleteShader(fragment_shader_id)
    return program_id