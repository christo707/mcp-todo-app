class Config:
    SEED = 42
    MODEL = "QWEN_2_5"
    OLLAMA_CONTEXT_WINDOW = 4096 # increase to have longer conversation but slower response

    class Server:
        HOST = "0.0.0.0"
        PORT = 8001
        SSE_PATH = "/sse"
        TRANSPORT = "sse"

    class Agent:
        MAX_ITERATIONS = 10

def server_url():
    return f"http://{Config.Server.HOST}:{Config.Server.PORT}{Config.Server.SSE_PATH}"