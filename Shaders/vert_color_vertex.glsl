#version 330

in vec3 position;
in vec3 vertex_normal;
in vec3 vertex_color;

out vec3 color;

uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;

void main()
{
    gl_Position = projection_mat * inverse(view_mat)  * model_mat * vec4(position, 1);
    color = vertex_color;
}