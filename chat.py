from ctransformers import AutoModelForCausalLM

# Ruta al archivo .gguf del modelo
model_path = "/Users/Nico/.cache/lm-studio/models/TheBloke/LLama-2-7B-Chat-GGUF/llama-2-7b-chat.Q4_K_S.gguf"

# Cargar el modelo
print("🔄 Cargando el modelo, por favor espera...")
llm = AutoModelForCausalLM.from_pretrained(
    model_path,
    model_type="llama",
    max_new_tokens=256,
    gpu_layers=0  # Aumentar si tenés GPU
)
print("✅ Modelo cargado. Iniciando chat...\n")

# Chat interactivo
print("💬 Escribí tu pregunta o 'salir' para terminar.")

while True:
    prompt = input("\n👤 Tú: ")
    if prompt.lower() in ["salir", "exit", "quit"]:
        print("👋 ¡Hasta luego!")
        break

    response = llm(prompt)
    print(f"🤖 LLaMA: {response}")
