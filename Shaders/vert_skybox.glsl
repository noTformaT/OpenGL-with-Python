#version 330

in vec3 position;
in vec3 vertex_normal;
in vec3 vertex_color;

out vec3 color;
out vec3 uv;

uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;

void main()
{
    mat4 fix = mat4(mat3(view_mat));
    gl_Position = projection_mat * inverse(fix) * vec4(position, 1);
    uv = position;
    color = vertex_color;
}