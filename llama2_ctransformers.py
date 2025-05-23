from ctransformers import AutoModelForCausalLM

# Ruta al modelo GGUF descargado con LM Studio
model_path = "/Users/Nico/.cache/lm-studio/models/TheBloke/LLama-2-7B-Chat-GGUF/llama-2-7b-chat.Q4_K_S.gguf"


# Cargar el modelo
llm = AutoModelForCausalLM.from_pretrained(
    model_path,
    model_type="llama",
    max_new_tokens=100,
    gpu_layers=0  
)

# Prompt de ejemplo
prompt = "Translate English to French: Configuration files are easy to use!"

# Generar respuesta
response = llm(prompt)

print("Respuesta del modelo:")
print(response)
