# model_config.py

from langchain_ollama import OllamaLLM
import tiktoken

MODEL_NAME = "carriegpt"
MAX_TOKENS = 80

llm = OllamaLLM(model=MODEL_NAME)
tokenizer = tiktoken.get_encoding("cl100k_base")

def trim_to_sentence(text, max_tokens=MAX_TOKENS):
    tokens = tokenizer.encode(text)
    if len(tokens) <= max_tokens:
        return text.strip()
    trimmed = tokenizer.decode(tokens[:max_tokens])
    for end in [".", "!", "?"]:
        if end in trimmed:
            trimmed = trimmed.rsplit(end, 1)[0] + end
            return trimmed.strip()
    return trimmed.strip() + "... 💋"