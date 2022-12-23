#version 330 core

in vec3 color;
in vec3 normal;
in vec2 uv;
in vec3 frag_pos;
in vec3 view_pos;
in vec3 reflected_view;

out vec4 frag_color;


uniform sampler2D tex;
uniform samplerCube skybox;

const vec3 lightDirection = normalize(vec3(0, -1, -1));

void main()
{
    vec4 uv_color = texture(tex, uv);
    //vec4 skybox_color = texture(skybox, reflected_view);
    //float brightness = max(dot(-lightDirection, normalize(normal)), 0.0) + 0.3;

    //frag_color = uv_color * brightness;

    //frag_color = skybox_color;

    
    vec3 n_normal = normalize(normal);

    vec3 view_dir = normalize(frag_pos - view_pos);
    vec3 reflect_dir = reflect(view_dir, n_normal);

    vec4 skybox_color = texture(skybox, reflect_dir);

    frag_color = mix(vec4(color, 1.0), skybox_color, 1.0);
}