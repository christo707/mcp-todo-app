from dataclasses import dataclass
from enum import Enum

class ModelProvider(str, Enum):
    OLLAMA = "ollama"
    GROQ = "groq"

@dataclass
class ModelConfig:
    name: str
    temperature: float
    provider: ModelProvider

QWEN_2_5 = ModelConfig("qwen2.5", temperature=0.0, provider=ModelProvider.OLLAMA)
LLAMA_3_3 = ModelConfig("llama-3.3-70b-versatile", temperature=0.0, provider=ModelProvider.GROQ)

class Config:
    SEED = 42
    MODEL = "QWEN_2_5"
    OLLAMA_CONTEXT_WINDOW = 4096 # increase to have longer conversation but slower response

    class ServerSSE:
        HOST = "0.0.0.0"
        PORT = 8001
        SSE_PATH = "/sse"
        TRANSPORT = "stdio"
    
    class ServerStdIo:
        HOST = "0.0.0.0"
        PORT = 8002
        TRANSPORT = "stdio"

    class Agent:
        MAX_ITERATIONS = 10

def server_url():
    return f"http://{Config.Server.HOST}:{Config.Server.PORT}{Config.Server.SSE_PATH}"