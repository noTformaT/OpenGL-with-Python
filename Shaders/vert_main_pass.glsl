#version 330

in vec3 position;
in vec3 vertex_normal;
in vec3 vertex_color;
in vec2 vertex_uv;

out vec3 color;
out vec3 normal;
out vec2 uv;
out vec3 frag_pos;
out vec3 view_pos;

uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;

void main()
{
    view_pos = vec3(vec4(view_mat[3][0], view_mat[3][1], view_mat[3][2], 1));
    gl_Position = projection_mat * inverse(view_mat)  * model_mat * vec4(position, 1);
    color = vertex_color;
    normal = mat3(transpose(inverse(model_mat))) * vertex_normal;;
    uv = vertex_uv;
    frag_pos = vec3(model_mat * vec4(position, 1));
}