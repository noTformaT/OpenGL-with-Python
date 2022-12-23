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

out vec3 reflected_view;
out vec3 refracted_view;

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

    vec4 world_pos = model_mat * vec4(position, 1);

    vec3 unit_normal = normalize(normal);

    vec3 view_dir = normalize(world_pos.xyz - view_pos);
    
    refracted_view = refract(view_dir, unit_normal, 1.0 / 1.3);
    reflected_view = reflect(unit_normal, view_dir);
}