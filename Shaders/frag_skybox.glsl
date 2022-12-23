#version 330 core

in vec3 color;
in vec3 uv;

out vec4 frag_color;

uniform samplerCube skybox;

void main()
{
    //frag_color = vec4(uv, 1);
    frag_color = texture(skybox, uv);
}