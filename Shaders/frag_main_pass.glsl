#version 330 core

#define NUM_LIGHTS 2

in vec3 color;
in vec3 normal;
in vec2 uv;
in vec3 frag_pos;
in vec3 view_pos;

out vec4 frag_color;

struct Light
{
    vec3 position;
    vec3 color;
};

uniform Light lights_data[NUM_LIGHTS];
uniform sampler2D tex;

vec4 CreateLight(vec3 lightPos, vec3 lightColor, vec3 normal, vec3 fragPos, vec3 viewPos)
{
    //ambient
    float a_strength = 0.1;
    vec3 ambient = a_strength * lightColor;

    // diffuse
    float diff_strength = 0.3;
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(lightPos - fragPos);
    float dif = max(dot(norm, light_dir), 0.0);
    vec3 diffuse = lightColor * dif * diff_strength;

    // specular
    float s_strenth = 1.0;

    vec3 direction = fragPos - lightPos;
    vec3 fragToEye = normalize(viewPos - fragPos);
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

    vec3 specular = s_strenth * specularFactor * lightColor;

    return vec4(ambient + diffuse + specular, 1);
}

vec4 CalcAllPoints()
{
    int lightsCount = 2;

    vec4 final_color = vec4(0, 0, 0, 1);

    for (int i = 0; i < lightsCount; i++)
    {
        final_color += CreateLight(lights_data[i].position, lights_data[i].color, normal, frag_pos, view_pos);
    }

    return final_color;
}

void main()
{
    vec4 uv_color = texture(tex, uv);
    
    vec4 final_color = vec4(color, 1) * uv_color; 
    
    final_color *= CalcAllPoints();

    frag_color = final_color;
}